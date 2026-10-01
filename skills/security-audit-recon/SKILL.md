---
name: security-audit-recon
description: Deterministic security reconnaissance, OWASP Top 10 analysis, secret detection, and vulnerability scanning.
---

# Security Audit Reconnaissance Skill

## Reconnaissance Checklist
1. **Dependency CVEs:** Run `npm audit`, `pip-audit`, or equivalent native package audit.
2. **Exposed Credentials:** Scan source tree for unmasked API keys, tokens, and private key blocks.
3. **Injection Vectors:**
   - Raw SQL concatenation (`SELECT ... + req.body`)
   - Arbitrary code execution (`eval()`, `exec()`)
   - Command injection (`child_process.exec` with string interpolation)
   - Unsanitized HTML rendering (`dangerouslySetInnerHTML`)
4. **Security Headers:** Verify CSP, HSTS, X-Content-Type-Options on web application routes.
