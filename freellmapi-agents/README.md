# FreeLLMAPI Global AI Development Environment (`flm`)

A unified, high-reliability local AI engineering environment centered on **FreeLLMAPI**, coordinating local coding agents (**Claude Code**, **Codex CLI**, **Gemini CLI**, **DeepSeek Harness**), global **AI-Dev-Team** orchestration, and local **Qwen** bridges on Apple Silicon macOS.

---

## Architecture Overview

```
                      ┌───────────────────┐
                      │    Antigravity    │
                      └─────────┬─────────┘
                                │
                      ┌─────────▼─────────┐
                      │   AI DEV TEAM     │
                      │  ORCHESTRATION    │
                      └─────────┬─────────┘
                                │
                      ┌─────────▼─────────┐
                      │       FLM         │
                      │ Local Dispatcher  │
                      └─────────┬─────────┘
                                │
                      ┌─────────▼─────────┐
                      │    FreeLLMAPI     │
                      │ Gateway / Router  │
                      └─────────┬─────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
   ┌─────▼──────┐        ┌──────▼─────┐         ┌──────▼─────┐
   │  Google    │        │ OpenRouter │         │ Local Qwen │
   │  Gemini    │        │ / Groq / CF│         │   Bridge   │
   └────────────┘        └────────────┘         └────────────┘
```

---

## Quick Start & Main Commands

The unified dispatcher command is `flm` (accessible globally via `~/.local/bin/flm` or PATH):

```bash
# Environment status & doctor check
flm status
flm doctor

# Quota telemetry & model catalog
flm quotas
flm models
flm providers
flm routing

# Mode switching (Fast vs Normal)
flm mode fast       # Sub-second TTFT (<1.5s), high-throughput models
flm mode normal     # Balanced 1M context, high reasoning, robust fallback
flm mode status

# End-to-end performance and latency tests
flm test

# Launching agents through FreeLLMAPI
flm claude -p "Say OK"
flm codex exec --skip-git-repo-check --ephemeral "Say OK"
flm gemini
flm dsh

# Automated repair & backups
flm repair
flm backup
flm logs -n 50
```

---

## Native Compatibility & Integrations

- **`h4s`**: Existing workflow launcher is 100% preserved and verified at `/Users/subhajkar/.local/bin/h4s`.
- **Claude Code**: Configured at `~/.claude/settings.json` pointing directly to Anthropic Messages interface `http://127.0.0.1:31415`.
- **Codex CLI**: Configured at `~/.codex/config.toml` via `[model_providers.freellmapi]` pointing to `http://127.0.0.1:31415/v1` with Responses wire protocol.
- **Gemini CLI**: Retains Google OAuth mode with capability for `--freellmapi` and `--local-qwen` flags.
- **DeepSeek Harness (dsh)**: Running as active web service on `127.0.0.1:3080`.
- **Local Qwen**: Script verified at `/Users/subhajkar/Developer/qwen-antigravity/bridge.py` (FastAPI bridge on port 8787).
