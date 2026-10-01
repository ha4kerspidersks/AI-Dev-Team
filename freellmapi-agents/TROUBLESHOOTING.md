# TROUBLESHOOTING GUIDE — FREELLMAPI ENVIRONMENT

## Common Issues & Verified Fixes

### 1. Claude Code hangs or streams stop after a few minutes
- **Symptom**: Claude Code stops generating tokens; session hangs or aborts after 300 seconds.
- **Root Cause**: The router selected `nvidia/nemotron-3.5-lightning:free` on OpenRouter, which suffers from severe upstream queuing (170s-350s latency) and connection resets.
- **Fix**:
  1. Run `flm mode fast` to switch to low-latency verified models, or
  2. Use `flm claude` which automatically injects optimized model routing.

### 2. HTTP 413 "Exceeded model context window limit (24000)"
- **Symptom**: Error when sending files or large prompts to Claude or Codex.
- **Root Cause**: FreeLLMAPI attempted fallback to Cloudflare's `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, which has an undersized 24k token limit.
- **Fix**:
  - The model has been quarantined in `config/routing.json`. Run `flm repair` to sync health telemetry.

### 3. "FreeLLMAPI is not reachable at 127.0.0.1:31415"
- **Symptom**: `flm doctor` reports Gateway Reachability FAIL.
- **Root Cause**: The FreeLLMAPI desktop application is closed.
- **Fix**:
  - Open `/Applications/FreeLLMAPI.app` from Spotlight, Finder, or terminal (`open /Applications/FreeLLMAPI.app`).

### 4. "Router9 key validation inconclusive (HTTP 429)" in logs
- **Symptom**: Periodic log messages indicating key 7 rate limit.
- **Root Cause**: Provider router9 has exhausted its trial rate quota.
- **Fix**:
  - Expected behavior. FreeLLMAPI marks router9 in temporary cooldown and routes requests to the other 19 healthy providers automatically.

### 5. Running automated diagnostics and repair
- Whenever unexpected behavior occurs, run:
  ```bash
  flm doctor
  flm repair
  ```
  This creates an automatic backup snapshot, validates endpoints, checks permissions, and verifies connectivity.
