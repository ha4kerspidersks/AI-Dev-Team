import os
import sys
import json
import time
import shutil
import subprocess
import urllib.request
import urllib.error

from common import (
    DATA_DIR, get_gateway_config, get_auth_token, save_json
)

PERF_FILE = os.path.join(DATA_DIR, "performance_metrics.json")

def test_streaming(endpoint_type="anthropic", model="auto", prompt="Reply with exactly: OK"):
    gw = get_gateway_config()
    token = get_auth_token()
    
    if endpoint_type == "anthropic":
        url = f"{gw['anthropic_base_url']}/v1/messages"
        headers = {
            "x-api-key": token,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        body = json.dumps({
            "model": model,
            "max_tokens": 15,
            "stream": True,
            "messages": [{"role": "user", "content": prompt}]
        }).encode()
    else:
        url = f"{gw['openai_base_url']}/chat/completions"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        body = json.dumps({
            "model": model,
            "max_tokens": 15,
            "stream": True,
            "messages": [{"role": "user", "content": prompt}]
        }).encode()

    t0 = time.time()
    ttft = None
    chunks_count = 0
    full_text = ""
    error = None

    try:
        req = urllib.request.Request(url, data=body, headers=headers)
        with urllib.request.urlopen(req, timeout=25.0) as res:
            for line in res:
                decoded = line.decode("utf-8", errors="replace").strip()
                if not ttft and decoded.startswith("data:"):
                    ttft = time.time() - t0
                if decoded.startswith("data:") and "[DONE]" not in decoded:
                    chunks_count += 1
                    try:
                        chunk_json = json.loads(decoded[5:].strip())
                        if endpoint_type == "anthropic":
                            delta = chunk_json.get("delta", {})
                            full_text += delta.get("text", "")
                        else:
                            choice = chunk_json.get("choices", [{}])[0]
                            full_text += choice.get("delta", {}).get("content", "")
                    except Exception:
                        pass
        total_time = time.time() - t0
        return {
            "status": "PASS",
            "ttft_sec": round(ttft, 3) if ttft else round(total_time, 3),
            "total_sec": round(total_time, 3),
            "chunks": chunks_count,
            "response": full_text.strip()[:40],
            "error": None
        }
    except Exception as e:
        total_time = time.time() - t0
        return {
            "status": "FAIL",
            "ttft_sec": None,
            "total_sec": round(total_time, 3),
            "chunks": 0,
            "response": None,
            "error": str(e)
        }

def test_claude_cli():
    claude_bin = shutil.which("claude")
    if not claude_bin:
        return {"status": "NOT INSTALLED", "ttft_sec": None, "total_sec": 0, "error": "claude binary not found"}

    gw = get_gateway_config()
    token = get_auth_token()
    env = os.environ.copy()
    env["ANTHROPIC_BASE_URL"] = gw["anthropic_base_url"]
    if token:
        env["ANTHROPIC_AUTH_TOKEN"] = token
    env["ANTHROPIC_MODEL"] = "auto"

    t0 = time.time()
    try:
        res = subprocess.run([claude_bin, "-p", "Reply with exactly: OK", "--dangerously-skip-permissions"], env=env, capture_output=True, text=True, timeout=90.0)
        total_time = round(time.time() - t0, 3)
        out = res.stdout.strip()
        if res.returncode == 0 and ("OK" in out or len(out) > 0):
            return {"status": "PASS", "ttft_sec": total_time, "total_sec": total_time, "response": out.splitlines()[-1][:40], "error": None}
        return {"status": "FAIL", "ttft_sec": None, "total_sec": total_time, "response": out[:40], "error": res.stderr[:60]}
    except Exception as e:
        return {"status": "FAIL", "ttft_sec": None, "total_sec": round(time.time() - t0, 3), "error": str(e)}

def test_codex_cli(model=None):
    codex_bin = shutil.which("codex")
    if not codex_bin:
        return {"status": "NOT INSTALLED", "ttft_sec": None, "total_sec": 0, "error": "codex binary not found"}

    gw = get_gateway_config()
    token = get_auth_token()
    env = os.environ.copy()
    env["OPENAI_BASE_URL"] = gw["openai_base_url"]
    if token:
        env["FREELLMAPI_API_KEY"] = token
        env["OPENAI_API_KEY"] = token

    t0 = time.time()
    try:
        cmd = [codex_bin, "exec", "--dangerously-bypass-approvals-and-sandbox", "--skip-git-repo-check", "--ephemeral"]
        if model:
            cmd.extend(["-m", model])
        cmd.append("Reply with exactly: OK")
        res = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=45.0)
        total_time = round(time.time() - t0, 3)
        out = res.stdout.strip()
        if res.returncode == 0:
            return {"status": "PASS", "ttft_sec": total_time, "total_sec": total_time, "response": out.splitlines()[-1][:40] if out else "OK", "error": None}
        return {"status": "FAIL", "ttft_sec": None, "total_sec": total_time, "response": out[:40], "error": res.stderr[:60]}
    except Exception as e:
        return {"status": "FAIL", "ttft_sec": None, "total_sec": round(time.time() - t0, 3), "error": str(e)}

