# Cross-Platform Dependencies Guide

## Overview
This document outlines all dependencies required for the LEARN platform across Windows, macOS, and Linux.

---

## Core Dependencies (Required)

### Python 3.8+
- **Purpose**: CLI interface and lesson management
- **Installation**:
  - **Windows**: Download from [python.org](https://www.python.org/downloads/)
  - **macOS**: `brew install python3` or download from python.org
  - **Linux**: `sudo apt install python3 python3-pip` (Debian/Ubuntu)

### Neovim 0.9+
- **Purpose**: Enhanced code editing with LSP support
- **Installation**:
  - **Windows**: `scoop install neovim` or download from [neovim.io](https://neovim.io)
  - **macOS**: `brew install neovim`
  - **Linux**: `sudo apt install neovim` or use AppImage

### Git
- **Purpose**: Version control and repository management
- **Installation**:
  - **Windows**: Download from [git-scm.com](https://git-scm.com)
  - **macOS**: `brew install git` (usually pre-installed)
  - **Linux**: `sudo apt install git`

---

## Language Runtimes (Install as needed)

### C/C++
- **Compiler**: gcc/g++ or clang
- **Windows**: MinGW-w64 or MSYS2 (`pacman -S mingw-w64-gcc`)
- **macOS**: `xcode-select --install` or `brew install gcc`
- **Linux**: `sudo apt install build-essential`

### Rust
- **Installation**: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
- **Works on**: Windows, macOS, Linux (same command)
- **Verify**: `rustc --version && cargo --version`

### Python
- Already installed for CLI (see Core Dependencies)
- **Verify**: `python3 --version`

### JavaScript/TypeScript
- **Runtime**: Node.js 18+
- **Windows**: Download from [nodejs.org](https://nodejs.org)
- **macOS**: `brew install node`
- **Linux**: `sudo apt install nodejs npm`
- **TypeScript**: `npm install -g typescript`

### Go
- **Installation**: Download from [go.dev](https://go.dev/dl/)
- **Windows**: MSI installer
- **macOS**: `brew install go`
- **Linux**: `sudo apt install golang-go`

### Java
- **JDK**: OpenJDK 17+
- **Windows**: Download from [adoptium.net](https://adoptium.net)
- **macOS**: `brew install openjdk@17`
- **Linux**: `sudo apt install openjdk-17-jdk`

### Lua
- **Installation**:
- **Windows**: Download from [luabinaries.sourceforge.net](http://luabinaries.sourceforge.net)
- **macOS**: `brew install lua`
- **Linux**: `sudo apt install lua5.4`

### PHP
- **Installation**:
- **Windows**: Download from [windows.php.net](https://windows.php.net/download/)
- **macOS**: `brew install php`
- **Linux**: `sudo apt install php-cli`

### R
- **Installation**: Download from [r-project.org](https://www.r-project.org)
- **Windows**: Install via R installer
- **macOS**: `brew install r`
- **Linux**: `sudo apt install r-base`

### Julia
- **Installation**: Download from [julialang.org](https://julialang.org/downloads/)
- **Windows**: Install via MSI
- **macOS**: `brew install julia`
- **Linux**: Download tarball or use `sudo apt install julia`

### Zig
- **Installation**: Download from [ziglang.org](https://ziglang.org/download/)
- **Windows**: Extract ZIP to PATH
- **macOS**: `brew install zig`
- **Linux**: Download tarball or `sudo snap install zig --classic`

### Kotlin
- **Installation**: Requires Java (see above)
- **Compiler**: `sdk install kotlin` (via sdkman) or download from [kotlinlang.org](https://kotlinlang.org)

### Swift
- **Installation**:
- **Windows**: Download from [swift.org](https://swift.org/download/)
- **macOS**: Pre-installed with Xcode or `xcode-select --install`
- **Linux**: Download from swift.org

### C#
- **Runtime**: .NET SDK 7+
- **Windows**: Download from [dotnet.microsoft.com](https://dotnet.microsoft.com/download)
- **macOS**: `brew install dotnet`
- **Linux**: `sudo apt install dotnet-sdk-7.0`

### Dart
- **Installation**: Download from [dart.dev](https://dart.dev/get-dart)
- **Windows**: Use Chocolatey `choco install dart-sdk`
- **macOS**: `brew install dart`
- **Linux**: `sudo apt install dart`

### PowerShell
- **Installation**: PowerShell Core 7+
- **Windows**: Pre-installed (Windows PowerShell) or download PowerShell 7
- **macOS**: `brew install powershell`
- **Linux**: `sudo apt install powershell`

### Bash/Shell
- **Windows**: Git Bash (included with Git) or WSL
- **macOS**: Pre-installed
- **Linux**: Pre-installed

### SQL
- **Database**: SQLite (lightweight, no server)
- **Windows**: Download from [sqlite.org](https://www.sqlite.org/download.html)
- **macOS**: Pre-installed or `brew install sqlite`
- **Linux**: `sudo apt install sqlite3`

### NoSQL
- **Database**: MongoDB Community Edition
- **Installation**: Follow guides at [mongodb.com](https://www.mongodb.com/try/download/community)
- **Note**: May require additional configuration

---

## Optional but Recommended

### ripgrep
- **Purpose**: Fast code searching
- **Installation**:
  - **Windows**: `scoop install ripgrep`
  - **macOS**: `brew install ripgrep`
  - **Linux**: `sudo apt install ripgrep`

### fd-find
- **Purpose**: Fast file finding
- **Installation**:
  - **Windows**: `scoop install fd`
  - **macOS**: `brew install fd`
  - **Linux**: `sudo apt install fd-find`

---

## Common Issues and Solutions

### Windows-Specific

**Issue**: Command not found after installation
- **Solution**: Add to PATH manually via System Environment Variables
- **Check**: Restart terminal after PATH changes

**Issue**: `gcc` not found
- **Solution**: Install MinGW-w64 or use MSYS2
- **Alternative**: Use WSL (Windows Subsystem for Linux)

**Issue**: Python not found
- **Solution**: Ensure "Add Python to PATH" was checked during install
- **Manual**: Add `C:\Python3X` to PATH

### macOS-Specific

**Issue**: Developer tools not installed
- **Solution**: Run `xcode-select --install`

**Issue**: Homebrew not installed
- **Solution**: Install from [brew.sh](https://brew.sh)

### Linux-Specific

**Issue**: Permission denied for installed binaries
- **Solution**: Use `sudo` or check `/usr/local/bin` permissions

**Issue**: Older package versions in apt
- **Solution**: Use PPA or download official binaries

---

## Verification Commands

Run these to verify installations:

```bash
# Core
python3 --version
nvim --version
git --version

# Languages
gcc --version
rustc --version
node --version
go version
java -version
lua -v
php --version
Rscript --version
julia --version
zig version
kotlinc -version
swift --version
dotnet --version
dart --version
pwsh --version
bash --version
sqlite3 --version
mongod --version
```

---

## Dependency Installation Script (Future)

**TODO**: Create automated installation scripts
- `install-windows.ps1`: PowerShell script for Windows
- `install-mac.sh`: Bash script for macOS (uses Homebrew)
- `install-linux.sh`: Bash script for Ubuntu/Debian

Each script should:
1. Check for existing installations
2. Prompt user for which languages to install
3. Provide progress feedback
4. Verify successful installation
5. Report any failures with troubleshooting links

---

## Maintenance Notes

- Keep this document updated when adding new languages
- Test installation procedures on all three platforms
- Document any platform-specific quirks or limitations
- Link to official documentation for complex setups
