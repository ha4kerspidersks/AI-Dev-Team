# FINAL PRE-MIGRATION VALIDATION REPORT
**Antigravity Global AI Infrastructure & Agent-Ecosystem Engineering Dev Team**  
**Workspace**: `/Users/subhajkar/Developer`  
**Central AI Agent Home**: `/Users/subhajkar/Developer/AI-Dev-Team/`  
**Date**: October 1, 2026  
**Status**: 100% READ-ONLY VALIDATION PASS COMPLETED — ZERO MUTATIONS EXECUTED

---

## 1. Executive Summary

This validation pass serves as the definitive pre-migration audit before any centralization actions are taken. In strict compliance with the **Phase 17B Read-Only Directive**, **zero files have been moved, renamed, copied, deleted, or overwritten**, and no configuration in `~/.gemini/` or project roots has been touched.

### Core Discoveries:
1. **Scope Distinction**: 
   - **Global Native Antigravity Subagents** (12 in `~/.gemini/config/agents/` and 2 in plugins) are actively managed by the Antigravity host runtime. Moving them would destroy native IDE discovery. They are classified as `KEEP GEMINI NATIVE` / `KEEP ANTIGRAVITY NATIVE` and will only be cataloged/referenced within `AI-Dev-Team`.
   - **Framework Constituent Agents** (AgentTeam: 13 roles; OpenSepia: 9 sprint agents; autonomous-dev-team: 3 pipeline agents) operate under specific orchestration runtimes within `AI-Dev-Team/repos/`.
   - **Specialist Agent Suites** (OpenHands, Strix, Understand-Anything, Awesome-LLM-Apps) provide domain-specific autonomous engines.
   - **Project-Local Agents & Tools** (`LinkedIn-Audit`, `subhajitportfolio-2.0`, `qwen-antigravity`) must remain in their respective project workspaces due to the Protected Workspaces Invariant and local runtime bindings.
2. **Exhaustive Master List**: A total of **77 genuine agents and autonomous entities** (`AGT-001` through `AGT-077`) have been identified, verified, and mapped.
3. **Broken Symlink Root Cause**: Exactly 20 symlinks in `AI-Dev-Team/skills/` (and `skills/global/`) are broken because their targets were moved during Antigravity's plugin restructuring into `~/.gemini/config/plugins/data-agent-kit-plugin/skills/` with underscore naming (e.g. `bigquery_graph`). All 20 targets have been verified to exist.
4. **Stray Directory Verification**: `/Users/subhajkar/Developer/Developer/` contains only empty folders (`subhajitportfolio-2.0/docs/audit/responsive/`), has **0 files**, is not a git repo, and is not referenced by any project.

---

## 2. Complete Agent Master List (AGT-001 – AGT-077)

