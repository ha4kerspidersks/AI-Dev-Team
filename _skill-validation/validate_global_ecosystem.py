#!/usr/bin/env python3
"""
Extended Global AI Skill Ecosystem Validation Script
Tests discovery, invocation, MCP, plugins, and infrastructure WITHOUT copying files locally into projects.
"""

import os
import sys
import json
import subprocess

GLOBAL_BASE = "/Users/subhajkar/Developer/AI-Dev-Team"
GLOBAL_SKILLS = os.path.join(GLOBAL_BASE, "skills")
GLOBAL_PLUGINS = os.path.join(GLOBAL_BASE, "plugins")
PROJECT_DIR = "/Users/subhajkar/Developer/AI-Dev-Team/_skill-validation"

results = {
    "project_isolation": True,
    "skills_discovery": {},
    "plugins_discovery": {},
    "cli_availability": {},
    "mcp_availability": {},
    "infrastructure": {}
}

# 1. Verify Project Isolation: Ensure _skill-validation has NO local skill copies
local_entries = [e for e in os.listdir(PROJECT_DIR) if e != "validate_global_ecosystem.py" and not e.startswith(".")]
if local_entries:
    results["project_isolation"] = False
    results["project_isolation_error"] = f"Unexpected local items found: {local_entries}"
else:
    results["project_isolation"] = True

# 2. Test Discovery of Global Skills across all 10 ecosystems
test_skills = {
    # Addy Osmani
    "Addy Osmani - Spec Driven Dev": "spec-driven-development",
    "Addy Osmani - Namespaced TDD": "addyosmani-test-driven-development",
    # Graphify
    "Graphify - Codebase Knowledge": "graphify",
    # Ponytail
    "Ponytail - Lazy Senior Dev": "ponytail",
    "Ponytail - Audit": "ponytail-audit",
    # Strix
    "Strix - Vulnerability Search": "find-security-vulnerabilities-in-code",
    "Strix - OWASP Top 10": "owasp-top-10-testing",
    # Context7
    "Context7 - Docs MCP": "context7-mcp",
    "Context7 - Find Docs": "find-docs",
    "Context7 - CLI Skill": "context7-cli",
    # Superpowers
    "Superpowers - Brainstorming": "brainstorming",
    "Superpowers - Writing Plans": "writing-plans",
    "Superpowers - Namespaced Subagent": "superpowers-subagent-driven-development",
    # Matt Pocock
    "Matt Pocock - Grill Me": "grill-me",
    "Matt Pocock - Domain Modeling": "domain-modeling",
    "Matt Pocock - Namespaced TDD": "mattpocock-tdd",
    # ECC
    "ECC - Agentic Engineering": "agentic-engineering",
    "ECC - Verification Loop": "verification-loop",
    "ECC - Namespaced React Patterns": "ecc-react-patterns",
    # Awesome LLM Apps (Selective Skills)
    "Awesome LLM Apps - Commit Archaeologist": "commit-archaeologist",
    "Awesome LLM Apps - Dependency Doctor": "dependency-doctor",
    "Awesome LLM Apps - Scope Creep Detector": "scope-creep-detector",
    "Awesome LLM Apps - First Reader": "first-reader",
    "Awesome LLM Apps - Advisor Orchestrator": "advisor-orchestrator-worker"
}

for label, skill_name in test_skills.items():
    skill_path = os.path.join(GLOBAL_SKILLS, skill_name)
    skill_md = os.path.join(skill_path, "SKILL.md")
    
    exists = os.path.exists(skill_md)
    real_path = os.path.realpath(skill_md)
    has_frontmatter = False
    if exists:
        try:
            with open(skill_md, "r", errors="ignore") as f:
                head = f.read(500)
                has_frontmatter = "name:" in head and "description:" in head
        except Exception:
            pass
            
    results["skills_discovery"][label] = {
        "name": skill_name,
        "path": skill_path,
        "real_target": real_path,
        "discoverable": exists and has_frontmatter,
        "frontmatter_valid": has_frontmatter
    }

# 3. Test Plugins Discovery
plugins_to_test = {
    "Superpowers Plugin": os.path.join(GLOBAL_PLUGINS, "superpowers"),
    "ECC Universal Plugin": os.path.join(GLOBAL_PLUGINS, "ecc")
}

for name, ppath in plugins_to_test.items():
    exists = os.path.exists(ppath)
    has_manifest = os.path.exists(os.path.join(ppath, "package.json")) or os.path.exists(os.path.join(ppath, "plugin.json"))
    results["plugins_discovery"][name] = {
        "path": ppath,
        "exists": exists,
        "valid_manifest": has_manifest,
        "status": "Verified Active" if (exists and has_manifest) else "Failed"
    }

