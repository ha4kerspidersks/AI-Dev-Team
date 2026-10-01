# Architectural Decision Records (ADRs): AI-Dev-Team

## Documentation and ADRs
- **DATE**: 2025-01-15
- **STATUS**: Accepted | Superseded by ADR-XXX | Deprecated
- **DECISION / RATIONALE**: Use PostgreSQL with Prisma ORM....
- **CONTEXT**: We need a primary database for the task management application. Key requirements:
- Relational data model (users, tasks, teams with relationships)
- ACID transactions for task state changes
- Support for full-text search on task content
- Managed hosting available (for small team, limited ops capaci...
- **IMPACT**: - Prisma provides type-safe database access and migration management
- We can use PostgreSQL's full-text search instead of adding Elasticsearch
- Team needs PostgreSQL knowledge (standard skill, low risk)
- Hosting on managed service (Supabase, Neon, or RDS)
```...
- **SOURCE**: [`skills/addyosmani/skills/documentation-and-adrs/SKILL.md`](file:///Users/subhajkar/Developer/AI-Dev-Team/skills/addyosmani/skills/documentation-and-adrs/SKILL.md)

## ADR Format
- **DATE**: 2026-09-17
- **STATUS**: Accepted
- **DECISION / RATIONALE**: Documented in ADR source
- **CONTEXT**: Documented in ADR source
- **IMPACT**: Architectural alignment & stability
- **SOURCE**: [`skills/mattpocock/engineering/domain-modeling/ADR-FORMAT.md`](file:///Users/subhajkar/Developer/AI-Dev-Team/skills/mattpocock/engineering/domain-modeling/ADR-FORMAT.md)

