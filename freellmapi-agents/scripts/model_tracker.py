import os
import sys
import json
import time
import sqlite3
import urllib.request
import urllib.error
from datetime import datetime

from common import (
    PROJECT_ROOT, CONFIG_DIR, DATA_DIR, get_db_connection, load_json, save_json,
    get_gateway_config, get_auth_token
)

HEALTH_FILE = os.path.join(DATA_DIR, "model_health.json")
ROUTING_FILE = os.path.join(CONFIG_DIR, "routing.json")

# State Machine Definitions:
# HEALTHY     -> Success rate >= 80%, no active cooldown, latency acceptable (<15s)
# DEGRADED    -> Intermittent errors (50-79%), elevated latency (15s-45s)
# FAILED      -> Repeated 5xx errors or 0% success on recent requests
# QUARANTINED -> In blocked/quarantined config, active multi-hour cooldown, or all upstream providers exhausted
# RETEST      -> Model queued for or undergoing probe retest
def classify_health_state(tot, succ, err, avg_lat, is_cooling, cd_rem_sec, is_blocked, recent_errs):
    if is_blocked:
        return "QUARANTINED"
    if is_cooling and cd_rem_sec > 1800:
        return "QUARANTINED"
    if is_cooling:
        return "DEGRADED"
    if recent_errs >= 3 or (tot >= 3 and (succ / tot) == 0):
        return "FAILED"
    if tot >= 3 and (succ / tot) < 0.5:
        return "FAILED"
    if tot >= 3 and (succ / tot) < 0.8:
        return "DEGRADED"
    if avg_lat and avg_lat > 25.0:
        return "DEGRADED"
    return "HEALTHY"

def probe_model_live(model_name, timeout=8.0):
    gw = get_gateway_config()
    token = get_auth_token()
    url = f"{gw['openai_base_url']}/chat/completions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": "Reply with OK"}],
        "max_tokens": 10,
        "stream": True
    }
    t0 = time.time()
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as res:
            ttft = None
            first_chunk = ""
            for line in res:
                dec = line.decode("utf-8", errors="replace").strip()
                if not ttft and dec.startswith("data:"):
                    ttft = time.time() - t0
                if dec.startswith("data:") and "[DONE]" not in dec:
                    try:
                        cj = json.loads(dec[5:].strip())
                        first_chunk += cj.get("choices", [{}])[0].get("delta", {}).get("content", "")
                    except Exception:
                        pass
            total_time = round(time.time() - t0, 3)
            return {
                "success": True,
                "ttft_sec": round(ttft, 3) if ttft else total_time,
                "total_sec": total_time,
                "response": first_chunk.strip()[:20],
                "error": None
            }
    except Exception as e:
        total_time = round(time.time() - t0, 3)
        return {
            "success": False,
            "ttft_sec": None,
            "total_sec": total_time,
            "response": None,
            "error": str(e)
        }

