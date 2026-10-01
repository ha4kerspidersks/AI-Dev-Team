"""Finding schema and data structures for PRE-LIVE-FULL-AUDIT.

Defines standardized finding contracts complying with Phase 10:
- ID, CATEGORY, SEVERITY, CONFIDENCE, TITLE, DESCRIPTION, FILE, LINE,
  COMPONENT, FAILURE_SCENARIO, EVIDENCE, REPRODUCTION, IMPACT,
  RECOMMENDATION, SOURCE_AGENT, SOURCE_REPOSITORY, VERIFIED,
  VERIFICATION_METHOD, STATUS.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"


class Status(str, Enum):
    OPEN = "OPEN"
    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"
    DISPUTED = "DISPUTED"
    FALSE_POSITIVE = "FALSE_POSITIVE"
    FIXED = "FIXED"
    REGRESSION = "REGRESSION"


class Category(str, Enum):
    SECURITY = "SECURITY"
    AUTHENTICATION = "AUTHENTICATION"
    AUTHORIZATION = "AUTHORIZATION"
    SECRETS = "SECRETS"
    INJECTION = "INJECTION"
    DEPENDENCIES = "DEPENDENCIES"
    SUPPLY_CHAIN = "SUPPLY_CHAIN"
    CORRECTNESS = "CORRECTNESS"
    BUG_LOGIC = "BUG_LOGIC"
    ARCHITECTURE = "ARCHITECTURE"
    PERFORMANCE = "PERFORMANCE"
    DATABASE = "DATABASE"
    API = "API"
    FRONTEND = "FRONTEND"
    UI_UX = "UI_UX"
    ACCESSIBILITY = "ACCESSIBILITY"
    SEO = "SEO"
    INFRASTRUCTURE = "INFRASTRUCTURE"
    CI_CD = "CI_CD"
    DEPLOYMENT = "DEPLOYMENT"
    OBSERVABILITY = "OBSERVABILITY"
    DOCUMENTATION = "DOCUMENTATION"
    LICENSE = "LICENSE"
    ADVERSARIAL = "ADVERSARIAL"


@dataclass
class Finding:
    id: str
    category: str
    severity: str
    confidence: float  # 0.0 to 1.0
    title: str
    description: str
    file: str
    line: Optional[int] = None
    component: str = "general"
    failure_scenario: str = ""
    evidence: str = ""
    reproduction: str = ""
    impact: str = ""
    recommendation: str = ""
    source_agent: str = "pre-live-full-audit"
    source_repository: str = "AI-Dev-Team"
    verified: bool = False
    verification_method: str = "AUTOMATIC_STATIC"
    status: str = "OPEN"
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Finding:
        # Normalize fields
        cleaned = dict(data)
        if "severity" in cleaned and isinstance(cleaned["severity"], str):
            cleaned["severity"] = cleaned["severity"].upper()
        if "status" in cleaned and isinstance(cleaned["status"], str):
            cleaned["status"] = cleaned["status"].upper()
        return cls(**cleaned)


@dataclass
class ReleaseGateResult:
    status: str  # "BLOCKED", "READY_FOR_REVIEW", "PASS"
    summary: str
    timestamp: str
    project_path: str
    blocking_reasons: List[str] = field(default_factory=list)
    warning_reasons: List[str] = field(default_factory=list)
    total_findings: int = 0
    findings_by_severity: Dict[str, int] = field(default_factory=dict)
    mandatory_gates_evaluated: Dict[str, bool] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