| ID | Agent Name | Agent Type | Purpose | Primary Category | Secondary Category | Current Location | Source | GitHub Repository | Invocation Method | Runtime | Model | MCP Deps | Skill Deps | Project Deps | Health | Migration Risk | Recommended Action | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AGT-001** | Master Orchestrator | Global Agent | Ecosystem task orchestration & multi-backend routing | Orchestration | Multi-Backend | `~/.gemini/config/agents/master-orchestrator` | Antigravity Native | N/A (Local System) | Antigravity Runtime | System Node/Python | Dynamic (Gemini/Claude/Copilot) | All managed MCPs | `orchestration` | Host IDE | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Root Antigravity coordinator; moving breaks IDE |
| **AGT-002** | Architect | Global Subagent | System design, schema modeling, API contract definition | Software Development | Cloud / IAM | `~/.gemini/config/agents/architect` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Gemini 3.1 Pro / Sonnet 4.6 | `filesystem`, `web` | `c4-architecture`, `api-designer` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Native IDE subagent; moving breaks IDE discovery |
| **AGT-003** | Developer | Global Subagent | Core feature engineering, full-stack implementation | Software Development | Full Stack | `~/.gemini/config/agents/developer` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Gemini 3.8 Flash / Pro | `filesystem`, `git` | `tdd-workflow`, `modern-web-guidance` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Core code implementation agent; host managed |
| **AGT-004** | Fast Developer | Global Subagent | Rapid low-risk single-file fixes & quick tweaks | Software Development | Debugging | `~/.gemini/config/agents/fast-developer` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Gemini 3.8 Flash | `filesystem` | `fast-developer` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | High-speed single-step dev agent; host managed |
| **AGT-005** | Tester | Global Subagent | Automated test execution, TDD cycles & coverage | Testing / QA | Automation | `~/.gemini/config/agents/tester` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Gemini 3.8 Flash | `filesystem`, `browser` | `tdd-workflows`, `jest-skill` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Native testing subagent; host managed |
| **AGT-006** | Security Reviewer | Global Subagent | SAST, threat modeling (STRIDE), secret leak scan | Cybersecurity | Security Audit | `~/.gemini/config/agents/security-reviewer` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Claude Sonnet / Opus 4.6 | `filesystem` | `007`, `vulnerability-scanner` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Security gate subagent; host managed |
| **AGT-007** | Deep Reviewer | Global Subagent | Concurrency, edge cases & deep architectural review | Code Review | Architecture | `~/.gemini/config/agents/deep-reviewer` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Claude Sonnet 4.6 Thinking | `filesystem`, `git` | `systematic-debugging`, `differential-review` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Deep diagnostic reviewer; host managed |
| **AGT-008** | Second Opinion | Global Subagent | Orthogonal, un-biased code & architecture critique | Code Review | Quality Assurance | `~/.gemini/config/agents/second-opinion` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Claude Opus 4.6 Thinking | `filesystem` | `code-reviewer`, `grilling` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Bias-free secondary audit subagent |
| **AGT-009** | Researcher | Global Subagent | Autonomous technical literature & documentation lookup | Research | Web Research | `~/.gemini/config/agents/researcher` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Gemini 3.1 Pro | `web`, `gemini-api-docs` | `deep-research`, `search-first` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Research subagent; host managed |
| **AGT-010** | Documentation | Global Subagent | Technical documentation, living docs & ADR generation | Documentation | Technical Writing | `~/.gemini/config/agents/documentation` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Gemini 3.8 Flash | `filesystem` | `api-documenter`, `living-docs-governance` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Living docs subagent; host managed |
| **AGT-011** | Git Release | Global Subagent | Conventional commits, git worktrees & release notes | Git / GitHub | DevOps | `~/.gemini/config/agents/git-release` | Antigravity Native | N/A (Local System) | Antigravity Subagent | Host IDE | Gemini 3.8 Flash | `git`, `github` | `git-workflow`, `pr-writer` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Safe staging & release subagent |
| **AGT-012** | GitHub Copilot | External Agent | Multi-model external delegation via Copilot CLI/ACP | Git / GitHub | CI/CD | `~/.gemini/config/sidecars/copilot-bridge.mjs` | GitHub Copilot CLI | N/A (GitHub Sidecar) | Copilot Bridge CLI | Node.js | Copilot Auto / GPT-5.3 / Sonnet 5 | `github` | `copilot` | Global | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | External Copilot bridge; strictly tied to IDE config |
| **AGT-013** | Firestore Rules Author | Plugin Subagent | Cloud Firestore security rules authoring & verification | Cloud | Cybersecurity | `~/.gemini/config/plugins/firebase/agents` | Firebase Plugin | N/A (Google Plugin) | Antigravity Subagent | Host IDE | Gemini 3.8 Flash | `filesystem` | `firestore-rules-creation` | Firebase | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Firebase plugin subagent; plugin-managed |
| **AGT-014** | Flutter A11y Agent | Plugin Subagent | Flutter UI accessibility compliance auditor | Mobile | Testing / QA | `~/.gemini/config/plugins/flutter/agents` | Flutter Plugin | N/A (Google Plugin) | Antigravity Subagent | Host IDE | Gemini 3.8 Flash | `filesystem` | `flutter-apply-architecture` | Flutter | HEALTHY | BLOCKED | **KEEP ANTIGRAVITY NATIVE** | Flutter plugin subagent; plugin-managed |
| **AGT-015** | Product Manager | Agent Role | Product strategy, user story definition, acceptance | Software Development | Product Management | `AI-Dev-Team/agents/product-manager.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team` | `spec-kit` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-016** | Project Manager | Agent Role | Sprint planning, task breakdown, issue tracking | Software Development | Project Management | `AI-Dev-Team/agents/project-manager.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team` | `track-management` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-017** | Specification Engineer | Agent Role | Spec-driven requirement formalization & checklists | Documentation | Specifications | `AI-Dev-Team/agents/specification-engineer.md` | GitHub Spec Kit | `https://github.com/github/spec-kit` | `ai-team specify` | Python 3.14 | Dynamic | None | `spec-driven-development` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-018** | Software Architect | Agent Role | System topology, modular boundaries, schema design | Software Development | Architecture | `AI-Dev-Team/agents/software-architect.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team`, `filesystem` | `c4-architecture` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-019** | Frontend Developer | Agent Role | UI/UX engineering, React/Vue component creation | Software Development | Frontend | `AI-Dev-Team/agents/frontend-developer.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team`, `filesystem` | `modern-web-guidance` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-020** | Backend Developer | Agent Role | API endpoints, microservices, databases, auth | Software Development | Backend | `AI-Dev-Team/agents/backend-developer.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team`, `filesystem` | `api-patterns` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-021** | AI/ML Developer | Agent Role | LLM integration, agentic workflows, prompt tuning | AI / LLM | Data Engineering | `AI-Dev-Team/agents/aiml-developer.md` | AI-Dev-Team | `https://github.com/OpenHands/OpenHands` | Specification / Prompt | Multi-Agent | Dynamic | None | `gemini-api-dev` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-022** | DevOps Engineer | Agent Role | CI/CD, Docker containerization, Kubernetes, cloud | DevOps | Cloud | `AI-Dev-Team/agents/devops-engineer.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team` | `github-actions-templates` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-023** | QA Engineer | Agent Role | Automated testing, unit/integration/E2E test suites | Testing / QA | Automation | `AI-Dev-Team/agents/qa-engineer.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team`, `browser` | `tdd-workflow` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-024** | Security Engineer | Agent Role | SAST scanning, secret auditing, remediation | Cybersecurity | Security Audit | `AI-Dev-Team/agents/security-engineer.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team` | `security-scanning-security-sast` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-025** | Code Reviewer | Agent Role | Code quality audits, complexity checks, linting | Code Review | Quality Assurance | `AI-Dev-Team/agents/code-reviewer.md` | autonomous-dev-team | `https://github.com/zxkane/autonomous-dev-team` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team` | `code-reviewer` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-026** | Documentation Engineer | Agent Role | API docs, architectural blueprints, guides | Documentation | Technical Writing | `AI-Dev-Team/agents/documentation-engineer.md` | AI-Dev-Team | `https://github.com/RichardLemmon/AgentTeam` | Specification / Prompt | Multi-Agent | Dynamic | `agent-team` | `documentation` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-027** | Research Engineer | Agent Role | Scientific & technical evaluations, library analysis | Research | Web Research | `AI-Dev-Team/agents/research-engineer.md` | AI-Dev-Team | `https://github.com/Egonex-AI/Understand-Anything` | Specification / Prompt | Multi-Agent | Dynamic | `web` | `deep-research` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-028** | Git/GitHub Engineer | Agent Role | Issue management, worktrees, branches, PRs | Git / GitHub | DevOps | `AI-Dev-Team/agents/github-engineer.md` | autonomous-dev-team | `https://github.com/zxkane/autonomous-dev-team` | Specification / Prompt | Multi-Agent | Dynamic | `github`, `git` | `git-workflow` | None | HEALTHY | LOW | **CENTRALIZE** | Move to `AI-Dev-Team/roles/`; symlink in `agents/` |
| **AGT-029** | AgentTeam Full-Stack Dev | Agent Role | Full-stack feature developer within AgentTeam | Software Development | Full Stack | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-030** | AgentTeam Backend Dev | Agent Role | Backend API & DB developer within AgentTeam | Software Development | Backend | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-031** | AgentTeam Frontend Dev | Agent Role | Web frontend developer within AgentTeam | Software Development | Frontend | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-032** | AgentTeam Mobile Dev | Agent Role | Mobile application developer within AgentTeam | Mobile | Flutter / React Native | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-033** | AgentTeam DevOps | Agent Role | CI/CD & container engineer within AgentTeam | DevOps | Cloud | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-034** | AgentTeam QA | Agent Role | Test authoring & execution within AgentTeam | Testing / QA | Automation | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-035** | AgentTeam Security | Agent Role | Security compliance & threat check in AgentTeam | Cybersecurity | Security Audit | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-036** | AgentTeam Product Manager | Agent Role | Product backlog & user stories in AgentTeam | Software Development | Product Management | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-037** | AgentTeam Project Manager | Agent Role | Project coordinator & sprint manager in AgentTeam | Software Development | Project Management | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-038** | AgentTeam Data Engineer | Agent Role | Data pipelines & storage schemas in AgentTeam | Data Engineering | Databases | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-039** | AgentTeam Data Scientist | Agent Role | Analytics & predictive modeling in AgentTeam | Data Analysis | AI / ML | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-040** | AgentTeam UX Researcher | Agent Role | User journey analysis & personas in AgentTeam | Software Development | UI / UX | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-041** | AgentTeam UX/UI Designer | Agent Role | Interface design & token layout in AgentTeam | Software Development | UI / UX | `AI-Dev-Team/repos/AgentTeam/agents` | AgentTeam Repo | `https://github.com/RichardLemmon/AgentTeam` | AgentTeam Prompt | Node 22 LTS | Dynamic | `agent-team` | None | AgentTeam | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Framework constituent agent prompt |
| **AGT-042** | OpenSepia Product Owner | Agent Role | Agile PO managing user stories & acceptance | Software Development | Product Management | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`po`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-043** | OpenSepia Project Manager | Agent Role | Agile PM managing boards, milestones & assignments | Software Development | Project Management | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`pm`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-044** | OpenSepia Developer 1 | Agent Role | Primary full-stack feature developer in sprint | Software Development | Full Stack | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`dev1`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-045** | OpenSepia Developer 2 | Agent Role | Secondary developer for concurrent task sprints | Software Development | Full Stack | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`dev2`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-046** | OpenSepia QA Tester | Agent Role | Acceptance tester running test suites & reporting | Testing / QA | Automation | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`tester`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-047** | OpenSepia DevOps | Agent Role | CI/CD build scripts & deployment manager | DevOps | CI/CD | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`devops`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-048** | OpenSepia Security Analyst | Agent Role | SAST auditing & security approval for MRs | Cybersecurity | Security Audit | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`sec_analyst`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-049** | OpenSepia Arch Reviewer | Agent Role | Architecture design conformity reviewer | Code Review | Architecture | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`arch_reviewer`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-050** | OpenSepia Scrum Master | Agent Role | Sprint cycle transitions & team retrospectives | Software Development | Agile / Sprints | `AI-Dev-Team/repos/OpenSepia` | OpenSepia Repo | `https://github.com/CelaenoIndustry/OpenSepia` | CLI (`scrum_master`) | Python 3.14 venv | Claude Code CLI | None | None | OpenSepia | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent framework sprint role |
| **AGT-051** | Autonomous Dispatcher | Workflow Agent | Cron-driven issue scanner detecting `autonomous` labels | Automation | DevOps | `AI-Dev-Team/repos/autonomous-dev-team` | autonomous-dev-team | `https://github.com/zxkane/autonomous-dev-team` | Shell / Cron | Zsh / Git | Agnostic | None | `autonomous-dispatcher` | autonomous-dev-team | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Automated issue scanner pipeline |
| **AGT-052** | Autonomous Dev Agent | Workflow Agent | TDD implementation in isolated git worktrees | Software Development | Full Stack | `AI-Dev-Team/repos/autonomous-dev-team` | autonomous-dev-team | `https://github.com/zxkane/autonomous-dev-team` | Shell Dispatch | Zsh / Antigravity CLI | Gemini / Claude | `filesystem`, `git` | `autonomous-dev` | autonomous-dev-team | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Worktree isolated feature builder |
| **AGT-053** | Autonomous Review Agent | Workflow Agent | PR review, merge conflict check & auto-merge | Code Review | Git / GitHub | `AI-Dev-Team/repos/autonomous-dev-team` | autonomous-dev-team | `https://github.com/zxkane/autonomous-dev-team` | Shell Dispatch | Zsh / Antigravity CLI | Gemini / Claude | `git`, `github` | `autonomous-review` | autonomous-dev-team | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Automated PR reviewer & merger |
| **AGT-054** | OpenHands Agent Canvas | Agent Platform | Autonomous AI software engineer with visual canvas | Software Development | Full Stack | `AI-Dev-Team/repos/OpenHands` | OpenHands Repo | `https://github.com/OpenHands/OpenHands` | `ai-team canvas` | Node 24+ / Python 3.14 | Dynamic | Docker / MCP | None | OpenHands | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Autonomous coding platform |
| **AGT-055** | Strix Pentesting Agent | Global Agent | Autonomous AI penetration tester finding app vulns | Cybersecurity | Penetration Testing | `AI-Dev-Team/repos/strix` | Strix Repo | `https://github.com/usestrix/strix` | Python CLI | Python 3.14 | Dynamic LLM | None | `web-app-penetration-testing` | Strix | PARTIAL | NONE | **KEEP INSIDE REPOSITORY** | Requires live target URL & auth token |
| **AGT-056** | Understand-Anything | Agent System | AST-driven knowledge graph & code comprehension | Code Review | Architecture | `AI-Dev-Team/repos/Understand-Anything` | Understand-Anything Repo | `https://github.com/Egonex-AI/Understand-Anything` | CLI / Web UI | Node.js | Gemini / Claude | None | `understand-chat`, `understand-explain` | None | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | AST repository understanding engine |
| **AGT-057** | Spec Kit Runner | Workflow Agent | Specification-driven development CLI & check engine | Documentation | Specifications | `AI-Dev-Team/repos/spec-kit` | GitHub Spec Kit | `https://github.com/github/spec-kit` | `ai-team specify` | Python 3.14 venv | Agnostic | None | `spec-driven-development` | None | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Official GitHub specification toolkit |
| **AGT-058** | AI Fraud Investigation | Specialist Agent | Public records cross-examination & fraud detection | Data Analysis | Cybersecurity | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | None | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Domain-specific LLM agent application |
| **AGT-059** | Insurance Claim Live Team | Multi-Agent Team | Real-time voice & text insurance claim settlement | Automation | Voice AI | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `voice-agents` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Domain-specific live agent team |
| **AGT-060** | AI Dashboard Canvas Agent | Specialist Agent | Generative UI dashboard builder with canvas | Frontend | Generative UI | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python / React | Python 3.14 / Node | OpenAI / Gemini | None | `magic-ui-generator` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Generative UI agent application |
| **AGT-061** | AI Deep Research Agent | Specialist Agent | Multi-step autonomous research & synthesis | Research | Web Research | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `deep-research` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Autonomous deep research agent |
| **AGT-062** | AI Financial Coach Agent | Specialist Agent | Personal finance management & spending analysis | Data Analysis | Automation | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | None | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Financial coaching agent app |
| **AGT-063** | Shadcn Component Gen | Specialist Agent | React Shadcn component generation & preview | Frontend | Web Development | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python / React | Python 3.14 / Node | OpenAI / Gemini | None | `ui-component` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | UI component generative agent |
| **AGT-064** | AI MCP App Builder | Specialist Agent | Autonomous MCP application builder & connector | AI / LLM | Tooling | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | MCP SDK | `mcp-server-patterns` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | MCP application builder agent |
| **AGT-065** | AI Knowledge Explorer | Specialist Agent | Graph-based knowledge retrieval & interactive chat | Research | Data Analysis | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | None | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Knowledge explorer agent |
| **AGT-066** | Mixture of Agents | Multi-Agent Team | Multi-LLM collaborative reasoning architecture | AI / LLM | Research | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | Multiple Models | None | None | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Multi-agent ensemble architecture |
| **AGT-067** | AI Data Analysis Agent | Specialist Agent | Pandas/Polars automated statistical data analyst | Data Analysis | Python | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `data-engineer` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Automated data analysis agent |
| **AGT-068** | Web Scraping AI Agent | Specialist Agent | Intelligent DOM navigation & web data extraction | Web Scraping | Automation | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `apify-lead-generation` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Web scraping agent app |
| **AGT-069** | AI Reasoning Agent | Specialist Agent | Step-by-step chain-of-thought logic verifier | AI / LLM | Research | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `thinking-out-loud` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Chain-of-thought reasoning agent |
| **AGT-070** | Startup Trend Analysis | Specialist Agent | Real-time market sizing & startup opportunity audit | Research | Market Research | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `market-research` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Market research agent app |
| **AGT-071** | Voice Customer Support | Specialist Agent | Real-time bidirectional voice customer support agent | Automation | Voice AI | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `voice-agents` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Voice customer support agent |
| **AGT-072** | DeepSeek Local RAG Agent | Specialist Agent | Local offline RAG pipeline powered by DeepSeek | AI / LLM | Data Analysis | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | DeepSeek R1 / V3 | None | `rag-implementation` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Local RAG agent app |
| **AGT-073** | Project Graveyard Agent | Specialist Agent | Dead side-project autopsy & code asset extractor | Software Development | Productivity | `AI-Dev-Team/repos/awesome-llm-apps` | awesome-llm-apps | `https://github.com/Shubhamsaboo/awesome-llm-apps` | Python Script | Python 3.14 | OpenAI / Gemini | None | `project-graveyard` | awesome-llm-apps | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Codebase autopsy agent |
| **AGT-074** | Qwen Antigravity Bridge | Model Router | FastAPI Gemini-to-Qwen3.8-27B translation proxy | Model Router | AI / LLM | `qwen-antigravity/bridge.py` | Custom Local Utility | N/A (Local Project) | Uvicorn / HTTP | Python 3.14 (`.venv`) | Qwen3.8-27B (HF Router) | None | None | `qwen-antigravity` | HEALTHY | BLOCKED | **KEEP PROJECT-LOCAL** | Dedicated local model bridge |
| **AGT-075** | OmniRoute Gateway | Model Router | Free AI gateway managing 359 providers & fallback | Model Router | Multi-Backend | `AI-Dev-Team/repos/omniroute` | OmniRoute Repo | `https://github.com/diegosouzapw/OmniRoute` | Node / CLI | Node 22+ | Multi-Provider | None | None | None | HEALTHY | NONE | **KEEP INSIDE REPOSITORY** | Enterprise multi-model gateway |
| **AGT-076** | LinkedIn Profile Reader | Project-Local Tool | Authenticated Chrome reader for LinkedIn audits | LinkedIn | Automation | `LinkedIn-Audit/linkedin_reader.py` | Custom Local Project | N/A (Protected Repo) | Python / AppleScript | Python 3.14 | None | None | `li-profile`, `li-human` | `LinkedIn-Audit` | HEALTHY | BLOCKED | **KEEP PROJECT-LOCAL** | Bound to protected LinkedIn workspace |
| **AGT-077** | Portfolio Testing Suite | Project-Local Suite | Playwright & security testing skills bound to portfolio | Testing / QA | Cybersecurity | `subhajitportfolio-2.0/.agent/skills` | subhajitportfolio-2.0 | N/A (Protected Repo) | Playwright / Node | Node.js | Dynamic | None | 17 project skills | `subhajitportfolio-2.0` | HEALTHY | BLOCKED | **KEEP PROJECT-LOCAL** | Bound to protected portfolio workspace |

