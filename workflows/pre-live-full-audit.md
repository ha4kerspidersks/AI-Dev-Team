# Workflow: PRE-LIVE-FULL-AUDIT

Master pre-release quality, security, and release gating workflow for AI-Dev-Team.

## Objective
Execute a comprehensive, evidence-grounded audit across codebase, dependencies, security, performance, accessibility, SEO, and release readiness before any production deployment.

## Execution Sequence
```
               ┌────────────────────────────────────────────────────────┐
               │              PHASE 1: TECH STACK DISCOVERY             │
               │  Detect languages, frameworks, DBs, cloud, containers   │
               └──────────────────────────┬─────────────────────────────┘
                                          │
               ┌──────────────────────────▼─────────────────────────────┐
               │           PHASE 2: REAL SCANNERS & TOOLING             │
               │  npm/pip audit, regex secrets, OWASP injection, git     │
               └──────────────────────────┬─────────────────────────────┘
                                          │
               ┌──────────────────────────▼─────────────────────────────┐
               │       PHASE 3: MULTI-AGENT SPECIALIST REVIEW LANES     │
               │  Security, Quality, Architecture, Web, Adversarial     │
               └──────────────────────────┬─────────────────────────────┘
                                          │
               ┌──────────────────────────▼─────────────────────────────┐
               │        PHASE 4: MANDATORY FINDING VERIFICATION         │
               │  Validate file existence, line bounds, reject fakes    │
               └──────────────────────────┬─────────────────────────────┘
                                          │
               ┌──────────────────────────▼─────────────────────────────┐
               │         PHASE 5: CONSOLIDATION & DEDUPLICATION         │
               │  Merge overlapping reports, correlate root causes      │
               └──────────────────────────┬─────────────────────────────┘
                                          │
               ┌──────────────────────────▼─────────────────────────────┐
               │             PHASE 6: STRICT RELEASE GATE               │
               │  BLOCKED | READY_FOR_REVIEW | PASS                     │
               └──────────────────────────┬─────────────────────────────┘
                                          │
               ┌──────────────────────────▼─────────────────────────────┐
               │          PHASE 7: 13-DELIVERABLE REPORTING             │
               │  AUDIT_REPORT, SECURITY, QA, FINDINGS.json, etc.       │
               └────────────────────────────────────────────────────────┘
```

## CLI Invocation
```bash
python scripts/pre_live_full_audit.py /path/to/project --mode full
```
