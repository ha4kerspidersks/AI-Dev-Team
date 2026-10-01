# Ponytail Integration Matrix

**Repository:** `https://github.com/DietrichGebert/ponytail.git` (`DietrichGebert/ponytail`)  
**Version:** 4.10.0 (`e3ba2aa`)  
**Canonical Local Location:** `/Users/subhajkar/Developer/AI-Dev-Team/repos/ponytail`  
**Date:** 2026-10-01  

---

## 1. Integration Matrix

| Component | Ponytail Source | Existing Component | Relationship | Duplicate? | Conflict? | Keep Both? | Integration Method | Status |
|---|---|---|---|---|---|---|---|---|
| **Ponytail Repository** | `DietrichGebert/ponytail` | None | Reusable Core Library | No | No | Yes | Centralized in `AI-Dev-Team/repos/ponytail` | ACTIVE |
| **`ponytail` Skill** | `repos/ponytail/skills/ponytail/SKILL.md` | `skills/ponytail/SKILL.md` | Core Lazy Senior Dev Mode | Yes (Identical SHA-256) | No | Yes (Source-linked) | Preserved in central skills; linked to repo | ACTIVE |
| **`ponytail-audit` Skill** | `repos/ponytail/skills/ponytail-audit/SKILL.md` | `skills/ponytail-audit/SKILL.md` | PR / Diff Overengineering Audit | Yes (Identical SHA-256) | No | Yes (Source-linked) | Preserved in central skills; linked to repo | ACTIVE |
| **`ponytail-debt` Skill** | `repos/ponytail/skills/ponytail-debt/SKILL.md` | `skills/ponytail-debt/SKILL.md` | Speculative Tech Debt Elimination | Yes (Identical SHA-256) | No | Yes (Source-linked) | Preserved in central skills; linked to repo | ACTIVE |
| **`ponytail-gain` Skill** | `repos/ponytail/skills/ponytail-gain/SKILL.md` | `skills/ponytail-gain/SKILL.md` | Lines of Code / Simplification ROI | Yes (Identical SHA-256) | No | Yes (Source-linked) | Preserved in central skills; linked to repo | ACTIVE |
| **`ponytail-help` Skill** | `repos/ponytail/skills/ponytail-help/SKILL.md` | `skills/ponytail-help/SKILL.md` | Interactive Help & Mode Cheatsheet | Yes (Identical SHA-256) | No | Yes (Source-linked) | Preserved in central skills; linked to repo | ACTIVE |
| **`ponytail-review` Skill** | `repos/ponytail/skills/ponytail-review/SKILL.md` | `skills/ponytail-review/SKILL.md` | Pre-commit Simplification Gate | Yes (Identical SHA-256) | No | Yes (Source-linked) | Preserved in central skills; linked to repo | ACTIVE |
| **`ponytail-mcp` Server** | `repos/ponytail/ponytail-mcp/index.js` | None | Stdio MCP Ruleset Server | No (Unique) | No | Yes | Installed isolated npm deps; registered in Catalog | ACTIVE (Optional) |
| **`ponytail_instructions` Tool**| `repos/ponytail/ponytail-mcp/index.js` | None | MCP Tool returning ruleset by mode | No (Unique) | No | Yes | Validated live tool call over JSON-RPC | ACTIVE |
| **`/ponytail` Command** | `commands/ponytail.toml` | None | Command switching mode | No | No | Yes | Cataloged in central library | ACTIVE |
| **`/ponytail-review` Command** | `commands/ponytail-review.toml` | None | Command triggering review | No | No | Yes | Cataloged in central library | ACTIVE |
| **`/ponytail-audit` Command** | `commands/ponytail-audit.toml` | None | Command triggering audit | No | No | Yes | Cataloged in central library | ACTIVE |
| **`/ponytail-debt` Command** | `commands/ponytail-debt.toml` | None | Command triggering debt elimination | No | No | Yes | Cataloged in central library | ACTIVE |
| **`/ponytail-gain` Command** | `commands/ponytail-gain.toml` | None | Command calculating velocity gains | No | No | Yes | Cataloged in central library | ACTIVE |
| **`/ponytail-help` Command** | `commands/ponytail-help.toml` | None | Command displaying help | No | No | Yes | Cataloged in central library | ACTIVE |
| **Claude/Codex Lifecycle Hooks** | `hooks/claude-codex-hooks.json` | None | Local lifecycle hook definitions | No | No | Yes (Cataloged) | Kept in repository; requires user action to activate globally | CATALOGED (User Gate) |
| **Copilot CLI Hooks** | `hooks/copilot-hooks.json` | None | Copilot CLI prompt hook | No | No | Yes (Cataloged) | Kept in repository; compatible with ACP bridge | CATALOGED (User Gate) |
| **Cursor Hooks** | `hooks/cursor-hooks.json` | None | Cursor IDE session hooks | No | No | Yes (Cataloged) | Kept in repository; requires user action to activate globally | CATALOGED (User Gate) |
| **Qoder Hooks** | `hooks/qoder-hooks.json` | None | Qoder prompt hooks | No | No | Yes (Cataloged) | Kept in repository; isolated from global runtime | CATALOGED (User Gate) |
| **Gemini / Antigravity Adapter** | `gemini-extension.json` | None | Antigravity extension context loader | No | No | Yes | Compatible with agy CLI and AGENTS.md | ACTIVE |
| **Multi-Platform Plugins Suite**| `.opencode/`, `pi-extension/`, etc. | None | Adapters for 12 IDE platforms | No | No | Yes | Reusable platform adapters kept inside repository | ACTIVE |

---

## 2. Duplicate Analysis Summary

1. **Skills (6 items):**
   - The 6 skills (`ponytail`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`, `ponytail-review`) existed in `/Users/subhajkar/Developer/AI-Dev-Team/skills/` from prior imports.
   - SHA-256 analysis confirmed that all 6 files are 100% byte-for-byte identical with the repository version in `AI-Dev-Team/repos/ponytail/skills/`.
   - Resolution: Marked as **Shared / Source-Linked Component**. No overwrites performed.

2. **Commands & Hooks:**
   - No conflicting commands exist in AI-Dev-Team.
   - Hooks have been reviewed and cataloged. None have been blindly injected into global configs, honoring the strict user gate policy.