---

## 3. Classification Breakdown

To avoid confusing repositories or skill libraries with agents, the ecosystem is partitioned into exact functional types:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   ECOSYSTEM TAXONOMY & CLASSIFICATION                  │
├────────────────────────────┬───────────────────────────────────────────┤
│ Classification             │ Count & Representative Entities           │
├────────────────────────────┼───────────────────────────────────────────┤
│ 1. GLOBAL AGENTS           │ 14 (12 Antigravity Native + 2 Plugin)     │
│ 2. AGENT ROLES             │ 36 (14 Standardized + 13 AgentTeam + 9 OS)│
│ 3. AGENT PLATFORMS         │ 1 (OpenHands Agent Canvas)                │
│ 4. MULTI-AGENT FRAMEWORKS  │ 3 (OpenSepia, AgentTeam, Awesome-LLM)     │
│ 5. ORCHESTRATORS           │ 2 (Master Orchestrator, Auto-Dispatcher)  │
│ 6. MODEL ROUTERS           │ 2 (OmniRoute, Qwen Bridge)                │
│ 7. SKILLS                  │ 1,345 centralized skill links             │
│ 8. MCP SERVERS             │ 15 active (AgentTeam, Filesystem, etc.)   │
│ 9. MCP TOOLS               │ 120+ registered tools                     │
│ 10. WORKFLOWS              │ 4 (Spec Kit SDD, Worktree TDD, etc.)      │
│ 11. PROJECT-LOCAL TOOLS    │ 2 (LinkedIn Reader, Portfolio Test Suite) │
│ 12. NORMAL PROJECT CODE    │ subhajitportfolio-2.0, LinkedIn-Audit     │
└────────────────────────────┴───────────────────────────────────────────┘
```

---

## 4. Agent Hierarchy

```
AI Dev Ecosystem Architecture
│
├── [Global Antigravity Runtime] (Host IDE Orchestration)
│   ├── Master Orchestrator (AGT-001)
│   ├── Architect Specialist (AGT-002)
│   ├── Developer (AGT-003)
│   ├── Fast Developer (AGT-004)
│   ├── Tester (AGT-005)
│   ├── Security Reviewer (AGT-006)
│   ├── Deep Reviewer (AGT-007)
│   ├── Second Opinion (AGT-008)
│   ├── Researcher (AGT-009)
│   ├── Documentation (AGT-010)
│   ├── Git Release (AGT-011)
│   ├── GitHub Copilot Bridge (AGT-012)
│   └── Plugins
│       ├── Firebase: Firestore Rules Author (AGT-013)
│       └── Flutter: Flutter A11y Agent (AGT-014)
│
├── [OpenSepia Framework] (Continuous Autonomous Agile Sprints)
│   ├── Orchestrator: run_agent_cli.py / cron
│   ├── Product Owner (po) (AGT-042)
│   ├── Project Manager (pm) (AGT-043)
│   ├── Scrum Master (AGT-050)
│   ├── Architecture Reviewer (AGT-049)
│   ├── Developer 1 (dev1) (AGT-044)
│   ├── Developer 2 (dev2) (AGT-045)
│   ├── QA Tester (tester) (AGT-046)
│   ├── DevOps Engineer (devops) (AGT-047)
│   └── Security Analyst (sec_analyst) (AGT-048)
│
├── [AgentTeam Framework] (Collaborative Team & SQLite Store)
│   ├── Orchestrator / MCP: AgentTeam MCP Server (44 tools)
│   ├── Product Manager (AGT-036)
│   ├── Project Manager (AGT-037)
│   ├── Full-Stack Developer (AGT-029)
│   ├── Frontend Developer (AGT-031)
│   ├── Backend Developer (AGT-030)
│   ├── Mobile Developer (AGT-032)
│   ├── Data Engineer (AGT-038)
│   ├── Data Scientist (AGT-039)
│   ├── UX Researcher (AGT-040)
│   ├── UX/UI Designer (AGT-041)
│   ├── QA Engineer (AGT-034)
│   ├── DevOps Engineer (AGT-033)
│   └── Security Engineer (AGT-035)
│
├── [autonomous-dev-team Pipeline] (Git Worktree Delivery Pipeline)
│   ├── Autonomous Dispatcher (AGT-051)
│   ├── Autonomous Dev Agent (AGT-052)
│   └── Autonomous Review Agent (AGT-053)
│
├── [OpenHands Autonomous Platform] (Autonomous Software Engineer)
│   └── OpenHands Agent Canvas / Server (AGT-054)
│
├── [Specialist Security & Comprehension Engines]
│   ├── Strix Autonomous Pentesting Agent (AGT-055)
│   └── Understand-Anything AST Engine (AGT-056)
│
└── [Model Routing Gateways]
    ├── OmniRoute Multi-Provider Gateway (AGT-075)
    └── Qwen Antigravity Bridge Proxy (AGT-074)
