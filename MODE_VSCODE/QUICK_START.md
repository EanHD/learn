# VS CODE MODE: Quick Start Guide

Get up and running with VS Code + Vim in under 5 minutes!

---

## Prerequisites

- ✅ VS Code installed (or install via the setup script - see below)
- ✅ A compiler for your language (gcc, rustc, python3, etc.)

**Windows users:** The PowerShell installer (`install.ps1`) automatically installs VS Code extensions!

---

## Step 1: Install Vim Extension (2 minutes)

### Option A: From VS Code

1. Press `Ctrl+Shift+X`
2. Search for "Vim"
3. Install "Vim" by vscodevim
4. Press `Ctrl+Shift+P` → Type "Reload Window"

### Option B: Command Line

```bash
code --install-extension vscodevim.vim
```

Then reload VS Code.

---

## Step 2: Open LEARN Workspace (1 minute)

```bash
cd ~/LEARN
code .
```

**That's it!** All settings are already configured in `.vscode/`

---

## Step 3: Your First Lesson (2 minutes)

### Open Files

1. **Lesson**: Open `dart/stage-1/level-1/lesson.md` (or any language)
2. **Split**: Press `Ctrl+\`
3. **Code**: Open `main.dart` in the right pane
4. **Terminal**: Press `Ctrl+Shift+T`

### Your Layout

```
╔═══════════════════╦═══════════════════╗
║   lesson.md       ║   main.dart       ║
║   (read-only)     ║   (your code)     ║
╠═══════════════════╩═══════════════════╣
║  Terminal                             ║
╚═══════════════════════════════════════╝
```

---

## Step 4: Learn the Basics (as you go)

### Most Important Keys

| Key | What It Does |
|-----|--------------|
| `i` | Start typing (Insert mode) |
| `Esc` or `jk` | Stop typing (Normal mode) |
| `h` `j` `k` `l` | Move left, down, up, right |
| `<Space>w` | Save file (in Normal mode) |
| `<Space>t` | Toggle terminal |
| `Ctrl+h` | Move to left window |
| `Ctrl+l` | Move to right window |

### Quick Test

1. In code pane, press `i` to type
2. Type: `void main() { print('Hello!'); }`
3. Press `Esc` to exit Insert mode
4. Press `<Space>` then `w` to save
5. Press `Ctrl+Shift+T` for terminal
6. Run your code!

---

## What You Get

✅ **Vim motions** - Navigate without arrow keys
✅ **Split screen** - Lesson + code side-by-side
✅ **Hidden activity bar** - More screen space
✅ **Protected lessons** - Can't accidentally edit
✅ **Smart hotkeys** - `<Space>` as leader key
✅ **Integrated terminal** - Compile and run instantly
✅ **Relative line numbers** - Jump anywhere fast
✅ **Language servers** - Auto-complete and docs

---

## Next Steps

1. Read [README.md](README.md) for full documentation
2. Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for all commands
3. Learn Vim gradually - don't memorize everything at once
4. Use `Ctrl+K Ctrl+S` to see all keybindings in VS Code

---

## Troubleshooting

**Vim not working?**
```bash
code --install-extension vscodevim.vim
# Then Ctrl+Shift+P → "Reload Window"
```

**Settings not applied?**
- Make sure you opened the folder: `code ~/LEARN` (not individual files)
- Check bottom right corner - should say "Vim" mode

**Want to disable Vim temporarily?**
- `Ctrl+Shift+P` → "Toggle Vim Mode"

---

**That's it! Start learning! 🚀**

For help: Press `F1` or check `MODE_VSCODE/README.md`
