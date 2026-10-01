#!/usr/bin/env bash
# ==============================================================================
# AI-Dev-Team Restore & Environment Recreation Script
# Portable, safe to rerun, non-destructive
# Re-creates links, restores runtimes, and provides credential guidance
# ==============================================================================
set -eo pipefail

AI_DEV_TEAM_ROOT="${AI_DEV_TEAM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

echo "================================================================================"
echo "          AI-DEV-TEAM ENVIRONMENT RESTORATION SYSTEM                            "
echo "================================================================================"
echo "Workspace Root: $AI_DEV_TEAM_ROOT"

# 1. Verify Manifest
if [ -f "$AI_DEV_TEAM_ROOT/registry/manifest.yaml" ]; then
  echo "[PASS] Found registry/manifest.yaml"
else
  echo "[WARN] registry/manifest.yaml missing! Creating snapshot..."
  "$AI_DEV_TEAM_ROOT/scripts/snapshot.sh"
fi

# 2. Relink Skills
echo "[STEP 1/4] Relinking central skills..."
python3 "$AI_DEV_TEAM_ROOT/scripts/relink_skills.py"

# 3. Verify / Run Bootstrap
echo "[STEP 2/4] Running ecosystem bootstrap..."
"$AI_DEV_TEAM_ROOT/scripts/bootstrap.sh"

# 4. Verify Runtimes
echo "[STEP 3/4] Running system doctor..."
"$AI_DEV_TEAM_ROOT/scripts/doctor.sh"

# 5. Security & Credential Guidance
echo "[STEP 4/4] Environment Configuration & Secrets Management"
echo "--------------------------------------------------------------------------------"
echo "CRITICAL SECURITY NOTICE:"
echo "This public repository NEVER stores real credentials or API keys."
echo ""
echo "To supply credentials on this machine:"
echo "  1. Copy the example configuration template:"
echo "     cp $AI_DEV_TEAM_ROOT/.env.example $AI_DEV_TEAM_ROOT/.env"
echo ""
echo "  2. Populate your local secrets in .env (which is strictly .gitignored):"
echo "     - FREELLMAPI_BASE_URL (default: http://127.0.0.1:31415)"
echo "     - FREELLMAPI_API_KEY (if configured)"
echo "     - GITHUB_TOKEN (optional, for GitHub CLI & Copilot bridge)"
echo "     - HF_TOKEN (optional, for Hugging Face datasets and jobs)"
echo "     - OPENAI_API_KEY / ANTHROPIC_API_KEY / GEMINI_API_KEY (if direct routing)"
echo ""
echo "  3. Verify security:"
echo "     git status"
echo "     (Confirm that .env remains untracked and ignored)"
echo "--------------------------------------------------------------------------------"
echo "Restoration completed successfully."
