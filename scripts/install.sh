#!/usr/bin/env bash
# ==============================================================================
# AI-Dev-Team Global CLI Installer
# Installs ai-team and flm CLI wrappers into ~/.local/bin or ~/bin
# ==============================================================================
set -eo pipefail

AI_DEV_TEAM_ROOT="${AI_DEV_TEAM_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

TARGET_BIN="$HOME/.local/bin"
if [ ! -d "$TARGET_BIN" ]; then
  TARGET_BIN="$HOME/bin"
fi
mkdir -p "$TARGET_BIN"

echo "=== Installing AI-Dev-Team CLI Wrappers into $TARGET_BIN ==="

# 1. Install ai-team CLI
ln -sf "$AI_DEV_TEAM_ROOT/scripts/ai-team" "$TARGET_BIN/ai-team"
echo "[PASS] Linked ai-team -> $TARGET_BIN/ai-team"

# 2. Install flm CLI
if [ -f "$AI_DEV_TEAM_ROOT/freellmapi-agents/bin/flm" ]; then
  ln -sf "$AI_DEV_TEAM_ROOT/freellmapi-agents/bin/flm" "$TARGET_BIN/flm"
  echo "[PASS] Linked flm -> $TARGET_BIN/flm"
fi

# 3. Install flm-18 agent wrappers
if [ -d "$AI_DEV_TEAM_ROOT/freellmapi-agents/bin" ]; then
  for wrapper in "$AI_DEV_TEAM_ROOT"/freellmapi-agents/bin/flm-*; do
    if [ -x "$wrapper" ]; then
      base=$(basename "$wrapper")
      ln -sf "$wrapper" "$TARGET_BIN/$base"
    fi
  done
  echo "[PASS] Linked FreeLLMAPI agent wrappers into $TARGET_BIN"
fi

echo ""
echo "Installation complete!"
if [[ ":$PATH:" != *":$TARGET_BIN:"* ]]; then
  echo "[NOTE] Add $TARGET_BIN to your PATH in ~/.zshrc or ~/.bashrc:"
  echo "       export PATH=\"$TARGET_BIN:\$PATH\""
fi
