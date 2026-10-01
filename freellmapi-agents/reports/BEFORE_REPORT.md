# GLOBAL AI DEVELOPMENT ENVIRONMENT — BEFORE DISCOVERY REPORT

**Generated:** 2026-10-01
**Location:** `/Users/subhajkar/Developer/AI-Dev-Team/freellmapi-agents/reports/BEFORE_REPORT.md`
**System:** Apple Silicon macOS

---

## 1. System & Host Environment

- **Operating System:** macOS 27.0.1 (Build 26A434)
- **Kernel:** Darwin 27.0.0 (Darwin Kernel Version 27.0.0: Tue Aug 11 21:05:48 PDT 2026; root:xnu-13432.1.9~1/RELEASE_ARM64_T6041)
- **Architecture:** `arm64` (Apple Silicon)
- **User Shell:** `/bin/zsh`
- **PATH Components:**
  - `/opt/homebrew/opt/ruby/bin`
  - `/opt/homebrew/lib/ruby/gems/3.4.0/bin`
  - `/opt/homebrew/opt/openjdk/bin`
  - `/Users/subhajkar/.antigravity-ide/antigravity-ide/bin`
  - `/opt/homebrew/bin`
  - `/Users/subhajkar/.local/bin`
  - `/usr/local/bin`
  - `/usr/bin`
  - `/bin`
  - `/usr/sbin`
  - `/sbin`

---

## 2. Core Tooling Versions

- **Homebrew:** 7.0.6
- **Node.js:** v26.9.0
- **npm:** 12.0.2
- **npx:** 12.0.2
- **Python:** 3.14.7 (Homebrew)
- **Git:** 2.55.0
- **Docker:** NOT INSTALLED
- **Docker Compose:** NOT INSTALLED

---

## 3. FreeLLMAPI Installation & Gateway

- **Application Location:** `/Applications/FreeLLMAPI.app` (Electron runtime)
- **Running Process:** PID 1318 `/Applications/FreeLLMAPI.app/Contents/MacOS/FreeLLMAPI`
- **Gateway Version:** v0.4.1 (protocol compatible with FreeLLMAPI Desktop v0.11.0)
- **Primary Gateway Endpoint:** `http://127.0.0.1:31415`
- **Active Listening Port:** `127.0.0.1:31415` (TCP IPv4)
- **CLI Package:** `freellmapi` CLI available via `npx freellmapi` (supports setup-claude, setup-codex, setup-aider, setup-opencode, etc.)
- **Configuration & Storage:**
  - Settings: `/Users/subhajkar/Library/Application Support/FreeLLMAPI/config.json`
  - SQLite Database: `/Users/subhajkar/Library/Application Support/FreeLLMAPI/freeapi.db` (20.5MB, WAL mode enabled)
  - Logs: `/Users/subhajkar/Library/Application Support/FreeLLMAPI/logs/freeapi.log`
- **Total Catalog Models:** 863+ models registered across 20 provider platforms.
- **Exposed Models via `/v1/models`:** 496 models returned.
- **Wire Protocols Supported:**
  - Anthropic Messages API: `http://127.0.0.1:31415/v1/messages` (Root/V1 compatible)
  - OpenAI Chat Completions: `http://127.0.0.1:31415/v1/chat/completions`
  - OpenAI Models: `http://127.0.0.1:31415/v1/models`

---

## 4. FreeLLMAPI Health & Key Telemetry

- **Total Provider Keys Configured:** 20 keys across 20 platforms:
  - `openrouter`: 1 key (healthy)
  - `ollama`: 1 key (healthy)
  - `google`: 1 key (healthy)
  - `groq`: 1 key (healthy)
  - `waterfall`: 1 key (healthy)
  - `anyapi`: 1 key (healthy)
  - `router9`: 1 key (frequent HTTP 429 rate limit errors during health checks)
  - `cerebras`: 1 key (healthy)
  - `sail`: 1 key (healthy)
  - `electronhub`: 1 key (healthy)
  - `experiential`: 1 key (healthy)
  - `septor`: 1 key (healthy, 59/60 daily requests remaining)
  - `speechify`: 1 key (healthy)
  - `nvidia`: 1 key (healthy)
  - `unorouter`: 1 key (healthy)
  - `orcarouter`: 1 key (healthy)
  - `routeway`: 1 key (healthy)
  - `github`: 1 key (healthy)
  - `blaze`: 1 key (healthy)
  - `cloudflare`: 1 key (healthy)

---

## 5. Installed AI Agents & Diagnostic Status