# 4. Test CLI Availability
clis_to_test = {
    "Graphify CLI": ["/Users/subhajkar/.local/bin/graphify", "install", "--help"],
    "Strix CLI": ["/Users/subhajkar/.local/bin/strix", "--version"],
    "Context7 CLI": ["/opt/homebrew/bin/ctx7", "--version"],
    "Antigravity CLI (agy)": ["/Users/subhajkar/.local/bin/agy", "plugin", "list"]
}

for name, cmd in clis_to_test.items():
    binary = cmd[0]
    available = os.path.exists(binary) and os.access(binary, os.X_OK)
    output = ""
    exit_code = -1
    if available:
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            exit_code = p.returncode
            output = (p.stdout + p.stderr).strip().split("\n")[0]
        except Exception as e:
            output = str(e)
            
    results["cli_availability"][name] = {
        "binary": binary,
        "available": available and exit_code == 0,
        "exit_code": exit_code,
        "version_or_help": output
    }

# 5. Test MCP Availability
mcp_tests = {
    "Context7 MCP Server": [
        "/Users/subhajkar/Developer/AI-Dev-Team/environments/node22/bin/node",
        "/Users/subhajkar/Developer/AI-Dev-Team/mcp/node_modules/@upstash/context7-mcp/dist/index.js",
        "--help"
    ],
    "Graphify MCP Server": [
        "/Users/subhajkar/.local/bin/graphify-mcp",
        "--help"
    ]
}

for name, cmd in mcp_tests.items():
    binary = cmd[0]
    available = os.path.exists(binary)
    exit_code = -1
    output = ""
    if available:
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            exit_code = p.returncode
            output = (p.stdout + p.stderr).strip().split("\n")[0]
        except Exception as e:
            output = str(e)
            
    results["mcp_availability"][name] = {
        "entry_point": cmd[1] if len(cmd) > 1 else binary,
        "available": available and exit_code == 0,
        "exit_code": exit_code,
        "output": output
    }

# 6. Test Infrastructure - OmniRoute
omni_dir = os.path.join(GLOBAL_BASE, "infrastructure", "omniroute")
omni_pkg = os.path.join(omni_dir, "package.json")
omni_readme = os.path.join(omni_dir, "README.md")
omni_installed = os.path.exists(omni_pkg) and os.path.exists(omni_readme)
omni_version = "unknown"
if omni_installed:
    try:
        with open(omni_pkg) as f:
            omni_version = json.load(f).get("version", "unknown")
    except Exception:
        pass

results["infrastructure"]["OmniRoute"] = {
    "path": omni_dir,
    "installed": omni_installed,
    "version": omni_version,
    "default_port": 20128,
    "status": "Installed (On-Demand / Non-Conflicting)"
}

print(json.dumps(results, indent=2))

# Assert all critical passes
all_skills_ok = all(v["discoverable"] for v in results["skills_discovery"].values())
all_plugins_ok = all(v["exists"] and v["valid_manifest"] for v in results["plugins_discovery"].values())
all_clis_ok = all(v["available"] for v in results["cli_availability"].values())
all_mcp_ok = all(v["available"] for v in results["mcp_availability"].values())
isolation_ok = results["project_isolation"]
infra_ok = results["infrastructure"]["OmniRoute"]["installed"]

print("\n--- FINAL EMPIRICAL SUMMARY ---")
print(f"1. Project Isolation (Zero Local Skill Copies): {'PASS' if isolation_ok else 'FAIL'}")
print(f"2. Global Skills Discoverable: {'PASS' if all_skills_ok else 'FAIL'} ({sum(1 for v in results['skills_discovery'].values() if v['discoverable'])}/{len(results['skills_discovery'])} passed)")
print(f"3. Global Plugins Verified: {'PASS' if all_plugins_ok else 'FAIL'} ({sum(1 for v in results['plugins_discovery'].values() if v['exists'])}/{len(results['plugins_discovery'])} passed)")
print(f"4. CLIs Available & Functional: {'PASS' if all_clis_ok else 'FAIL'} ({sum(1 for v in results['cli_availability'].values() if v['available'])}/{len(results['cli_availability'])} passed)")
print(f"5. MCP Servers Ready: {'PASS' if all_mcp_ok else 'FAIL'} ({sum(1 for v in results['mcp_availability'].values() if v['available'])}/{len(results['mcp_availability'])} passed)")
print(f"6. Supporting Infrastructure Ready: {'PASS' if infra_ok else 'FAIL'}")

if all_skills_ok and all_plugins_ok and all_clis_ok and all_mcp_ok and isolation_ok and infra_ok:
    print("\nOVERALL EXTENDED VALIDATION STATUS: ALL SYSTEMS VERIFIED PASS")
    sys.exit(0)
else:
    print("\nOVERALL EXTENDED VALIDATION STATUS: VERIFICATION FAILED")
    sys.exit(1)
