# Windows Setup Guide

**Complete guide to setting up LEARN on Windows, including all prerequisites.**

---

## 🎯 Prerequisites

Before installing LEARN, you need several tools. We'll walk through installing everything step-by-step.

### Option 1: Using Chocolatey (Recommended)

**Chocolatey** is a package manager for Windows that makes installation super easy.

#### Step 1: Install Chocolatey

1. **Open PowerShell as Administrator**
   - Press `Win + X`
   - Select "Windows PowerShell (Admin)" or "Terminal (Admin)"

2. **Run this command:**
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

3. **Verify installation:**
   ```powershell
   choco --version
   ```

#### Step 2: Install Required Tools with Chocolatey

**Still in PowerShell as Administrator**, run:

```powershell
# Essential tools
choco install git -y
choco install neovim -y
choco install python -y

# Build tools (required for telescope-fzf-native)
choco install cmake -y
choco install mingw -y

# Optional but recommended compilers
choco install nodejs -y
choco install rust -y
choco install golang -y
```

**Close and reopen PowerShell** after installation to refresh your PATH.

#### Step 3: Verify Everything is Installed

```powershell
# Check each tool
git --version
nvim --version
python --version
cmake --version
gcc --version
```

All commands should return version numbers without errors.

---

### Option 2: Manual Installation

If you prefer not to use Chocolatey, install each tool manually:

1. **Git**: Download from [git-scm.com](https://git-scm.com/download/win)
2. **Neovim**: Download from [neovim.io](https://neovim.io) (get the Windows installer)
3. **Python**: Download from [python.org](https://www.python.org/downloads/)
4. **CMake**: Download from [cmake.org](https://cmake.org/download/)
5. **MinGW**: Download from [mingw-w64.org](https://www.mingw-w64.org/downloads/)

**Important:** Check "Add to PATH" during each installation!

---

## 🚀 Install LEARN

Once prerequisites are installed, open **PowerShell** (doesn't need Admin) and run:

```powershell
# One-line install
irm https://raw.githubusercontent.com/EanHD/learn/main/install.ps1 | iex
```

Or download and run manually:

```powershell
# Clone repository
cd ~
git clone https://github.com/EanHD/learn.git LEARN
cd LEARN

# Run installer
powershell -File install.ps1
```

---

## 🔧 Post-Installation Setup

### Build Telescope FZF Native

The first time you open Neovim with LEARN, the `telescope-fzf-native` plugin needs to compile. This happens automatically, but you need:

1. **CMake** - Already installed if you followed Chocolatey steps
2. **C Compiler (MinGW)** - Already installed if you followed Chocolatey steps

**To verify it's working:**

```powershell
# Launch LEARN
learn

# Or open a specific lesson
learn open python 1 1
```

If you see the error: `cannot load module 'libfzf.dll'`, do this:

```powershell
# Navigate to Neovim data directory
cd $env:LOCALAPPDATA\nvim-data\lazy\telescope-fzf-native.nvim

# Remove the plugin
cd ..
Remove-Item -Recurse -Force telescope-fzf-native.nvim

# Reopen Neovim - it will rebuild automatically
nvim
```

---

## 🛠️ Troubleshooting

### "Command not found: learn"

**Close and reopen PowerShell** - the PATH needs to refresh.

If still not working:
```powershell
# Check if LEARN is in PATH
$env:Path -split ';' | Select-String "LEARN"

# If missing, add it manually
$env:Path += ";$HOME\LEARN"
```

To make it permanent:
```powershell
[System.Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::User)
```

---

### "nvim: command not found"

Neovim isn't in your PATH.

**Solution:**
```powershell
# If installed with Chocolatey
refreshenv

# If installed manually, add to PATH:
$nvimPath = "C:\Program Files\Neovim\bin"
$env:Path += ";$nvimPath"
[System.Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::User)
```

---

### "cannot load module 'libfzf.dll'"

This means telescope-fzf-native didn't compile.

**Requirements:**
- CMake must be installed
- A C compiler (MinGW) must be installed

**Solution:**
```powershell
# Install missing tools
choco install cmake mingw -y

# Remove the broken plugin
Remove-Item -Recurse -Force $env:LOCALAPPDATA\nvim-data\lazy\telescope-fzf-native.nvim

# Reopen Neovim to trigger rebuild
nvim
```

---

### "Python not found"

```powershell
# Install Python
choco install python -y

# Or download from python.org
# Make sure to check "Add to PATH" during installation
```

---

### "Git not found"

```powershell
# Install Git
choco install git -y

# Or download from git-scm.com
```

---

### Plugins not loading

```powershell
# Open Neovim
nvim

# Inside Neovim, run:
:Lazy sync
:Mason update

# Restart Neovim
```

---

## 🎮 Using LEARN on Windows

Everything works exactly the same as Linux/Mac:

```powershell
# Interactive menu
learn

# Open a lesson
learn open python 1 1

# Check progress
learn progress

# Run code
learn run python 1 1
```

### Terminal Integration

**PowerShell** is the recommended terminal on Windows. You can also use:
- **Windows Terminal** (best experience)
- **Git Bash**
- **WSL2** (if you prefer Linux environment)

---

## 🔍 Check Your Setup

Run the doctor command to verify everything:

```powershell
learn doctor
```

This checks for:
- ✅ Git
- ✅ Neovim
- ✅ Python
- ✅ Compilers
- ✅ LSP servers
- ✅ Build tools

---

## 💡 Pro Tips for Windows Users

### Use Windows Terminal

**Windows Terminal** gives you a better experience:

```powershell
choco install microsoft-windows-terminal -y
```

Features:
- Multiple tabs
- Better fonts
- GPU acceleration
- Customizable themes

### Enable Developer Mode

1. Open **Settings**
2. Go to **Update & Security** → **For Developers**
3. Enable **Developer Mode**

This speeds up some operations and enables symbolic links.

### Use PowerShell 7

The newer PowerShell is faster:

```powershell
choco install powershell-core -y
```

---

## 📚 Next Steps

Once installed, start learning:

```powershell
# Launch interactive menu
learn

# Or browse categories
learn browse

# Or jump right in
learn open python 1 1
```

Press `<Space>h` in Neovim for help anytime!

---

## 🆘 Still Having Issues?

1. **Read the FAQ**: See `MODE_VIM/FAQ.md`
2. **Check main docs**: See `README.md`
3. **Run diagnostics**: `learn doctor`
4. **File an issue**: Include output from `learn doctor`

---

**Happy Learning on Windows! 🎓**