| Agent | Binary / Location | Version | Config Location | Initial Status |
| :--- | :--- | :--- | :--- | :--- |
| **Claude Code** | `/opt/homebrew/bin/claude` | 2.1.284 | `~/.claude/settings.json` | INSTALLED / CONFIGURED (experiencing latency/timeout with `auto`) |
| **Codex CLI** | `/opt/homebrew/bin/codex` | 0.155.1 | `~/.codex/config.toml` | INSTALLED / CONFIGURED for FreeLLMAPI (`/v1`) |
| **Gemini CLI** | `/opt/homebrew/bin/gemini` | 0.60.0 | `~/.gemini/settings.json` | INSTALLED / Configured for Google Personal OAuth |
| **Cursor** | `/Applications/Cursor.app`, `/usr/local/bin/cursor` | Desktop App | System Application | INSTALLED |
| **DeepSeek Harness (dsh)** | Port 3080 (`dsh web --no-open`) | Node runtime | Port 3080 | RUNNING AS BACKGROUND SERVICE |
| **Aider** | Not in PATH | N/A | None | NOT INSTALLED |
| **OpenCode** | Not in PATH | N/A | None | NOT INSTALLED |
| **Qwen Code** | Not in PATH | N/A | None | NOT INSTALLED |
| **Cline** | Not in PATH | N/A | None | NOT INSTALLED |
| **Goose** | Not in PATH | N/A | None | NOT INSTALLED |
| **Roo / Kilo / Crush / etc.** | Not in PATH | N/A | None | NOT INSTALLED |

---

## 6. Existing Infrastructure & Orchestration

- **Antigravity IDE & CLI:**
  - IDE: `/Users/subhajkar/.antigravity-ide/antigravity-ide`
  - CLI: `/Users/subhajkar/.local/bin/agy` (v1.17.0)
  - Router wrapper in `~/.zshrc`: `agy()` routing between `antigravity` and `agy`.
- **AI-Dev-Team Global Framework:**
  - Root: `/Users/subhajkar/Developer/AI-Dev-Team`
  - CLI: `/Users/subhajkar/.local/bin/ai-team` -> `/Users/subhajkar/Developer/AI-Dev-Team/scripts/ai-team`
  - Spec Kit: `/Users/subhajkar/Developer/AI-Dev-Team/environments/speckit-env/bin/specify`
  - Strix: `/Users/subhajkar/.local/bin/strix`
- **Local Qwen Infrastructure:**
  - Location: `/Users/subhajkar/Developer/qwen-antigravity/`
  - Script: `bridge.py` (FastAPI bridge on `127.0.0.1:8787`) bridging Gemini API schema to HuggingFace `Qwen/Qwen3.8-27B`.
  - Python Environment: `/Users/subhajkar/Developer/qwen-antigravity/.venv` (FastAPI, httpx, uvicorn verified).
- **GitHub Copilot Sidecar:**
  - Location: `~/.gemini/config/sidecars/copilot-bridge.mjs`
- **Existing MCP Infrastructure:**
  - Global Gemini MCP: `~/.gemini/config/mcp_config.json`
  - Codex MCP: `~/.codex/config.toml` (node_repl, filesystem, memory, sequential-thinking, universal-developer)
  - AI-Dev-Team MCP: `/Users/subhajkar/Developer/AI-Dev-Team/mcp/`
  - Claude Desktop MCP: `~/Library/Application Support/Claude/claude_desktop_config.json`

---

## 7. Analysis of the Existing `h4s` Script & Claude Code Issue

- **Location:** `/Users/subhajkar/.local/bin/h4s`
- **Type:** Executable POSIX Bash script.
- **Workflow:**
  1. Checks FreeLLMAPI connectivity on `127.0.0.1:31415`.
  2. Extracts token from `~/.claude/settings.json` (`env.ANTHROPIC_AUTH_TOKEN`).
  3. Verifies auth via `GET ${ENDPOINT}/v1/models`.
  4. Exports `ANTHROPIC_BASE_URL="http://127.0.0.1:31415"` and `ANTHROPIC_AUTH_TOKEN`.
  5. Executes `/opt/homebrew/bin/claude "$@"`.
- **Root Cause of Failure:**
  - `~/.claude/settings.json` was configured with `ANTHROPIC_MODEL: auto`.
  - When Claude Code dispatched complex coding prompts with tool definitions to `auto`, FreeLLMAPI routed them to `openrouter/nvidia/nemotron-3.5-lightning:free`.
  - Upstream OpenRouter Free tier on `nemotron-3.5-lightning:free` showed average latency of 174.6s, with multiple requests taking 200s to 352s or dropping the SSE connection unexpectedly ("OpenRouter stream ended unexpectedly").
  - FreeLLMAPI's internal fallback then cascaded to Cloudflare `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, which has only a 24k token context window, immediately throwing HTTP 413: "The estimated number of input and maximum output tokens exceeded this model context window limit (24000)".
  - This caused Claude Code sessions to hang, disconnect, or fail with limit/context errors.
  - In contrast, routing to high-throughput, high-context models (`nvidia/nemotron-3-super-120b-a12b:free`, `gemini-2.5-flash`, `gpt-oss:120b`) completes with 100% success and 1s to 5s TTFT!

---

## 8. Relevant Listening Ports & Processes

- `127.0.0.1:31415` -> `FreeLLMAPI` (PID 1318)
- `127.0.0.1:3080`  -> `dsh web --no-open` (PID 57349)
- `127.0.0.1:56042` -> `agy` (PID 55943)
- `127.0.0.1:9004`  -> `Electron` IDE helper
- `127.0.0.1:20241` -> `cloudflared` (PID 3260)
- `*:5173`          -> `node` local dev server (PID 3159)

*(Note: Sensitive tokens and credentials have been strictly redacted from this report.)*
