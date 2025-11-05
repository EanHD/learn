# VS CODE MODE Documentation Index

Complete navigation guide for all VS Code Mode documentation.

---

## 🚀 Getting Started

**New to VS Code Mode? Start here:**

1. **[SETUP_COMPLETE.md](SETUP_COMPLETE.md)** - Overview of what's configured
2. **[QUICK_START.md](QUICK_START.md)** - 5-minute setup guide
3. **[README.md](README.md)** - Full feature documentation

---

## 📚 Documentation Files

### Essential Reading

| File | Purpose | When to Read |
|------|---------|--------------|
| [**QUICK_START.md**](QUICK_START.md) | Fast 5-minute setup | First time setup |
| [**README.md**](README.md) | Complete feature guide | Learning the system |
| [**QUICK_REFERENCE.md**](QUICK_REFERENCE.md) | All commands & keybindings | Daily reference |

### Detailed Guides

| File | Purpose | When to Read |
|------|---------|--------------|
| [**COMPLETE_SETUP.md**](COMPLETE_SETUP.md) | Detailed configuration | Customizing settings |
| [**FAQ.md**](FAQ.md) | Common questions & answers | When you're stuck |
| [**SETUP_COMPLETE.md**](SETUP_COMPLETE.md) | What's been configured | After initial setup |

### Workflows

| File | Purpose | When to Read |
|------|---------|--------------|
| [**WORKFLOWS/split-screen-learning.md**](WORKFLOWS/split-screen-learning.md) | Step-by-step learning workflow | Learning to use split-screen |

---

## 🔧 Configuration Files

Located in `CONFIG/` directory:

| File | Purpose |
|------|---------|
| [**CONFIG/settings.json**](CONFIG/settings.json) | VS Code settings template |
| [**CONFIG/keybindings.json**](CONFIG/keybindings.json) | Keyboard shortcuts template |
| [**CONFIG/extensions.json**](CONFIG/extensions.json) | Extension recommendations |

**Note:** The actual active configuration is in `../.vscode/` (parent directory)

---

## 📖 Reading Order

### For Absolute Beginners

1. [SETUP_COMPLETE.md](SETUP_COMPLETE.md) - See what you have
2. [QUICK_START.md](QUICK_START.md) - Get it working
3. [WORKFLOWS/split-screen-learning.md](WORKFLOWS/split-screen-learning.md) - Learn the workflow
4. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Bookmark for daily use

### For Experienced VS Code Users

1. [QUICK_START.md](QUICK_START.md) - Install Vim extension
2. [README.md](README.md) - Learn Vim integration features
3. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Vim commands reference

### For Vim Users

1. [README.md](README.md) - See how Vim works in VS Code
2. [COMPLETE_SETUP.md](COMPLETE_SETUP.md) - Customize Vim behavior
3. [FAQ.md](FAQ.md) - VS Code-specific Vim questions

---

## 🎯 Quick Links

### By Topic

