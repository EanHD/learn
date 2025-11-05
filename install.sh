#!/bin/bash

# LEARN Platform - One-Shot Installer (Linux/Mac)
# For Windows, use: install.ps1
# Installs CLI, Neovim config, and all dependencies

set -e

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║         LEARN Platform - Installation Script                ║"
echo "║                                                              ║"
echo "║  This will install:                                          ║"
echo "║  • LEARN CLI command                                         ║"
echo "║  • Neovim configuration (learning mode)                      ║"
echo "║  • Required dependencies                                     ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Parse arguments
UPDATE_MODE=false
if [ "$1" == "--update" ] || [ "$1" == "-u" ]; then
    UPDATE_MODE=true
    echo "🔄 Running in UPDATE mode"
    echo ""
fi

# Check if running with sudo
if [ "$EUID" -eq 0 ]; then
   echo "⚠️  Please do not run this script with sudo"
   echo "   It will prompt for sudo when needed"
   exit 1
fi

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="mac"
else
    echo "❌ Unsupported OS: $OSTYPE"
    exit 1
fi

echo "🔍 Detected OS: $OS"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
if [ "$OS" == "linux" ]; then
    # Check if apt is available
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip git curl neovim ripgrep fd-find
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3 python3-pip git curl neovim ripgrep fd-find
    elif command -v pacman &> /dev/null; then
        sudo pacman -S --noconfirm python python-pip git curl neovim ripgrep fd
    else
        echo "❌ Unsupported package manager. Please install manually:"
        echo "   python3, python3-pip, git, curl, neovim, ripgrep, fd-find"
        exit 1
    fi
elif [ "$OS" == "mac" ]; then
    # Install Homebrew if not present
    if ! command -v brew &> /dev/null; then
        echo "📥 Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install python git neovim ripgrep fd
fi

echo "✅ Dependencies installed"
echo ""

# Clone or update repository
LEARN_DIR="$HOME/LEARN"
if [ -d "$LEARN_DIR" ]; then
    if [ "$UPDATE_MODE" = true ]; then
        echo "� Updating LEARN repository..."
        cd "$LEARN_DIR"
        git pull
        echo "✅ Repository updated"
    else
        echo "�📁 LEARN directory exists"
        echo "   Run with --update to pull latest changes"
        cd "$LEARN_DIR"
    fi
else
    echo "📥 Cloning LEARN repository..."
    git clone https://github.com/EanHD/learn.git "$LEARN_DIR"
    cd "$LEARN_DIR"
    echo "✅ Repository cloned"
fi

echo ""

# Install CLI
echo "🔧 Installing LEARN CLI..."
chmod +x CLI/install.sh
bash CLI/install.sh

echo "✅ CLI installed"
echo ""

# Setup Neovim configuration
echo "🎨 Setting up Neovim configuration..."
NVIM_CONFIG="$HOME/.config/nvim"
mkdir -p "$NVIM_CONFIG"

# Backup existing config if present
if [ -f "$NVIM_CONFIG/init.lua" ] || [ -f "$NVIM_CONFIG/init.vim" ]; then
    echo "⚠️  Existing Neovim config found, backing up..."
    mv "$NVIM_CONFIG" "$NVIM_CONFIG.backup.$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$NVIM_CONFIG"
fi

# Copy learning config
cp MODE_VIM/CONFIG/init-learning.lua "$NVIM_CONFIG/init.lua"

echo "✅ Neovim configured"
echo ""

# Setup VS Code configuration (if VS Code is installed)
echo "🎨 Checking for VS Code..."
if command -v code &> /dev/null; then
    echo "📝 Installing VS Code extensions..."
    code --install-extension vscodevim.vim 2>/dev/null || true
    code --install-extension ms-vscode.cpptools 2>/dev/null || true
    code --install-extension rust-lang.rust-analyzer 2>/dev/null || true
    code --install-extension ms-python.python 2>/dev/null || true
    code --install-extension yzhang.markdown-all-in-one 2>/dev/null || true
    code --install-extension streetsidesoftware.code-spell-checker 2>/dev/null || true
    code --install-extension eamodio.gitlens 2>/dev/null || true
    echo "✅ VS Code extensions installed"
else
    echo "⚠️  VS Code not found (optional)"
    echo "   To install VS Code: https://code.visualstudio.com/"
    echo "   Then run: code --install-extension vscodevim.vim"
fi
echo ""

# Install Python dependencies for CLI
echo "🐍 Installing Python dependencies..."
pip3 install --user rich

echo "✅ Python dependencies installed"
echo ""

# Test installation
echo "🧪 Testing installation..."
if command -v learn &> /dev/null; then
    echo "✅ LEARN CLI is available"
else
    echo "⚠️  LEARN CLI not found in PATH"
    echo "   You may need to restart your terminal or add to PATH:"
    echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
fi

# Check Neovim
if command -v nvim &> /dev/null; then
    NVIM_VERSION=$(nvim --version | head -n1)
    echo "✅ Neovim is available: $NVIM_VERSION"
else
    echo "❌ Neovim not found"
fi

echo ""
if [ "$UPDATE_MODE" = true ]; then
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                   🎉 Update Complete!                       ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "✨ What's New:"
    echo "   • Check CHANGELOG.md for latest updates"
    echo "   • New lessons and improvements"
    echo ""
    echo "🔄 To update again later, run:"
    echo "   bash ~/LEARN/install.sh --update"
else
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                   🎉 Installation Complete!                 ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "🚀 Quick Start:"
    echo ""
    echo "   1. Restart your terminal (or run: source ~/.bashrc)"
    echo "   2. Type: learn"
    echo "   3. Select a language and start learning!"
    echo ""
    echo "📖 Documentation:"
    echo "   • README: $LEARN_DIR/README.md"
    echo "   • Features: $LEARN_DIR/FEATURES.md"
    echo "   • Vim Guide: $LEARN_DIR/MODE_VIM/README.md"
    echo "   • VS Code Guide: $LEARN_DIR/MODE_VSCODE/README.md"
    echo ""
    echo "💡 Tips:"
    echo "   • Press <Space> in Neovim to see all commands"
    echo "   • Press <Space>h for essential shortcuts"
    echo "   • Press <Space>g for quick navigation guide"
    echo "   • For VS Code: Ctrl+Shift+X to install recommended extensions"
    echo ""
    echo "🔄 To update later, run:"
    echo "   bash ~/LEARN/install.sh --update"
fi
echo ""
echo "Happy Learning! 🎓"
