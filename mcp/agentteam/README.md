# AgentTeam MCP Module

- **Package**: AgentTeam MCP Server (`~/Developer/AI-Dev-Team/repos/AgentTeam/mcp-server`)
- **Runtime**: Node.js 22 LTS (`~/Developer/AI-Dev-Team/environments/node22/bin/node`)
- **Transport**: Stdio (JSON-RPC 2.0)
- **Runner**: `~/Developer/AI-Dev-Team/mcp/agentteam/run.sh`
- **Database**: SQLite3 at `~/.agent-team/team.db` (15 tables)

## Role in Architecture
AgentTeam acts as the persistent multi-agent coordination, orchestration, and project tracking backbone across the ecosystem.

## Capabilities (46 Tools)
- Project lifecycle (`create_project`, `get_project`, `update_project_status`, `list_projects`, `delete_project`)
- Project summaries & versioning (`get_project_summary`, `update_project_summary`, `get_summary_version`, `list_summary_history`)
- Team roster (`add_team_member`, `remove_team_member`, `list_team_members`)
- Task management (`create_task`, `update_task`, `get_task`, `list_tasks`)
- Work logging (`log_work`, `get_my_work`, `get_work_history`)
- Task comments (`add_task_comment`, `list_task_comments`, `list_my_comments`)
- Discussions & decisions (`create_discussion`, `add_discussion_participant`, `add_discussion_message`, `update_discussion_summary`, `get_discussion`, `list_discussions`, `log_decision`, `list_decisions`, `get_decision`)
- Artifacts & journal (`share_artifact`, `update_artifact`, `list_artifacts`, `get_artifact`, `log_journal_entry`, `list_journal_entries`)
- User interaction & team expansion (`ask_user_question`, `list_user_questions`, `answer_user_question`, `request_team_expansion`, `list_expansion_requests`, `resolve_expansion_request`)
- Orchestration instructions (`get_team_protocol`, `get_orchestration_instructions`, `get_agent_prompt`)
