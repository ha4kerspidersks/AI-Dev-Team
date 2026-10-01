# GitHub MCP Module

- **Package**: `@modelcontextprotocol/server-github` (Official Model Context Protocol)
- **Runtime**: Node.js 22 LTS (`~/Developer/AI-Dev-Team/environments/node22/bin/node`)
- **Transport**: Stdio (JSON-RPC 2.0)
- **Runner**: `~/Developer/AI-Dev-Team/mcp/github/run.sh`

## Capabilities
- Repository inspection & search (`search_repositories`, `get_file_contents`, `search_code`)
- Issue management (`list_issues`, `get_issue`, `create_issue`, `update_issue`, `add_issue_comment`, `search_issues`)
- Pull requests (`list_pull_requests`, `get_pull_request`, `create_pull_request`, `create_pull_request_review`, `merge_pull_request`, `get_pull_request_files`)
- Git references (`create_branch`, `list_commits`, `create_repository`, `fork_repository`)

## Authentication & Security
- Requires `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable.
- **Least Privilege**: Only read operations are auto-invocable. Write/destructive actions (creating repos, pushing files, merging PRs) require explicit user confirmation.
