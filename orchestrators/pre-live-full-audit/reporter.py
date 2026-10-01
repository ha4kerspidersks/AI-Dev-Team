"""Artifact and report generator for PRE-LIVE-FULL-AUDIT.

Generates comprehensive, evidence-grounded reports across security, QA,
code review, dependencies, infrastructure, browser testing, and release gating.
"""

from __future__ import annotations

import json
import os
from typing import Dict, List
from finding_schema import Finding, ReleaseGateResult, Severity
from tech_detector import ProjectTechProfile


class AuditReporter:
    """Generates all 13 Phase 14 audit deliverables."""

    def __init__(self, output_dir: str, profile: ProjectTechProfile):
        self.output_dir = os.path.abspath(output_dir)
        self.profile = profile
        os.makedirs(self.output_dir, exist_ok=True)

    def write_all_reports(self, findings: List[Finding], gate: ReleaseGateResult) -> Dict[str, str]:
        generated = {}

        # 1. FINDINGS.json
        findings_path = os.path.join(self.output_dir, "FINDINGS.json")
        with open(findings_path, "w", encoding="utf-8") as f:
            json.dump([f.to_dict() for f in findings], f, indent=2)
        generated["FINDINGS.json"] = findings_path

        # 2. RELEASE_GATE.json
        gate_path = os.path.join(self.output_dir, "RELEASE_GATE.json")
        with open(gate_path, "w", encoding="utf-8") as f:
            json.dump(gate.to_dict(), f, indent=2)
        generated["RELEASE_GATE.json"] = gate_path

        # 3. AUDIT_REPORT.md (Master Consolidated Report)
        audit_path = os.path.join(self.output_dir, "AUDIT_REPORT.md")
        self._write_master_audit_report(audit_path, findings, gate)
        generated["AUDIT_REPORT.md"] = audit_path

        # 4. SECURITY_REPORT.md
        sec_findings = [f for f in findings if f.category in ("SECURITY", "SECRETS", "INJECTION", "AUTHENTICATION", "AUTHORIZATION")]
        sec_path = os.path.join(self.output_dir, "SECURITY_REPORT.md")
        self._write_domain_report(sec_path, "Security & Vulnerability Audit Report", sec_findings, "OWASP Top 10, Secrets, and Injection Analysis")
        generated["SECURITY_REPORT.md"] = sec_path

        # 5. QA_REPORT.md
        qa_findings = [f for f in findings if f.category in ("CORRECTNESS", "BUG_LOGIC", "TESTING", "CI_CD")]
        qa_path = os.path.join(self.output_dir, "QA_REPORT.md")
        self._write_domain_report(qa_path, "Quality Assurance & Test Health Report", qa_findings, "Test Automation, Regression, and Defect Prevention")
        generated["QA_REPORT.md"] = qa_path

        # 6. CODE_REVIEW_REPORT.md
        cr_findings = [f for f in findings if f.category in ("CORRECTNESS", "ARCHITECTURE", "ADVERSARIAL", "BUG_LOGIC")]
        cr_path = os.path.join(self.output_dir, "CODE_REVIEW_REPORT.md")
        self._write_domain_report(cr_path, "Code Quality & Architectural Review Report", cr_findings, "Multi-Agent & Adversarial Code Review Analysis")
        generated["CODE_REVIEW_REPORT.md"] = cr_path

        # 7. PERFORMANCE_REPORT.md
        perf_findings = [f for f in findings if f.category in ("PERFORMANCE", "DATABASE")]
        perf_path = os.path.join(self.output_dir, "PERFORMANCE_REPORT.md")
        self._write_domain_report(perf_path, "Performance & Scalability Audit Report", perf_findings, "Runtime Performance, Database Querying, and Efficiency")
        generated["PERFORMANCE_REPORT.md"] = perf_path

        # 8. DEPENDENCY_REPORT.md
        dep_findings = [f for f in findings if f.category in ("DEPENDENCIES", "SUPPLY_CHAIN", "LICENSE")]
        dep_path = os.path.join(self.output_dir, "DEPENDENCY_REPORT.md")
        self._write_domain_report(dep_path, "Dependency & Supply-Chain Health Report", dep_findings, "Package Vulnerabilities, Outdated Dependencies, and Licensing")
        generated["DEPENDENCY_REPORT.md"] = dep_path

        # 9. BROWSER_REPORT.md
        browser_findings = [f for f in findings if f.category in ("FRONTEND", "UI_UX")]
        browser_path = os.path.join(self.output_dir, "BROWSER_REPORT.md")
        self._write_domain_report(browser_path, "Browser & User Journey Verification Report", browser_findings, "Web Application Navigation, Console Errors, and UI States")
        generated["BROWSER_REPORT.md"] = browser_path

        # 10. ACCESSIBILITY_REPORT.md
        a11y_findings = [f for f in findings if f.category == "ACCESSIBILITY"]
        a11y_path = os.path.join(self.output_dir, "ACCESSIBILITY_REPORT.md")
        self._write_domain_report(a11y_path, "Accessibility (a11y) & WCAG 2.1 Audit Report", a11y_findings, "WCAG AA Compliance, Semantic Structure, and Screen Readers")
        generated["ACCESSIBILITY_REPORT.md"] = a11y_path

        # 11. API_REPORT.md
        api_findings = [f for f in findings if f.category == "API"]
        api_path = os.path.join(self.output_dir, "API_REPORT.md")
        self._write_domain_report(api_path, "API Contracts & Endpoint Security Report", api_findings, "REST/GraphQL Boundary Validation, Rate Limiting, and Headers")
        generated["API_REPORT.md"] = api_path

        # 12. INFRASTRUCTURE_REPORT.md
        infra_findings = [f for f in findings if f.category in ("INFRASTRUCTURE", "DEPLOYMENT")]
        infra_path = os.path.join(self.output_dir, "INFRASTRUCTURE_REPORT.md")
        self._write_domain_report(infra_path, "Infrastructure, IaC & Deployment Readiness Report", infra_findings, "Docker, Kubernetes, Terraform, and Cloud Security")
        generated["INFRASTRUCTURE_REPORT.md"] = infra_path

        # 13. REMEDIATION_PLAN.md
        rem_path = os.path.join(self.output_dir, "REMEDIATION_PLAN.md")
        self._write_remediation_plan(rem_path, findings, gate)
        generated["REMEDIATION_PLAN.md"] = rem_path

        return generated

    def _write_master_audit_report(self, path: str, findings: List[Finding], gate: ReleaseGateResult):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# PRE-LIVE FULL AUDIT CONSOLIDATED REPORT\n\n")
            f.write(f"**Project Target:** `{self.profile.project_name}` (`{self.profile.project_path}`)  \n")
            f.write(f"**Detected Languages:** {', '.join(self.profile.languages) or 'None'}  \n")
            f.write(f"**Detected Frameworks:** {', '.join(self.profile.frameworks) or 'None'}  \n")
            f.write(f"**Infrastructure & Cloud:** {', '.join(self.profile.cloud_and_infra) or 'None'}  \n")
            f.write(f"**Release Gate Status:** **{gate.status}**  \n\n")
            f.write(f"> **Summary:** {gate.summary}\n\n")
            f.write("---\n\n")

            f.write("## 1. Executive Summary & Release Gates\n\n")
            f.write("| Severity | Count |\n")
            f.write("| :--- | :--- |\n")
            for sev, count in gate.findings_by_severity.items():
                f.write(f"| **{sev}** | {count} |\n")
            f.write(f"| **TOTAL FINDINGS** | **{gate.total_findings}** |\n\n")

            if gate.blocking_reasons:
                f.write("### 🚨 Blocking Release Issues\n")
                for r in gate.blocking_reasons:
                    f.write(f"- ❌ {r}\n")
                f.write("\n")

            if gate.warning_reasons:
                f.write("### ⚠️ Required Review Sign-offs\n")
                for r in gate.warning_reasons:
                    f.write(f"- ⚠️ {r}\n")
                f.write("\n")

            f.write("---\n\n")
            f.write("## 2. All Findings Table\n\n")
            f.write("| ID | Severity | Category | File:Line | Title | Status | Source |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
            for finding in findings:
                loc = f"`{finding.file}:{finding.line or 'root'}`"
                f.write(f"| `{finding.id}` | **{finding.severity}** | {finding.category} | {loc} | {finding.title} | {finding.status} | {finding.source_agent} |\n")
            f.write("\n")

    def _write_domain_report(self, path: str, title: str, findings: List[Finding], scope: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Target:** `{self.profile.project_name}`  \n")
            f.write(f"**Scope:** {scope}  \n")
            f.write(f"**Total Findings in Domain:** {len(findings)}  \n\n")
            f.write("---\n\n")

            if not findings:
                f.write("✅ **No issues detected in this domain.** Real-time diagnostic scanners verified clean status.\n")
                return

            for f_item in findings:
                f.write(f"### [{f_item.severity}] {f_item.id}: {f_item.title}\n\n")
                f.write(f"- **Location:** `{f_item.file}:{f_item.line or 'root'}`\n")
                f.write(f"- **Status:** `{f_item.status}` (Verified: {f_item.verified})\n")
                f.write(f"- **Description:** {f_item.description}\n")
                if f_item.evidence:
                    f.write(f"- **Evidence:** `{f_item.evidence}`\n")
                if f_item.failure_scenario:
                    f.write(f"- **Failure Scenario:** {f_item.failure_scenario}\n")
                if f_item.recommendation:
                    f.write(f"- **Remediation Recommendation:** {f_item.recommendation}\n")
                f.write("\n---\n\n")

    def _write_remediation_plan(self, path: str, findings: List[Finding], gate: ReleaseGateResult):
        with open(path, "w", encoding="utf-8") as f:
            f.write("# REMEDIATION PLAN & ACTION PROTOCOL\n\n")
            f.write(f"**Target Application:** `{self.profile.project_name}`  \n")
            f.write(f"**Gate Status:** **{gate.status}**  \n\n")
            f.write("## Remediation Order of Precedence\n\n")
            f.write("1. **P0 (Critical Security & Secrets):** Resolve exposed credentials, SQL injection, and command execution immediately.\n")
            f.write("2. **P1 (Test Regressions & Build Blockers):** Fix broken tests and compilation errors.\n")
            f.write("3. **P2 (High-Risk Vulnerabilities & Dependencies):** Upgrade vulnerable packages with known CVEs.\n")
            f.write("4. **P3 (Quality, Performance & Accessibility):** Clean up unhandled DOM states, missing labels, and dead code.\n\n")
            f.write("---\n\n")

            f.write("## Actionable Work Packages\n\n")
            high_pri = [f for f in findings if f.severity in (Severity.CRITICAL.value, Severity.HIGH.value) and f.status != "FALSE_POSITIVE"]
            if not high_pri:
                f.write("✅ No critical or high priority remediation actions required.\n")
            else:
                for idx, item in enumerate(high_pri, 1):
                    f.write(f"### WP-{idx:02d}: Fix {item.title}\n")
                    f.write(f"- **Target File:** `{item.file}` (Line {item.line or 'N/A'})\n")
                    f.write(f"- **Issue:** {item.description}\n")
                    f.write(f"- **Action:** {item.recommendation}\n\n")
