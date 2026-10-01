#!/usr/bin/env bash
# ==============================================================================
# AI-Dev-Team Diagnostic Doctor
# Verifies system health, runtimes, symlinks, and component availability
# ==============================================================================
set -eo pipefail

AI_DEV_TEAM_ROOT="${AI_DEV_TEAM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

echo "=== Running AI Dev Team Diagnostic Health Check ==="
errors=0
warnings=0

# 1. Check Python
if ! command -v python3 >/dev/null 2>&1; then
  echo "[FAIL] python3 not found in PATH"
  ((errors++))
else
  py_ver=$(python3 --version 2>&1)
  echo "[PASS] $py_ver available"
fi

# 2. Check Node
if [ -x "$AI_DEV_TEAM_ROOT/environments/node22/bin/node" ]; then
  echo "[PASS] Isolated Node 22 ready ($("$AI_DEV_TEAM_ROOT/environments/node22/bin/node" -v))"
elif command -v node >/dev/null 2>&1; then
  echo "[PASS] System Node ready ($(node -v))"
else
  echo "[FAIL] Node runtime not found (install Node 20+ or Node 22)"
  ((errors++))
fi

# 3. Check Git
if ! command -v git >/dev/null 2>&1; then
  echo "[FAIL] git not found"
  ((errors++))
else
  echo "[PASS] git available ($(git --version))"
fi

# 4. Check GitHub CLI
if command -v gh >/dev/null 2>&1; then
  echo "[PASS] GitHub CLI available ($(gh --version | head -n 1))"
else
  echo "[WARN] GitHub CLI (gh) not found in PATH"
  ((warnings++))
fi

# 5. Check AgentTeam MCP
if [ -f "$AI_DEV_TEAM_ROOT/repos/AgentTeam/mcp-server/dist/index.js" ]; then
  echo "[PASS] AgentTeam dist/index.js verified"
else
  echo "[INFO] AgentTeam dist/index.js not pre-built (optional, build via scripts/bootstrap.sh)"
fi

# 6. Check Broken Symlinks in skills/
if [ -d "$AI_DEV_TEAM_ROOT/skills" ]; then
  broken=$(find "$AI_DEV_TEAM_ROOT/skills" -type l ! -exec test -e {} \; -print | wc -l | tr -d ' ')
  total_skills=$(find "$AI_DEV_TEAM_ROOT/skills" -maxdepth 1 -mindepth 1 | wc -l | tr -d ' ')
  if [ "$broken" -gt 0 ]; then
    echo "[WARN] Found $broken broken symlink(s) in skills/ (out of $total_skills total)"
    ((warnings++))
  else
    echo "[PASS] 0 broken symlinks in skills/ ($total_skills registered)"
  fi
else
  echo "[FAIL] skills/ directory missing"
  ((errors++))
fi

# 7. Check Manifest
if [ -f "$AI_DEV_TEAM_ROOT/registry/manifest.yaml" ]; then
  echo "[PASS] registry/manifest.yaml verified"
else
  echo "[WARN] registry/manifest.yaml missing"
  ((warnings++))
fi

# 8. Check Core Directories
for dir in "agents" "roles" "mcp" "orchestrators" "workflows" "freellmapi-agents" "scripts"; do
  if [ -d "$AI_DEV_TEAM_ROOT/$dir" ]; then
    echo "[PASS] Component directory $dir/ present"
  else
    echo "[FAIL] Essential directory $dir/ missing"
    ((errors++))
  fi
done

# 9. Check Protected Workspaces (if on primary machine)
for p in "/Users/subhajkar/Developer/LinkedIn-Audit" "/Users/subhajkar/Developer/subhajitportfolio-2.0"; do
  if [ -d "$p" ]; then
    echo "[PASS] Protected workspace $p intact"
  elif [ "$USER" = "subhajkar" ]; then
    echo "[FAIL] Protected workspace $p missing!"
    ((errors++))
  fi
done

echo ""
if [ "$errors" -eq 0 ]; then
  echo "=== Doctor Verdict: ALL CHECKS HEALTHY ($warnings warning(s)) ==="
  exit 0
else
  echo "=== Doctor Verdict: $errors ISSUE(S) DETECTED ==="
  exit 1
fi
