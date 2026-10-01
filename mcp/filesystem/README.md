# Filesystem MCP Module

- **Package**: `@modelcontextprotocol/server-filesystem` (Official Model Context Protocol)
- **Runtime**: Node.js 22 LTS (`~/Developer/AI-Dev-Team/environments/node22/bin/node`)
- **Transport**: Stdio (JSON-RPC 2.0)
- **Runner**: `~/Developer/AI-Dev-Team/mcp/filesystem/run.sh`
- **Scoped Root**: `/Users/subhajkar/Developer`

## Capabilities (14 Tools)
- `read_file`, `read_text_file`, `read_media_file`, `read_multiple_files`
- `write_file`, `edit_file`
- `create_directory`, `list_directory`, `list_directory_with_sizes`, `directory_tree`
- `move_file`, `search_files`, `get_file_info`, `list_allowed_directories`

## Security & Path Confinement
- Root is strictly confined to `/Users/subhajkar/Developer`.
- Access to root `/`, `~/.ssh`, `~/.aws`, `~/.gnupg` or arbitrary system directories outside `/Users/subhajkar/Developer` is blocked by design.
- Protected repositories (`~/Developer/LinkedIn-Audit`, `~/Developer/subhajitportfolio-2.0`) are protected by policy and must remain untouched.
