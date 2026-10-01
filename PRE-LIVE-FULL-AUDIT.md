# PRE-LIVE-FULL-AUDIT: Architecture, Methodology & Provenance Guide

## 1. System Overview

**PRE-LIVE-FULL-AUDIT** is an enterprise-grade, multi-agent pre-release quality, security, and verification orchestrator integrated into the `AI-Dev-Team` ecosystem.

It provides automated, evidence-grounded evaluation of:
- Source codebases (JavaScript/TypeScript, Python, Java, Go, Rust)
- Web applications and APIs (REST, GraphQL, WebSockets)
- Dependencies and supply-chain health
- Application security and OWASP Top 10 vulnerabilities
- Hardcoded secrets and credential exposures
- Runtime performance, database access patterns, and query health
- Accessibility (WCAG 2.1 AA) and technical SEO
- Automated testing and CI/CD pipelines
- Release gating (`BLOCKED`, `READY_FOR_REVIEW`, `PASS`)

---

## 2. Integrated Provenance Registry

Components within `PRE-LIVE-FULL-AUDIT` are synthesized and adapted from five frontier repositories:

| Source | Upstream Repository / Gist | Commit / Tag | Original License | Adaptation & Role |
| :--- | :--- | :--- | :--- | :--- |
| **Source 1** | [claude-code-agents](https://github.com/undeadlist/claude-code-agents) | `13e3d51f` | MIT License | Specialized auditor agents, domain review workflows, and report structure. Adapted to native Antigravity architecture. |
| **Source 2** | [multi-agent-review-orchestrator](https://gist.github.com/8058aac0df0e48a3740776963fa87805) | `9c568f14` | MIT / Public Gist | Parallel reviewer lanes, exact `file:line` finding schema, honest severity classification, and evidence collection. |
| **Source 3** | [multi-model-code-review-agent](https://github.com/pelednoam/multi-model-code-review-agent) | `d41b7535` | MIT License | Deterministic preflight audit, multi-model ensemble review convergence loop, and test gates. |
| **Source 4** | [Claude-Code-Promts-Skills](https://github.com/Rtur2003/Claude-Code-Promts-Skills) | `ac0502e7` | MIT License | Deep security audit reconnaissance checklist (OWASP Top 10, secrets, injection, auth, headers) and deterministic scanning regexes. |
| **Source 5** | [ai-code-review-prompts](https://github.com/soul-sol/ai-code-review-prompts) | `ff21994c` | MIT License | Adversarial review lenses: hostile input tracing, injection boundaries, test sufficiency verification, and AI-generated code validation. |

---

## 3. Architecture & Execution Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PRE-LIVE-FULL-AUDIT PIPELINE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. TECH DISCOVERY: Auto-detects languages, frameworks, DBs, cloud, web UI  │
│ 2. REAL SCANNERS: Executes npm audit, secret regexes, OWASP checks, git     │
│ 3. MULTI-AGENT REVIEW: Dispatches parallel specialist audit lanes           │
│ 4. FINDING VERIFICATION: Checks physical filesystem to eliminate fakes      │
│ 5. CONSOLIDATION: Deduplicates findings, correlates root causes             │
│ 6. RELEASE GATE: Evaluates BLOCKED | READY_FOR_REVIEW | PASS                │
│ 7. 13-DELIVERABLE REPORTING: Generates reports and remediation work packages│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Specialist Audit Agents & Roles

1. `code-auditor`: Clean architecture, code quality, and technical debt.
2. `security-auditor`: OWASP Top 10, auth, authorization, headers, and crypto.
3. `bug-auditor`: Concurrency, logic defects, state leaks, and edge cases.
4. `infra-auditor`: Docker, Kubernetes, Terraform, and cloud configurations.
5. `perf-auditor`: Event loop blocking, bundle sizes, Core Web Vitals, and caching.
6. `db-auditor`: Indexes, N+1 queries, schema integrity, and ORM safety.
7. `dep-auditor`: Supply chain, package CVEs, and open source licensing.
8. `ui-auditor`: Frontend design, responsive viewports, and WCAG 2.1 AA a11y.
9. `api-tester`: REST/GraphQL contracts, boundary conditions, and rate limits.
10. `seo-auditor`: Meta tags, Open Graph, sitemaps, and search crawlability.
11. `adversarial-reviewer`: Hostile input tracing, boundary abuse, and AI validation.
12. `review-consolidator`: Cross-lane correlation, deduplication, and synthesis.
13. `release-gatekeeper`: Authoritative release gate evaluation and work package creation.

---

## 5. Finding Schema Contract (Phase 10)

Every finding conforms to a strict data structure:
```json
{
  "id": "SEC-SECRET-001",
  "category": "SECRETS",
  "severity": "CRITICAL",
  "confidence": 0.95,
  "title": "Hardcoded Credential in Source Code",
  "description": "Exposed credential detected.",
  "file": "server/config.js",
  "line": 42,
  "component": "auth",
  "failure_scenario": "Credentials committed to source control can be exploited.",
  "evidence": "Masked match: AKIA****************",
  "reproduction": "Inspect server/config.js at line 42.",
  "impact": "Account compromise or unauthorized API access.",
  "recommendation": "Migrate secret to environment variables or secret manager.",
  "source_agent": "security-auditor",
  "source_repository": "Claude-Code-Promts-Skills",
  "verified": true,
  "verification_method": "INDEPENDENT_EVIDENCE_CONFIRMED",
  "status": "VERIFIED"
}
```

---

## 6. Release Gate Evaluation (Phase 13)

- **`BLOCKED`:**
  - Any confirmed CRITICAL security vulnerability.
  - Any exposed production credential or private key.
  - Any failing test in the automated test suite.
  - Any build compilation or syntax failure.
- **`READY_FOR_REVIEW`:**
  - Zero blockers present.
  - One or more verified HIGH or MEDIUM risks require sign-off.
- **`PASS`:**
  - All mandatory gates satisfied.
  - Zero blockers, zero unresolved critical risks.

---

## 7. Deliverables & Outputs (Phase 14)

All audits default to **READ-ONLY** mode, producing 13 comprehensive artifacts:
1. `AUDIT_REPORT.md`: Consolidated master report.
2. `SECURITY_REPORT.md`: Deep security and vulnerability audit.
3. `QA_REPORT.md`: Test automation and quality assurance findings.
4. `CODE_REVIEW_REPORT.md`: Multi-agent code review analysis.
5. `PERFORMANCE_REPORT.md`: Performance and database query audit.
6. `DEPENDENCY_REPORT.md`: Supply chain, package CVEs, and licensing.
7. `BROWSER_REPORT.md`: Browser automation, navigation, and console errors.
8. `ACCESSIBILITY_REPORT.md`: WCAG 2.1 Level AA accessibility evaluation.
9. `API_REPORT.md`: API boundary contracts and endpoints.
10. `INFRASTRUCTURE_REPORT.md`: Container, Kubernetes, and IaC health.
11. `FINDINGS.json`: Machine-readable array of all findings.
12. `RELEASE_GATE.json`: Automated gate decision and criteria evaluation.
13. `REMEDIATION_PLAN.md`: Prioritized work packages (`WP-01`, `WP-02`) for remediation.

---

## 8. CLI Usage Examples

```bash
# Run full pre-live audit in read-only mode against a target project
python scripts/pre_live_full_audit.py /path/to/project --mode full

# Run quick pre-commit audit
python scripts/pre_live_full_audit.py /path/to/project --mode quick

# Output reports to a custom directory
python scripts/pre_live_full_audit.py /path/to/project --output-dir /tmp/audit-output
```
