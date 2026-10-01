"""Finding consolidation and release gate engine for PRE-LIVE-FULL-AUDIT.

Consolidates multi-agent findings, removes duplicates, correlates root causes,
and evaluates strict release gating rules.
"""

from __future__ import annotations

import datetime
from typing import Dict, List, Tuple
from finding_schema import Finding, ReleaseGateResult, Severity, Status


class FindingConsolidator:
    """Merges duplicate findings, preserves evidence, and assesses release gates."""

    def __init__(self, project_path: str):
        self.project_path = project_path

    def consolidate(self, findings: List[Finding]) -> List[Finding]:
        """Deduplicate findings based on file, line, and category."""
        dedup_map: Dict[Tuple[str, int, str], Finding] = {}
        unique_findings: List[Finding] = []

        for f in findings:
            line_key = f.line if f.line is not None else 0
            key = (f.file.lower(), line_key, f.category.upper())

            if key in dedup_map:
                existing = dedup_map[key]
                # Merge sources and notes
                if f.source_agent not in existing.source_agent:
                    existing.source_agent += f", {f.source_agent}"
                # Keep highest severity
                sev_order = {Severity.CRITICAL.value: 4, Severity.HIGH.value: 3, Severity.MEDIUM.value: 2, Severity.LOW.value: 1, Severity.INFO.value: 0}
                if sev_order.get(f.severity, 0) > sev_order.get(existing.severity, 0):
                    existing.severity = f.severity
                    existing.title = f.title
                    existing.description = f.description
                # Merge evidence
                if f.evidence and f.evidence not in existing.evidence:
                    existing.evidence += f" | {f.evidence}"
            else:
                dedup_map[key] = f
                unique_findings.append(f)

        # Sort findings by severity (CRITICAL down to INFO) then file/line
        sev_rank = {Severity.CRITICAL.value: 0, Severity.HIGH.value: 1, Severity.MEDIUM.value: 2, Severity.LOW.value: 3, Severity.INFO.value: 4}
        unique_findings.sort(key=lambda x: (sev_rank.get(x.severity, 5), x.file, x.line or 0))

        return unique_findings

    def evaluate_release_gate(self, findings: List[Finding], test_failures: int = 0, build_failures: int = 0) -> ReleaseGateResult:
        """Evaluate strict release gating rules according to Phase 13."""
        blocking_reasons: List[str] = []
        warning_reasons: List[str] = []

        severity_counts = {
            Severity.CRITICAL.value: 0,
            Severity.HIGH.value: 0,
            Severity.MEDIUM.value: 0,
            Severity.LOW.value: 0,
            Severity.INFO.value: 0
        }

        for f in findings:
            if f.status in (Status.FALSE_POSITIVE.value, Status.FIXED.value):
                continue
            severity_counts[f.severity] = severity_counts.get(f.severity, 0) + 1

            if f.severity == Severity.CRITICAL.value:
                blocking_reasons.append(f"CRITICAL Finding: {f.title} ({f.file}:{f.line or 'root'})")
            elif f.severity == Severity.HIGH.value and f.verified:
                warning_reasons.append(f"Verified HIGH Risk: {f.title} ({f.file}:{f.line or 'root'})")
            elif f.severity == Severity.MEDIUM.value:
                warning_reasons.append(f"MEDIUM Finding: {f.title} ({f.file}:{f.line or 'root'})")

        if test_failures > 0:
            blocking_reasons.append(f"Automated test suite has {test_failures} failing test(s).")
        if build_failures > 0:
            blocking_reasons.append(f"Build compilation/lint verification failed with {build_failures} error(s).")

        # Determine Gate Status
        mandatory_gates = {
            "no_critical_security_vulnerabilities": severity_counts[Severity.CRITICAL.value] == 0,
            "no_exposed_credentials_or_secrets": not any(f.category == "SECRETS" and f.severity in (Severity.CRITICAL.value, Severity.HIGH.value) and f.verified for f in findings),
            "no_failing_automated_tests": test_failures == 0,
            "no_build_compilation_errors": build_failures == 0
        }

        if blocking_reasons or not all(mandatory_gates.values()):
            gate_status = "BLOCKED"
            summary = f"RELEASE BLOCKED: {len(blocking_reasons)} critical blocker(s) detected. Remediation mandatory before deployment."
        elif warning_reasons:
            gate_status = "READY_FOR_REVIEW"
            summary = f"READY FOR REVIEW: 0 blockers, but {len(warning_reasons)} medium/high items require reviewer sign-off."
        else:
            gate_status = "PASS"
            summary = "RELEASE GATE PASSED: All mandatory security, test, and quality gates satisfied."

        return ReleaseGateResult(
            status=gate_status,
            summary=summary,
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            project_path=self.project_path,
            blocking_reasons=blocking_reasons,
            warning_reasons=warning_reasons[:20],
            total_findings=len(findings),
            findings_by_severity=severity_counts,
            mandatory_gates_evaluated=mandatory_gates
        )
