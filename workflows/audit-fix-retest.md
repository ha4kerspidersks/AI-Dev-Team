# Workflow: Audit-Fix-Retest Convergence Loop

Iterative remediation cycle:
`AUDIT → PROPOSE FIX → RUN TESTS → RE-AUDIT → GATE EVALUATION`

## Remediation Protocol
1. Assign exclusive file ownership to prevent concurrent collision.
2. Generate clean minimal diff.
3. Run target regression test suite.
4. Rerun verification audit to confirm elimination of defect without regression.
