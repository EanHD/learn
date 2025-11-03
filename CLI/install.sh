#!/bin/bash
# Installation script for Learn CLI

set -euo pipefail

echo "=================================================="
echo "  Learn CLI - Installation"
echo "=================================================="
echo ""

LEARN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLI_DIR="$LEARN_DIR/CLI"

echo "Learn directory: $LEARN_DIR"
echo "CLI directory: $CLI_DIR"
echo ""

echo "Making CLI scripts executable..."
chmod +x "$CLI_DIR/learn" 2>/dev/null || true
chmod +x "$CLI_DIR/learn_cli.py" 2>/dev/null || true
echo "Scripts are now executable"
echo ""

# Robust shell rc detection
detect_shell_rc() {
  if [ -n "${ZDOTDIR:-}" ] && [ -f "$ZDOTDIR/.zshrc" ]; then
    echo "$ZDOTDIR/.zshrc"
  elif [ -f "$HOME/.zshrc" ]; then
    echo "$HOME/.zshrc"
  elif [ -f "$HOME/.bashrc" ]; then
    echo "$HOME/.bashrc"
  elif [ -f "$HOME/.profile" ]; then
    echo "$HOME/.profile"
  else
    echo "$HOME/.bashrc"
  fi
}

SHELL_CONFIG="$(detect_shell_rc)"
ADDED_PATH=0

# Add CLI to PATH if missing (idempotent)
if ! echo ":$PATH:" | grep -q ":$CLI_DIR:"; then
  echo "Adding CLI to PATH in $SHELL_CONFIG"
  {
    echo ""
    echo "# Learn CLI"
    echo "export PATH=\"\$PATH:$CLI_DIR\""
  } >> "$SHELL_CONFIG"
  ADDED_PATH=1
else
  echo "CLI directory already in PATH"
fi

# Dependency checks
echo ""
echo "Checking for required tools..."
command -v nvim >/dev/null 2>&1 && echo "Neovim: OK" || echo "Neovim: MISSING (install: sudo apt install neovim)"
command -v code >/dev/null 2>&1 && echo "VS Code: OK" || echo "VS Code: not found (optional)"
command -v less >/dev/null 2>&1 && echo "less: OK" || echo "less: MISSING (install: sudo apt install less)"

echo ""
echo "=================================================="
echo "  Installation Complete"
echo "=================================================="
echo ""
echo "Next steps:"
if [ "$ADDED_PATH" -eq 1 ]; then
  echo "  1) Reload your shell:  source \"$SHELL_CONFIG\""
  echo "  2) Run setup wizard:   learn init"
  echo "  3) Start a lesson:     learn c++ 1"
else
  echo "  1) Run setup wizard:   learn init"
  echo "  2) Start a lesson:     learn c++ 1"
fi
echo ""
echo "Quick commands:"
echo "  learn                   # Interactive mode"
echo "  learn init              # First-time setup wizard"
echo "  learn doctor            # Verify system setup"
echo "  learn c++ 1             # Open first C++ lesson"
echo "  learn --help            # Show all options"
echo ""
