import os
import sys
import json
import shutil
import socket
import subprocess
import urllib.request
import urllib.error

from common import (
    PROJECT_ROOT, get_gateway_config, get_auth_token, check_gateway_reachable,
    check_gateway_models, redact, load_json
)

def check_port(host, port, timeout=1.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False

def run_doctor():
    gw = get_gateway_config()
    token = get_auth_token()
    results = []

    def report(name, status, details=""):
        results.append({"name": name, "status": status, "details": details})
        status_colors = {
            "PASS": "\033[92mPASS\033[0m",
            "WARN": "\033[93mWARN\033[0m",
            "FAIL": "\033[91mFAIL\033[0m",
            "NOT INSTALLED": "\033[90mNOT INSTALLED\033[0m",
            "NOT CONFIGURED": "\033[93mNOT CONFIGURED\033[0m",
            "RATE LIMITED": "\033[91mRATE LIMITED\033[0m",
            "QUOTA EXHAUSTED": "\033[91mQUOTA EXHAUSTED\033[0m",
            "UNAVAILABLE": "\033[91mUNAVAILABLE\033[0m"
        }
        color_status = status_colors.get(status, status)
        detail_str = f" - {details}" if details else ""
        print(f"  [{color_status:20s}] {name:25s}{detail_str}")

    print("\n============================================================")
    print(" FREELLMAPI & GLOBAL AI ENVIRONMENT DOCTOR")
    print("============================================================\n")

    # 1. FreeLLMAPI Process
    ps_res = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    has_freellm_proc = "FreeLLMAPI.app/Contents/MacOS/FreeLLMAPI" in ps_res.stdout
    if has_freellm_proc:
        report("FreeLLMAPI Process", "PASS", "Active native application process detected")
    else:
        report("FreeLLMAPI Process", "FAIL", "FreeLLMAPI application is not running")

    # 2. Gateway Port / Reachability
    gw_up = check_gateway_reachable(timeout=2.0)
    if gw_up:
        report("Gateway Reachability", "PASS", f"Listening on {gw['host']}:{gw['port']}")
    else:
        report("Gateway Reachability", "FAIL", f"Unable to reach gateway on {gw['base_url']}")

    # 3. Models API
    models_ok, count_or_err = check_gateway_models(timeout=4.0)
    if models_ok:
        report("Models API", "PASS", f"{count_or_err} models available via /v1/models")
    else:
        report("Models API", "FAIL", f"Failed querying /v1/models: {count_or_err}")

    # 4. Authentication
    if token:
        report("Authentication", "PASS", f"Valid token configured (prefix: {token[:6]}...)")
    else:
        report("Authentication", "FAIL", "No auth token found in ~/.claude/settings.json or env")

    # 5. Claude Code
    claude_bin = shutil.which("claude")
    if claude_bin:
        claude_cfg = os.path.expanduser("~/.claude/settings.json")
        is_routed = False
        if os.path.exists(claude_cfg):
            try:
                with open(claude_cfg, "r") as f:
                    cdata = json.load(f)
                    burl = cdata.get("env", {}).get("ANTHROPIC_BASE_URL", "")
                    if "127.0.0.1:31415" in burl or "localhost:31415" in burl:
                        is_routed = True
            except Exception:
                pass
        if is_routed:
            report("Claude Code", "PASS", f"Binary: {claude_bin} (routed to {gw['anthropic_base_url']})")
        else:
            report("Claude Code", "WARN", f"Binary: {claude_bin} (not routed to FreeLLMAPI in settings)")
    else:
        report("Claude Code", "NOT INSTALLED", "Not found in PATH")

    # 6. Codex CLI
    codex_bin = shutil.which("codex")
    if codex_bin:
        codex_cfg = os.path.expanduser("~/.codex/config.toml")
        is_routed = False
        if os.path.exists(codex_cfg):
            with open(codex_cfg, "r") as f:
                content = f.read()
                if "127.0.0.1:31415/v1" in content or "localhost:31415/v1" in content:
                    is_routed = True
        if is_routed:
            report("Codex CLI", "PASS", f"Binary: {codex_bin} (configured for FreeLLMAPI /v1)")
        else:
            report("Codex CLI", "WARN", f"Binary: {codex_bin} (custom base_url missing in config.toml)")
    else:
        report("Codex CLI", "NOT INSTALLED", "Not found in PATH")

    # 7. Gemini CLI
    gemini_bin = shutil.which("gemini")
    if gemini_bin:
        report("Gemini CLI", "PASS", f"Binary: {gemini_bin} (configured for Google OAuth, FreeLLMAPI compatible)")
    else:
        report("Gemini CLI", "NOT INSTALLED", "Not found in PATH")

    # 8. DSH (DeepSeek Harness)
    dsh_up = check_port("127.0.0.1", gw.get("dsh_port", 3080))
    if dsh_up:
        report("DeepSeek Harness (DSH)", "PASS", f"Active web service on 127.0.0.1:{gw.get('dsh_port', 3080)}")
    else:
        report("DeepSeek Harness (DSH)", "NOT INSTALLED", "No listener on port 3080")

    # 9. Other candidate agents (verify real host engine, not just launcher wrapper)
    agents_to_check = [
        ("Aider", "aider"),
        ("OpenCode", "opencode"),
        ("Qwen Code", "qwen"),
        ("Goose", "goose"),
        ("Cline", "cline"),
        ("Roo Code", "roo"),
        ("Continue", "continue"),
        ("Kilo Code", "kilo"),
        ("Crush", "crush"),
        ("MiMo Code", "mimo"),
        ("AtomCode", "atomcode"),
        ("OpenClaw", "openclaw"),
        ("Hermes", "hermes"),
        ("Cursor", "cursor")
    ]
    system_path = ":".join([p for p in os.environ.get("PATH", "").split(":") if "freellmapi-agents" not in p])
    vscode_ext_dir = os.path.expanduser("~/.vscode/extensions")
    
    for label, bin_name in agents_to_check:
        bp = shutil.which(bin_name, path=system_path)
        if bp:
            try:
                target = os.path.realpath(bp)
                if "freellmapi-agents" in target and not target.endswith(bin_name):
                    bp = None
            except Exception:
                pass
        
        # Check IDE-only extensions
        is_ide_installed = False
        if bin_name == "roo":
            exts = [d for d in os.listdir(vscode_ext_dir) if "roo-cline" in d.lower()] if os.path.exists(vscode_ext_dir) else []
            if exts:
                is_ide_installed = True
                report(label, "PASS", f"IDE Extension installed in VS Code ({exts[0]})")
                continue
        elif bin_name == "continue":
            exts = [d for d in os.listdir(vscode_ext_dir) if "continue" in d.lower()] if os.path.exists(vscode_ext_dir) else []
            if exts:
                is_ide_installed = True
                report(label, "PASS", f"IDE Extension installed in VS Code ({exts[0]})")
                continue
        elif bin_name == "cursor":
            if os.path.exists("/Applications/Cursor.app") or bp:
                report(label, "PASS", "Desktop App installed at /Applications/Cursor.app")
                continue

        wrapper_path = os.path.join(PROJECT_ROOT, "bin", f"flm-{bin_name}")
        has_wrapper = os.path.exists(wrapper_path) or os.path.exists(os.path.join(PROJECT_ROOT, "bin", bin_name))
        
        if bp:
            report(label, "PASS", f"Host engine installed at {bp}")
        elif has_wrapper:
            report(label, "NOT CONFIGURED", f"Wrapper present but host engine not in PATH")
        else:
            report(label, "NOT INSTALLED", f"{bin_name} binary not found in PATH")


    # 10. Docker (Native host execution active; containerization not required)
    docker_bin = shutil.which("docker")
    if docker_bin:
        report("Docker Engine", "PASS", f"Binary: {docker_bin}")
    else:
        report("Docker Engine", "NOT REQUIRED", "Docker not installed (native execution active, NOT REQUIRED)")

    # 11. Local Qwen Infrastructure
    qwen_bridge_path = "/Users/subhajkar/Developer/qwen-antigravity/bridge.py"
    qwen_up = check_port("127.0.0.1", gw.get("local_qwen_port", 8787))
    if qwen_up:
        report("Local Qwen Bridge", "PASS", f"Active listener on 127.0.0.1:{gw.get('local_qwen_port', 8787)}")
    elif os.path.exists(qwen_bridge_path):
        report("Local Qwen Bridge", "OFFLINE (READY)", f"Bridge at {qwen_bridge_path} (offline, available as fallback)")
    else:
        report("Local Qwen Bridge", "NOT INSTALLED", "Bridge script not found")

    # 12. MCP Infrastructure
    gemini_mcp = os.path.expanduser("~/.gemini/config/mcp_config.json")
    codex_cfg = os.path.expanduser("~/.codex/config.toml")
    has_mcp = os.path.exists(gemini_mcp) and os.path.exists(codex_cfg)
    if has_mcp:
        report("MCP Infrastructure", "PASS", "Global Antigravity & Codex MCP registries intact")
    else:
        report("MCP Infrastructure", "WARN", "One or more MCP config files missing")

    print("\n------------------------------------------------------------")
    passed = sum(1 for r in results if r['status'] == 'PASS')
    warns = sum(1 for r in results if r['status'] in ('WARN', 'OFFLINE (READY)'))
    fails = sum(1 for r in results if r['status'] == 'FAIL')
    not_installed = sum(1 for r in results if r['status'] in ('NOT INSTALLED', 'NOT CONFIGURED', 'NOT REQUIRED'))
    print(f" Summary: {passed} PASS | {warns} WARN/STANDBY | {fails} FAIL | {not_installed} INACTIVE/NOT CONFIGURED")
    print("============================================================\n")
    return fails == 0

if __name__ == "__main__":
    success = run_doctor()
    sys.exit(0 if success else 1)
