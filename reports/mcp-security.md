# Global MCP Security & Permissions Governance Policy

## 1. Security Architecture & Threat Model

The Model Context Protocol (MCP) provides AI agents with dynamic invocation capabilities over local runtimes, cloud endpoints, and developer tooling. Without rigorous guardrails, MCP servers represent a significant attack surface:
- Insecure filesystem servers can expose SSH keys, AWS credentials, and system binaries.
- Unsanitized GitHub tools can accidentally push commits, overwrite remote branches, or publicly publish private code.
- Stateful database servers can suffer from cross-project credential leakage or catastrophic accidental data drops (`DROP DATABASE`).

### 1.1 Core Security Principles
1. **Least Privilege by Default**: Tool access is restricted to the minimum capability necessary for development tasks.
2. **Directory Confinement**: Filesystem servers are strictly scoped to `/Users/subhajkar/Developer`. System directories (`/`, `/etc`, `/Applications`, `~/.ssh`, `~/.aws`, `~/.gnupg`) are strictly inaccessible.
3. **No Hardcoded Secrets**: Zero API keys or tokens in configuration files. Tokens are passed exclusively through environment variables (`${GITHUB_PERSONAL_ACCESS_TOKEN}`) or secure OS keychains.
4. **No Unprompted External Publication**: The agent must NEVER automatically execute `git push`, create public PRs, or release packages without explicit user authorization.
5. **Browser Isolation**: Headless Chromium instances are sandboxed with no access to the user's host browser profiles, cookies, saved logins, or active sessions.
6. **Zero Offensive Tools**: Offensive security exploits or destructive scanning suites are strictly barred from the global MCP layer.

---

## 2. Five-Tier Permission Classification Matrix

Every tool across all MCP servers is categorized into one of five permission tiers:

| Tier | Policy | Description | Execution Gate |
| :--- | :--- | :--- | :--- |
| **READ ONLY** | Allowed | Inspects files, queries status, searches docs, retrieves logs | Automatic |
| **SAFE WRITE** | Allowed | Edits project files, creates local branches, stages files, logs work | In-context approval |
| **DESTRUCTIVE** | Restricted | Overwrites branches, resets HEAD, deletes project records, drops tables | Requires explicit user confirmation |
| **EXTERNAL ACTION**| Restricted | Pushes to GitHub, opens external PRs, publishes releases, triggers webhooks | Requires explicit user confirmation |
| **CREDENTIAL SENSITIVE**| Locked | Uses cloud OAuth, queries production data, manages service accounts | Explicit auth & credential check |

---

## 3. Tool Permissions Mapping

### 3.1 GitHub Server (`github`)
| Tool | Category | Policy |
| :--- | :--- | :--- |
| `search_repositories`, `get_file_contents`, `search_code`, `search_issues`, `search_users`, `get_issue`, `get_pull_request`, `list_pull_requests`, `get_pull_request_files`, `get_pull_request_status`, `get_pull_request_comments`, `get_pull_request_reviews`, `list_commits`, `list_issues` | **READ ONLY** | Auto-permitted |
| `add_issue_comment`, `create_branch`, `create_pull_request_review` | **SAFE WRITE** | Allowed in task flow |
| `create_issue`, `update_issue`, `create_pull_request`, `update_pull_request_branch` | **EXTERNAL ACTION** | User authorization required |
| `create_repository`, `fork_repository`, `merge_pull_request`, `push_files`, `create_or_update_file` | **DESTRUCTIVE / EXTERNAL** | Explicit confirmation required |

### 3.2 Git Server (`git`)
| Tool | Category | Policy |
| :--- | :--- | :--- |
| `git_status`, `git_diff_unstaged`, `git_diff_staged`, `git_diff`, `git_log`, `git_show`, `git_branch` | **READ ONLY** | Auto-permitted |
| `git_add`, `git_commit`, `git_create_branch`, `git_checkout` | **SAFE WRITE** | Allowed within project repository |
| `git_reset` | **DESTRUCTIVE** | User confirmation required |

