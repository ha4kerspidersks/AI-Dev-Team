import os
import sys
import json
import sqlite3

from common import (
    CONFIG_DIR, DATA_DIR, get_db_connection, load_json, save_json
)
from model_tracker import get_cached_health

MODES_FILE = os.path.join(CONFIG_DIR, "modes.json")
ROUTING_FILE = os.path.join(CONFIG_DIR, "routing.json")

def cmd_models(filter_q=None, tools_only=False):
    conn = get_db_connection(readonly=True)
    if not conn:
        print("Error: Could not connect to FreeLLMAPI database.")
        return
    c = conn.cursor()
    query = """
        SELECT m.platform, m.model_id, m.display_name, m.context_window, m.supports_tools, m.enabled
        FROM models m
        WHERE m.enabled = 1
    """
    params = []
    if tools_only:
        query += " AND m.supports_tools = 1"
    if filter_q:
        query += " AND (m.model_id LIKE ? OR m.display_name LIKE ? OR m.platform LIKE ?)"
        pattern = f"%{filter_q}%"
        params.extend([pattern, pattern, pattern])
    query += " ORDER BY m.platform ASC, m.context_window DESC"

    rows = c.execute(query, params).fetchall()
    print(f"\nAvailable FreeLLMAPI Models ({len(rows)} matching):")
    print("-" * 88)
    print(f"{'Platform':14s} | {'Model ID':42s} | {'Context':9s} | {'Tools':5s}")
    print("-" * 88)
    for r in rows[:40]:
        tools_str = "YES" if r['supports_tools'] else "NO"
        ctx_str = f"{r['context_window']:,}" if r['context_window'] else "N/A"
        print(f"{r['platform']:14s} | {r['model_id'][:42]:42s} | {ctx_str:9s} | {tools_str:5s}")
    if len(rows) > 40:
        print(f"... and {len(rows) - 40} more models. Use 'flm models <filter>' to narrow down.")
    print("-" * 88 + "\n")
    conn.close()

def cmd_providers():
    conn = get_db_connection(readonly=True)
    if not conn:
        print("Error: Could not connect to FreeLLMAPI database.")
        return
    c = conn.cursor()
    rows = c.execute("SELECT id, platform, status, last_checked_at, last_health_error FROM api_keys ORDER BY id ASC").fetchall()
    print("\nConfigured FreeLLMAPI Providers & Platforms:")
    print("-" * 88)
    print(f"{'ID':3s} | {'Platform':15s} | {'Status':10s} | {'Last Checked':19s} | {'Notes / Errors'}")
    print("-" * 88)
    for r in rows:
        err = r['last_health_error'] or "OK"
        print(f"{r['id']:3d} | {r['platform']:15s} | {r['status']:10s} | {str(r['last_checked_at'])[:19]:19s} | {err[:35]}")
    print("-" * 88 + "\n")
    conn.close()

def cmd_quotas():
    health = get_cached_health()
    quotas = health.get("quotas", {})
    cooldowns = health.get("cooldowns", {})

    print("\nFreeLLMAPI Quota Pools & Cooldown Telemetry:")
    print("-" * 88)
    print(f"{'Platform':14s} | {'Pool / Metric':28s} | {'Remaining / Limit':20s} | {'Reset / Status'}")
    print("-" * 88)

    for plat, pools in quotas.items():
        for p in pools:
            rem = f"{p['remaining']}/{p['limit']}" if p['limit'] is not None else (f"{p['remaining']}" if p['remaining'] is not None else "unmetered")
            reset = str(p['reset_at'] or p['notes'] or "N/A")[:24]
            metric_str = f"{p['pool']} ({p['metric']})"[:28]
            print(f"{plat:14s} | {metric_str:28s} | {rem:20s} | {reset}")

    active_cds = [cd for cd in cooldowns.values() if cd.get("is_active")]
    print("-" * 88)
    if active_cds:
        print(f"Active Rate-Limit Cooldowns ({len(active_cds)}):")
        for k, v in cooldowns.items():
            if v.get("is_active"):
                print(f"  * {k:40s} -> cooling for {v['remaining_seconds']}s ({v['source']})")
    else:
        print("Active Rate-Limit Cooldowns: None (All active models ready)")
    print("-" * 88 + "\n")

def cmd_routing():
    routing_cfg = load_json(ROUTING_FILE)
    modes_cfg = load_json(MODES_FILE)
    active_mode = modes_cfg.get("active_mode", "normal")
    profiles = routing_cfg.get("task_profiles", {})

    print(f"\nModel Routing Profiles (Current Mode: {active_mode.upper()}):")
    print("=" * 88)
    for name, p in profiles.items():
        print(f"[{name}] - {p.get('description', '')}")
        print(f"  Primary:   {p.get('primary')}")
        print(f"  Fallbacks: {' -> '.join(p.get('fallbacks', []))}")
        if p.get('preferred_providers'):
            print(f"  Providers: {', '.join(p.get('preferred_providers'))}")
        print()
    blocked = routing_cfg.get("blocked_or_quarantined_models", [])
    if blocked:
        print("Quarantined Models (Excluded from Auto-Routing):")
        for b in blocked:
            print(f"  x {b['platform']}/{b['model_id']}: {b['reason']}")
    print("=" * 88 + "\n")

def cmd_mode(target=None):
    modes_cfg = load_json(MODES_FILE)
    if not target or target == "status":
        print(f"Active Mode: {modes_cfg.get('active_mode', 'normal').upper()}")
        mode_info = modes_cfg.get("modes", {}).get(modes_cfg.get("active_mode", "normal"), {})
        print(f"Description: {mode_info.get('description', '')}")
        print(f"Claude Model: {mode_info.get('default_claude_model')}")
        print(f"Codex Model:  {mode_info.get('default_codex_model')}")
        return

    target = target.lower()
    if target not in ["fast", "normal"]:
        print("Error: Invalid mode. Usage: flm mode [fast|normal|status]")
        sys.exit(1)

    modes_cfg["active_mode"] = target
    save_json(MODES_FILE, modes_cfg)
    print(f"Switched FreeLLMAPI mode to: {target.upper()}")
    mode_info = modes_cfg.get("modes", {}).get(target, {})
    print(f"Description: {mode_info.get('description', '')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: model_manager.py [models|providers|quotas|routing|mode] [args...]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "models":
        q = sys.argv[2] if len(sys.argv) > 2 else None
        tools = "--tools" in sys.argv
        cmd_models(q, tools)
    elif cmd == "providers":
        cmd_providers()
    elif cmd == "quotas":
        cmd_quotas()
    elif cmd == "routing":
        cmd_routing()
    elif cmd == "mode":
        target = sys.argv[2] if len(sys.argv) > 2 else None
        cmd_mode(target)
    else:
        print(f"Unknown subcommand: {cmd}")
        sys.exit(1)
