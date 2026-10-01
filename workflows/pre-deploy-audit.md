# Workflow: Pre-Deploy Audit

Rigorous release-gate audit executed before staging or production deployment.

## Mandatory Release Gates
- `BLOCKED`: Any verified CRITICAL security finding, unmasked secret, or failing test.
- `READY_FOR_REVIEW`: Non-blocking HIGH or MEDIUM issues requiring human sign-off.
- `PASS`: All automated tests green, 0 blockers, all mandatory gates satisfied.
