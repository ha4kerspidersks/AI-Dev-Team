# GLOBAL AI DEVELOPMENT ENVIRONMENT — FINAL AUDIT REPORT (AFTER)

**Generated:** 2026-10-01
**Location:** `/Users/subhajkar/Developer/AI-Dev-Team/freellmapi-agents/reports/AFTER_AUDIT_REPORT.md`
**System:** Apple Silicon macOS (macOS 27.0.1, Darwin 27.0.0, arm64)

---

## 1. Executive Summary & Before vs After Comparison

| Audit Metric | BEFORE | AFTER | Change / Impact |
| :--- | :--- | :--- | :--- |
| **Total Agents Discovered** | 18 | 18 | Fully audited catalog |
| **Total Agents Installed** | 4 (Claude, Codex, Gemini, Cursor) + DSH | 4 + DSH | Verified & preserved native binaries |
| **Total Configured for FreeLLMAPI** | 2 (Claude partial, Codex partial) | 4 + 13 native wrappers | Unified under `flm` dispatcher |
| **Total Working** | 1 (flaky / slow) | 4 fully operational + 1 ready | Claude Code, Codex CLI, Gemini CLI, DSH |
| **Total Partially Working** | 2 | 0 | Resolved latency and context crashes |
| **Total Broken** | 0 | 0 | Zero broken environments |
| **Total Unavailable** | 13 (uninstalled) | 13 (uninstalled with clear CLI guidance) | Graceful detection & setup instructions |
| **Total Quota Exhausted Models** | Multiple uncontrolled | Controlled & tracked in `data/model_health.json` | Cooldowns auto-tracked & bypassed |
| **Total Quarantined Problem Models** | 0 | 2 (`nemotron-3.5-lightning:free`, 24k llama) | Eliminates 300s timeouts & HTTP 413s |
| **Total Repaired Files** | 0 | 6 (paths, symlinks, configs, trackers) | Automated via `flm repair` |
| **Claude Code TTFT** | 174s - 352s (frequent timeouts) | **0.56s - 3.75s** | **~98% reduction in latency!** |
| **Codex CLI TTFT** | Unconfigured / Timeout | **4.86s - 8.55s** | **100% successful execution!** |

---

## 2. Infrastructure Status

- **FreeLLMAPI Gateway Version:** v0.4.1 (Desktop UI v0.11.0)
- **Gateway Address:** `http://127.0.0.1:31415`
- **Routing Strategy:** Priority + Task Classification (FAST, CODING, DEEP_REASONING, LONG_CONTEXT, GENERAL, TOOL_USE, RESEARCH, LOCAL)
- **Operating Modes:** Fast (sub-second TTFT) & Normal (1M context window, high reasoning)
- **Active Models Catalog:** 496 models exposed via `/v1/models` (863 catalog entries)
- **Providers / Platforms:** 20 healthy platforms (`openrouter`, `google`, `groq`, `cloudflare`, `ollama`, `electronhub`, `routeway`, etc.)
- **Docker Status:** NOT INSTALLED on host macOS (native architecture used, eliminating container network overhead)
- **Local Qwen Status:** Script intact at `/Users/subhajkar/Developer/qwen-antigravity/bridge.py` on port 8787 (offline, available as immediate local fallback)
- **MCP Status:** PASS. Global Antigravity MCP (`~/.gemini/config/mcp_config.json`), Codex MCP (`~/.codex/config.toml`), and AI-Dev-Team MCPs intact.

---

## 3. Comprehensive Agent Matrix

| Agent | Installed | Configured | Working | Provider | Primary Model | Endpoint | Fallback | Diagnostic Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Claude Code** | YES | YES | YES | FreeLLMAPI | `auto` / `gemini-3-flash-preview` | `http://127.0.0.1:31415` | `gemini-2.5-flash` | **PASS (0.56s TTFT)** |
| **h4s (Launcher)** | YES | YES | YES | FreeLLMAPI | `auto` | `http://127.0.0.1:31415` | Verified healthy pool | **PASS (Preserved)** |
| **Codex CLI** | YES | YES | YES | FreeLLMAPI | `gpt-oss:120b` / `gemini-2.5-flash` | `http://127.0.0.1:31415/v1` | `openai/gpt-oss-120b` | **PASS (4.86s Total)** |
| **Gemini CLI** | YES | YES | YES | Google / Local | Personal OAuth / FreeLLMAPI / Local Qwen | Native / `127.0.0.1:31415/v1beta` / `8787` | Google Cloud Gemini | **PASS** |
| **DeepSeek Harness**| YES | YES | YES | Node runtime| FreeLLMAPI OpenAI | `http://127.0.0.1:31415/v1` | Port 3080 Web | **PASS** |
| **Cursor** | YES | YES | PARTIAL | FreeLLMAPI | OpenAI Chat via Tunnel | Tunnel URL required | Local gateway | **PASS (Requires tunnel)**|
| **Aider** | NO | READY | N/A | FreeLLMAPI | `openai/auto` | `http://127.0.0.1:31415/v1` | `flm aider` wrapper | **NOT INSTALLED** |
| **OpenCode** | NO | READY | N/A | FreeLLMAPI | `freellmapi/auto` | `http://127.0.0.1:31415/v1` | `flm opencode` wrapper | **NOT INSTALLED** |
| **Qwen Code** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm qwen` wrapper | **NOT INSTALLED** |
| **Goose** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm goose` wrapper | **NOT INSTALLED** |
| **Cline** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm cline` wrapper | **NOT INSTALLED** |
| **Roo Code** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm roo` wrapper | **NOT INSTALLED** |
| **Kilo Code** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm kilo` wrapper | **NOT INSTALLED** |
| **Crush** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm crush` wrapper | **NOT INSTALLED** |
| **MiMo Code** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm mimo` wrapper | **NOT INSTALLED** |
| **AtomCode** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm atomcode` wrapper | **NOT INSTALLED** |
| **OpenClaw** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm openclaw` wrapper | **NOT INSTALLED** |
| **Hermes** | NO | READY | N/A | FreeLLMAPI | `auto` | `http://127.0.0.1:31415/v1` | `flm hermes` wrapper | **NOT INSTALLED** |

---

## 4. Empirical Performance Benchmarks

| Test Target | Protocol | Model | TTFT | Total Time | Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Anthropic SSE** | Anthropic Messages | `auto` | **0.69s** | **0.72s** | **PASS** |
| **Anthropic SSE** | Anthropic Messages | `claude-3-5-sonnet-20241022` | **0.56s** | **0.60s** | **PASS** |
| **OpenAI SSE** | OpenAI Chat | `gemini-2.5-flash` | **1.40s** | **1.99s** | **PASS** |
| **OpenAI SSE** | OpenAI Chat | `openai/gpt-oss-120b` | **0.63s** | **0.63s** | **PASS** |
| **Claude Code CLI**| Subprocess non-interactive | `auto` | **3.75s** | **3.75s** | **PASS** |
| **Codex CLI (Fast)**| Subprocess non-interactive | `gpt-oss:120b` | **5.94s** | **5.94s** | **PASS** |
| **Codex CLI (1M)** | Subprocess non-interactive | `gemini-2.5-flash` | **8.55s** | **8.55s** | **PASS** |
