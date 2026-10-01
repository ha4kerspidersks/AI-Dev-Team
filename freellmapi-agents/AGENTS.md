# AGENTS INTEGRATION SPECIFICATION

This document details the configuration, protocol, endpoints, and diagnostic status for all coding agents supported by the FreeLLMAPI environment.

---

## 1. Supported Agent Matrix

| Agent | Installed | Binary Location | Config File | FreeLLMAPI Wire Protocol | Base URL | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Claude Code** | YES | `/opt/homebrew/bin/claude` | `~/.claude/settings.json` | Anthropic Messages | `http://127.0.0.1:31415` | **OPERATIONAL (PASS)** |
| **h4s (Launcher)** | YES | `/Users/subhajkar/.local/bin/h4s` | Script wrapper | Anthropic Messages | `http://127.0.0.1:31415` | **OPERATIONAL (PASS)** |
| **Codex CLI** | YES | `/opt/homebrew/bin/codex` | `~/.codex/config.toml` | OpenAI Responses | `http://127.0.0.1:31415/v1` | **OPERATIONAL (PASS)** |
| **Gemini CLI** | YES | `/opt/homebrew/bin/gemini` | `~/.gemini/settings.json` | Google Personal OAuth / Gemini | `http://127.0.0.1:31415/v1beta` | **OPERATIONAL (PASS)** |
| **DeepSeek Harness** | YES | Port 3080 (`dsh web`) | `~/.dsh/settings.yaml` | OpenAI Chat | `http://127.0.0.1:31415/v1` | **OPERATIONAL (PASS)** |
| **Cursor** | YES | `/Applications/Cursor.app` | App Settings | OpenAI Chat via Tunnel | Tunnel URL | **INSTALLED** |
| **Aider** | NO | `bin/aider` wrapper | `~/.aider.conf.yml` | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **OpenCode** | NO | `bin/opencode` wrapper | `~/.config/opencode/opencode.json` | OpenAI Compatible | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **Qwen Code** | NO | `bin/qwen` wrapper | `~/.qwen/settings.json` | OpenAI or Gemini | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **Goose** | NO | `bin/goose` wrapper | `~/.config/goose/custom_providers/` | OpenAI Engine | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **Cline** | NO | `bin/cline` wrapper | `~/.cline/data/settings/` | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **Roo Code** | NO | `bin/roo` wrapper | `~/.roo/` | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **Kilo Code** | NO | `bin/kilo` wrapper | Config | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **Crush** | NO | `bin/crush` wrapper | Config | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **MiMo Code** | NO | `bin/mimo` wrapper | Config | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **AtomCode** | NO | `bin/atomcode` wrapper | Config | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **OpenClaw** | NO | `bin/openclaw` wrapper | Config | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |
| **Hermes** | NO | `bin/hermes` wrapper | Config | OpenAI Chat | `http://127.0.0.1:31415/v1` | READY TO INSTALL |

---

## 2. Launching Agents

Every agent can be launched through the unified dispatcher:

```bash
# Claude Code with FreeLLMAPI environment injected
flm claude

# Codex CLI non-interactive execution
flm codex exec "fix syntax error in index.ts"

# Gemini CLI with local Qwen bridge or FreeLLMAPI
flm gemini --local-qwen
flm gemini --freellmapi
```
