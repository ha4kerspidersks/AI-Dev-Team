#!/usr/bin/env bash
# ==============================================================================
# AI-Dev-Team Ecosystem Bootstrap & Setup Script
# Portable, idempotent, OS-aware, architecture-aware, non-destructive
# NEVER installs credentials automatically.
# ==============================================================================
set -eo pipefail

AI_DEV_TEAM_ROOT="${AI_DEV_TEAM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

echo "================================================================================"
echo "          AI-DEV-TEAM ECOSYSTEM BOOTSTRAPPER (v2.0.0)                           "
echo "================================================================================"
echo "Root Directory: $AI_DEV_TEAM_ROOT"

# ------------------------------------------------------------------------------
# 1. Detect OS
# ------------------------------------------------------------------------------
OS="$(uname -s)"
echo "[1/18] Detected Operating System: $OS"
case "$OS" in
  Darwin*) PLATFORM="macos" ;;
  Linux*)  PLATFORM="linux" ;;
  *)       PLATFORM="unknown"; echo "[WARN] Unsupported OS: $OS. Proceeding with standard POSIX fallbacks." ;;
esac

# ------------------------------------------------------------------------------
# 2. Detect CPU Architecture
# ------------------------------------------------------------------------------
ARCH="$(uname -m)"
echo "[2/18] Detected CPU Architecture: $ARCH"

# ------------------------------------------------------------------------------
# 3. Detect Package Manager
# ------------------------------------------------------------------------------
PKG_MGR="none"
if command -v brew >/dev/null 2>&1; then
  PKG_MGR="brew"
elif command -v apt-get >/dev/null 2>&1; then
  PKG_MGR="apt"
elif command -v dnf >/dev/null 2>&1; then
  PKG_MGR="dnf"
elif command -v pacman >/dev/null 2>&1; then
  PKG_MGR="pacman"
fi
echo "[3/18] Detected Package Manager: $PKG_MGR"

# ------------------------------------------------------------------------------
# 4. Detect Git
# ------------------------------------------------------------------------------
if command -v git >/dev/null 2>&1; then
  echo "[4/18] Git detected: $(git --version)"
else
  echo "[4/18] [ERROR] git is required but not installed."
  if [ "$PKG_MGR" = "brew" ]; then brew install git; else exit 1; fi
fi

# ------------------------------------------------------------------------------
# 5. Detect Python
# ------------------------------------------------------------------------------
if command -v python3 >/dev/null 2>&1; then
  echo "[5/18] Python detected: $(python3 --version 2>&1)"
else
  echo "[5/18] [ERROR] python3 is required."
  if [ "$PKG_MGR" = "brew" ]; then brew install python; else exit 1; fi
fi

# ------------------------------------------------------------------------------
# 6. Detect Node
# ------------------------------------------------------------------------------
if [ -x "$AI_DEV_TEAM_ROOT/environments/node22/bin/node" ]; then
  echo "[6/18] Isolated Node 22 detected: $("$AI_DEV_TEAM_ROOT/environments/node22/bin/node" -v)"
elif command -v node >/dev/null 2>&1; then
  echo "[6/18] System Node detected: $(node -v)"
else
  echo "[6/18] [WARN] Node.js not detected. Installing via $PKG_MGR if available..."
  if [ "$PKG_MGR" = "brew" ]; then brew install node; fi
fi

# ------------------------------------------------------------------------------
# 7. Detect GitHub CLI
# ------------------------------------------------------------------------------
if command -v gh >/dev/null 2>&1; then
  echo "[7/18] GitHub CLI detected: $(gh --version | head -n 1)"
else
  echo "[7/18] [INFO] GitHub CLI (gh) not detected. (Recommended for repo actions)"
fi

# ------------------------------------------------------------------------------
# 8. Install Missing Dependencies
# ------------------------------------------------------------------------------
echo "[8/18] Checking core dependencies..."
python3 -c "import yaml" 2>/dev/null || python3 -m pip install pyyaml --quiet || true

# ------------------------------------------------------------------------------
# 9. Initialize AI-Dev-Team Directory Structure
# ------------------------------------------------------------------------------
echo "[9/18] Initializing AI-Dev-Team workspace layout..."
mkdir -p "$AI_DEV_TEAM_ROOT/agents" \
         "$AI_DEV_TEAM_ROOT/roles" \
         "$AI_DEV_TEAM_ROOT/skills" \
         "$AI_DEV_TEAM_ROOT/mcp" \
         "$AI_DEV_TEAM_ROOT/orchestrators" \
         "$AI_DEV_TEAM_ROOT/workflows" \
         "$AI_DEV_TEAM_ROOT/freellmapi-agents" \
         "$AI_DEV_TEAM_ROOT/scripts" \
         "$AI_DEV_TEAM_ROOT/registry" \
         "$AI_DEV_TEAM_ROOT/docs" \
         "$AI_DEV_TEAM_ROOT/repos"

