#!/usr/bin/env python3
"""CLI Entrypoint for PRE-LIVE-FULL-AUDIT.

Usage:
    python scripts/pre_live_full_audit.py /path/to/project [--mode full|quick|fix] [--output-dir <dir>] [--read-only]
"""

import argparse
import os
import sys

# Add orchestrators to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "orchestrators", "pre-live-full-audit")))

from orchestrator import PreLiveFullAudit


def main():
    parser = argparse.ArgumentParser(description="PRE-LIVE-FULL-AUDIT Orchestrator")
    parser.add_argument("project_path", help="Path to project directory to audit")
    parser.add_argument("--mode", choices=["full", "quick", "fix"], default="full", help="Audit execution mode (default: full)")
    parser.add_argument("--output-dir", help="Directory where audit reports will be generated")
    parser.add_argument("--no-read-only", action="store_true", help="Allow fix modifications (default is read-only)")

    args = parser.parse_args()

    project_path = os.path.abspath(args.project_path)
    if not os.path.exists(project_path):
        print(f"Error: Target path does not exist: {project_path}", file=sys.stderr)
        sys.exit(1)

    read_only = not args.no_read_only

    audit = PreLiveFullAudit(project_path=project_path, output_dir=args.output_dir, read_only=read_only)
    results = audit.run(mode=args.mode)

    gate_status = results["gate"]["status"]
    print("\n" + "=" * 60)
    print(f"FINAL AUDIT RESULT: {gate_status}")
    print("=" * 60)
    if gate_status == "BLOCKED":
        sys.exit(2)
    elif gate_status == "READY_FOR_REVIEW":
        sys.exit(0)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
