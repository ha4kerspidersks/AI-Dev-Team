# ARCHITECTURE SPECIFICATION — FREELLMAPI GLOBAL ENVIRONMENT

## 1. System Layers

1. **User / Host Orchestrator Layer**:
   - **Antigravity IDE & CLI (`agy`)**: Global pair programming assistant and agent coordination engine.
   - **AI-Dev-Team Global Dev Framework**: Roles, skills, memory, and orchestration in `~/Developer/AI-Dev-Team/`.

2. **Dispatcher & Protocol Bridge (`flm`)**:
   - Resides in `~/Developer/AI-Dev-Team/freellmapi-agents/bin/flm`.
   - Symlinked to `~/.local/bin/flm` for zero-latency execution from any shell or script.
   - Responsible for agent health probing, dynamic credential injection, task profile routing, and failover management.

3. **Core Local Gateway (FreeLLMAPI)**:
   - Application: `/Applications/FreeLLMAPI.app` (Electron runtime v0.4.1 / v0.11.0 UI).
   - Listening Address: `127.0.0.1:31415` (IPv4 loopback only; non-routable externally).
   - Database: `/Users/subhajkar/Library/Application Support/FreeLLMAPI/freeapi.db` (SQLite in WAL mode).
   - Logs: `/Users/subhajkar/Library/Application Support/FreeLLMAPI/logs/freeapi.log`.

4. **Wire Protocol Compatibility**:
   - **Anthropic Messages Protocol**: `http://127.0.0.1:31415` (root/v1). Used by Claude Code CLI and `h4s`.
   - **OpenAI Chat Protocol**: `http://127.0.0.1:31415/v1/chat/completions`. Used by OpenAI-compatible clients, Codex, Aider, Cline.
   - **OpenAI Responses Wire Protocol**: Used by Codex CLI (`wire_api = "responses"`).
   - **Gemini Native Protocol**: `http://127.0.0.1:31415/v1beta`. Used by Gemini CLI when routed locally.

5. **Upstream Providers & Fallback Engine**:
   - 20 provider platforms configured (Google, OpenRouter, Groq, Cloudflare, Ollama, ElectronHub, Routeway, etc.).
   - Local Qwen Bridge on `127.0.0.1:8787` (`qwen-antigravity/bridge.py`).

---

## 2. Directory Layout

```
~/Developer/AI-Dev-Team/freellmapi-agents/
├── bin/
│   ├── flm              # Main executable CLI entrypoint
│   ├── aider            # Agent wrapper for Aider
│   ├── opencode         # Agent wrapper for OpenCode
│   ├── qwen             # Agent wrapper for Qwen Code
│   ├── goose            # Agent wrapper for Goose
│   ├── cline            # Agent wrapper for Cline
│   ├── roo              # Agent wrapper for Roo Code
│   ├── kilo             # Agent wrapper for Kilo Code
│   ├── crush            # Agent wrapper for Crush
│   ├── dsh              # Agent wrapper for DeepSeek Harness
│   ├── mimo             # Agent wrapper for MiMo Code
│   ├── atomcode         # Agent wrapper for AtomCode
│   ├── openclaw         # Agent wrapper for OpenClaw
│   └── hermes           # Agent wrapper for Hermes Agent
├── config/
│   ├── gateway.json     # Endpoint ports, host, database paths
│   ├── routing.json     # Task classification profiles & quarantines
│   └── modes.json       # Operating mode definitions (Fast vs Normal)
├── scripts/
│   ├── common.py        # Shared utilities & credential handling
│   ├── doctor.py        # Diagnostic health inspection engine
│   ├── model_tracker.py # Telemetry & cooldown synchronizer
│   ├── model_manager.py # Model/quota/provider querying CLI
│   ├── tester.py        # End-to-end performance and latency suite
│   ├── repair_engine.py # Automated backup, repair, and rollback engine
│   └── agent_launcher.py# Dynamic agent dispatcher
├── data/
│   ├── model_health.json# Synchronized model health and cooldown state
│   └── performance_metrics.json # Latency benchmarks & TTFT logs
├── backups/             # Timestamped snapshots (excluded from git)
├── logs/                # Local runtime logs
├── reports/
│   ├── BEFORE_REPORT.md # Initial environment discovery report
│   └── AFTER_AUDIT_REPORT.md # Post-repair audit comparison
└── docs/                # Extended documentation
```
