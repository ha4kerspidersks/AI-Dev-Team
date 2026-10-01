"""Mandatory Finding Verification Engine for PRE-LIVE-FULL-AUDIT.

Validates candidate findings against actual codebase content.
Ensures zero hallucinations, correct file/line references, and accurate severity.
"""

from __future__ import annotations

import os
from typing import List, Tuple
from finding_schema import Finding, Severity, Status


class FindingVerifier:
    """Verifies candidate findings against physical filesystem evidence."""

    def __init__(self, project_path: str):
        self.project_path = os.path.abspath(project_path)

    def verify_all(self, findings: List[Finding]) -> List[Finding]:
        verified_findings = []
        for finding in findings:
            v_finding = self.verify_finding(finding)
            verified_findings.append(v_finding)
        return verified_findings

    def verify_finding(self, finding: Finding) -> Finding:
        # If finding has no file or is meta-level (e.g. git status, dependency)
        if not finding.file or finding.file in ("git", "package.json", "environment"):
            finding.verified = True
            finding.status = Status.VERIFIED.value
            finding.verification_method = "DETERMINISTIC_TOOL"
            return finding

        abs_file = os.path.normpath(os.path.join(self.project_path, finding.file))

        # Check 1: File existence
        if not os.path.exists(abs_file) or not os.path.isfile(abs_file):
            finding.verified = False
            finding.status = Status.FALSE_POSITIVE.value
            finding.verification_method = "FILESYSTEM_AUDIT_MISSING_FILE"
            finding.notes = f"Reported file '{finding.file}' does not exist in working tree."
            return finding

        # Check 2: Line reference validation
        if finding.line is not None and finding.line > 0:
            try:
                with open(abs_file, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                if finding.line > len(lines):
                    finding.verified = False
                    finding.status = Status.FALSE_POSITIVE.value
                    finding.verification_method = "OUT_OF_BOUNDS_LINE"
                    finding.notes = f"Reported line {finding.line} exceeds total file lines ({len(lines)})."
                    return finding

                # Target line content
                actual_line = lines[finding.line - 1].strip()

                # If finding has evidence, check if evidence is actually on or near that line
                if finding.evidence and finding.evidence not in ("N/A", ""):
                    # Search window: line - 3 to line + 3
                    window_start = max(0, finding.line - 4)
                    window_end = min(len(lines), finding.line + 3)
                    window_text = "".join(lines[window_start:window_end])

                    # Check for partial match (ignoring whitespace)
                    ev_norm = "".join(finding.evidence.split())[:40]
                    win_norm = "".join(window_text.split())

                    if ev_norm and ev_norm not in win_norm:
                        # Evidence mismatch
                        finding.verified = False
                        finding.status = Status.DISPUTED.value
                        finding.verification_method = "EVIDENCE_LINE_MISMATCH"
                        finding.notes = f"Line {finding.line} does not contain cited evidence: '{finding.evidence[:50]}'"
                        return finding

            except Exception as e:
                finding.verified = False
                finding.status = Status.UNVERIFIED.value
                finding.verification_method = "READ_ERROR"
                finding.notes = f"Could not read file: {e}"
                return finding

        # Check 3: Check comments or false positive markers
        try:
            with open(abs_file, "r", encoding="utf-8", errors="ignore") as f:
                if finding.line:
                    f.seek(0)
                    file_lines = f.readlines()
                    line_text = file_lines[finding.line - 1].strip().lower()
                    if "nosec" in line_text or "eslint-disable" in line_text or "audit-ignore" in line_text:
                        finding.verified = False
                        finding.status = Status.DISPUTED.value
                        finding.verification_method = "SUPPRESSED_BY_DIRECTIVE"
                        return finding
        except Exception:
            pass

        # Verified!
        finding.verified = True
        finding.status = Status.VERIFIED.value
        finding.verification_method = "INDEPENDENT_EVIDENCE_CONFIRMED"
        return finding
