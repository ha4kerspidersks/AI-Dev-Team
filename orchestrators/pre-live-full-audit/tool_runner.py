"""Deterministic tool runners and security scanners for PRE-LIVE-FULL-AUDIT.

Executes real scanners, linters, tests, and security patterns against
the target codebase without hallucinating findings.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from typing import Any, Dict, List, Optional
from finding_schema import Finding, Severity, Status, Category
from tech_detector import ProjectTechProfile


class ToolRunner:
    """Coordinates deterministic scanners and tools."""

    def __init__(self, profile: ProjectTechProfile):
        self.profile = profile
        self.project_path = profile.project_path

    def run_all_scans(self) -> List[Finding]:
        findings: List[Finding] = []
        findings.extend(self.scan_git_state())
        findings.extend(self.scan_secrets())
        findings.extend(self.scan_code_vulnerabilities())
        findings.extend(self.scan_dependencies())
        return findings

    def scan_git_state(self) -> List[Finding]:
        """Check for uncommitted files, detached head, or broken git state."""
        findings = []
        if not self.profile.has_git:
            return findings

        res = subprocess.run(
            ["git", "-C", self.project_path, "status", "--porcelain"],
            capture_output=True, text=True
        )
        if res.returncode == 0:
            lines = res.stdout.strip().splitlines()
            if len(lines) > 50:
                findings.append(Finding(
                    id="GIT-001",
                    category=Category.CI_CD.value,
                    severity=Severity.LOW.value,
                    confidence=1.0,
                    title="Large Uncommitted Working Tree",
                    description=f"Working tree has {len(lines)} uncommitted changes.",
                    file="git",
                    evidence=f"{len(lines)} dirty files",
                    recommendation="Review and commit or stash changes before final pre-live release.",
                    source_agent="git-auditor",
                    source_repository="AI-Dev-Team",
                    verified=True,
                    status=Status.VERIFIED.value
                ))
        return findings

    def scan_secrets(self) -> List[Finding]:
        """Scan code for exposed API keys, private keys, and passwords."""
        findings = []
        secret_patterns = [
            ("AWS Access Key ID", r"AKIA[0-9A-Z]{16}", Severity.CRITICAL, "Exposed AWS Access Key ID"),
            ("Private Key Block", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", Severity.CRITICAL, "Hardcoded Private Key"),
            ("GitHub Personal Access Token", r"gh[pous]_[0-9a-zA-Z]{36}", Severity.CRITICAL, "Exposed GitHub Token"),
            ("Hardcoded Password/Secret", r"(?:password|secret_key|api_key|auth_token)\s*=\s*['\"][a-zA-Z0-9_\-\.]{12,}['\"]", Severity.HIGH, "Hardcoded Credential in Source Code")
        ]

        # Ignore patterns
        ignored_dirs = {".git", "node_modules", "venv", ".venv", "backups", "dist", "build", ".next", "coverage"}
        allowed_exts = {".js", ".jsx", ".ts", ".tsx", ".py", ".go", ".java", ".json", ".yaml", ".yml", ".env.example", ".sh"}

        finding_idx = 1
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in ignored_dirs and not d.startswith(".")]
            for f in files:
                ext = os.path.splitext(f)[1]
                if ext not in allowed_exts and f != ".env.example":
                    continue
                file_path = os.path.join(root, f)
                rel_path = os.path.relpath(file_path, self.project_path)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
                        for line_no, line in enumerate(fp, 1):
                            # Skip comments or masked lines
                            if "xxxx" in line.lower() or "example" in line.lower() or "dummy" in line.lower():
                                continue
                            for name, pat, sev, desc in secret_patterns:
                                m = re.search(pat, line, re.IGNORECASE)
                                if m:
                                    # Mask matched secret
                                    matched_val = m.group(0)
                                    masked = matched_val[:4] + "*" * (len(matched_val) - 8) + matched_val[-4:] if len(matched_val) > 8 else "***"
                                    findings.append(Finding(
                                        id=f"SEC-SECRET-{finding_idx:03d}",
                                        category=Category.SECRETS.value,
                                        severity=sev.value,
                                        confidence=0.95,
                                        title=f"Potential {name} Exposed",
                                        description=f"{desc} detected at {rel_path}:{line_no}.",
                                        file=rel_path,
                                        line=line_no,
                                        evidence=f"Masked match: {masked}",
                                        failure_scenario="Credentials committed to source control can be leaked or exploited by unauthorized actors.",
                                        recommendation="Move secrets to environment variables or secret manager (e.g. Secret Manager, Vault, .env).",
                                        source_agent="security-auditor",
                                        source_repository="AI-Dev-Team",
                                        verified=True,
                                        status=Status.VERIFIED.value
                                    ))
                                    finding_idx += 1
                                    if len(findings) > 50:
                                        return findings
                except Exception:
                    pass

        return findings

    def scan_code_vulnerabilities(self) -> List[Finding]:
        """Scan code for OWASP Top 10 vulnerabilities (eval, command injection, XSS)."""
        findings = []
        ignored_dirs = {".git", "node_modules", "venv", ".venv", "backups", "dist", "build", "tests", "__tests__"}
        vuln_patterns = [
            ("Code Execution (eval/exec)", r"\b(?:eval|exec)\s*\(", Category.INJECTION, Severity.HIGH, "Use of eval() or exec() poses severe arbitrary code execution risks."),
            ("Dangerous DOM InnerHTML", r"dangerouslySetInnerHTML\s*=", Category.FRONTEND, Severity.MEDIUM, "Direct HTML injection without sanitization can lead to Cross-Site Scripting (XSS)."),
            ("Unsafe Child Process Exec", r"\bchild_process\.exec\s*\(\s*['\"`][^'\"]*\$\{", Category.INJECTION, Severity.HIGH, "Interpolating dynamic variables into child_process.exec may allow command injection."),
            ("Raw SQL Concatenation", r"(?:SELECT|INSERT|UPDATE|DELETE).*\+.*(?:req\.|params\.|body\.)", Category.DATABASE, Severity.HIGH, "Raw SQL query string concatenation with request parameters risks SQL injection.")
        ]

        finding_idx = 1
        for root, dirs, files in os.walk(self.project_path):
            dirs[:] = [d for d in dirs if d not in ignored_dirs and not d.startswith(".")]
            for f in files:
                ext = os.path.splitext(f)[1]
                if ext not in {".js", ".jsx", ".ts", ".tsx", ".py", ".go", ".java"}:
                    continue
                file_path = os.path.join(root, f)
                rel_path = os.path.relpath(file_path, self.project_path)

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
                        for line_no, line in enumerate(fp, 1):
                            line_stripped = line.strip()
                            if line_stripped.startswith("//") or line_stripped.startswith("#") or line_stripped.startswith("/*"):
                                continue
                            for name, pat, cat, sev, desc in vuln_patterns:
                                if re.search(pat, line):
                                    findings.append(Finding(
                                        id=f"VULN-{finding_idx:03d}",
                                        category=cat.value,
                                        severity=sev.value,
                                        confidence=0.85,
                                        title=name,
                                        description=f"{desc} Found at {rel_path}:{line_no}.",
                                        file=rel_path,
                                        line=line_no,
                                        evidence=line_stripped[:120],
                                        failure_scenario="Exploitable by untrusted input crossing application boundaries.",
                                        recommendation="Use parameterized interfaces, contextual escaping, or safe parsing libraries.",
                                        source_agent="bug-auditor",
                                        source_repository="AI-Dev-Team",
                                        verified=True,
                                        status=Status.VERIFIED.value
                                    ))
                                    finding_idx += 1
                                    if len(findings) > 50:
                                        return findings
                except Exception:
                    pass

        return findings

    def scan_dependencies(self) -> List[Finding]:
        """Run npm audit if package.json is present and npm is available."""
        findings = []
        if "npm" in self.profile.package_managers or "package.json" in self.profile.detected_files:
            try:
                res = subprocess.run(
                    ["npm", "audit", "--json"],
                    cwd=self.project_path,
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                if res.stdout:
                    data = json.loads(res.stdout)
                    vulns = data.get("vulnerabilities", {})
                    finding_idx = 1
                    for pkg_name, details in vulns.items():
                        sev_str = details.get("severity", "moderate").upper()
                        sev = Severity.CRITICAL if sev_str == "CRITICAL" else (
                            Severity.HIGH if sev_str == "HIGH" else (
                                Severity.MEDIUM if sev_str in ("MODERATE", "MEDIUM") else Severity.LOW
                            )
                        )
                        via_list = details.get("via", [])
                        via_title = via_list[0].get("title", "Known vulnerability") if via_list and isinstance(via_list[0], dict) else "Known CVE"
                        findings.append(Finding(
                            id=f"DEP-NPM-{finding_idx:03d}",
                            category=Category.DEPENDENCIES.value,
                            severity=sev.value,
                            confidence=1.0,
                            title=f"Vulnerable Package: {pkg_name} ({sev_str})",
                            description=f"{pkg_name}: {via_title}.",
                            file="package.json",
                            evidence=f"Affected range: {details.get('range', 'N/A')}",
                            recommendation=f"Update {pkg_name} to a secure patched version.",
                            source_agent="dep-auditor",
                            source_repository="AI-Dev-Team",
                            verified=True,
                            status=Status.VERIFIED.value
                        ))
                        finding_idx += 1
                        if len(findings) > 25:
                            break
            except Exception:
                pass

        return findings
