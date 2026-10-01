# CHANGELOG

## [1.0.0] - 2026-10-01

### Added
- **Unified Dispatcher (`flm`)**: Global CLI executable under `bin/flm` with subcommands:
  - `status`, `doctor`, `health`, `models`, `providers`, `quotas`, `routing`, `mode`, `test`, `audit`, `repair`, `backup`, `update`, `logs`.
- **Agent Dispatching Architecture**:
  - `flm claude`: Zero-credential leak Claude Code launcher with mode-aware routing.
  - `flm codex`: Zero-credential leak Codex CLI launcher with OpenAI-compatible responses protocol.
  - `flm gemini`: Dual-mode launcher supporting Google OAuth, FreeLLMAPI native Gemini (`v1beta`), and Local Qwen bridge (`port 8787`).
  - Native wrappers for missing candidate agents (`aider`, `opencode`, `qwen`, `goose`, `cline`, `roo`, `kilo`, `crush`, `dsh`, `mimo`, `atomcode`, `openclaw`, `hermes`).
- **Telemetry & Health Tracking**:
  - `scripts/model_tracker.py` synchronizing real-time request attempts, latency metrics, cooldowns, and quota states from `freeapi.db` into `data/model_health.json`.
- **Diagnostic Engine (`flm doctor`)**:
  - Multi-point diagnostic verifying FreeLLMAPI process, gateway port, models catalog, auth token, agents, Docker, Local Qwen, and MCP configurations.
- **Performance & Testing Suite (`flm test`)**:
  - Automated TTFT and stream validation measuring Anthropic SSE, OpenAI SSE, Claude Code CLI, and Codex CLI.
- **Automated Repair Engine (`flm repair`)**:
  - Safe repair system with automatic timestamped snapshots, configuration verification, and rollback upon test failure.
- **Mode Switching Engine (`flm mode`)**:
  - Fast mode (low-latency <1.5s TTFT) and Normal mode (1M token context, high reasoning).

### Fixed
- **Claude Code & `h4s` Stream Drops / Timeouts**:
  - Identified root cause where `ANTHROPIC_MODEL: auto` routed to `openrouter/nvidia/nemotron-3.5-lightning:free` which had 170s-350s upstream latency and connection resets.
  - Quarantined `nemotron-3.5-lightning:free` and prioritized healthy sub-second models (`gemini-2.5-flash`, `gpt-oss:120b`, `nemotron-3-super-120b-a12b:free`).
- **Context Window Overflow Crashes (HTTP 413)**:
  - Quarantined Cloudflare `@cf/meta/llama-3.3-70b-instruct-fp8-fast` (24k token limit) to prevent crashes on large code repositories.
- **Codex CLI Environment Integration**:
  - Injected `FREELLMAPI_API_KEY` dynamically into child process environment without persisting secrets in plain text config files.
- **Global Terminal PATH**:
  - Safely added `~/Developer/AI-Dev-Team/freellmapi-agents/bin` to `~/.zshrc` and created global symlink in `~/.local/bin/flm`.
