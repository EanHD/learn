# VS CODE MODE: Setup Complete! 🎉

Your VS Code is now configured as a powerful, focused learning environment with Vim motions!

---

## What's Been Configured

### ✅ Vim Motions Enabled

- Navigate with `hjkl`
- Leader key set to `<Space>`
- Quick exit with `jk` from Insert mode
- Relative line numbers for fast jumping
- System clipboard integration

### ✅ Distraction-Free Interface

- Activity bar hidden (more screen space)
- Minimap disabled
- Clean, focused layout
- Lesson files protected (read-only)
- Auto-save enabled

### ✅ Split-Screen Layout

- Easy window navigation: `Ctrl+h/j/k/l`
- Quick split: `Ctrl+\`
- Equalize windows: `Ctrl+=`
- Perfect for lesson + code side-by-side

### ✅ Smart Keybindings

| Action | Key |
|--------|-----|
| Save | `<Space>w` |
| Toggle Terminal | `<Space>t` or `Ctrl+Shift+T` |
| File Explorer | `<Space>e` |
| Quick Open | `<Space>ff` |
| Find in Files | `<Space>fg` |
| Zen Mode | `<Space>z` |

### ✅ Language Support

Recommended extensions for:
- C/C++ (IntelliSense)
- Rust (rust-analyzer)
- Python (Pylance)
- Dart/Flutter
- Go
- JavaScript/TypeScript

### ✅ Documentation Created

- **README.md** - Complete guide
- **QUICK_START.md** - 5-minute setup
- **QUICK_REFERENCE.md** - All commands
- **COMPLETE_SETUP.md** - Detailed configuration
- **FAQ.md** - Common questions
- **WORKFLOWS/split-screen-learning.md** - Step-by-step workflow

---

## Next Steps

### 1. Install Vim Extension (Required)

```bash
code --install-extension vscodevim.vim
```

Then reload: `Ctrl+Shift+P` → "Reload Window"

### 2. Install Language Extensions (Recommended)

```bash
# Install all at once
code --install-extension ms-vscode.cpptools \
     --install-extension rust-lang.rust-analyzer \
     --install-extension ms-python.python \
     --install-extension yzhang.markdown-all-in-one
```

### 3. Open LEARN Workspace

```bash
cd ~/LEARN
code .
```

Settings automatically apply! ✨

### 4. Start Your First Lesson

1. Open a lesson: `dart/stage-1/level-1/lesson.md`
2. Split editor: `Ctrl+\`
3. Open code file: `main.dart`
4. Toggle terminal: `Ctrl+Shift+T`
5. Start coding!

---

## Quick Test

Try this to verify everything works:

1. **Open VS Code:** `code ~/LEARN`
2. **Check Vim:** Bottom-right should show "NORMAL"
3. **Test leader key:**
   - Press `Space`
   - Wait 1 second
   - You should see command hints
4. **Test navigation:**
   - Press `Ctrl+h/l` to switch windows
   - Press `Ctrl+Shift+T` for terminal

If everything works, you're ready! 🚀

---

## Learning Path

### Week 1: Vim Basics
- `hjkl` movement
- `i` (insert) and `Esc` (normal)
- `<Space>w` to save
- `dd`, `yy`, `p` (delete, copy, paste)

### Week 2: Navigation
- `w`, `b`, `e` (word movement)
- `0`, `$` (line start/end)
- `gg`, `G` (file start/end)
- `/search` and `n` (search)

### Week 3: Editing
- Text objects: `ciw`, `di"`, `ya{`
- Visual mode: `v`, `V`
- Change: `cw`, `ci(`, `cc`

### Month 2+: Advanced
- Macros: `qa`, `@a`
- Marks: `ma`, `'a`
- Leader commands
- Language server features

---

## Configuration Files

All settings are in these files:

```
LEARN/
├── .vscode/
│   ├── settings.json          ← Workspace settings (Vim, editor)
│   ├── keybindings.json       ← Custom keybindings
│   ├── extensions.json        ← Recommended extensions
│   └── tasks.json             ← Build/run tasks
│
└── MODE_VSCODE/
    ├── README.md              ← Main documentation
    ├── QUICK_START.md         ← Fast setup guide
    ├── QUICK_REFERENCE.md     ← All commands
    ├── COMPLETE_SETUP.md      ← Detailed config
    ├── FAQ.md                 ← Common questions
    │
    ├── CONFIG/
    │   ├── settings.json      ← Template settings
    │   ├── keybindings.json   ← Template keybindings
    │   └── extensions.json    ← Extension list
    │
    └── WORKFLOWS/
        └── split-screen-learning.md  ← Learning workflow
```

