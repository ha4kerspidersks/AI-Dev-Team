# Git MCP Module

- **Package**: `mcp-server-git` (Official Model Context Protocol)
- **Runtime**: Python 3.14 venv (`~/Developer/AI-Dev-Team/environments/mcp-env/bin/python`)
- **Transport**: Stdio (JSON-RPC 2.0)
- **Runner**: `~/Developer/AI-Dev-Team/mcp/git/run.sh`

## Capabilities (12 Tools)
- `git_status`: Check working tree status
- `git_diff_unstaged`: Inspect unstaged modifications
- `git_diff_staged`: Inspect staged modifications
- `git_diff`: Diff between commits or branches
- `git_commit`: Record changes to the repository
- `git_add`: Add file contents to the staging area
- `git_reset`: Reset current HEAD to specified state
- `git_log`: View commit logs
- `git_create_branch`: Create new branch
- `git_checkout`: Switch branches or restore files
- `git_show`: Inspect commit objects
- `git_branch`: List and manage branches

## Security Rules
- Read-only operations (`git_status`, `git_diff`, `git_log`, `git_show`, `git_branch`) are auto-approved.
- Local state changes (`git_add`, `git_commit`, `git_checkout`, `git_create_branch`) are safe write.
- Destructive resets (`git_reset`) require user confirmation.
- Remote push actions are strictly forbidden from automatic execution.