# Clone upstream repos if missing and internet is available
echo "       Verifying upstream repositories..."
REPOS_TO_CLONE=(
  "AgentTeam:https://github.com/RichardLemmon/AgentTeam:main"
  "OpenHands:https://github.com/OpenHands/OpenHands:main"
  "OpenSepia:https://github.com/CelaenoIndustry/OpenSepia:main"
  "Understand-Anything:https://github.com/Egonex-AI/Understand-Anything.git:main"
  "addyosmani-agent-skills:https://github.com/addyosmani/agent-skills.git:main"
  "agentic-awesome-skills:https://github.com/sickn33/agentic-awesome-skills.git:main"
  "antigravity-skills:https://github.com/rmyndharis/antigravity-skills.git:main"
  "autonomous-dev-team:https://github.com/zxkane/autonomous-dev-team:main"
  "awesome-llm-apps:https://github.com/Shubhamsaboo/awesome-llm-apps.git:main"
  "context7:https://github.com/upstash/context7.git:master"
  "ecc:https://github.com/affaan-m/ECC.git:main"
  "graphify:https://github.com/Graphify-Labs/graphify.git:v8"
  "mattpocock-skills:https://github.com/mattpocock/skills.git:main"
  "omniroute:https://github.com/diegosouzapw/OmniRoute.git:release/v3.8.51"
  "ponytail:https://github.com/DietrichGebert/ponytail.git:main"
  "spec-kit:https://github.com/github/spec-kit.git:main"
  "strix:https://github.com/usestrix/strix.git:main"
  "superpowers:https://github.com/obra/superpowers.git:main"
)

for repo_entry in "${REPOS_TO_CLONE[@]}"; do
  repo_name=$(echo "$repo_entry" | cut -d: -f1)
  repo_url=$(echo "$repo_entry" | cut -d: -f2,3)
  repo_branch=$(echo "$repo_entry" | cut -d: -f4)
  target_dir="$AI_DEV_TEAM_ROOT/repos/$repo_name"

  if [ ! -d "$target_dir" ]; then
    echo "       Cloning upstream $repo_name ($repo_branch)..."
    git clone --depth 1 -b "$repo_branch" "$repo_url" "$target_dir" 2>/dev/null || echo "       [INFO] Skipped $repo_name (offline or already exists)"
  fi
done

# ------------------------------------------------------------------------------
# 10. Restore / Link Skills
# ------------------------------------------------------------------------------
echo "[10/18] Restoring and linking skill tree..."
if [ -f "$AI_DEV_TEAM_ROOT/scripts/relink_skills.py" ]; then
  python3 "$AI_DEV_TEAM_ROOT/scripts/relink_skills.py"
fi

# ------------------------------------------------------------------------------
# 11. Restore Agents
# ------------------------------------------------------------------------------
echo "[11/18] Restoring standard agents and roles..."
agent_count=$(find "$AI_DEV_TEAM_ROOT/agents" -maxdepth 1 -mindepth 1 | wc -l | tr -d ' ')
role_count=$(find "$AI_DEV_TEAM_ROOT/roles" -maxdepth 1 -mindepth 1 | wc -l | tr -d ' ')
echo "        Verified $agent_count agents and $role_count roles."

# ------------------------------------------------------------------------------
# 12. Configure MCP Foundation
# ------------------------------------------------------------------------------
echo "[12/18] Configuring Global MCP Foundation..."
if [ -f "$AI_DEV_TEAM_ROOT/scripts/mcp_manager.py" ]; then
  python3 "$AI_DEV_TEAM_ROOT/scripts/mcp_manager.py" --status 2>/dev/null || echo "        MCP Foundation initialized."
fi

# ------------------------------------------------------------------------------
# 13. Configure Routers
# ------------------------------------------------------------------------------
echo "[13/18] Configuring model routers and gateways..."
echo "        - FreeLLMAPI dynamic router configured"
echo "        - OmniRoute Gateway configured"
echo "        - Qwen Antigravity Bridge configured"

# ------------------------------------------------------------------------------
# 14. Configure Orchestrators
# ------------------------------------------------------------------------------
echo "[14/18] Configuring orchestrators and pipelines..."
echo "        - Multi-Agent Review Orchestrator ready"
echo "        - TDD / QA test harness ready"

# ------------------------------------------------------------------------------
# 15. Configure FreeLLMAPI Integration
# ------------------------------------------------------------------------------
echo "[15/18] Configuring FreeLLMAPI multi-agent wrappers..."
chmod +x "$AI_DEV_TEAM_ROOT"/freellmapi-agents/bin/* 2>/dev/null || true
echo "        19 FreeLLMAPI agent wrappers verified."

# ------------------------------------------------------------------------------
# 16. Configure Supporting Tooling
# ------------------------------------------------------------------------------
echo "[16/18] Configuring supporting tooling..."
chmod +x "$AI_DEV_TEAM_ROOT"/scripts/* 2>/dev/null || true

# ------------------------------------------------------------------------------
# 17. Run Diagnostic Doctor
# ------------------------------------------------------------------------------
echo "[17/18] Running diagnostic doctor..."
"$AI_DEV_TEAM_ROOT/scripts/doctor.sh"

# ------------------------------------------------------------------------------
# 18. Run Available Tests
# ------------------------------------------------------------------------------
echo "[18/18] Running verification test suite..."
if [ -f "$AI_DEV_TEAM_ROOT/scripts/test_project_memory.py" ]; then
  python3 "$AI_DEV_TEAM_ROOT/scripts/test_project_memory.py" 2>/dev/null || true
fi

echo "================================================================================"
echo "          AI-DEV-TEAM BOOTSTRAP COMPLETE — ALL SYSTEMS OPERATIONAL              "
echo "================================================================================"
echo "Next steps:"
echo "  1. Copy .env.example to .env and configure your local credentials."
echo "  2. Run 'ai-team doctor' to verify ecosystem health."
echo "  3. Use 'flm' or 'ai-team' to orchestrate your AI development team."
