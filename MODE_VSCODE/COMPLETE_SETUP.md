# VS CODE MODE: Complete Setup & Configuration Guide

Comprehensive guide for setting up the perfect learning environment in VS Code.

---

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Workspace Layout](#workspace-layout)
4. [Customization](#customization)
5. [Troubleshooting](#troubleshooting)

---

## Installation

### Prerequisites

Ensure you have these installed:

```bash
# Check VS Code
code --version

# Check compilers (install what you need)
gcc --version        # C/C++
rustc --version      # Rust
python3 --version    # Python
dart --version       # Dart
go version          # Go
```

### Step 1: Install VS Code Extensions

#### Required Extension

```bash
# Install Vim extension
code --install-extension vscodevim.vim
```

#### Recommended Extensions

```bash
# Language support
code --install-extension ms-vscode.cpptools
code --install-extension rust-lang.rust-analyzer
code --install-extension ms-python.python
code --install-extension golang.go
code --install-extension dart-code.dart-code

# Productivity
code --install-extension yzhang.markdown-all-in-one
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension eamodio.gitlens
code --install-extension pkief.material-icon-theme
```

#### Install All at Once

```bash
code --install-extension vscodevim.vim \
     --install-extension ms-vscode.cpptools \
     --install-extension rust-lang.rust-analyzer \
     --install-extension ms-python.python \
     --install-extension yzhang.markdown-all-in-one \
     --install-extension streetsidesoftware.code-spell-checker
```

### Step 2: Reload VS Code

After installing extensions:

```
Ctrl+Shift+P → "Developer: Reload Window"
```

Or simply restart VS Code.

---

## Configuration

All configuration is in the `.vscode/` directory of the LEARN workspace.

### Configuration Files

```
LEARN/
├── .vscode/
│   ├── settings.json      # Workspace settings
│   ├── keybindings.json   # Custom keybindings
│   ├── extensions.json    # Recommended extensions
│   └── tasks.json         # Build/run tasks
└── MODE_VSCODE/
    └── CONFIG/
        ├── settings.json      # Template settings
        ├── keybindings.json   # Template keybindings
        └── extensions.json    # Extension recommendations
```

### Automatic Configuration

When you open the LEARN folder in VS Code:

1. **Settings load automatically** from `.vscode/settings.json`
2. **Extensions are recommended** (you'll see a notification)
3. **Keybindings work** immediately after Vim extension is installed
4. **Lesson files become read-only**

No manual setup needed! ✨

---

## Workspace Layout

### Recommended Setup for Learning

#### Layout 1: Side-by-Side (Most Common)

```
╔════════════════════╦════════════════════╗
║                    ║                    ║
║   lesson.md        ║   main.dart        ║
║   (left pane)      ║   (right pane)     ║
║                    ║                    ║
║   Read-only        ║   Editable         ║
║   Markdown         ║   Code             ║
║                    ║                    ║
╠════════════════════╩════════════════════╣
║  Terminal (bash)                        ║
║  $ dart run                             ║
╚═════════════════════════════════════════╝
```

**How to set up:**

1. Open `lesson.md`
2. Press `Ctrl+\` to split
3. Open code file in right pane
4. Press `Ctrl+Shift+T` for terminal
5. Press `Ctrl+=` to equalize widths

#### Layout 2: Markdown Preview

```
╔════════════════════╦════════════════════╗
║                    ║                    ║
║   lesson.md        ║   lesson.md        ║
║   (source)         ║   (preview)        ║
║                    ║                    ║
╠════════════════════╬════════════════════╣
║                    ║                    ║
║   main.cpp         ║   Terminal         ║
║                    ║                    ║
╚════════════════════╩════════════════════╝
```

**How to set up:**

1. Open `lesson.md`
2. Press `Ctrl+Shift+V` for preview
3. Press `Ctrl+\` to split bottom
4. Open code file in bottom left
5. Press `Ctrl+Shift+T` for terminal (bottom right)

#### Layout 3: Zen Mode (Focus)

```
╔═════════════════════════════════════════╗
║                                         ║
║                                         ║
║           main.rs                       ║
║                                         ║
║   (Fullscreen, no distractions)         ║
║                                         ║
║                                         ║
╚═════════════════════════════════════════╝
```

**How to activate:**

- Press `Ctrl+Shift+Z` or `<Space>z`
- Press `Esc Esc` to exit

---

## Customization

### Change Theme

```
Ctrl+K Ctrl+T → Select theme
```

Recommended themes:
- **Default Dark+** (built-in)
- **Tokyo Night** (install extension)
- **One Dark Pro** (install extension)
- **Dracula** (install extension)

### Change Font

Edit `.vscode/settings.json`:

```json
{
  "editor.fontFamily": "'Fira Code', 'Consolas', monospace",
  "editor.fontSize": 16,
  "editor.lineHeight": 1.8,
  "editor.fontLigatures": true
}
```

Popular coding fonts:
- JetBrains Mono (current default)
- Fira Code
- Cascadia Code
- Source Code Pro
- Hack

### Change Leader Key

Default is `<Space>`. To change to comma:

```json
{
  "vim.leader": ","
}
```

### Enable System Clipboard

Already enabled! Copy/paste between Vim and system:

```json
{
  "vim.useSystemClipboard": true
}
```

### Adjust Vim Behavior

Edit `.vscode/settings.json`:

```json
{
  "vim.hlsearch": true,              // Highlight search
  "vim.incsearch": true,             // Incremental search
  "vim.smartcase": true,             // Smart case search
  "vim.ignorecase": true,            // Ignore case in search
  "vim.easymotion": true,            // Enable easymotion
  "vim.sneak": true,                 // Enable sneak
  "vim.surround": true,              // Enable surround
  "vim.commentary": true             // Enable commentary
}
```

### Customize Terminal

```json
{
  "terminal.integrated.fontSize": 14,
  "terminal.integrated.fontFamily": "'JetBrains Mono'",
  "terminal.integrated.cursorStyle": "line",
  "terminal.integrated.cursorBlinking": true,
  "terminal.integrated.defaultProfile.linux": "bash"
}
```

### Show/Hide UI Elements

```json
{
  // Activity bar (left sidebar icons)
  "workbench.activityBar.location": "default",  // or "hidden"

  // Status bar (bottom)
  "workbench.statusBar.visible": true,          // or false

  // Minimap
  "editor.minimap.enabled": false,              // or true

  // Breadcrumbs (file path at top)
  "breadcrumbs.enabled": true,                  // or false

  // Editor tabs
  "workbench.editor.showTabs": "multiple"       // or "single", "none"
}
```

### Customize Keybindings

Edit `.vscode/keybindings.json` or use `Ctrl+K Ctrl+S`.

Example custom binding:

```json
[
  {
    "key": "ctrl+shift+r",
    "command": "workbench.action.tasks.runTask",
    "args": "Rust: Run"
  }
]
```

---

## Advanced Features

### Vim Plugins (via VS Code Vim)

The Vim extension includes these features:

- **Surround** - Change surrounding quotes/brackets
  - `cs"'` - Change surrounding `"` to `'`
  - `ds"` - Delete surrounding `"`
  - `ysiw"` - Surround word with `"`

- **Commentary** - Smart commenting
  - `gcc` - Toggle line comment
  - `gc` in Visual mode - Comment selection

- **EasyMotion** - Jump anywhere quickly
  - `<leader><leader>w` - Jump to word
  - `<leader><leader>f{char}` - Jump to character

Enable these in settings:

```json
{
  "vim.surround": true,
  "vim.commentary": true,
  "vim.easymotion": true
}
```

### Language Server Features

Each language extension provides:

1. **Auto-completion** - `Ctrl+Space`
2. **Go to Definition** - `gd` or `F12`
3. **Find References** - `gr` or `Shift+F12`
4. **Hover Documentation** - `K`
5. **Rename Symbol** - `F2`
6. **Format Document** - `Shift+Alt+F`
7. **Code Actions** - `Ctrl+.`

### Tasks (Build & Run)

The workspace includes tasks in `.vscode/tasks.json`:

- **C++: Compile** - `Ctrl+Shift+B`
- **C++: Run** - `Ctrl+Shift+R`
- **Rust: Run**
- **Python: Run**

Run any task:
```
Ctrl+Shift+P → "Tasks: Run Task" → Select task
```

### Snippets

Create custom snippets:

```
Ctrl+Shift+P → "Preferences: Configure User Snippets"
```

Example for C++:

```json
{
  "Hello World": {
    "prefix": "hello",
    "body": [
      "#include <iostream>",
      "",
      "int main() {",
      "    std::cout << \"Hello, World!\" << std::endl;",
      "    return 0;",
      "}"
    ]
  }
}
```

---

## Troubleshooting

### Vim Extension Issues

#### Problem: Vim mode indicator not showing

**Solution:**
```bash
code --install-extension vscodevim.vim
# Then: Ctrl+Shift+P → "Reload Window"
```

#### Problem: Keybindings not working

**Solution:** Check if Vim is enabled:
- Bottom-right corner should show "NORMAL", "INSERT", etc.
- If not, press `Ctrl+Shift+P` → "Toggle Vim Mode"

#### Problem: Vim is too slow

**Solution:** Disable expensive features:

```json
{
  "vim.highlightedyank.enable": false,
  "vim.neovimPath": "",  // Don't use neovim integration
  "extensions.experimental.affinity": {
    "vscodevim.vim": 1
  }
}
```

### Settings Not Applied

#### Problem: Workspace settings not working

**Solution:**
1. Make sure you opened the LEARN **folder**, not individual files
2. Check: `File → Open Folder` → Select `LEARN` directory
3. Bottom-left should show "LEARN" workspace name

### Language Server Issues

#### Problem: No auto-completion

**Solution:**
1. Install language extension
2. Reload window: `Ctrl+Shift+P` → "Reload Window"
3. Check bottom-right for errors
4. Try opening a file of that language

#### Problem: C++ IntelliSense not working

**Solution:**
1. Install C++ extension: `code --install-extension ms-vscode.cpptools`
2. Create or update `c_cpp_properties.json`
3. Reload window

### Terminal Issues

#### Problem: Terminal won't open

**Solution:**
- Press `Ctrl+Shift+T` or `<Space>t`
- Or: `View → Terminal` from menu
- Check shell is installed: `echo $SHELL`

#### Problem: Terminal output garbled

**Solution:**
```json
{
  "terminal.integrated.gpuAcceleration": "off"
}
```

### Performance Issues

#### Problem: VS Code is slow

**Solution:**

1. Disable unused extensions
2. Reduce watcher files:

```json
{
  "files.watcherExclude": {
    "**/.git/objects/**": true,
    "**/node_modules/**": true,
    "**/target/**": true,
    "**/__pycache__/**": true
  }
}
```

3. Disable telemetry:

```json
{
  "telemetry.telemetryLevel": "off"
}
```

---

## Maintenance

### Update Extensions

```bash
# Update all extensions
code --update-extensions

# Or in VS Code
Ctrl+Shift+X → Click ⋯ → "Update All Extensions"
```

### Backup Settings

Your settings are in `.vscode/` - they're automatically backed up with the workspace!

To backup user settings:

```bash
cp ~/.config/Code/User/settings.json ~/settings-backup.json
cp ~/.config/Code/User/keybindings.json ~/keybindings-backup.json
```

### Reset to Defaults

To reset workspace settings:

```bash
cd ~/LEARN
rm .vscode/settings.json
# Then copy from MODE_VSCODE/CONFIG/settings.json
cp MODE_VSCODE/CONFIG/settings.json .vscode/
```

---

## Learning Resources

### Vim

- [../VIM_CHEATSHEET.md](../VIM_CHEATSHEET.md) - Basic Vim reference
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - All commands
- [vimtutor](http://www2.geog.ucl.ac.uk/~plewis/teaching/unix/vimtutor) - Interactive tutorial

### VS Code

- [Official Docs](https://code.visualstudio.com/docs)
- [Keyboard Shortcuts PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
- [Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

### This Project

- [README.md](README.md) - Main VS Code Mode docs
- [QUICK_START.md](QUICK_START.md) - Fast setup guide
- [../README.md](../README.md) - Project overview

---

## Support

### Getting Help

1. Check this guide first
2. Read [README.md](README.md)
3. Search VS Code docs
4. Check Vim extension docs

### Reporting Issues

If you find issues with the LEARN workspace configuration:

1. Describe the problem
2. Include VS Code version: `code --version`
3. Include Vim extension version
4. Share error messages

---

**You're all set! Happy learning! 🚀**
