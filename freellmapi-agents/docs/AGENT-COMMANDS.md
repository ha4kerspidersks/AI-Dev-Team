# FreeLLMAPI Unified Agent Execution Guide

This document explains how to invoke, configure, and use all **18 agents** in the FreeLLMAPI local AI development ecosystem on macOS Apple Silicon.

---

## 1. Architecture Overview

```
                User / Terminal / IDE
                         │
                         ▼
        Unified Wrapper (flm-<agent> / flm agent <agent>)
                         │
                         ▼
               Real Agent Execution Engine
                         │
                         ▼
             FreeLLMAPI Unified Gateway
               http://127.0.0.1:31415
                         │
                         ▼
                  Dynamic Model Router
            (Auto failover, load balancing, quotas)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
     Provider 1       Provider 2       Provider 3
```

- **Execution Layer**: Local agent engines (Claude Code, Codex, Aider, OpenCode, Goose, Qwen, Crush, etc.).
- **Model / Gateway Layer**: FreeLLMAPI handles bearer tokens, endpoint proxying, quota monitoring, and dynamic model routing. No individual provider API keys are needed per agent.
- **Root Anthropic Endpoint**: `http://127.0.0.1:31415` (for Claude Code).
- **OpenAI Compatible Endpoint**: `http://127.0.0.1:31415/v1` (for Codex, Aider, OpenCode, Goose, Qwen, Cline, Kilo, Crush, AtomCode, OpenClaw, Hermes, Cursor, etc.).

---

## 2. Global Management Commands

| Command | Description |
| :--- | :--- |
| `flm status` | Check gateway status, active mode, and bridge health |
| `flm doctor` | Comprehensive environment, network, and agent diagnostic check |
| `flm health` | Real-time provider and model telemetry |
| `flm models [query]` | Query available models from FreeLLMAPI catalog |
| `flm providers` | View connected provider status and quotas |
| `flm quotas` | View token usage and active cooldowns |
| `flm routing` | View task classification routing profiles |
| `flm mode [fast\|normal]` | Toggle dispatcher routing mode |
| `flm test` | Run latency and E2E gateway test suite |
| `flm agents` | View status matrix across all 18 agents |
| `flm agents list` | Detailed registry and metadata for all 18 agents |
| `flm agents test [agent]`| Run automated E2E validation against FreeLLMAPI |

---

## 3. Dedicated CLI Agent Wrappers

All wrappers are exposed in `~/.local/bin` and can be invoked from any terminal or directory.

### 01. Claude Code
- **Wrapper**: `flm-claude` or `flm agent claude`
- **Underlying Binary**: `/opt/homebrew/bin/claude`
- **Protocol**: Native Anthropic API (`http://127.0.0.1:31415`)
- **Usage**:
  ```bash
  flm-claude
  flm-claude -p "Refactor auth middleware to handle JWT expiration"
  flm-claude --dangerously-skip-permissions
  ```

### 02. Codex CLI
- **Wrapper**: `flm-codex` or `flm agent codex`
- **Underlying Binary**: `/opt/homebrew/bin/codex`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-codex
  flm-codex exec "Write a unit test for payment gateway"
  flm-codex exec -C ./my-project --dangerously-bypass-approvals-and-sandbox "Build the project"
  ```

### 03. Cline CLI
- **Wrapper**: `flm-cline` or `flm agent cline`
- **Underlying Binary**: `/opt/homebrew/bin/cline`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-cline
  flm-cline --auto-approve true -c ./project "Fix failing tests"
  ```

### 04. Aider
- **Wrapper**: `flm-aider` or `flm agent aider`
- **Underlying Binary**: `/Users/subhajkar/.local/bin/aider`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-aider
  flm-aider --message "Add docstrings to all functions in api.py"
  ```

### 05. OpenCode
- **Wrapper**: `flm-opencode` or `flm agent opencode`
- **Underlying Binary**: `/opt/homebrew/bin/opencode`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-opencode
  flm-opencode run "Audit dependencies for vulnerabilities"
  ```

### 06. Goose
- **Wrapper**: `flm-goose` or `flm agent goose`
- **Underlying Binary**: `/opt/homebrew/bin/goose`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-goose
  flm-goose run --text "Inspect git status and list uncommitted changes"
  ```

### 07. Qwen Code
- **Wrapper**: `flm-qwen` or `flm agent qwen`
- **Underlying Binary**: `/opt/homebrew/bin/qwen`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-qwen
  flm-qwen -y -p "Create a simple FastAPI server"
  ```

