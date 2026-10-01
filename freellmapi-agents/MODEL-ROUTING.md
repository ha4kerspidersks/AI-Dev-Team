# MODEL ROUTING & QUOTA MANAGEMENT SPECIFICATION

## 1. Principles of Resilient Routing

1. **Independent Quota Pools**:
   Aggregate FreeLLMAPI token figures do not guarantee individual model availability. FreeLLMAPI tracks independent platform quotas (`requests`, `tokens`, `credits`).
2. **Context Window Protection**:
   Coding agents frequently send project context between 30k and 150k tokens. Models with restricted context windows (e.g. 24,000 tokens) are quarantined to prevent HTTP 413 / 400 errors.
3. **Latency-Aware Tiering**:
   Models with high average latencies (>60s) or stream drops (e.g. `openrouter/nvidia/nemotron-3.5-lightning:free` at 174s) are excluded from primary auto-routing.

---

## 2. Task Classification Profiles

The environment classifies tasks across 8 operational profiles:

### FAST
- **Intent**: Rapid feedback, micro-edits, inline questions, terminal queries.
- **Latency Target**: TTFT < 1.5s, Total < 3s.
- **Primary**: `openai/gpt-oss-120b` (Groq/Ollama)
- **Fallbacks**: `gemini-3-flash-preview` -> `gemini-2.5-flash` -> `nvidia/nemotron-3-super-120b-a12b:free`

### CODING
- **Intent**: File modifications, refactoring, test generation, AST manipulation.
- **Latency Target**: 3s - 10s.
- **Primary**: `gemini-2.5-flash` (1,048,576 token context, tool use verified)
- **Fallbacks**: `nvidia/nemotron-3-super-120b-a12b:free` (1M context) -> `openai/gpt-oss-120b` -> `codestral-2508`

### DEEP_REASONING
- **Intent**: Architecture decision analysis, complex algorithm synthesis, security audits.
- **Primary**: `gemini-3-flash-preview`
- **Fallbacks**: `deepseek-r1-distill-qwen-32b` -> `nemotron-3-super-120b-a12b:free`

### LONG_CONTEXT
- **Intent**: Whole-repository indexing, cross-module dependency auditing (>256k tokens).
- **Primary**: `gemini-2.5-flash` (1,048,576 tokens)
- **Fallbacks**: `gemini-3-flash-preview` (1M tokens) -> `nemotron-3-super-120b-a12b:free` (1M tokens)

### GENERAL
- **Intent**: Interactive pair programming with Claude Code or Codex.
- **Primary**: `auto` (FreeLLMAPI internal dynamic router prioritizing healthy models)
- **Fallbacks**: `gemini-2.5-flash` -> `nemotron-3-super-120b-a12b:free`

### TOOL_USE
- **Intent**: Strict function calling and structured schema generation.
- **Primary**: `gemini-2.5-flash`
- **Fallbacks**: `nemotron-3-super-120b-a12b:free` -> `openai/gpt-oss-120b`

### RESEARCH
- **Intent**: Literature review, web search synthesis, documentation generation.
- **Primary**: `gemini-3-flash-preview`
- **Fallbacks**: `gemini-2.5-flash` -> `openai/gpt-oss-120b`

### LOCAL
- **Intent**: Offline processing, air-gapped workflows, data sovereignty.
- **Primary**: `local-qwen-bridge` (`http://127.0.0.1:8787`)
- **Fallbacks**: `gemini-2.5-flash` -> `openai/gpt-oss-120b`

---

## 3. Quarantined Models

The following models are explicitly quarantined from auto-routing:

1. **`openrouter/nvidia/nemotron-3.5-lightning:free`**:
   - *Reason*: Upstream latency averages 174.6s (spikes to 352s) with frequent stream aborts.
2. **`cloudflare/@cf/meta/llama-3.3-70b-instruct-fp8-fast`**:
   - *Reason*: Context length hard-capped at 24,000 tokens, throwing HTTP 413 on multi-file coding prompts.