```

---

## 5. Global Gemini & Antigravity Agents Dedicated Analysis

A deep architectural evaluation was performed on all agents residing under `~/.gemini/config/agents/` and plugin directories:

| Agent Name | Location | Native Owner | Discovery Mechanism | Can Move? | Can Copy? | Can Symlink? | Recommended Strategy | Risk of Moving |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **master-orchestrator** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks IDE root orchestration |
| **architect** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks subagent invocation |
| **developer** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks core coding pipeline |
| **fast-developer** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks rapid single-file workflow |
| **tester** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks automated test verification |
| **security-reviewer** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Bypasses mandatory security gates |
| **deep-reviewer** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks deep architectural review |
| **second-opinion** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Destroys orthogonal critique |
| **researcher** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks research tool delegation |
| **documentation** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks automated doc authoring |
| **git-release** | `~/.gemini/config/agents/` | Antigravity Host | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks git release management |
| **github-copilot** | `~/.gemini/config/agents/` | Copilot Bridge | Global Agent Discovery (`agent.md`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Breaks external Copilot bridge |
| **firestore-rules-author** | `~/.gemini/config/plugins/firebase` | Firebase Plugin | Plugin Manifest (`plugin.json`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Disables Firebase security author |
| **flutter_a11y_agent** | `~/.gemini/config/plugins/flutter` | Flutter Plugin | Plugin Manifest (`plugin.json`) | NO | YES | YES | **KEEP ANTIGRAVITY NATIVE** | CRITICAL: Disables Flutter a11y reviews |

**Architectural Policy**: Antigravity discovers subagents strictly from `~/.gemini/config/agents/` and active plugins. **Never move these directories.** Instead, maintain them as the authoritative runtime source and establish reference catalog entries in `AI-Dev-Team/inventory/`.

---

## 6. Project-Local Agents & Protected Workspaces Analysis

| Project Workspace | Artifact | Purpose | Project Dependency | Reusable Globally? | Migration Possible? | Migration Recommended? | Reason & Invariants |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **LinkedIn-Audit** | `linkedin_reader.py` | Authenticated Chrome reader for profile re-audits | HARD | NO | NO | **NO** | **PROTECTED WORKSPACE INVARIANT**. Requires authenticated Chrome session on target user machine. |
| **LinkedIn-Audit** | `generate_full_reaudit_pdf.py` | 39-section PDF report generator adhering to rubric | HARD | NO | NO | **NO** | **PROTECTED WORKSPACE INVARIANT**. Produces client-ready PDF outputs to `~/Desktop/LinkedIn-Audit`. |
| **subhajitportfolio-2.0** | `.agent/skills/` (17 skills) | Playwright, accessibility & security test harnesses | HARD | PARTIAL | NO | **NO** | **PROTECTED WORKSPACE INVARIANT**. Hardcoded selectors and assertions for portfolio frontend. |
| **qwen-antigravity** | `bridge.py` | Gemini-to-Qwen OpenAI completion API proxy | STANDALONE | YES | NO | **NO** | Operates as a local background HTTP service. Keep in place; document in central model router catalog. |

---

## 7. Centralization Strategy & Authority Matrix

Every discovered entity has been assigned an explicit operational directive:

1. **`AI-Dev-Team/agents/` (The 14 Standardized Role Specifications)**:
   - **Strategy**: `CENTRALIZE`.
   - **Action**: Organize the role markdown specifications into `AI-Dev-Team/roles/`, and place backward-compatible symlinks in `AI-Dev-Team/agents/`.
2. **`~/.gemini/config/agents/` (12 Antigravity Global Subagents)**:
   - **Strategy**: `KEEP ANTIGRAVITY NATIVE`.
   - **Action**: Authoritative copies remain in `~/.gemini/config/agents/`. Referenced in `AI-Dev-Team/inventory/`.
3. **`~/.gemini/config/plugins/*/agents/` (2 Plugin Subagents)**:
   - **Strategy**: `KEEP ANTIGRAVITY NATIVE`.
   - **Action**: Authoritative copies remain in plugin directories. Referenced in `AI-Dev-Team/inventory/`.
4. **`AI-Dev-Team/repos/` (Frameworks: AgentTeam, OpenSepia, autonomous-dev-team, OpenHands, Strix)**:
   - **Strategy**: `KEEP INSIDE REPOSITORY`.
   - **Action**: Framework-specific agents must remain with their respective codebases, venvs, and test harnesses.
5. **Project-Local Agents (`LinkedIn-Audit`, `subhajitportfolio-2.0`, `qwen-antigravity`)**:
   - **Strategy**: `KEEP PROJECT-LOCAL`.
   - **Action**: Strictly respect Protected Workspace Invariants. Catalog capabilities only.

---

## 8. Deduplication Analysis

```
┌────────────────────────────────────────────────────────────────────────┐
│                        DEDUPLICATION RESOLUTION                        │
├────────────────────────────┬───────────────────────────────────────────┤
│ Agent / Artifact           │ Authoritative vs Reference Mapping        │
├────────────────────────────┼───────────────────────────────────────────┤
│ Standardized Roles         │ Authoritative: AI-Dev-Team/roles/         │
│                            │ Reference / Backward Link: agents/        │
│                            │ Catalog Entry: AGT-015 - AGT-028          │
├────────────────────────────┼───────────────────────────────────────────┤
│ AgentTeam Role Prompts     │ Authoritative: repos/AgentTeam/agents/    │
│                            │ Runtime: AgentTeam MCP Server             │
│                            │ Catalog Entry: AGT-029 - AGT-041          │
├────────────────────────────┼───────────────────────────────────────────┤
│ Superpowers Skills         │ Authoritative: plugins/superpowers/skills │
│                            │ Reference Copy: repos/superpowers/skills  │
│                            │ Symlink Target: AI-Dev-Team/skills/       │
├────────────────────────────┼───────────────────────────────────────────┤
│ ECC Skills                 │ Authoritative: repos/ecc/skills/          │
│                            │ Runtime Copy: plugins/ecc/skills/         │
│                            │ Symlink Target: AI-Dev-Team/skills/       │
└────────────────────────────┴───────────────────────────────────────────┘
```

---

## 9. Broken Symlinks Comprehensive Root-Cause Analysis

All 20 broken symlinks identified by `ai-team doctor` have been traced to their exact verified targets:

| # | Broken Link Path | Current Invalid Target | Verified Actual Target | Root Cause | Target Verified? | Repair Command (Pending Approval) |
|---|---|---|---|---|:---:|---|
| 1 | `skills/bigquery-graph` | `~/.gemini/config/skills/bigquery-graph` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/bigquery_graph` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/bigquery_graph skills/bigquery-graph` |
| 2 | `skills/bigtable-basics` | `~/.gemini/config/skills/bigtable-basics` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/bigtable_basics` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/bigtable_basics skills/bigtable-basics` |
| 3 | `skills/gcp-composer-troubleshooting` | `~/.gemini/config/skills/gcp-composer-troubleshooting` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_composer_troubleshooting` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_composer_troubleshooting skills/gcp-composer-troubleshooting` |
| 4 | `skills/gcp-managed-airflow-dag-authoring` | `~/.gemini/config/skills/gcp-managed-airflow-dag-authoring` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_managed_airflow_dag_authoring` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_managed_airflow_dag_authoring skills/gcp-managed-airflow-dag-authoring` |
| 5 | `skills/gcp-managed-airflow-migrations` | `~/.gemini/config/skills/gcp-managed-airflow-migrations` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_managed_airflow_migrations` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_managed_airflow_migrations skills/gcp-managed-airflow-migrations` |
| 6 | `skills/gcp-managed-airflow-recommendations`| `~/.gemini/config/skills/gcp-managed-airflow-recommendations` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_managed_airflow_recommendations` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcp_managed_airflow_recommendations skills/gcp-managed-airflow-recommendations` |
| 7 | `skills/gcs-security-assessment` | `~/.gemini/config/skills/gcs-security-assessment` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcs_security_assessment` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/gcs_security_assessment skills/gcs-security-assessment` |
| 8 | `skills/google-cloud-storage-basics` | `~/.gemini/config/skills/google-cloud-storage-basics` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/google_cloud_storage_basics` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/google_cloud_storage_basics skills/google-cloud-storage-basics` |
| 9 | `skills/google-cloud-storage-bucket-architect`| `~/.gemini/config/skills/google-cloud-storage-bucket-architect` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/google_cloud_storage_bucket_architect` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/google_cloud_storage_bucket_architect skills/google-cloud-storage-bucket-architect` |
| 10 | `skills/google-cloud-storage-fuse` | `~/.gemini/config/skills/google-cloud-storage-fuse` | `~/.gemini/config/plugins/data-agent-kit-plugin/skills/google_cloud_storage_fuse` | Renamed with underscore in plugin | YES | `ln -sfn ~/.gemini/config/plugins/data-agent-kit-plugin/skills/google_cloud_storage_fuse skills/google-cloud-storage-fuse` |
| 11-20 | `skills/global/*` (same 10 skills as above) | Duplicate links under `skills/global/` | Same 10 plugin targets | Same root cause | YES | Same repair command targeting `skills/global/` |

---

## 10. Stray Directory Verification

Detailed investigation of `/Users/subhajkar/Developer/Developer`:
- **Directory Tree**: `/Users/subhajkar/Developer/Developer/subhajitportfolio-2.0/docs/audit/responsive/`
- **File Count**: Exactly **0 files** (verified via Python walk & filesystem count).
- **Git Tracking**: **Not tracked by Git** (no `.git` directory exists).
- **References**: Zero references in `AI-Dev-Team`, `subhajitportfolio-2.0`, or global configs.
- **Accidental Generation**: Created accidentally by a script that was executed from `~/Developer` with a relative path intended for `subhajitportfolio-2.0`.
- **Verdict**: Completely safe to remove upon explicit approval.

---

## 11. Proposed Excel Master Catalog Architecture

The proposed `AI-Dev-Team/Agent-Catalog.xlsx` workbook will feature **13 structured worksheets**:

1. **`Agent Catalog`**: Master tabular dataset with all 77 agents, capabilities, runtimes, clickable GitHub URLs, health, and actions.
2. **`Purpose View`**: Categorized grouping by domain (Web, Security, Cloud, Data, DevOps, Research, etc.).
3. **`Quick Reference`**: Fast lookup: "I need to perform X. Which agents do I have that support X?" with documented capabilities.
4. **`Capability Matrix`**: Strict YES/NO/PARTIAL matrix across 25 technical domains for all 77 agents.
5. **`Agent Hierarchy`**: Visual parent-child tree showing multi-agent frameworks, orchestrators, constituent agents, and tools.
6. **`GitHub Sources`**: Full provenance table with verified GitHub URLs, organizations, branches, commits, and licenses.
7. **`Duplicates`**: Deduplication table documenting Authoritative, Reference, and Runtime copies.
8. **`Dependencies`**: Comprehensive mapping of runtimes, MCP servers, skills, and model requirements.
9. **`Health Status`**: Granular operational health states, entrypoints, and issues.
10. **`Migration Status`**: Pre- and post-migration states with risk levels and rollback procedures.
11. **`Global Gemini Agents`**: Dedicated analysis of `~/.gemini/config/agents/` and plugin subagents.
12. **`Project-Local Agents`**: Dedicated view of protected project tools (`LinkedIn-Audit`, `subhajitportfolio-2.0`, `qwen-antigravity`).
13. **`Summary`**: Dynamic summary KPI cards (Total Agents, Healthy, Broken, Categories, Frameworks).

---

## 12. Quick Reference Guide Preview

| Task / Objective | Recommended Applicable Agents | When To Use | Required Dependencies | Health Status | Primary Source |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Web Development (Full-Stack)** | `developer` (AGT-003), `frontend-developer` (AGT-019), `backend-developer` (AGT-020), `agentteam-full-stack-developer` (AGT-029) | Building new web apps, React/Vue components, REST/GraphQL APIs | Node.js, Python, MCP filesystem | HEALTHY | Antigravity Native / AgentTeam |
| **Security Audit & SAST** | `security-reviewer` (AGT-006), `security-engineer` (AGT-024), `opensepia-security-analyst` (AGT-048) | Reviewing code for OWASP top 10, secret leaks, vulnerability checks | SAST tools, Claude Opus/Sonnet | HEALTHY | Antigravity Native / OpenSepia |
| **Penetration Testing** | `strix-agent` (AGT-055) | Autonomous white-box/black-box application penetration testing | Python 3.14, target URL, API key | PARTIAL (Needs Config) | `https://github.com/usestrix/strix` |
| **Cloud & IAM Architecture** | `architect` (AGT-002), `software-architect` (AGT-018), `firestore-rules-author` (AGT-013) | Designing cloud topology, database schemas, IAM boundaries | Host IDE, Terraform/Cloud MCPs | HEALTHY | Antigravity Native / Firebase Plugin |
| **Repository Comprehension** | `understand-anything` (AGT-056), `researcher` (AGT-009) | Visualizing unfamiliar codebases with AST knowledge graphs | Node.js, Tree-sitter | HEALTHY | `https://github.com/Egonex-AI/Understand-Anything` |
| **Automated Testing & TDD** | `tester` (AGT-005), `qa-engineer` (AGT-023), `autonomous-dev` (AGT-052) | Writing unit/integration tests, running TDD red-green cycles | Pytest, Vitest, Playwright | HEALTHY | Antigravity Native / autonomous-dev-team |
| **Autonomous Issue-to-PR** | `autonomous-dispatcher` (AGT-051), `autonomous-dev` (AGT-052), `autonomous-review` (AGT-053) | Unattended issue scanning, git worktree coding, and PR review | Zsh, Git Worktrees, GitHub CLI | HEALTHY | `https://github.com/zxkane/autonomous-dev-team` |
| **Multi-Model Routing & Gateway**| `omniroute-gateway` (AGT-075), `qwen-antigravity-bridge` (AGT-074) | Aggregating free AI tiers, fallback routing, and local HuggingFace proxies | Node.js / Python FastAPI | HEALTHY | `https://github.com/diegosouzapw/OmniRoute` |

---

## 13. Verified GitHub Sources Table

| Repository | Organization | Verified URL | Branch | Verified Commit | License | Source Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **AgentTeam** | Richard Lemmon | `https://github.com/RichardLemmon/AgentTeam` | `main` | `bfffdf2dc1cfc048b8c5cf98c6a0d4508c9b2813` | MIT | VERIFIED |
| **OpenHands** | OpenHands AI | `https://github.com/OpenHands/OpenHands` | `main` | `82203bb1011cdf0e6eb318a32111806a6f6f734a` | MIT | VERIFIED |
| **OpenSepia** | Celaeno Industry | `https://github.com/CelaenoIndustry/OpenSepia` | `main` | `ecdd19fe92acf74a9f1d2b7274d4738d042a99a2` | Apache 2.0 | VERIFIED |
| **Understand-Anything** | Egonex-AI | `https://github.com/Egonex-AI/Understand-Anything.git` | `main` | `6df3065f1d8ddc2ce3615314d1d493f36d6b1c80` | MIT | VERIFIED |
| **addyosmani-agent-skills**| Addy Osmani | `https://github.com/addyosmani/agent-skills.git` | `main` | `be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39` | MIT | VERIFIED |
| **agentic-awesome-skills** | sickn33 | `https://github.com/sickn33/agentic-awesome-skills.git` | `main` | `69906dde999aaa0f3d173f0e3d5bcdb84c87a294` | Apache 2.0 | VERIFIED |
| **antigravity-skills** | rmyndharis | `https://github.com/rmyndharis/antigravity-skills.git` | `main` | `3eff4af253b3a15e2ba6edf2c2b743b53fd81211` | MIT | VERIFIED |
| **autonomous-dev-team** | zxkane | `https://github.com/zxkane/autonomous-dev-team` | `main` | `549d103ae07f1e22b8d374736671f7d0ddf53184` | MIT | VERIFIED |
| **awesome-llm-apps** | Shubham Saboo | `https://github.com/Shubhamsaboo/awesome-llm-apps.git` | `main` | `f163bb5a92111cee4610ac98e5dce4c6a2a09c26` | Apache 2.0 | VERIFIED |
| **context7** | Upstash | `https://github.com/upstash/context7.git` | `master` | `dedb03d589e6e03e8fb5a2b858bd3c853ac6893e` | MIT | VERIFIED |
| **ecc** | Affaan Mustafa | `https://github.com/affaan-m/ECC.git` | `main` | `8321021c54d670126ce3b2969d5deb880b4b0c2a` | MIT | VERIFIED |
| **graphify** | Graphify Labs | `https://github.com/Graphify-Labs/graphify.git` | `v8` | `26b02b5e3430e4ab85dd7e72c7b98836d8e65c48` | MIT | VERIFIED |
| **mattpocock-skills** | Matt Pocock | `https://github.com/mattpocock/skills.git` | `main` | `74ca5fe077456a0b3b2f5310cf9430999fd0b5fd` | MIT | VERIFIED |
| **omniroute** | Diego Souza | `https://github.com/diegosouzapw/OmniRoute.git` | `release/v3.8.51`| `0d089e7e396c18107a64a7130a7ffb897c21b3ef` | GPL-3.0 | VERIFIED |
| **ponytail** | Dietrich Gebert | `https://github.com/DietrichGebert/ponytail.git` | `main` | `e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156` | MIT | VERIFIED |
| **spec-kit** | GitHub | `https://github.com/github/spec-kit.git` | `main` | `319fb84f5a6dc8db1cd8558e0a5504948b6ca2ea` | MIT | VERIFIED |
| **strix** | UseStrix | `https://github.com/usestrix/strix.git` | `main` | `910c1ea4bbf22f8c01ab6c2a54bad09b94ccbc3b` | Apache 2.0 | VERIFIED |
| **superpowers** | Jesse Vincent | `https://github.com/obra/superpowers.git` | `main` | `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` | MIT | VERIFIED |

---

## 14. Final Pre-Migration Action Table

| ID | Agent / Component | Current Location | Type | Action | Proposed Destination | Risk | Reason & Invariant | Dependency Impact |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **AGT-001** | Master Orchestrator | `~/.gemini/config/agents/` | Global Agent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-002** | Architect | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-003** | Developer | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-004** | Fast Developer | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-005** | Tester | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-006** | Security Reviewer | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-007** | Deep Reviewer | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-008** | Second Opinion | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-009** | Researcher | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-010** | Documentation | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-011** | Git Release | `~/.gemini/config/agents/` | Global Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Host IDE owns discovery | None |
| **AGT-012** | GitHub Copilot | `~/.gemini/config/sidecars/` | External Agent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | External bridge configuration | None |
| **AGT-013** | Firestore Rules Author | `~/.gemini/config/plugins/firebase` | Plugin Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Firebase plugin discovery | None |
| **AGT-014** | Flutter A11y Agent | `~/.gemini/config/plugins/flutter` | Plugin Subagent | **KEEP ANTIGRAVITY NATIVE** | N/A (Cataloged) | NONE | Flutter plugin discovery | None |
| **AGT-015–028**| Standardized Roles (14) | `AI-Dev-Team/agents/` | Agent Roles | **CENTRALIZE** | `AI-Dev-Team/roles/` + symlinks in `agents/` | LOW | Standardizes role architecture | Preserves all references via symlinks |
| **AGT-029–041**| AgentTeam Roles (13) | `AI-Dev-Team/repos/AgentTeam` | Framework Roles | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Bound to AgentTeam runtime & MCP | None |
| **AGT-042–050**| OpenSepia Roles (9) | `AI-Dev-Team/repos/OpenSepia` | Framework Roles | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Bound to OpenSepia CLI & cron | None |
| **AGT-051–053**| Autonomous Pipeline (3) | `AI-Dev-Team/repos/autonomous-dev-team` | Pipeline Agents | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Bound to worktree dispatcher scripts | None |
| **AGT-054** | OpenHands Agent Canvas | `AI-Dev-Team/repos/OpenHands` | Agent Platform | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Standalone autonomous platform | None |
| **AGT-055** | Strix Pentesting Agent | `AI-Dev-Team/repos/strix` | Security Agent | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Standalone penetration test engine | None |
| **AGT-056** | Understand-Anything | `AI-Dev-Team/repos/Understand-Anything` | Agent System | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Tree-sitter knowledge graph system | None |
| **AGT-057** | Spec Kit Runner | `AI-Dev-Team/repos/spec-kit` | Workflow Agent | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | GitHub specification CLI | None |
| **AGT-058–073**| Awesome-LLM Agents (16) | `AI-Dev-Team/repos/awesome-llm-apps` | Specialist Agents | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Standalone Python agent applications | None |
| **AGT-074** | Qwen Bridge | `qwen-antigravity/` | Model Router | **KEEP PROJECT-LOCAL** | N/A (Cataloged) | NONE | Standalone local FastAPI proxy | None |
| **AGT-075** | OmniRoute Gateway | `AI-Dev-Team/repos/omniroute` | Model Router | **KEEP INSIDE REPOSITORY** | N/A (Cataloged) | NONE | Cloned gateway engine | None |
| **AGT-076** | LinkedIn Reader | `LinkedIn-Audit/` | Project-Local Tool | **KEEP PROJECT-LOCAL** | N/A (Cataloged) | BLOCKED | Protected Workspace Invariant | None |
| **AGT-077** | Portfolio Testing Suite | `subhajitportfolio-2.0/` | Project-Local Suite | **KEEP PROJECT-LOCAL** | N/A (Cataloged) | BLOCKED | Protected Workspace Invariant | None |
| **SYM-01–20** | Broken Skill Symlinks (20) | `AI-Dev-Team/skills/` | Skills | **REPAIR SYMLINKS** | Relink to `data-agent-kit-plugin` | LOW | Fixes broken GCP/Storage links | Restores 100% skill health |
| **STR-01** | Stray Nested Folder | `Developer/Developer/` | Stray Empty Directory | **SAFE PRUNE** | Prune after backup | NONE | 0 files; unreferenced | Zero impact |

---

## 15. Risks & Rollback Strategy

1. **Zero Runtime Disruption**: Because native Antigravity agents (`~/.gemini/config/`) and framework agents (`AI-Dev-Team/repos/`) remain in their authoritative native locations, neither Antigravity nor the framework runtimes can suffer disruption.
2. **Backward-Compatible Symlinks**: Moving role markdown files into `AI-Dev-Team/roles/` is accompanied by symlinks in `AI-Dev-Team/agents/`, ensuring any script expecting the old path continues to function transparently.
3. **Symlink Restoration**: If repaired skill symlinks need to be reverted, a snapshot backup is recorded in `AI-Dev-Team/backups/`.
4. **Stray Directory Backup**: Before pruning `Developer/Developer/`, an archive of the empty directory structure will be preserved in `AI-Dev-Team/backups/`.

---

## 16. Final Recommendation

1. **Keep all Native & Framework Agents in place**: Catalog them centrally in `AI-Dev-Team/inventory/` and `Agent-Catalog.xlsx` rather than physically relocating them.
2. **Standardize Role Specs**: Move the 14 standardized markdown role specifications into `AI-Dev-Team/roles/` with symlinks in `AI-Dev-Team/agents/`.
3. **Repair the 20 Broken Symlinks**: Relink them to their verified locations in `data-agent-kit-plugin/skills/`.
4. **Clean up Stray Empty Folder**: Prune `Developer/Developer/` after saving a record to `backups/`.
5. **Install `openpyxl` & Generate Catalog**: Install `openpyxl` in `AI-Dev-Team/environments/mcp-env` and generate the 13-sheet `Agent-Catalog.xlsx` and `AGENT-INVENTORY.md`.

---
*Report generated and validated by Antigravity Global AI Infrastructure Dev Team.*