### 08. Kilo Code
- **Wrapper**: `flm-kilo` or `flm agent kilo`
- **Underlying Binary**: `/opt/homebrew/bin/kilo`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-kilo
  flm-kilo run --auto "Generate tests for math utility library"
  ```

### 09. Crush
- **Wrapper**: `flm-crush` or `flm agent crush`
- **Underlying Binary**: `/opt/homebrew/bin/crush`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-crush
  flm-crush run "Explain the architecture of this repo"
  ```

### 10. DeepSeek Harness (DSH)
- **Wrapper**: `flm-dsh` or `flm agent dsh`
- **Endpoint**: `http://127.0.0.1:3080` (DSH Service)
- **Usage**:
  ```bash
  flm-dsh
  ```

### 11. MiMo Code
- **Wrapper**: `flm-mimo` or `flm agent mimo`
- **Underlying Binary**: `/Users/subhajkar/.local/bin/mimo`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-mimo chat
  ```

### 12. AtomCode
- **Wrapper**: `flm-atomcode` or `flm agent atomcode`
- **Underlying Binary**: `/Users/subhajkar/.local/bin/atomcode`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-atomcode
  flm-atomcode -p "Implement binary search in search.py" -y
  ```

### 13. OpenClaw
- **Wrapper**: `flm-openclaw` or `flm agent openclaw`
- **Underlying Binary**: `/opt/homebrew/bin/openclaw`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-openclaw
  flm-openclaw agent exec "Audit repository structure"
  ```

### 14. Hermes Agent
- **Wrapper**: `flm-hermes` or `flm agent hermes`
- **Underlying Binary**: `/Users/subhajkar/.local/bin/hermes`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-hermes
  flm-hermes -z "Generate a summary of the codebase" --yolo
  ```

### 15. Cursor CLI
- **Wrapper**: `flm-cursor` or `flm agent cursor`
- **Underlying Binary**: `/usr/local/bin/cursor`
- **Protocol**: OpenAI Compatible (`http://127.0.0.1:31415/v1`)
- **Usage**:
  ```bash
  flm-cursor .
  ```

---

## 4. IDE Integrations (Antigravity & VS Code)

### Continue (`Continue.continue`)
- **Type**: `IDE_ONLY`
- **Status**: Installed in VS Code (`~/.vscode/extensions/Continue.continue-2.0.0`)
- **Configuration**: `~/.continue/config.json`
- **Provider Settings**:
  ```json
  {
    "models": [
      {
        "title": "FreeLLMAPI Auto",
        "provider": "openai",
        "model": "auto",
        "apiBase": "http://127.0.0.1:31415/v1",
        "apiKey": "${FREELLMAPI_API_KEY}"
      }
    ]
  }
  ```

### Roo Code (`RooVeterinaryInc.roo-cline`)
- **Type**: `IDE_ONLY`
- **Status**: Installed in VS Code (`~/.vscode/extensions/RooVeterinaryInc.roo-cline-3.54.0`)
- **Configuration**: Custom OpenAI provider pointing to `http://127.0.0.1:31415/v1`

### Cline (`saoudrizwan.claude-dev`)
- **Type**: `CLI / IDE`
- **Status**: Installed in VS Code (`~/.vscode/extensions/saoudrizwan.claude-dev-4.1.22`) and CLI (`/opt/homebrew/bin/cline`)
- **Configuration**: `~/.cline/` configured with `OpenAI Compatible` provider and model `auto`.

### Kilo Code
- **Type**: `CLI / IDE`
- **Status**: Installed CLI (`/opt/homebrew/bin/kilo`) and IDE configuration in `~/.config/kilo/kilo.jsonc`.

### Antigravity IDE Integration
- Antigravity IDE retains its native agents, MCP server registrations, and CDP connection on port 9004.
- In-terminal sessions can launch any `flm-<agent>` inside Antigravity's integrated terminal with full FreeLLMAPI gateway routing.

---

## 5. Generic OpenAI Client Profile

For any generic SDK or third-party tool connecting to the local FreeLLMAPI gateway:

- **Base URL**: `http://127.0.0.1:31415/v1`
- **API Key**: Unified FreeLLMAPI bearer token
- **Model**: `auto` (or explicit target, e.g., `gemini-2.5-flash`, `deepseek-chat`)
- **Python Example**:
  ```python
  from openai import OpenAI
  import os

  client = OpenAI(
      base_url="http://127.0.0.1:31415/v1",
      api_key=os.environ.get("FREELLMAPI_API_KEY", "auto-token")
  )

  response = client.chat.completions.create(
      model="auto",
      messages=[{"role": "user", "content": "Hello world!"}]
  )
  print(response.choices[0].message.content)
  ```
