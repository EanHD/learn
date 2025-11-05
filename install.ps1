# LEARN Platform - One-Shot Installer (Windows)
# For Linux/Mac, use: install.sh
# Installs CLI, Neovim config, and all dependencies

param(
    [switch]$Update
)

# Require administrator for Chocolatey/Scoop installation
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║         LEARN Platform - Installation Script                ║" -ForegroundColor Cyan
Write-Host "║                                                              ║" -ForegroundColor Cyan
Write-Host "║  This will install:                                          ║" -ForegroundColor Cyan
Write-Host "║  • LEARN CLI command                                         ║" -ForegroundColor Cyan
Write-Host "║  • Neovim configuration (learning mode)                      ║" -ForegroundColor Cyan
Write-Host "║  • Required dependencies                                     ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

if ($Update) {
    Write-Host "🔄 Running in UPDATE mode" -ForegroundColor Yellow
    Write-Host ""
}

# Check for Git
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git is not installed" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Git first:" -ForegroundColor Yellow
    Write-Host "  1. Download from: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "  2. Or use Chocolatey: choco install git" -ForegroundColor Yellow
    Write-Host "  3. Or use Scoop: scoop install git" -ForegroundColor Yellow
    exit 1
}

# Check for Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python first:" -ForegroundColor Yellow
    Write-Host "  1. Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "  2. Or use Chocolatey: choco install python" -ForegroundColor Yellow
    Write-Host "  3. Or use Scoop: scoop install python" -ForegroundColor Yellow
    exit 1
}

# Check for Neovim
if (-not (Get-Command nvim -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️  Neovim is not installed" -ForegroundColor Yellow
    Write-Host ""

    # Try to install with Chocolatey if available
    if (Get-Command choco -ErrorAction SilentlyContinue) {
        Write-Host "📦 Installing Neovim with Chocolatey..." -ForegroundColor Cyan
        if (-not $isAdmin) {
            Write-Host "❌ Administrator privileges required to install Neovim" -ForegroundColor Red
            Write-Host "   Please run PowerShell as Administrator" -ForegroundColor Yellow
            exit 1
        }
        choco install neovim -y
    }
    # Try Scoop
    elseif (Get-Command scoop -ErrorAction SilentlyContinue) {
        Write-Host "📦 Installing Neovim with Scoop..." -ForegroundColor Cyan
        scoop install neovim
    }
    else {
        Write-Host "Please install Neovim manually:" -ForegroundColor Yellow
        Write-Host "  1. Download from: https://github.com/neovim/neovim/releases" -ForegroundColor Yellow
        Write-Host "  2. Or install Chocolatey: https://chocolatey.org/install" -ForegroundColor Yellow
        Write-Host "  3. Or install Scoop: https://scoop.sh" -ForegroundColor Yellow
        exit 1
    }
}

Write-Host "✅ Core dependencies found" -ForegroundColor Green
Write-Host ""

# Install optional dependencies (ripgrep, fd)
Write-Host "📦 Installing optional dependencies..." -ForegroundColor Cyan
if (Get-Command choco -ErrorAction SilentlyContinue) {
    if ($isAdmin) {
        choco install ripgrep fd -y 2>$null
    } else {
        Write-Host "⚠️  Skipping ripgrep/fd (requires admin)" -ForegroundColor Yellow
    }
} elseif (Get-Command scoop -ErrorAction SilentlyContinue) {
    scoop install ripgrep fd 2>$null
}

# Clone or update repository
$learnDir = Join-Path $env:USERPROFILE "LEARN"
if (Test-Path $learnDir) {
    if ($Update) {
        Write-Host "🔄 Updating LEARN repository..." -ForegroundColor Cyan
        Set-Location $learnDir
        git pull
        Write-Host "✅ Repository updated" -ForegroundColor Green
    } else {
        Write-Host "📁 LEARN directory exists" -ForegroundColor Yellow
        Write-Host "   Run with -Update to pull latest changes" -ForegroundColor Yellow
        Set-Location $learnDir
    }
} else {
    Write-Host "📥 Cloning LEARN repository..." -ForegroundColor Cyan
    git clone https://github.com/EanHD/learn.git $learnDir
    Set-Location $learnDir
    Write-Host "✅ Repository cloned" -ForegroundColor Green
}

Write-Host ""

# Install CLI
Write-Host "🔧 Installing LEARN CLI..." -ForegroundColor Cyan

# Create CLI wrapper script for Windows
$cliPath = Join-Path $learnDir "CLI\learn_cli.py"
$binDir = Join-Path $env:USERPROFILE ".local\bin"
$learnCmd = Join-Path $binDir "learn.bat"

# Create .local/bin if it doesn't exist
if (-not (Test-Path $binDir)) {
    New-Item -ItemType Directory -Path $binDir -Force | Out-Null
}

# Create batch wrapper
$batchContent = @"
@echo off
python "$cliPath" %*
"@
Set-Content -Path $learnCmd -Value $batchContent

# Add to PATH if not already there
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$binDir*") {
    Write-Host "📝 Adding to PATH..." -ForegroundColor Cyan
    [Environment]::SetEnvironmentVariable("Path", "$userPath;$binDir", "User")
    $env:Path += ";$binDir"
    Write-Host "✅ Added to PATH (restart terminal to apply)" -ForegroundColor Green
}