### 3.3 Filesystem Server (`filesystem`)
| Tool | Category | Policy |
| :--- | :--- | :--- |
| `read_file`, `read_text_file`, `read_media_file`, `read_multiple_files`, `list_directory`, `list_directory_with_sizes`, `directory_tree`, `search_files`, `get_file_info`, `list_allowed_directories` | **READ ONLY** | Auto-permitted within allowed path |
| `write_file`, `edit_file`, `create_directory` | **SAFE WRITE** | Allowed (confined to `~/Developer`) |
| `move_file` | **DESTRUCTIVE** | Allowed only for non-protected paths |

### 3.4 AgentTeam Server (`agent-team`)
| Tool | Category | Policy |
| :--- | :--- | :--- |
| `get_project`, `list_projects`, `get_project_summary`, `get_summary_version`, `list_summary_history`, `list_team_members`, `get_task`, `list_tasks`, `get_my_work`, `get_work_history`, `list_task_comments`, `list_my_comments`, `get_discussion`, `list_discussions`, `list_decisions`, `get_decision`, `get_team_protocol`, `get_orchestration_instructions`, `get_agent_prompt`, `list_artifacts`, `get_artifact`, `list_journal_entries`, `list_user_questions`, `list_expansion_requests` | **READ ONLY** | Auto-permitted |
| `create_project`, `update_project_summary`, `add_team_member`, `create_task`, `update_task`, `log_work`, `add_task_comment`, `create_discussion`, `add_discussion_participant`, `add_discussion_message`, `update_discussion_summary`, `log_decision`, `share_artifact`, `update_artifact`, `log_journal_entry`, `ask_user_question`, `answer_user_question`, `request_team_expansion`, `resolve_expansion_request`, `update_project_status` | **SAFE WRITE** | Allowed (records to `~/.agent-team/team.db`) |
| `delete_project`, `remove_team_member` | **DESTRUCTIVE** | Explicit confirmation required |

### 3.5 Browser & Web Servers (`browser`, `web`, `gemini-api_gemini-api-docs`)
| Tool | Category | Policy |
| :--- | :--- | :--- |
| `fetch` (web) | **READ ONLY** | Auto-permitted |
| `gemini_search_docs`, `gemini_get_doc` (gemini-docs) | **READ ONLY** | Auto-permitted |
| `puppeteer_navigate`, `puppeteer_screenshot` | **READ ONLY** | Auto-permitted (sandboxed Chromium) |
| `puppeteer_hover`, `puppeteer_click`, `puppeteer_fill`, `puppeteer_select`, `puppeteer_evaluate` | **SAFE WRITE** | Allowed in local test browser sessions |

### 3.6 Google Cloud Datacloud Endpoints (`datacloud_*`)
| Tool / Endpoint | Category | Policy |
| :--- | :--- | :--- |
| `notebooks` (inspect/read), `data-agent-kit` (context), `visualization` | **READ ONLY** | Auto-permitted within IDE session |
| `notebooks` (replace_cell, delete_cell) | **DESTRUCTIVE** | Confirmation required |
| `datacloud_bigquery_remote`, `datacloud_spanner_remote`, `datacloud_alloydb_remote`, `datacloud_cloud-sql_remote`, `datacloud_knowledge_catalog_remote`, `datacloud_dataproc_remote` | **CREDENTIAL SENSITIVE** | Governed by Google Cloud OAuth scopes |

---

## 4. Protected Workspaces Enforcement

The following repositories are hard-protected and MUST NEVER be modified, moved, renamed, deleted, or overwritten by any MCP tool:
1. `/Users/subhajkar/Developer/LinkedIn-Audit`
2. `/Users/subhajkar/Developer/subhajitportfolio-2.0`

Any attempt to perform write operations against these paths is intercepted and blocked.
