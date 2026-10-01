import os
import sys
import shutil
import subprocess

from common import (
    CONFIG_DIR, get_gateway_config, get_auth_token,
    check_gateway_reachable, load_json
)

MODES_FILE = os.path.join(CONFIG_DIR, "modes.json")

def get_active_mode_info():
    modes_cfg = load_json(MODES_FILE)
    mode_name = modes_cfg.get("active_mode", "normal")
    return mode_name, modes_cfg.get("modes", {}).get(mode_name, {})

def ensure_gateway_online():
    if not check_gateway_reachable(timeout=2.0):
        print("\033[91mError: FreeLLMAPI is not reachable on 127.0.0.1:31415.\033[0m", file=sys.stderr)
        print("Please start the FreeLLMAPI application from /Applications/FreeLLMAPI.app and retry.", file=sys.stderr)
        return False
    return True

def launch_claude(args):
    if not ensure_gateway_online():
        return 1

    claude_bin = shutil.which("claude")
    if not claude_bin:
        print("Error: Claude Code CLI ('claude') not found in PATH.", file=sys.stderr)
        return 1

    gw = get_gateway_config()
    token = get_auth_token()
    mode_name, mode_info = get_active_mode_info()

    env = os.environ.copy()
    env["ANTHROPIC_BASE_URL"] = gw["anthropic_base_url"]
    if token:
        env["ANTHROPIC_AUTH_TOKEN"] = token

    if mode_name == "fast":
        fast_model = mode_info.get("default_claude_model", "gemini-3.5-flash-lite")
        env["ANTHROPIC_MODEL"] = fast_model
        env["ANTHROPIC_DEFAULT_HAIKU_MODEL"] = fast_model
        env["ANTHROPIC_DEFAULT_OPUS_MODEL"] = fast_model
        env["ANTHROPIC_DEFAULT_SONNET_MODEL"] = fast_model
    else:
        env["ANTHROPIC_MODEL"] = "auto"

    return subprocess.run([claude_bin] + args, env=env).returncode

def launch_codex(args):
    if not ensure_gateway_online():
        return 1

    codex_bin = shutil.which("codex")
    if not codex_bin:
        print("Error: Codex CLI ('codex') not found in PATH.", file=sys.stderr)
        return 1

    gw = get_gateway_config()
    token = get_auth_token()
    mode_name, mode_info = get_active_mode_info()

    env = os.environ.copy()
    env["OPENAI_BASE_URL"] = gw["openai_base_url"]
    if token:
        env["FREELLMAPI_API_KEY"] = token
        env["OPENAI_API_KEY"] = token

    cmd = [codex_bin]
    if mode_name == "fast" and "-m" not in args and "--model" not in args:
        fast_model = mode_info.get("default_codex_model", "gemini-3.5-flash-lite")
        cmd.extend(["-m", fast_model])

    cmd.extend(args)
    return subprocess.run(cmd, env=env).returncode

def launch_gemini(args):
    gemini_bin = shutil.which("gemini")
    if not gemini_bin:
        print("Error: Gemini CLI ('gemini') not found in PATH.", file=sys.stderr)
        return 1

    gw = get_gateway_config()
    token = get_auth_token()
    env = os.environ.copy()

    if "--local-qwen" in args:
        args = [a for a in args if a != "--local-qwen"]
        env["GEMINI_API_BASE"] = "http://127.0.0.1:8787"
        print("[FLM Dispatcher] Routing Gemini CLI to Local Qwen Bridge on port 8787...")
    elif "--freellmapi" in args:
        args = [a for a in args if a != "--freellmapi"]
        if not ensure_gateway_online():
            return 1
        env["GEMINI_API_BASE"] = gw["gemini_base_url"]
        if token:
            env["GEMINI_API_KEY"] = token
        print("[FLM Dispatcher] Routing Gemini CLI to FreeLLMAPI Native Gemini endpoint...")

    return subprocess.run([gemini_bin] + args, env=env).returncode

def launch_dsh(args):
    dsh_bin = shutil.which("dsh")
    if dsh_bin:
        return subprocess.run([dsh_bin] + args).returncode
    return subprocess.run(["npx", "-y", "@deepseek-ai/dsh"] + args).returncode

def launch_generic_agent(agent_name, args):
    system_path = ":".join([p for p in os.environ.get("PATH", "").split(":") if "freellmapi-agents" not in p])
    bin_name = agent_name
    if agent_name == "mimo":
        bin_name = "mimo" if shutil.which("mimo", path=system_path) else "mimocode"

    bin_path = shutil.which(bin_name, path=system_path)
    if bin_path:
        try:
            target = os.path.realpath(bin_path)
            if "freellmapi-agents" in target and not target.endswith(bin_name):
                bin_path = None
        except Exception:
            pass

    if not bin_path:
        print(f"\n[FLM Dispatcher] Agent '{agent_name}' host engine is not installed on this system.", file=sys.stderr)
        print(f"Wrapper bin/flm-{agent_name} is ready to route to FreeLLMAPI once installed.", file=sys.stderr)
        return 1

    if not ensure_gateway_online():
        return 1

    gw = get_gateway_config()
    token = get_auth_token()
    env = os.environ.copy()
    env["OPENAI_BASE_URL"] = gw["openai_base_url"]
    env["OPENAI_API_BASE"] = gw["openai_base_url"]
    env["ANTHROPIC_BASE_URL"] = gw["anthropic_base_url"]
    if token:
        env["OPENAI_API_KEY"] = token
        env["ANTHROPIC_AUTH_TOKEN"] = token
        env["FREELLMAPI_API_KEY"] = token

    cmd = [bin_path]

    # Specific agent CLI adjustments
    if agent_name == "aider":
        if "--model" not in args:
            cmd.extend(["--model", "openai/auto"])
    elif agent_name == "qwen":
        if "-m" not in args and "--model" not in args:
            cmd.extend(["-m", "auto"])
    elif agent_name == "hermes":
        env["HERMES_INFERENCE_MODEL"] = "auto"
    elif agent_name == "goose":
        env["GOOSE_PROVIDER"] = "custom"

    cmd.extend(args)
    return subprocess.run(cmd, env=env).returncode

def main():
    if len(sys.argv) < 2:
        print("Usage: agent_launcher.py <agent_name> [args...]")
        sys.exit(1)

    agent = sys.argv[1].lower()
    args = sys.argv[2:]

    if agent == "claude":
        code = launch_claude(args)
    elif agent == "codex":
        code = launch_codex(args)
    elif agent == "gemini":
        code = launch_gemini(args)
    elif agent == "dsh":
        code = launch_dsh(args)
    else:
        code = launch_generic_agent(agent, args)

    sys.exit(code)

if __name__ == "__main__":
    main()