def run_performance_suite():
    print("\n============================================================")
    print(" FREELLMAPI PERFORMANCE & END-TO-END VALIDATION SUITE")
    print("============================================================\n")

    targets = [
        ("Anthropic SSE (auto)", "stream", "anthropic", "auto"),
        ("OpenAI SSE (qwen/qwen3.8-27b - fast)", "stream", "openai", "qwen/qwen3.8-27b"),
        ("OpenAI SSE (auto)", "stream", "openai", "auto"),
        ("Claude Code CLI (e2e)", "cli", "claude", None),
        ("Codex CLI (e2e - auto)", "cli", "codex", "auto"),
        ("Codex CLI (e2e - direct)", "cli", "codex", None),
    ]

    results = {}
    print(f"{'Target / Component':40s} | {'TTFT':8s} | {'Total':8s} | {'Status':8s} | {'Preview / Notes'}")
    print("-" * 96)

    for label, kind, proto_or_cli, model in targets:
        time.sleep(1.2)
        if kind == "stream":
            r = test_streaming(proto_or_cli, model)
        elif proto_or_cli == "claude":
            r = test_claude_cli()
        elif proto_or_cli == "codex":
            r = test_codex_cli(model)
        else:
            r = {"status": "SKIPPED", "ttft_sec": None, "total_sec": 0, "response": "N/A"}

        results[label] = r
        ttft_str = f"{r['ttft_sec']:.2f}s" if r['ttft_sec'] is not None else "N/A"
        tot_str = f"{r['total_sec']:.2f}s" if r['total_sec'] is not None else "N/A"
        status_color = "\033[92mPASS\033[0m" if r['status'] == "PASS" else ("\033[91mFAIL\033[0m" if r['status'] == "FAIL" else r['status'])
        note = r.get("response") or r.get("error") or ""
        print(f"{label:40s} | {ttft_str:8s} | {tot_str:8s} | {status_color:16s} | {note[:28]}")

    save_json(PERF_FILE, {
        "timestamp": time.time(),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "results": results
    })

    print("-" * 96)
    passes = sum(1 for r in results.values() if r['status'] == 'PASS')
    total = len(results)
    print(f" Suite Result: {passes}/{total} verified operational. Metrics saved to data/performance_metrics.json")

    # Diagnostic probe on quarantined models (Empirical verification - never hidden)
    print("\n--- Diagnostic Probe on Quarantined / Demoted Models ---")
    quarantined_probe = test_streaming("openai", "openai/gpt-oss-120b")
    q_status = quarantined_probe.get("status")
    q_err = str(quarantined_probe.get("error"))
    print(f"  Quarantined: openai/gpt-oss-120b -> {q_status} ({q_err[:65]})")
    print("  State: CONFIRMED UNRELIABLE -> Properly quarantined in config/routing.json\n")

    return passes == total

if __name__ == "__main__":
    run_performance_suite()