---

## Customization

Want to tweak settings?

1. **Editor settings:** Edit `.vscode/settings.json`
2. **Keybindings:** `Ctrl+K Ctrl+S` or edit `.vscode/keybindings.json`
3. **Theme:** `Ctrl+K Ctrl+T`
4. **Font size:** `Ctrl+` or `Ctrl-`

Changes apply immediately!

---

## Comparison: MODE_VSCODE vs MODE_VIM

| Feature | VS Code | Neovim |
|---------|---------|--------|
| **Vim Motions** | ✅ Via extension | ✅ Native |
| **GUI** | ✅ Rich interface | Terminal only |
| **Mouse** | ✅ Full support | Limited |
| **Setup** | Install extension | Already done |
| **Speed** | Good | ⚡ Faster |
| **Extensions** | VS Code marketplace | Lua plugins |
| **Learning Curve** | Gentler | Steeper |
| **Debugging** | ✅ Built-in | Via plugins |

Both are excellent! Choose what fits your style.

---

## Tips for Success

### Do's ✅

- **Start simple** - Learn basics first
- **Use cheat sheet** - Keep QUICK_REFERENCE.md open
- **Practice daily** - Muscle memory takes time
- **Use leader key** - `<Space>` is your friend
- **Ask for help** - Check FAQ.md

### Don'ts ❌

- **Don't memorize everything** - Learn gradually
- **Don't fight it** - If stuck, use mouse
- **Don't give up** - First week is hardest
- **Don't skip basics** - Master `hjkl` first

---

## Getting Help

### Documentation

- **[README.md](README.md)** - Full VS Code Mode guide
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - All commands
- **[FAQ.md](FAQ.md)** - Common problems
- **[../VIM_CHEATSHEET.md](../VIM_CHEATSHEET.md)** - Vim basics

### In VS Code

- `F1` or `Ctrl+Shift+P` - Command palette
- `Ctrl+K Ctrl+S` - Keyboard shortcuts
- `<Space>` - Leader key commands

### External

- [Vim Tutor](https://www.openvim.com/) - Interactive tutorial
- [VS Code Docs](https://code.visualstudio.com/docs) - Official docs
- [Vim extension docs](https://github.com/VSCodeVim/Vim) - Extension guide

---

## What Makes This Special?

### Unlike Default VS Code

- ✅ **Vim motions** - Navigate at speed of thought
- ✅ **Distraction-free** - Hidden UI elements
- ✅ **Protected lessons** - Can't accidentally edit
- ✅ **Smart defaults** - Everything pre-configured

### Unlike Plain Vim

- ✅ **Easier setup** - Just install extension
- ✅ **Rich GUI** - Mouse, sidebar, panels
- ✅ **Built-in LSP** - No configuration needed
- ✅ **Familiar** - Standard VS Code UI

### Best of Both Worlds

You get Vim's power with VS Code's convenience!

---

## Ready to Start?

1. ✅ Install Vim extension: `code --install-extension vscodevim.vim`
2. ✅ Reload VS Code: `Ctrl+Shift+P` → "Reload Window"
3. ✅ Open workspace: `code ~/LEARN`
4. ✅ Read: [QUICK_START.md](QUICK_START.md)
5. ✅ Start learning!

---

## Quick Command Summary

### Most Essential (Learn These First)

```vim
i                Enter Insert mode (start typing)
Esc or jk        Exit to Normal mode
hjkl             Move around
<Space>w         Save file
<Space>t         Toggle terminal
Ctrl+h/l         Switch between editor panes
```

### You're Ready When You Can...

- [ ] Open a lesson
- [ ] Split the editor
- [ ] Switch between panes
- [ ] Enter/exit Insert mode
- [ ] Save a file
- [ ] Open terminal
- [ ] Compile and run code

**If you can do these, you're ready to learn!**

---

## Enjoy Your New Setup!

You now have a professional, Vim-powered learning environment ready to go!

**Resources:**
- Full guide: [README.md](README.md)
- Quick start: [QUICK_START.md](QUICK_START.md)
- All commands: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

**Happy learning! 🚀**

---

*Last updated: 2025-01-04*
*VS Code + Vim = ❤️*
