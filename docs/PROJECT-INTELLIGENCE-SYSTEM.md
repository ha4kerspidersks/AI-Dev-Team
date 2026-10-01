# Global Project Intelligence & Memory System

> **Architecture, Operation, and Developer Guide**  
> **Antigravity Global Agentic Ecosystem**  
> **Version**: `2.0.0` | **Status**: `Production Verified`

---

## 1. Overview & Core Philosophy

The **Global Project Intelligence & Memory System** permanently enhances how Google Antigravity and autonomous coding agents interact with software repositories across the developer workstation (`/Users/subhajkar/Developer`).

### Mandatory Bootstrap Rule
**PROJECT CONTEXT MUST EXIST BEFORE DEVELOPMENT**. Whenever Antigravity starts working on ANY software project, repository, workspace, or codebase, you MUST automatically determine whether that project already has Project Intelligence / Context Memory. This rule applies to EVERY project and EVERY future task.

### Universal Operating Pipeline (Every Task)
```
DETECT
  ↓
IDENTIFY PROJECT
  ↓
LOAD PROJECT INTELLIGENCE
  ↓
IF MISSING → DISCOVER + CREATE MEMORY (Automated Prerequisite)
  ↓
VALIDATE MEMORY
  ↓
ANALYZE USER REQUEST
  ↓
INSPECT RELEVANT SOURCE
  ↓
IMPLEMENT
  ↓
BUILD / TEST / VERIFY
  ↓
UPDATE PROJECT INTELLIGENCE (Levels 1-4)
  ↓
FINAL VALIDATION
  ↓
REPORT
```

### Inviolable Invariant: Memory vs Source Code
- **Project Memory is an Architectural Navigation Layer**: It catalogues files, frameworks, APIs, test suites, and ADRs to eliminate repeated repository-wide code scanning.
- **Source Code is the Ultimate Source of Truth**: Agents must verify source code when implementing changes. If source code contradicts memory, trust the filesystem, implement changes, and refresh memory.
- **Automatic Prerequisite**: The first development task in a new project MUST automatically perform project initialization first. The user's prompt is still the task; initialization is an automatic prerequisite, not a separate user-requested task.


---

## 2. Project Detection & Identity Engine

### Root Detection Algorithm (`detect_project_root`)
1. **Git Traversal**: Probes `git rev-parse --show-toplevel`.
2. **Monorepo Sub-project Detection**: Checks if the target subdirectory contains its own standalone manifest (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, etc.). If so, boundaries are scoped to that sub-project.
3. **Non-Git Upward Walk**: Walks upward toward the filesystem root, checking for indicators:
   - Node: `package.json`, `pnpm-workspace.yaml`, `yarn.lock`, `package-lock.json`, `bun.lock`
   - Python: `pyproject.toml`, `requirements.txt`, `Pipfile`
   - Rust: `Cargo.toml`
   - Go: `go.mod`
   - Java/Kotlin: `pom.xml`, `build.gradle`, `build.gradle.kts`
   - Containers & Build: `Dockerfile`, `docker-compose.yml`, `Makefile`, `.git/`

### Stable Identity Algorithm (`get_project_identity`)
- **Git Repositories**: Derives identity from remote origin URL slug or stable repository root hash.
- **Local Folders**: Derives identity from canonical absolute path and an 8-character SHA256 digest (`<clean_name>-<hash>`).
- Guarantees identity permanence across system reboots, IDE restarts, and directory moves.

---

## 3. Storage Location Convention

Project intelligence is persisted locally in the repository root under:
- `<PROJECT_ROOT>/.agent/project-memory/` (or `<PROJECT_ROOT>/.agents/project-memory/`)

The directory selection adheres to existing workspace conventions:
- If `.agent` exists (or `.agents` is a symlink to `.agent`, e.g., in `subhajitportfolio-2.0`), memory is written to `.agent/project-memory/`.
- If `.agents` exists as a physical directory (e.g., in `AI-Dev-Team`), memory is written to `.agents/project-memory/`.
- Defaults to `.agents/project-memory/` for new projects.

---

## 4. The 10 Memory Documents

