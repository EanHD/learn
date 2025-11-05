# VS CODE MODE: Professional Learning IDE

**Learn programming in a beautiful, distraction-free VS Code environment with Vim motions.**

**Fully cross-platform:** Works perfectly on Linux, macOS, and Windows with automatic setup scripts.

---

## ✨ What You Get

When you open a lesson in VS Code, you get a fully configured IDE experience:

- ⌨️ **Vim Motions** - Navigate and edit like a pro with `hjkl`, `gg`, `G`, and more
- 🎨 **Clean Interface** - Activity bar hidden, minimal distractions
- 📖 **Split Screen** - Lesson on left, code on right
- 🔒 **Protected Lessons** - Lesson files are read-only
- ⚡ **Smart Hotkeys** - `<Space>` as leader key for all actions
- 💬 **Integrated Terminal** - Compile and run without leaving editor
- 📍 **Relative Line Numbers** - Jump quickly with Vim motions
- 🎯 **Language Servers** - Auto-completion, go-to-definition, and more
- 🖼️ **Markdown Preview** - Beautiful rendered lesson view

---

## 🚀 Quick Start

### Step 1: Install Vim Extension

**Automatic (Linux/Mac):** Run the install script:
```bash
bash ~/LEARN/install.sh
```

**Automatic (Windows):** Run the PowerShell installer:
```powershell
powershell -File ~\LEARN\install.ps1
```

Both installers automatically install the Vim extension and all language support extensions.

**Manual:** Open VS Code and install the **Vim extension**:

```
Ctrl+Shift+X  → Search "Vim" → Install "vscodevim.vim"
```

Or install from command line:
```bash
code --install-extension vscodevim.vim
```

### Step 2: Reload VS Code

After installing the Vim extension:
```
Ctrl+Shift+P → "Reload Window"
```

### Step 3: Open Your First Lesson

```bash
cd ~/LEARN
code .
```

Then open any lesson file, for example:
- `dart/stage-1/level-1/lesson.md`
- `c-c++/stage-1/level-1/lesson.md`
- `python/stage-1/level-1/lesson.md`

### Step 4: Set Up Your Layout

1. **Open lesson.md** (left side)
2. **Press** `Ctrl+\` to split editor
3. **Open your code file** (right side) - e.g., `main.cpp`, `main.py`
4. **Press** `Ctrl+=` to equalize window sizes
5. **Press** `Ctrl+Shift+T` to open terminal (bottom)

You'll see:

```
╔═══════════════════╦═══════════════════╗
║   lesson.md       ║   main.cpp        ║
║   (left)          ║   (right)         ║
║                   ║                   ║
║  # Learning Goals ║  #include <...>   ║
║                   ║                   ║
║  - Concept 1      ║  int main() {     ║
║  - Concept 2      ║      ▊            ║
║                   ║      return 0;    ║
║  (read-only)      ║  }                ║
║                   ║  (editable)       ║
╠═══════════════════╩═══════════════════╣
║  Terminal: bash                       ║
║  $ make                               ║
║  $ ./main                             ║
╚═══════════════════════════════════════╝
```

---

## ⚡ Essential Keybindings

**Leader Key**: `<Space>` (Space bar in Normal mode)

### Vim Basics

| Key | Action |
|-----|--------|
| `i` | Enter Insert mode (start typing) |
| `Esc` or `jk` | Exit Insert mode to Normal mode |
| `h` `j` `k` `l` | Move left, down, up, right |
| `w` `b` | Jump forward/backward by word |
| `0` `$` | Jump to start/end of line |
| `gg` `G` | Jump to top/bottom of file |
| `/text` | Search for "text" |
| `n` `N` | Next/previous search result |
| `dd` | Delete (cut) line |
| `yy` | Copy (yank) line |
| `p` | Paste |
| `u` | Undo |
| `Ctrl+r` | Redo |

### Leader Commands (Press Space then...)

| Keys | Action |
|------|--------|
| `<Space>w` | Save file |
| `<Space>q` | Close current editor |
| `<Space>ff` | Find files (Quick Open) |
| `<Space>fg` | Find in files (Search) |
| `<Space>t` | Toggle terminal |
| `<Space>e` | Toggle file explorer |
| `<Space>z` | Toggle Zen mode (distraction-free) |
| `<Space>s` | Split editor |
| `<Space>=` | Equalize editor widths |
| `<Space>c` | Comment line (in Visual mode) |

### Window Navigation

| Key | Action |
|-----|--------|
| `Ctrl+h` | Move to left editor |
| `Ctrl+j` | Move to bottom panel |
| `Ctrl+k` | Move to top panel |
| `Ctrl+l` | Move to right editor |
| `Ctrl+=` | Equalize editor widths |

### Code Navigation (Language Server)

| Key | Action |
|-----|--------|
| `gd` | Go to definition |
| `gr` | Find references |
| `K` | Show hover documentation |
| `Ctrl+Space` | Trigger suggestions |

### Quick Actions

| Key | Action |
|-----|--------|
| `Ctrl+Shift+T` | Toggle terminal |
| `Ctrl+Shift+B` | Toggle sidebar |
| `Ctrl+Shift+Z` | Toggle Zen mode |
| `Ctrl+Shift+V` | Markdown preview (in .md files) |
| `Ctrl+\` | Split editor |

---

## 🎨 Features Explained

### Vim Motions

Navigate your code at the speed of thought:
- **Never touch the mouse** - Everything via keyboard
- **Relative line numbers** - Jump to any line with `10j` or `5k`
- **Text objects** - Delete word with `daw`, change inside quotes with `ci"`
- **Visual mode** - Select text with `v`, line-wise with `V`, block with `Ctrl+v`