def sync_model_health():
    conn = get_db_connection(readonly=True)
    if not conn:
        return {"error": "Unable to connect to FreeLLMAPI database"}

    now_ms = int(time.time() * 1000)
    c = conn.cursor()

    routing_cfg = load_json(ROUTING_FILE, {})
    blocked_entries = routing_cfg.get("blocked_or_quarantined_models", [])
    blocked_ids = set(b.get("model_id") for b in blocked_entries)

    # 1. Fetch active cooldowns
    cooldowns = {}
    for r in c.execute("SELECT platform, model_id, expires_at_ms, source FROM rate_limit_cooldowns").fetchall():
        key = f"{r['platform']}/{r['model_id']}"
        rem_sec = max(0, (r['expires_at_ms'] - now_ms) / 1000.0)
        cooldowns[key] = {
            "expires_at_ms": r['expires_at_ms'],
            "remaining_seconds": round(rem_sec, 1),
            "source": r['source'],
            "is_active": r['expires_at_ms'] > now_ms
        }

    # 2. Fetch provider quota state
    quotas = {}
    for r in c.execute("SELECT platform, quota_pool_key, metric, limit_value, remaining_value, reset_at, source, notes FROM provider_quota_state").fetchall():
        plat = r['platform']
        if plat not in quotas:
            quotas[plat] = []
        quotas[plat].append({
            "pool": r['quota_pool_key'],
            "metric": r['metric'],
            "limit": r['limit_value'],
            "remaining": r['remaining_value'],
            "reset_at": r['reset_at'],
            "source": r['source'],
            "notes": r['notes']
        })

    # 3. Aggregate request statistics (latency, successes, failures)
    stats_query = """
        SELECT platform, model_id,
               COUNT(*) as total_requests,
               SUM(CASE WHEN status='success' THEN 1 ELSE 0 END) as successes,
               SUM(CASE WHEN status='error' THEN 1 ELSE 0 END) as errors,
               SUM(CASE WHEN status='canceled' THEN 1 ELSE 0 END) as canceled,
               AVG(CASE WHEN status='success' THEN latency_ms ELSE NULL END) as avg_latency_ms,
               MIN(CASE WHEN status='success' THEN latency_ms ELSE NULL END) as min_latency_ms,
               MAX(CASE WHEN status='success' THEN latency_ms ELSE NULL END) as max_latency_ms,
               MAX(CASE WHEN status='success' THEN created_at ELSE NULL END) as last_success,
               MAX(CASE WHEN status='error' THEN created_at ELSE NULL END) as last_failure
        FROM requests
        GROUP BY platform, model_id
    """
    
    models_stats = {}
    for r in c.execute(stats_query).fetchall():
        key = f"{r['platform']}/{r['model_id']}"
        tot = r['total_requests']
        succ = r['successes']
        err = r['errors']
        avg_lat = round(r['avg_latency_ms'] / 1000.0, 2) if r['avg_latency_ms'] else None
        
        # Check active cooldown
        cd = cooldowns.get(key, {})
        is_cooling = cd.get("is_active", False)
        cd_rem = cd.get("remaining_seconds", 0)

        # Check if quarantined in config
        is_blocked = (r['model_id'] in blocked_ids) or (key in blocked_ids) or (f"{r['platform']}/{r['model_id']}" in blocked_ids)

        # Estimate recent errors by checking last attempt
        recent_errs = 1 if r['last_failure'] and (not r['last_success'] or r['last_failure'] > r['last_success']) else 0

        # Transition via State Machine
        status = classify_health_state(tot, succ, err, avg_lat, is_cooling, cd_rem, is_blocked, recent_errs)

        models_stats[key] = {
            "platform": r['platform'],
            "model_id": r['model_id'],
            "total_requests": tot,
            "successes": succ,
            "errors": err,
            "canceled": r['canceled'],
            "success_rate": round((succ / tot) * 100, 1) if tot > 0 else 0,
            "avg_latency_sec": avg_lat,
            "min_latency_sec": round(r['min_latency_ms'] / 1000.0, 2) if r['min_latency_ms'] else None,
            "max_latency_sec": round(r['max_latency_ms'] / 1000.0, 2) if r['max_latency_ms'] else None,
            "last_success": r['last_success'],
            "last_failure": r['last_failure'],
            "status": status,
            "cooldown": cd
        }

    # 4. Compile health catalog
    health_data = {
        "updated_at": datetime.now().isoformat(),
        "total_tracked_models": len(models_stats),
        "active_cooldowns_count": sum(1 for cd in cooldowns.values() if cd.get("is_active")),
        "cooldowns": cooldowns,
        "quotas": quotas,
        "models": models_stats
    }

    save_json(HEALTH_FILE, health_data)
    conn.close()
    return health_data

def get_cached_health():
    if not os.path.exists(HEALTH_FILE):
        return sync_model_health()
    if time.time() - os.path.getmtime(HEALTH_FILE) > 60:
        return sync_model_health()
    return load_json(HEALTH_FILE)

if __name__ == "__main__":
    res = sync_model_health()
    print(f"Synchronized model health: {res.get('total_tracked_models')} models tracked, {res.get('active_cooldowns_count')} active cooldowns.")