Write-Host "✅ CLI installed" -ForegroundColor Green
Write-Host ""

# Setup Neovim configuration
Write-Host "🎨 Setting up Neovim configuration..." -ForegroundColor Cyan
$nvimConfig = Join-Path $env:LOCALAPPDATA "nvim"

# Backup existing config if present
if (Test-Path $nvimConfig) {
    $backupName = "nvim.backup." + (Get-Date -Format "yyyyMMdd_HHmmss")
    $backupPath = Join-Path $env:LOCALAPPDATA $backupName
    Write-Host "⚠️  Existing Neovim config found, backing up..." -ForegroundColor Yellow
    Move-Item $nvimConfig $backupPath
}

# Create config directory
New-Item -ItemType Directory -Path $nvimConfig -Force | Out-Null

# Copy learning config
$initLua = Join-Path $learnDir "MODE_VIM\CONFIG\init-learning.lua"
$destInit = Join-Path $nvimConfig "init.lua"
Copy-Item $initLua $destInit

Write-Host "✅ Neovim configured" -ForegroundColor Green
Write-Host ""

# Setup VS Code configuration
Write-Host "🎨 Setting up VS Code configuration..." -ForegroundColor Cyan

if (Get-Command code -ErrorAction SilentlyContinue) {
    Write-Host "📝 Installing VS Code extensions..." -ForegroundColor Cyan

    # Core extension for Vim motions
    code --install-extension vscodevim.vim --force | Out-Null

    # Language support extensions
    code --install-extension ms-vscode.cpptools --force | Out-Null
    code --install-extension rust-lang.rust-analyzer --force | Out-Null
    code --install-extension ms-python.python --force | Out-Null
    code --install-extension golang.go --force | Out-Null
    code --install-extension yzhang.markdown-all-in-one --force | Out-Null
    code --install-extension eamodio.gitlens --force | Out-Null
    code --install-extension streetsidesoftware.code-spell-checker --force | Out-Null
    code --install-extension ms-vscode.makefile-tools --force | Out-Null

    # Theme extension
    code --install-extension edeneast.nightfox --force | Out-Null

    Write-Host "✅ VS Code extensions installed" -ForegroundColor Green

    # Copy VS Code settings
    $vscodeConfig = Join-Path $env:APPDATA "Code\User"
    if (-not (Test-Path $vscodeConfig)) {
        New-Item -ItemType Directory -Path $vscodeConfig -Force | Out-Null
    }

    # Note: VS Code settings are automatically synced from workspace .vscode/settings.json
    Write-Host "💡 VS Code will use .vscode/settings.json from the LEARN directory" -ForegroundColor Cyan
} else {
    Write-Host "⚠️  VS Code not found" -ForegroundColor Yellow
    Write-Host "   Download from: https://code.visualstudio.com" -ForegroundColor Yellow
}