| File | Type | Purpose |
|---|---|---|
| [`PROJECT-CONTEXT.md`](file://.agent/project-memory/PROJECT-CONTEXT.md) | Markdown | Compact executive summary (<150 lines), tech stack, and subsystem navigation guide. Loaded first by agents. |
| [`METADATA.json`](file://.agent/project-memory/METADATA.json) | JSON | Machine-readable registry: file index with SHA256 hashes, mtimes, sizes, commands, and git commit. |
| [`PROJECT-MAP.json`](file://.agent/project-memory/PROJECT-MAP.json) | JSON | Subsystem topology: UI components, tabs, IAM/identity, 3D, manifests, services, APIs, tests. |
| [`ARCHITECTURE.md`](file://.agent/project-memory/ARCHITECTURE.md) | Markdown | Architectural patterns, layer boundaries, directory roles, entry points, and isolation rules. |
| [`DEPENDENCIES.md`](file://.agent/project-memory/DEPENDENCIES.md) | Markdown | Runtime dependencies, dev tooling, package managers, and external API providers. |
| [`DATA-FLOW.md`](file://.agent/project-memory/DATA-FLOW.md) | Markdown | Mermaid diagrams and data lifecycle: Input → Validation → Processing → Output. |
| [`API-MAP.md`](file://.agent/project-memory/API-MAP.md) | Markdown | Comprehensive route catalog with HTTP methods, paths, and clickable source file links. |
| [`TEST-MAP.md`](file://.agent/project-memory/TEST-MAP.md) | Markdown | Verification suite inventory: runners, frameworks, concurrency, and test file links. |
| [`DECISIONS.md`](file://.agent/project-memory/DECISIONS.md) | Markdown | Architectural Decision Records (ADRs): Date, Status, Rationale, Context, and Impact. |
| [`CHANGELOG.md`](file://.agent/project-memory/CHANGELOG.md) | Markdown | Chronological log of agent tasks, change levels (1-4), and impacted files. |

---

## 5. Change Detection & Architectural Levels

Changes are categorized into 4 distinct levels to minimize unnecessary processing:

- **Level 1 — Content Change**: Markdown wording, comments, formatting, minor CSS.  
  *Action*: Update file index metadata and append changelog entry.
- **Level 2 — Code Change**: Component logic, service methods, utility functions.  
  *Action*: Update file hashes, mtimes, changelog, and component references.
- **Level 3 — Structural Change**: New/deleted files, new routes/endpoints, new dependencies, new test files.  
  *Action*: Refresh `PROJECT-MAP.json`, `API-MAP.md`, `TEST-MAP.md`, and `DEPENDENCIES.md`.
- **Level 4 — Major Architecture Change**: Framework migrations, new databases, authentication architecture redesigns.  
  *Action*: Perform targeted deep architectural rescan and rebuild all subsystem maps.

---

## 6. How Agents Consume Memory Token-Efficiently

Future agent interactions must follow this sequential protocol:

1. **Step 1: Identify & Check**
   ```bash
   ai-team memory check [path]
   ```
2. **Step 2: Read High-Level Context (<150 lines)**
   ```bash
   ai-team memory load [path]
   ```
   *Agents do NOT load the entire repository or 50 source files.*
3. **Step 3: Pinpoint & Load Specific Subsystem (If Needed)**
   ```bash
   ai-team memory load [path] --subsystem api
   # Or: --subsystem test, --subsystem architecture, --subsystem decisions
   ```
4. **Step 4: Inspect Only Impacted Source Files**
   Navigate directly to the specific components or services specified in the memory guide.
5. **Step 5: Implement & Run Verification Tests**
   Execute the canonical test command recorded in memory (e.g. `npm test`, `pytest`).
6. **Step 6: Refresh Memory on Task Completion**
   ```bash
   ai-team memory refresh [path] --summary "Description of changes made"
   ```

---

## 7. Multi-Agent & SQLite Integration

### SQLite Synchronization (`~/.agent-team/team.db`)
Whenever project intelligence is generated or refreshed, the engine automatically syncs:
- **`projects` table**: Upserts `id`, `name`, `description`, `status = 'active'`, and timestamps.
- **`project_summaries` table**: Appends a versioned summary record (`version = N+1`).
- **`decisions` table**: Synchronizes all parsed ADRs from `DECISIONS.md`.

### Universal Tool Portability
Because memory is serialized as standard **GitHub-Flavored Markdown** and **JSON**, it is consumable by:
- Google Antigravity
- Claude Code (`CLAUDE.md` / `.claude`)
- Gemini CLI
- OpenAI Codex
- Custom CI/CD scripts

---

## 8. Privacy, Security & Exclusions

### Default Exclusions
Never scans or hashes dependency or ephemeral trees:
`node_modules`, `.git`, `dist`, `build`, `coverage`, `.cache`, `.pytest_cache`, `.turbo`, `.next`, `.nuxt`, `out`, `target`, `.venv`, `venv`, `env`, `__pycache__`, `.DS_Store`, `tmp`, `temp`, `test-results`, `.agent`, `.agents`.

### .gitignore & .agentignore Support
Respects all ignore rules declared in project-level `.gitignore` and `.agentignore`.

### Secret Scrubbing & Privacy Guarantees
- Environment files (`.env`, `.env.local`, etc.) are tracked **only by existence**. Their contents are never parsed, indexed, or stored.
- Any regex-matching API keys, OAuth tokens, bearer tokens, or private keys in tracked code snippets are automatically sanitized with `[REDACTED_SECRET]`.

---

## 9. Self-Healing & Recovery Procedures

### Automatic Recovery
If `METADATA.json` is corrupted or deleted:
```bash
ai-team memory recover [path]
```
The engine automatically rebuilds all 10 memory documents directly from current source code without affecting application files.

### Manual Force Refresh
To completely re-index a repository and discard cached signatures:
```bash
ai-team memory discover [path] --force
```

### Excluding a Project
To prevent an agent from creating or loading memory in a specific folder, create an `.agentignore` file in the project root containing:
```
.agents/
.agent/
```
