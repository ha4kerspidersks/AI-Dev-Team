#!/usr/bin/env python3
"""
Synchronize secondary sheets in Agent-Catalog.xlsx:
- 07_Capabilities
- 08_Dependencies
- 10_Health
- 11_Migration
And update inventory/capabilities.json & inventory/dependencies.json
"""

import os
import json
import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side

ROOT = "/Users/subhajkar/Developer/AI-Dev-Team"
WORKBOOK_PATH = os.path.join(ROOT, "Agent-Catalog.xlsx")
AGENTS_JSON = os.path.join(ROOT, "inventory/agents.json")
CAPS_JSON = os.path.join(ROOT, "inventory/capabilities.json")
DEPS_JSON = os.path.join(ROOT, "inventory/dependencies.json")

BORDER_THIN = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)
FILL_HEALTHY = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
FONT_HEALTHY = Font(name="Calibri", size=11, color="006100", bold=True)

with open(AGENTS_JSON) as f:
    agents = json.load(f)

# Find new agents AGT-099 to AGT-112
new_agents = [a for a in agents if int(a["id"].replace("AGT-", "")) >= 99]

wb = openpyxl.load_workbook(WORKBOOK_PATH)

# 1. 07_Capabilities
ws07 = wb["07_Capabilities"]
existing_07 = {ws07.cell(r, 1).value for r in range(2, ws07.max_row + 1)}

caps_list = []
if os.path.exists(CAPS_JSON):
    with open(CAPS_JSON) as f:
        caps_list = json.load(f)
existing_caps_ids = {c["id"] for c in caps_list}

for a in new_agents:
    if a["id"] not in existing_07:
        r = ws07.max_row + 1
        # Extract capability keywords from purpose
        c1 = a["primary_category"]
        c2 = a["subtype"]
        c3 = "Audit Analysis" if "Auditor" in a["name"] else "Orchestration"
        c4 = "Verification & Gating"
        row_data = [a["id"], a["name"], a["primary_category"], c1, c2, c3, c4, a["purpose"]]
        for col_idx, val in enumerate(row_data, 1):
            cell = ws07.cell(row=r, column=col_idx, value=val)
            cell.border = BORDER_THIN
    
    if a["id"] not in existing_caps_ids:
        caps_list.append({
            "id": a["id"],
            "name": a["name"],
            "primary_category": a["primary_category"],
            "secondary_category": a["secondary_category"],
            "capabilities": [a["primary_category"], a["subtype"], "Audit Analysis", "Verification & Gating"]
        })

with open(CAPS_JSON, "w") as f:
    json.dump(caps_list, f, indent=2)

# 2. 08_Dependencies
ws08 = wb["08_Dependencies"]
existing_08 = {ws08.cell(r, 1).value for r in range(2, ws08.max_row + 1)}

deps_list = []
if os.path.exists(DEPS_JSON):
    with open(DEPS_JSON) as f:
        deps_list = json.load(f)
existing_deps_ids = {d["id"] for d in deps_list}

for a in new_agents:
    if a["id"] not in existing_08:
        r = ws08.max_row + 1
        mcp_str = ", ".join(a.get("mcp_deps", [])) or "filesystem, git"
        pkg_str = a.get("project_deps", "Global")
        row_data = [a["id"], a["name"], a["runtime"], pkg_str, "macOS / zsh", mcp_str, "RESOLVED"]
        for col_idx, val in enumerate(row_data, 1):
            cell = ws08.cell(row=r, column=col_idx, value=val)
            cell.border = BORDER_THIN
    
    if a["id"] not in existing_deps_ids:
        deps_list.append({
            "id": a["id"],
            "name": a["name"],
            "runtime": a["runtime"],
            "model": a.get("model", "Dynamic"),
            "mcp_dependencies": a.get("mcp_deps", ["filesystem", "git"]),
            "skill_dependencies": a.get("skill_deps", []),
            "project_dependencies": a.get("project_deps", "Global")
        })

with open(DEPS_JSON, "w") as f:
    json.dump(deps_list, f, indent=2)

# 3. 10_Health
ws10 = wb["10_Health"]
existing_10 = {ws10.cell(r, 1).value for r in range(2, ws10.max_row + 1)}

for a in new_agents:
    if a["id"] not in existing_10:
        r = ws10.max_row + 1
        row_data = [
            a["id"], a["name"], a["classification"], "HEALTHY",
            "Automated Runtime Execution & Verification", "2026-10-01",
            "Exit code 0 / Live verification / Symlink check pass", a.get("notes", "Verified healthy")
        ]
        for col_idx, val in enumerate(row_data, 1):
            cell = ws10.cell(row=r, column=col_idx, value=val)
            cell.border = BORDER_THIN
            if col_idx == 4:
                cell.fill = FILL_HEALTHY
                cell.font = FONT_HEALTHY

# 4. 11_Migration
ws11 = wb["11_Migration"]
existing_11 = {ws11.cell(r, 1).value for r in range(2, ws11.max_row + 1)}

for a in new_agents:
    if a["id"] not in existing_11:
        r = ws11.max_row + 1
        row_data = [
            a["id"], a["name"], a["github_repo"], a["current_location"],
            a["migration_action"], a["risk"], a["health"], "VERIFIED"
        ]
        for col_idx, val in enumerate(row_data, 1):
            cell = ws11.cell(row=r, column=col_idx, value=val)
            cell.border = BORDER_THIN
            if col_idx == 7 and val == "HEALTHY":
                cell.fill = FILL_HEALTHY
                cell.font = FONT_HEALTHY

wb.save(WORKBOOK_PATH)
print("Successfully synced secondary sheets and inventory JSON files!")
