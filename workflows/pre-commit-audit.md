# Workflow: Pre-Commit Audit

Fast, lightweight staged-diff audit executed prior to git commit.

## Execution
```bash
python scripts/pre_live_full_audit.py . --mode quick
```

## Gate Criteria
1. No uncommitted private keys or credentials.
2. No syntax or compilation errors.
3. No newly introduced high/critical injection patterns.
