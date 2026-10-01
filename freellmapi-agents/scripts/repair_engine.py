import os
import sys
import json
import shutil
import datetime
import subprocess

from common import (
    PROJECT_ROOT, CONFIG_DIR, BACKUPS_DIR, DATA_DIR,
    get_gateway_config, get_auth_token, load_json, save_json
)
from model_tracker import sync_model_health
from doctor import run_doctor

def create_backup_snapshot():
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    bdir = os.path.join(BACKUPS_DIR, f"repair_{ts}")
    os.makedirs(bdir, exist_ok=True)

    targets = [
        ("~/.claude/settings.json", "claude_settings.json"),
        ("~/.codex/config.toml", "codex_config.toml"),
        ("~/.gemini/settings.json", "gemini_settings.json"),
        ("~/.local/bin/h4s", "h4s"),
        ("~/.zshrc", "zshrc")
    ]
    backed_up = []
    for src, name in targets:
        sp = os.path.expanduser(src)
        if os.path.exists(sp):
            dp = os.path.join(bdir, name)
            shutil.copy2(sp, dp)
            backed_up.append((sp, dp))
    return bdir, backed_up

def rollback_snapshot(backed_up):
    print("Rolling back modifications from backup...")
    for orig, snap in backed_up:
        if os.path.exists(snap):
            shutil.copy2(snap, orig)
            print(f"  Restored {orig}")

def run_repair(dry_run=False):
    print("\n============================================================")
    print(" FREELLMAPI AUTOMATIC DIAGNOSTIC & REPAIR ENGINE")
    print("============================================================\n")

    gw = get_gateway_config()
    bdir, backed_up = create_backup_snapshot()
    print(f"Pre-repair snapshot created in: {bdir}")

    changes_made = []

    try:
        # 1. Verify and create directory layout
        dirs_to_verify = [
            "bin", "config", "scripts", "tests", "backups",
            "logs", "reports", "data", "docker", "docs"
        ]
        for d in dirs_to_verify:
            dp = os.path.join(PROJECT_ROOT, d)
            if not os.path.exists(dp):
                if not dry_run:
                    os.makedirs(dp, exist_ok=True)
                changes_made.append(f"Created missing directory: {d}/")

        # 2. Fix script permissions
        bin_dir = os.path.join(PROJECT_ROOT, "bin")
        scripts_dir = os.path.join(PROJECT_ROOT, "scripts")
        for folder in [bin_dir, scripts_dir]:
            if os.path.exists(folder):
                for fname in os.listdir(folder):
                    fpath = os.path.join(folder, fname)
                    if os.path.isfile(fpath) and (fname.endswith(".py") or fname.endswith(".sh") or "." not in fname):
                        curr_mode = os.stat(fpath).st_mode
                        if not (curr_mode & 0o111):
                            if not dry_run:
                                os.chmod(fpath, curr_mode | 0o755)
                            changes_made.append(f"Made executable: {folder}/{fname}")

        # 3. Check and repair Claude Code configuration
        claude_cfg = os.path.expanduser("~/.claude/settings.json")
        if os.path.exists(claude_cfg):
            try:
                with open(claude_cfg, "r") as f:
                    cdata = json.load(f)
                env = cdata.get("env", {})
                updated_claude = False

                target_url = gw["anthropic_base_url"]
                if env.get("ANTHROPIC_BASE_URL") != target_url:
                    env["ANTHROPIC_BASE_URL"] = target_url
                    updated_claude = True
                    changes_made.append(f"Repaired ANTHROPIC_BASE_URL -> {target_url}")

                if not env.get("ANTHROPIC_AUTH_TOKEN"):
                    tok = get_auth_token()
                    if tok:
                        env["ANTHROPIC_AUTH_TOKEN"] = tok
                        updated_claude = True
                        changes_made.append("Injected missing ANTHROPIC_AUTH_TOKEN into Claude settings")

                if updated_claude and not dry_run:
                    cdata["env"] = env
                    with open(claude_cfg, "w") as f:
                        json.dump(cdata, f, indent=2)
            except Exception as e:
                print(f"Error parsing Claude settings: {e}")

        # 4. Check and repair Codex configuration
        codex_cfg = os.path.expanduser("~/.codex/config.toml")
        if os.path.exists(codex_cfg):
            try:
                with open(codex_cfg, "r") as f:
                    lines = f.readlines()
                
                has_freellm_provider = any("model_providers.freellmapi" in l for l in lines)
                has_correct_url = any("base_url = \"http://127.0.0.1:31415/v1\"" in l for l in lines)

                if not has_freellm_provider or not has_correct_url:
                    changes_made.append("Codex config.toml needs provider refresh (run npx freellmapi setup-codex)")
            except Exception as e:
                print(f"Error checking Codex config: {e}")

        # 5. Check and repair h4s launcher permissions
        h4s_p = os.path.expanduser("~/.local/bin/h4s")
        if os.path.exists(h4s_p):
            mode = os.stat(h4s_p).st_mode
            if not (mode & 0o111):
                if not dry_run:
                    os.chmod(h4s_p, mode | 0o755)
                changes_made.append("Restored executable permissions on ~/.local/bin/h4s")

        # 6. Check and repair PATH in ~/.zshrc
        zshrc_p = os.path.expanduser("~/.zshrc")
        flm_bin_path = os.path.join(PROJECT_ROOT, "bin")
        if os.path.exists(zshrc_p):
            with open(zshrc_p, "r") as f:
                zshrc_content = f.read()
            if flm_bin_path not in zshrc_content:
                addition = f"\n# FreeLLMAPI Global Agent Environment CLI\nexport PATH=\"{flm_bin_path}:$PATH\"\n"
                if not dry_run:
                    with open(zshrc_p, "a") as f:
                        f.write(addition)
                changes_made.append(f"Added {flm_bin_path} to ~/.zshrc PATH")

        # 7. Sync Model Health Cache
        if not dry_run:
            sync_model_health()
            changes_made.append("Synchronized real-time model health cache in data/model_health.json")

        print("Applied Repairs:")
        if changes_made:
            for c in changes_made:
                print(f"  ✓ {c}")
        else:
            print("  ✓ All configuration files, paths, and permissions are already optimal.")

        # 8. Post-repair Validation
        print("\nValidating repaired environment with doctor...")
        valid = run_doctor()
        if not valid:
            print("\nValidation failed! Rolling back changes...")
            rollback_snapshot(backed_up)
            return False

        print("Repair complete and verified successfully!\n")
        return True

    except Exception as e:
        print(f"Exception during repair: {e}")
        rollback_snapshot(backed_up)
        return False

if __name__ == "__main__":
    is_dry = "--dry-run" in sys.argv
    success = run_repair(dry_run=is_dry)
    sys.exit(0 if success else 1)
