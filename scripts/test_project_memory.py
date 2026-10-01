#!/usr/bin/env python3
"""
Comprehensive Validation Suite for Global Project Intelligence & Memory System.
Runs Tests 1 through 8 to empirically verify discovery, context loading,
incremental change detection, structural changes, token efficiency, and self-healing.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

SANDBOX_DIR = Path("/Users/subhajkar/Developer/AI-Dev-Team/test-projects/memory-test-sandbox")
PORTFOLIO_DIR = Path("/Users/subhajkar/Developer/subhajitportfolio-2.0")
ENGINE_SCRIPT = Path("/Users/subhajkar/Developer/AI-Dev-Team/scripts/project_memory_engine.py")

passed = 0
failed = 0

def run_step(test_name: str, fn):
    global passed, failed
    print(f"\n============================================================")
    print(f"RUNNING: {test_name}")
    print(f"============================================================")
    try:
        fn()
        print(f"--> [PASS] {test_name}")
        passed += 1
    except Exception as e:
        print(f"--> [FAIL] {test_name}: {e}")
        failed += 1

def test_1_new_project():
    """TEST 1: Automatic Discovery on New Project."""
    if SANDBOX_DIR.exists():
        shutil.rmtree(SANDBOX_DIR)
        
    SANDBOX_DIR.mkdir(parents=True)
    
    # Scaffold mini test project
    (SANDBOX_DIR / "package.json").write_text(json.dumps({
        "name": "sandbox-app",
        "version": "1.0.0",
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "test": "node --test"
        },
        "dependencies": {
            "express": "^4.18.2",
            "react": "^18.2.0"
        },
        "devDependencies": {
            "vite": "^5.0.0"
        }
    }, indent=2))
    
    (SANDBOX_DIR / "src").mkdir()
    (SANDBOX_DIR / "src" / "index.ts").write_text("console.log('App starting');")
    (SANDBOX_DIR / "src" / "api.ts").write_text("""
    import express from 'express';
    const app = express();
    app.get('/api/health', (req, res) => res.json({ status: 'ok' }));
    app.post('/api/items', (req, res) => res.json({ item: 'created' }));
    """)
    (SANDBOX_DIR / "tests").mkdir()
    (SANDBOX_DIR / "tests" / "health.test.js").write_text("console.log('Testing health');")
    
    # Run discovery
    res = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "discover", str(SANDBOX_DIR)],
        capture_output=True, text=True, check=True
    )
    data = json.loads(res.stdout)
    assert data["status"] == "DISCOVERY_COMPLETED", f"Unexpected status: {data}"
    
    mem_dir = SANDBOX_DIR / ".agents" / "project-memory"
    assert mem_dir.is_dir(), "Memory directory was not created"
    
    required = [
        "METADATA.json", "PROJECT-MAP.json", "PROJECT-CONTEXT.md",
        "ARCHITECTURE.md", "DEPENDENCIES.md", "DATA-FLOW.md",
        "API-MAP.md", "TEST-MAP.md", "DECISIONS.md", "CHANGELOG.md"
    ]
    for req in required:
        assert (mem_dir / req).is_file(), f"Missing required file: {req}"
        
    meta = json.loads((mem_dir / "METADATA.json").read_text())
    assert "React" in meta["frameworks"], "React framework not detected"
    assert "Express" in meta["frameworks"], "Express framework not detected"
    assert meta["file_count"] >= 4, f"File count mismatch: {meta['file_count']}"
    assert meta["test_count"] >= 1, f"Test count mismatch: {meta['test_count']}"
    assert meta["api_count"] == 2, f"API count mismatch: {meta['api_count']}"

def test_2_existing_project():
    """TEST 2: Open and Load Memory from Existing Project."""
    res = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "check", str(SANDBOX_DIR)],
        capture_output=True, text=True, check=True
    )
    data = json.loads(res.stdout)
    assert data["status"] == "CLEAN", f"Expected CLEAN status, got {data}"
    
    # Load context
    res_load = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "load", str(SANDBOX_DIR)],
        capture_output=True, text=True, check=True
    )
    assert "# PROJECT CONTEXT: memory-test-sandbox" in res_load.stdout or "sandbox-app" in res_load.stdout

def test_3_modify_file():
    """TEST 3: Modify File and Verify Incremental Detection (Level 2)."""
    index_file = SANDBOX_DIR / "src" / "index.ts"
    index_file.write_text("console.log('App starting with modified logic v2');")
    
    res = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "refresh", str(SANDBOX_DIR), "--summary", "Updated index logic"],
        capture_output=True, text=True, check=True
    )
    data = json.loads(res.stdout)
    assert data["status"] == "REFRESH_COMPLETED", f"Refresh failed: {data}"
    assert data["change_level"] == 2, f"Expected Level 2 change, got {data['change_level']}"
    assert "src/index.ts" in data["modified"], f"Modified file not detected: {data}"

def test_4_add_file():
    """TEST 4: Add File and Verify Structural Detection (Level 3)."""
    new_util = SANDBOX_DIR / "src" / "utils.ts"
    new_util.write_text("export const add = (a: number, b: number) => a + b;")
    
    res = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "refresh", str(SANDBOX_DIR), "--summary", "Added utils module"],
        capture_output=True, text=True, check=True
    )
    data = json.loads(res.stdout)
    assert data["status"] == "REFRESH_COMPLETED", f"Refresh failed: {data}"
    assert data["change_level"] == 3, f"Expected Level 3 change, got {data['change_level']}"
    assert "src/utils.ts" in data["added"], f"Added file not detected: {data}"

def test_5_delete_file():
    """TEST 5: Delete File and Verify Memory Updates."""
    new_util = SANDBOX_DIR / "src" / "utils.ts"
    new_util.unlink()
    
    res = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "refresh", str(SANDBOX_DIR), "--summary", "Removed utils module"],
        capture_output=True, text=True, check=True
    )
    data = json.loads(res.stdout)
    assert data["status"] == "REFRESH_COMPLETED", f"Refresh failed: {data}"
    assert "src/utils.ts" in data["deleted"], f"Deleted file not detected: {data}"

def test_6_architectural_change():
    """TEST 6: Architectural Change (New API Route & Service) Refreshes Targeted Maps."""
    routes_dir = SANDBOX_DIR / "src" / "routes"
    routes_dir.mkdir(parents=True, exist_ok=True)
    (routes_dir / "users.ts").write_text("""
    import express from 'express';
    const router = express.Router();
    router.get('/api/users', (req, res) => res.json([]));
    router.post('/api/users/auth', (req, res) => res.json({ token: 'jwt' }));
    """)
    
    res = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "refresh", str(SANDBOX_DIR), "--summary", "Added users authentication route"],
        capture_output=True, text=True, check=True
    )
    data = json.loads(res.stdout)
    assert data["status"] == "REFRESH_COMPLETED"
    
    # Verify API-MAP was updated
    api_map_content = (SANDBOX_DIR / ".agents" / "project-memory" / "API-MAP.md").read_text()
    assert "/api/users" in api_map_content, "New endpoint /api/users missing from API-MAP"
    assert "/api/users/auth" in api_map_content, "New endpoint /api/users/auth missing from API-MAP"

def test_7_token_efficiency():
    """TEST 7: Verify Token Efficiency (Compact Context vs Raw Codebase)."""
    res_load = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "load", str(SANDBOX_DIR)],
        capture_output=True, text=True, check=True
    )
    context_text = res_load.stdout
    lines = context_text.strip().splitlines()
    assert len(lines) < 150, f"Context too large for token efficiency: {len(lines)} lines"
    assert "Executive Summary" in context_text
    assert "Subsystem Navigation Guide" in context_text
    print(f"Context size: {len(lines)} lines, {len(context_text)} bytes (Highly token-efficient)")

def test_8_memory_recovery():
    """TEST 8: Memory Recovery after Deletion or Corruption."""
    mem_dir = SANDBOX_DIR / ".agents" / "project-memory"
    
    # 1. Corrupt JSON
    (mem_dir / "METADATA.json").write_text("{ corrupted invalid json ...")
    res_check = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "check", str(SANDBOX_DIR)],
        capture_output=True, text=True, check=True
    )
    check_data = json.loads(res_check.stdout)
    assert check_data["status"] == "CORRUPTED", f"Expected CORRUPTED status, got {check_data}"
    
    # 2. Recover
    res_rec = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "recover", str(SANDBOX_DIR)],
        capture_output=True, text=True, check=True
    )
    rec_data = json.loads(res_rec.stdout)
    assert rec_data["status"] == "DISCOVERY_COMPLETED", f"Recovery failed: {rec_data}"
    
    # 3. Verify clean
    res_check2 = subprocess.run(
        [sys.executable, str(ENGINE_SCRIPT), "check", str(SANDBOX_DIR)],
        capture_output=True, text=True, check=True
    )
    check_data2 = json.loads(res_check2.stdout)
    assert check_data2["status"] == "CLEAN", f"Post-recovery check failed: {check_data2}"

if __name__ == "__main__":
    print("Starting Global Project Intelligence & Memory System Validation Suite...")
    run_step("TEST 1: New Project Discovery", test_1_new_project)
    run_step("TEST 2: Existing Project Loading", test_2_existing_project)
    run_step("TEST 3: Modify File Incremental Detection (Level 2)", test_3_modify_file)
    run_step("TEST 4: Add File Structural Detection (Level 3)", test_4_add_file)
    run_step("TEST 5: Delete File Index Update", test_5_delete_file)
    run_step("TEST 6: Architectural Change Targeted Refresh", test_6_architectural_change)
    run_step("TEST 7: Token Efficiency Evaluation", test_7_token_efficiency)
    run_step("TEST 8: Memory Recovery & Self-Healing", test_8_memory_recovery)
    
    # Clean up sandbox
    if SANDBOX_DIR.exists():
        shutil.rmtree(SANDBOX_DIR)
        
    print("\n============================================================")
    print(f"VALIDATION SUMMARY: {passed} PASSED, {failed} FAILED")
    print("============================================================")
    sys.exit(0 if failed == 0 else 1)