### Clean Interface

Minimal distractions:
- **Activity bar hidden** - More space for code
- **Minimap disabled** - Focus on what matters
- **Breadcrumbs enabled** - Know where you are
- **Status bar visible** - See Vim mode and file info

### Protected Lessons

Lesson files (`lesson.md`) are read-only:
- Can't accidentally edit lessons
- Navigate with Vim motions
- Preview with `Ctrl+Shift+V`

### Split Screen Layout

Perfect for learning:
- **Left**: Lesson content (read-only)
- **Right**: Your code (editable)
- **Bottom**: Terminal for compiling/running

### Language Server Support

Smart code assistance:
- **Auto-completion** - Intelligent suggestions as you type
- **Go to Definition** - Jump to function/class definitions
- **Hover Docs** - See documentation on hover
- **Error Highlighting** - See problems in real-time

Supported languages:
- C/C++ (clangd)
- Rust (rust-analyzer)
- Python (Pylance)
- JavaScript/TypeScript
- Go, Dart, and more

### Terminal Integration

Integrated terminal at the bottom:
- **Compile**: `make`, `gcc`, `rustc`, `cargo build`
- **Run**: `./main`, `cargo run`, `python3 main.py`
- **Toggle**: `Ctrl+Shift+T` or `<Space>t`
- **Multiple terminals** - Create splits as needed

### Markdown Preview

Beautiful lesson rendering:
- **Press** `Ctrl+Shift+V` in any `.md` file
- **Scrolls in sync** with editor
- **GitHub-style** formatting
- **Side-by-side** with editor

---

## 🎓 Learning Workflow

### Your First Lesson

1. **Open VS Code in LEARN workspace**:
   ```bash
   cd ~/LEARN
   code .
   ```

2. **Open a lesson**:
   - Navigate to `c-c++/stage-1/level-1/lesson.md`
   - Or `dart/stage-1/level-1/lesson.md`