Write-Host ""

# Install Python dependencies for CLI
Write-Host "🐍 Installing Python dependencies..." -ForegroundColor Cyan
python -m pip install --user rich --quiet

Write-Host "✅ Python dependencies installed" -ForegroundColor Green
Write-Host ""

# Test installation
Write-Host "🧪 Testing installation..." -ForegroundColor Cyan

# Refresh environment variables
$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

if (Get-Command learn -ErrorAction SilentlyContinue) {
    Write-Host "✅ LEARN CLI is available" -ForegroundColor Green
} else {
    Write-Host "⚠️  LEARN CLI not found in PATH" -ForegroundColor Yellow
    Write-Host "   Please restart your terminal" -ForegroundColor Yellow
}

if (Get-Command nvim -ErrorAction SilentlyContinue) {
    $nvimVersion = (nvim --version | Select-Object -First 1)
    Write-Host "✅ Neovim is available: $nvimVersion" -ForegroundColor Green
} else {
    Write-Host "❌ Neovim not found" -ForegroundColor Red
}

if (Get-Command code -ErrorAction SilentlyContinue) {
    $codeVersion = (code --version | Select-Object -First 1)
    Write-Host "✅ VS Code is available: $codeVersion" -ForegroundColor Green
} else {
    Write-Host "⚠️  VS Code not found (optional)" -ForegroundColor Yellow
}

Write-Host ""

if ($Update) {
    Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║                   🎉 Update Complete!                       ║" -ForegroundColor Cyan
    Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "✨ What's New:" -ForegroundColor Yellow
    Write-Host "   • Check CHANGELOG.md for latest updates" -ForegroundColor White
    Write-Host "   • New lessons and improvements" -ForegroundColor White
    Write-Host ""
    Write-Host "🔄 To update again later, run:" -ForegroundColor Yellow
    Write-Host "   powershell -File ~\LEARN\install.ps1 -Update" -ForegroundColor White
} else {
    Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║                   🎉 Installation Complete!                 ║" -ForegroundColor Cyan
    Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🚀 Quick Start:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   1. Restart your terminal (PowerShell/CMD)" -ForegroundColor White
    Write-Host "   2. Type: learn" -ForegroundColor White
    Write-Host "   3. Select a language and start learning!" -ForegroundColor White
    Write-Host ""
    Write-Host "📖 Documentation:" -ForegroundColor Yellow
    Write-Host "   • README: $learnDir\README.md" -ForegroundColor White
    Write-Host "   • Features: $learnDir\FEATURES.md" -ForegroundColor White
    Write-Host "   • Vim Guide: $learnDir\MODE_VIM\README.md" -ForegroundColor White
    Write-Host "   • VS Code Guide: $learnDir\MODE_VSCODE\README.md" -ForegroundColor White
    Write-Host ""
    Write-Host "💡 Vim Tips:" -ForegroundColor Yellow
    Write-Host "   • Press <Space> in Neovim to see all commands" -ForegroundColor White
    Write-Host "   • Press <Space>h for essential shortcuts" -ForegroundColor White
    Write-Host "   • Press <Space>g for quick navigation guide" -ForegroundColor White
    Write-Host ""
    Write-Host "💡 VS Code Tips (if installed):" -ForegroundColor Yellow
    Write-Host "   • Press Ctrl+Shift+T to run lesson" -ForegroundColor White
    Write-Host "   • Press Ctrl+H/J/K/L for window navigation (Vim-style)" -ForegroundColor White
    Write-Host "   • Press <Space> as leader key for commands" -ForegroundColor White
    Write-Host ""
    Write-Host "🔄 To update later, run:" -ForegroundColor Yellow
    Write-Host "   powershell -File ~\LEARN\install.ps1 -Update" -ForegroundColor White
}

Write-Host ""
Write-Host "Happy Learning! 🎓" -ForegroundColor Green