**Installation & Setup**
- [Quick Start Guide](QUICK_START.md#step-1-install-vim-extension-2-minutes)
- [Complete Setup](COMPLETE_SETUP.md#installation)
- [Extension List](CONFIG/extensions.json)

**Vim Basics**
- [Vim Mode Overview](README.md#vim-motions)
- [Essential Keybindings](README.md#-essential-keybindings)
- [Vim Commands Reference](QUICK_REFERENCE.md#essential-vim-motions)
- [Learning Path](QUICK_REFERENCE.md#learning-path)

**Workspace Layout**
- [Split Screen Setup](README.md#split-screen-layout)
- [Window Navigation](QUICK_REFERENCE.md#window-navigation)
- [Workflow Guide](WORKFLOWS/split-screen-learning.md)

**Customization**
- [Settings Configuration](COMPLETE_SETUP.md#customization)
- [Keybindings](COMPLETE_SETUP.md#customize-keybindings)
- [Theme & Font](COMPLETE_SETUP.md#change-theme)

**Troubleshooting**
- [Common Issues](FAQ.md)
- [Vim Problems](FAQ.md#vim-questions)
- [Setup Problems](FAQ.md#setup-questions)
- [Performance Issues](COMPLETE_SETUP.md#troubleshooting)

---

## 🆘 Getting Help

### Quick Answers

1. **"How do I...?"** → Check [FAQ.md](FAQ.md)
2. **"What key does...?"** → Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
3. **"Is it normal that...?"** → Check [FAQ.md](FAQ.md)
4. **"How do I customize...?"** → Check [COMPLETE_SETUP.md](COMPLETE_SETUP.md)

### In VS Code

- `F1` - Command palette
- `Ctrl+K Ctrl+S` - Keyboard shortcuts
- `Ctrl+,` - Settings

### External Resources

- [Vim Tutor](https://www.openvim.com/) - Interactive Vim tutorial
- [VS Code Docs](https://code.visualstudio.com/docs) - Official documentation
- [VSCodeVim Extension](https://github.com/VSCodeVim/Vim) - Extension docs

---

## 📂 File Structure

```
MODE_VSCODE/
├── README.md                          ← Main documentation
├── QUICK_START.md                     ← 5-minute setup
├── QUICK_REFERENCE.md                 ← Command reference
├── COMPLETE_SETUP.md                  ← Detailed configuration
├── FAQ.md                             ← Q&A
├── SETUP_COMPLETE.md                  ← Setup summary
├── INDEX.md                           ← This file
│
├── CONFIG/
│   ├── settings.json                  ← Settings template
│   ├── keybindings.json               ← Keybindings template
│   └── extensions.json                ← Extensions list
│
└── WORKFLOWS/
    └── split-screen-learning.md       ← Learning workflow guide
```

---

## 🎓 Learning Resources

### This Project

- [Main Project README](../README.md) - LEARN platform overview
- [Vim Cheatsheet](../VIM_CHEATSHEET.md) - Basic Vim reference
- [MODE_VIM Documentation](../MODE_VIM/README.md) - Neovim alternative

### External

- **Vim Basics:**
  - [OpenVim](https://www.openvim.com/) - Interactive tutorial
  - [Vim Adventures](https://vim-adventures.com/) - Game-based learning
  - [Vimtutor](https://vimhelp.org/usr_01.txt.html) - Built-in tutorial

- **VS Code:**
  - [Official Docs](https://code.visualstudio.com/docs)
  - [Tips & Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
  - [Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)

---

## 📋 Checklists

### Initial Setup Checklist

- [ ] VS Code installed
- [ ] Vim extension installed (`vscodevim.vim`)
- [ ] VS Code reloaded
- [ ] LEARN workspace opened
- [ ] Vim mode indicator visible (bottom-right)
- [ ] Read [QUICK_START.md](QUICK_START.md)

### First Lesson Checklist

- [ ] Lesson file opened (`lesson.md`)
- [ ] Editor split (`Ctrl+\`)
- [ ] Code file opened in right pane
- [ ] Terminal opened (`Ctrl+Shift+T`)
- [ ] Can enter Insert mode (`i`)
- [ ] Can exit Insert mode (`Esc`)
- [ ] Can save file (`<Space>w`)
- [ ] Can switch panes (`Ctrl+h/l`)

### Week 1 Goals

- [ ] Master `hjkl` movement
- [ ] Comfortable with `i` and `Esc`
- [ ] Can save with `<Space>w`
- [ ] Can navigate with `Ctrl+h/j/k/l`
- [ ] Can use `dd`, `yy`, `p`
- [ ] Completed 3+ lessons using Vim

---

## 🔄 Quick Navigation

**From any doc, get to:**

- **Home:** [README.md](README.md)
- **Setup:** [QUICK_START.md](QUICK_START.md)
- **Commands:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **Help:** [FAQ.md](FAQ.md)
- **Workflow:** [WORKFLOWS/split-screen-learning.md](WORKFLOWS/split-screen-learning.md)
- **Index:** This file

---

## 💡 Tips

### For Documentation Navigation

- Use `Ctrl+P` in VS Code to quickly open any doc
- Bookmark [QUICK_REFERENCE.md](QUICK_REFERENCE.md) in your browser
- Print [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for desk reference
- Keep [FAQ.md](FAQ.md) open in a tab

### For Learning

- Don't read everything at once
- Start with [QUICK_START.md](QUICK_START.md)
- Reference [QUICK_REFERENCE.md](QUICK_REFERENCE.md) as needed
- Come back to [COMPLETE_SETUP.md](COMPLETE_SETUP.md) when ready to customize

---

## 📝 Document Summaries

### README.md (Main Documentation)
- Complete feature overview
- All keybindings explained
- Learning workflow
- Comparison with MODE_VIM
- **Length:** Long (comprehensive)
- **Read when:** Learning the system

### QUICK_START.md (Fast Setup)
- 5-minute setup guide
- Essential steps only
- Quick test procedure
- **Length:** Short (3 pages)
- **Read when:** First time setup

### QUICK_REFERENCE.md (Command Reference)
- All Vim commands
- All VS Code shortcuts
- Tables and examples
- Learning progression
- **Length:** Long (reference)
- **Read when:** Daily reference, keep handy

### COMPLETE_SETUP.md (Detailed Config)
- Installation instructions
- Configuration explanations
- Customization guide
- Advanced features
- **Length:** Very long
- **Read when:** Customizing settings

### FAQ.md (Questions & Answers)
- Common problems
- Quick solutions
- Troubleshooting tips
- **Length:** Long (reference)
- **Read when:** When stuck

### WORKFLOWS/split-screen-learning.md
- Step-by-step workflow
- Practical examples
- Pro tips
- **Length:** Long (tutorial)
- **Read when:** Learning workflow

---

## 🎯 Goals of Each Document

| Document | Primary Goal |
|----------|--------------|
| SETUP_COMPLETE.md | Show what's been configured |
| QUICK_START.md | Get working in 5 minutes |
| README.md | Understand all features |
| QUICK_REFERENCE.md | Quick command lookup |
| COMPLETE_SETUP.md | Deep customization |
| FAQ.md | Solve common problems |
| WORKFLOWS/split-screen-learning.md | Master the workflow |

---

**Welcome to VS Code Mode! 🚀**

*For questions or issues, check [FAQ.md](FAQ.md) or the main [README.md](README.md)*
