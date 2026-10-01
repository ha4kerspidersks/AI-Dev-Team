import os
import json
import sqlite3
import urllib.request
import urllib.error
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(PROJECT_ROOT, "config")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
BACKUPS_DIR = os.path.join(PROJECT_ROOT, "backups")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(BACKUPS_DIR, exist_ok=True)

def load_json(path, default=None):
    if not os.path.exists(path):
        return default if default is not None else {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    tmp_path = f"{path}.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp_path, path)

def get_gateway_config():
    config_path = os.path.join(CONFIG_DIR, "gateway.json")
    return load_json(config_path, {
        "host": "127.0.0.1",
        "port": 31415,
        "base_url": "http://127.0.0.1:31415",
        "openai_base_url": "http://127.0.0.1:31415/v1",
        "anthropic_base_url": "http://127.0.0.1:31415",
        "db_path": os.path.expanduser("~/Library/Application Support/FreeLLMAPI/freeapi.db"),
        "log_path": os.path.expanduser("~/Library/Application Support/FreeLLMAPI/logs/freeapi.log")
    })

def get_auth_token():
    token = os.environ.get("FREELLMAPI_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")
    if token:
        return token
    claude_settings = os.path.expanduser("~/.claude/settings.json")
    if os.path.exists(claude_settings):
        try:
            with open(claude_settings, "r", encoding="utf-8") as f:
                data = json.load(f)
                token = data.get("env", {}).get("ANTHROPIC_AUTH_TOKEN", "")
                if token:
                    return token
        except Exception:
            pass
    return ""

def redact(val):
    if not val:
        return ""
    s = str(val)
    if len(s) <= 8:
        return "***"
    return f"{s[:4]}...{s[-4:]}"

def get_db_connection(readonly=True):
    gw = get_gateway_config()
    db_path = gw.get("db_path")
    if not os.path.exists(db_path):
        return None
    uri = f"file:{db_path}?mode=ro" if readonly else db_path
    conn = sqlite3.connect(uri, uri=readonly)
    conn.row_factory = sqlite3.Row
    return conn

def check_gateway_reachable(timeout=2.0):
    gw = get_gateway_config()
    url = f"{gw['base_url']}/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "FLM-Dispatcher/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return res.status == 200
    except Exception:
        return False

def check_gateway_models(timeout=3.0):
    gw = get_gateway_config()
    token = get_auth_token()
    url = f"{gw['openai_base_url']}/models"
    headers = {"User-Agent": "FLM-Dispatcher/1.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as res:
            if res.status == 200:
                data = json.loads(res.read().decode())
                return True, len(data.get("data", []))
            return False, 0
    except Exception as e:
        return False, str(e)