3. **Split the editor**:
   - Press `Ctrl+\` to split
   - Open `main.cpp` (or language file) in right pane

4. **Read the lesson** (left pane):
   - Use `j/k` to scroll
   - Press `gg` to jump to top
   - Press `G` to jump to bottom
   - Use `/text` to search
   - Optional: `Ctrl+Shift+V` for preview

5. **Write code** (right pane):
   - Press `Ctrl+l` to move to right pane
   - Press `i` to enter Insert mode
   - Type your code
   - Press `Esc` to return to Normal mode
   - Press `<Space>w` to save

6. **Compile and run** (terminal):
   - Press `Ctrl+Shift+T` to open terminal
   - Type `make` or `cargo build` or `python3 main.py`
   - See output immediately

7. **Navigate to next lesson**:
   - Open next level's `lesson.md`
   - Repeat!

### Pro Tips

- **Don't memorize everything** - Learn Vim gradually
- **Start with basics** - `hjkl`, `i`, `Esc`, `<Space>w`
- **Use Ctrl+h/j/k/l** - Switch between windows quickly
- **Zen mode for focus** - `<Space>z` or `Ctrl+Shift+Z`
- **Terminal stays open** - Keep compilation output visible
- **Relative line numbers** - Jump quickly with `12j` or `5k`
- **Use `gd` often** - Jump to definitions when learning APIs

---

## 🔧 Configuration

All settings are in `.vscode/` directory:

- **settings.json** - Editor, Vim, and workspace settings
- **keybindings.json** - Custom keyboard shortcuts
- **extensions.json** - Recommended extensions
- **tasks.json** - Build and run tasks

### Customization

Want to tweak settings?

1. Press `Ctrl+,` to open Settings
2. Or edit `.vscode/settings.json` directly
3. Changes apply only to this workspace

Example customizations:
```json
{
  "editor.fontSize": 16,           // Bigger font
  "editor.lineHeight": 1.8,        // More spacing
  "workbench.colorTheme": "Tokyo Night",  // Different theme
  "vim.leader": ",",               // Different leader key
}
```

---

## 📦 Recommended Extensions

The workspace recommends these extensions:

### Essential
- **Vim** (`vscodevim.vim`) - Vim motions [REQUIRED]

### Language Support
- **C/C++** - IntelliSense and debugging
- **Rust Analyzer** - Rust language server
- **Python** - Python language server
- **Go** - Go language support
- **Dart** - Dart and Flutter support

### Productivity
- **Markdown All in One** - Enhanced markdown editing
- **GitLens** - Git integration
- **Code Spell Checker** - Catch typos
- **Material Icon Theme** - Beautiful file icons

### Optional but Nice
- **Tokyo Night** or **One Dark Pro** theme
- **Bracket Pair Colorizer** - Rainbow brackets

---

## 🆘 Troubleshooting

### Q: Vim extension not working?

**A**: Install and reload:
```bash
code --install-extension vscodevim.vim
```
Then: `Ctrl+Shift+P` → "Reload Window"

### Q: Can't remember keybindings?

**A**:
- Press `<Space>` in Normal mode (shows Which-Key style hints)
- Check `MODE_VSCODE/QUICK_REFERENCE.md`
- Press `Ctrl+K Ctrl+S` to see all keybindings

### Q: Lesson files are editable?

**A**: They should be read-only by default. Check `.vscode/settings.json`:
```json
"files.readonlyInclude": {
  "**/lesson.md": true
}
```

### Q: Terminal won't open?

**A**: Try:
- `Ctrl+Shift+T`
- Or `<Space>` then `t` (in Normal mode)
- Or View → Terminal from menu

### Q: Split editor not working?

**A**:
- Press `Ctrl+\` to split
- Or `<Space>s` in Normal mode
- Or right-click tab → "Split Right"

### Q: Language server not working?

**A**:
- Install extension for your language
- Check bottom-right status bar for errors
- Restart VS Code: `Ctrl+Shift+P` → "Reload Window"

### Q: How to exit Vim mode?

**A**: You don't! That's the point. But if you need to:
- Uninstall Vim extension
- Or disable: `Ctrl+Shift+P` → "Extensions: Disable" → "Vim"

### Q: Want to customize Vim settings?

**A**: Edit `.vscode/settings.json` - search for `vim.` settings:
```json
{
  "vim.leader": "<space>",
  "vim.useSystemClipboard": true,
  "vim.hlsearch": true
}
```

---

## 🎯 Vim Mode Comparison

| Feature | Neovim MODE_VIM | VS Code MODE_VSCODE |
|---------|-----------------|---------------------|
| Vim Motions | ✅ Native | ✅ Via Extension |
| Split Screen | ✅ Auto-setup | ✅ Manual setup |
| Terminal | ✅ Integrated | ✅ Integrated |
| Language Server | ✅ Mason | ✅ Built-in |
| Themes | ✅ Nightfox | ✅ Any VS Code theme |
| Plugins | ✅ 19 plugins | ✅ Extensions |
| Lesson Protection | ✅ Auto | ✅ Auto |
| Learning Curve | Steeper | Gentler |
| Performance | ⚡ Faster | Good |
| GUI Features | Terminal | ✅ Rich UI |

**Choose Neovim if**: You want maximum speed and terminal workflow

**Choose VS Code if**: You prefer GUI, mouse support, and easier setup

---

## 📖 More Resources

- [QUICK_START.md](QUICK_START.md) - Fast setup guide
- [COMPLETE_SETUP.md](COMPLETE_SETUP.md) - Detailed configuration
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - All commands
- [VIM_CHEATSHEET.md](../VIM_CHEATSHEET.md) - Vim basics
- [Main README](../README.md) - Platform overview

---

## 💡 Remember

### Vim Basics
- **`i`** - Start typing
- **`Esc`** or **`jk`** - Stop typing
- **`hjkl`** - Move around

### Essential Commands
- **`<Space>w`** - Save
- **`<Space>t`** - Terminal
- **`Ctrl+h/l`** - Switch windows
- **`Ctrl+Shift+Z`** - Focus mode

### Get Help
- Press `Ctrl+K Ctrl+S` - Show all keybindings
- Press `F1` - Command palette
- Check `MODE_VSCODE/` docs

**Happy Learning! 🎓**
