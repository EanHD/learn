# LEARN: Programming in 14 Languages

**490 hands-on lessons.** Fourteen languages. Five stages. Real projects.

Start coding in **5 minutes** with our **professional IDE setup**.

---

## ✨ What's New (2025)

- 🎨 **Nightfox Theme** - Beautiful dark theme with excellent syntax highlighting
- 📖 **Smart Markdown Rendering** - Lessons display beautifully with icons and formatting
- 🔒 **Protected Lessons** - Read-only lesson files prevent accidental edits
- 📍 **Auto-Positioning** - Cursor starts at line 4, ready to code
- 🎯 **Enhanced Which-Key** - Clean, organized command menu
- ⚡ **19 Neovim Plugins** - LSP, Telescope, Flash navigation, and more
- 💬 **Help Comments** - Every code file starts with quick help reference
- 🪟 **Smart Window Navigation** - Seamless switching between lesson and code

---

## 🚀 Quick Start

### One-line install (Linux/Mac)

\`\`\`bash
bash <(curl -fsSL https://raw.githubusercontent.com/EanHD/learn/main/install.sh)
\`\`\`

### Windows (PowerShell)

\`\`\`powershell
irm https://raw.githubusercontent.com/EanHD/learn/main/install.ps1 | iex
\`\`\`

This installs everything: CLI, Neovim config, and all dependencies.

### Update anytime

**Linux/Mac:**
\`\`\`bash
bash ~/LEARN/install.sh --update
\`\`\`

**Windows:**
\`\`\`powershell
powershell -File ~\LEARN\install.ps1 -Update
\`\`\`

### Launch

\`\`\`bash
learn
\`\`\`

This opens an **interactive menu** where you can browse lessons, track progress, and start learning immediately.

### Or jump straight to a lesson

\`\`\`bash
learn c++ 1                # Open C++ Stage 1, Level 1
learn rust 1               # Open Rust Stage 1, Level 1
learn python 1             # Open Python Stage 1, Level 1
\`\`\`

### Choose your editor

\`\`\`bash
learn c++ 1 --vim          # Neovim (default, enhanced IDE)
learn c++ 1 --vscode       # VS Code
learn c++ 1 --terminal     # Terminal (read-only)
\`\`\`

---

## 📚 What You'll Learn

| Stage | What It Is | Time |
|-------|-----------|------|
| **1** | Copy working code, learn syntax | Week 1 |
| **2** | Turn pseudocode into real code | Week 2 |
| **3** | Design solutions to small problems | Week 3 |
| **4** | Build full projects from scratch | Weeks 4-5 |
| **5** | Create your own capstone project | Week 6 |

**14 languages supported:**

- **Backend:** C++, Rust, Python, Go, Lua
- **Web:** JavaScript, TypeScript, C#
- **Systems:** Shell, PowerShell
- **Mobile:** Dart, Swift, Kotlin
- **Database:** SQL

**7 lessons per stage** × **5 stages** = **35 lessons per language**

**Total: 490 lessons** across all 14 languages

---

## 🎮 How to Navigate

| Command | What It Does |
|---------|-------------|
| \`learn\` | **Interactive menu** (recommended!) |
| \`learn c++ 1\` | Open C++ Stage 1, Level 1 |
| \`learn python 1\` | Open Python Stage 1, Level 1 |
| \`learn typescript 1\` | Open TypeScript Stage 1, Level 1 |
| \`learn --list\` | See all 490 lessons |
| \`learn --progress\` | Check your progress with stats |
| \`learn --next\` | Continue where you left off |

### Jump Around

\`\`\`bash
learn python 1           # Start Python
learn c++ 5 --stage 2    # Jump to Stage 2, Level 5
learn javascript 1       # Switch to JavaScript
learn go 3              # Try Go
\`\`\`

---

## 🛠️ Neovim IDE Features

When you open a lesson with Neovim (\`learn c++ 1\`), you get:

### 🎨 Beautiful Interface
- **Nightfox theme** - Professional dark theme
- **Lualine statusbar** - Shows file, mode, git status
- **Render-markdown** - Lessons display with icons (📌 📍 🔸 ⬜ ✅)
- **Anti-conceal** - See raw markdown on cursor line

### 🔍 Smart Navigation
- **Flash.nvim** - Jump anywhere instantly with \`s\`
- **Telescope** - Fuzzy find files with \`<Space>ff\`
- **Which-Key** - Press \`<Space>\` to see all commands
- **Auto-save** - Code saves when switching windows

### 💻 Code Intelligence
- **LSP Support** - 7 language servers auto-installed
- **Treesitter** - Advanced syntax highlighting
- **Mason** - Automatic LSP management
- **Code actions** - Quick fixes with \`<Space>ca\`

### 🪟 Workflow
- **Split screen** - Lesson on left, code on right
- **Terminal** - Toggle with \`<Space>t\`
- **Zen mode** - Distraction-free with \`<Space>xz\`
- **Window navigation** - \`Ctrl+h/l\` or \`<Space>←→\`

### 🔒 Lesson Protection
- **Read-only lessons** - Can't accidentally edit
- **Help comments** - Every code file starts with: \`// Press <Esc> <Space> h for help.\`
- **Auto-positioning** - Cursor starts on line 4, ready to code
- **Flash navigation** - \`s\` key works in lessons for quick jumps

### ⚡ Key Bindings

**In Neovim (after pressing Space):**

| Key | Action |
|-----|--------|
| \`<Space>g\` | Quick Guide popup |
| \`<Space>h\` | Essential Shortcuts popup |
| \`<Space>t\` | Toggle terminal |
| \`<Space>w\` | Save file |
| \`<Space>←\` | Move to left window (lesson) |
| \`<Space>→\` | Move to right window (code) |
| \`<Space>ff\` | Find files |
| \`<Space>fg\` | Live grep search |
| \`<Space>fb\` | Browse buffers |
| \`<Space>xx\` | Show diagnostics |
| \`<Space>xz\` | Toggle Zen mode |

**Always available:**

| Key | Action |
|-----|--------|
| \`Ctrl+h\` | Move to left window |
| \`Ctrl+l\` | Move to right window |
| \`s\` | Flash jump (even in lessons!) |
| \`Ctrl+d/u\` | Page down/up |
| \`:w\` | Save |
| \`:q\` | Quit |

---

## 🎯 Three Ways to Use This

### 1️⃣ I'm Learning to Code

1. Install: \`bash <(curl -fsSL https://raw.githubusercontent.com/EanHD/learn/main/install.sh)\`
2. Start: \`learn\` (interactive mode)
3. Select a language and lesson
4. Read the lesson (left pane) and write code (right pane)
5. Press \`<Space>h\` anytime for help
6. Mark complete: \`learn --complete <lang> 1 1\`
7. Continue: \`learn --next\`
8. Track progress: \`learn --progress\`

### 2️⃣ I'm Learning a New Language

1. Pick from 14 languages
2. Start: \`learn python 1\` (or use interactive mode)
3. Each file starts with help comment
4. Press \`<Space>g\` for navigation guide
5. Lessons get progressively harder (Stage 1 → Stage 5)
6. Learn multiple languages to spot patterns!

### 3️⃣ I'm Teaching Others

All 490 lessons are organized by language:
\`c-c++/\`, \`rust/\`, \`python/\`, \`javascript/\`, \`typescript/\`, \`go/\`, \`lua/\`,
\`dart/\`, \`swift/\`, \`kotlin/\`, \`sql/\`, \`csharp/\`, \`shell/\`, \`powershell/\`

Each lesson includes:

- Clear learning objectives
- Step-by-step instructions
- Language-specific code examples
- Success checklists
- Additional explanations
- Progressive difficulty

Students can track their own progress with the built-in progress system!

---

## 📖 Documentation

| File | Description |
|------|-------------|
| [FEATURES.md](FEATURES.md) | Complete feature list |
| [MODE_VIM/README.md](MODE_VIM/README.md) | Neovim setup and keybindings |
| [CLI/README.md](CLI/README.md) | CLI commands and usage |
| [VIM_CHEATSHEET.md](VIM_CHEATSHEET.md) | Quick Vim reference |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |

---

## 🆘 Need Help?

### Platform Support

| Platform | Status | Installer |
|----------|--------|-----------|
| 🐧 **Linux** | ✅ Fully Supported | \`install.sh\` |
| 🍎 **macOS** | ✅ Fully Supported | \`install.sh\` |
| 🪟 **Windows** | ✅ Fully Supported | \`install.ps1\` |

**All platforms include:** One-shot install, auto-update, CLI, and full Neovim IDE.

### Common Issues

| Problem | Solution |
|---------|----------|
| Command not found | Linux/Mac: \`bash install.sh\` • Windows: Run \`install.ps1\` |
| Need to update | Linux/Mac: \`bash ~/LEARN/install.sh --update\` |
|  | Windows: \`powershell -File ~\LEARN\install.ps1 -Update\` |
| Neovim issues | See: [MODE_VIM/README.md](MODE_VIM/README.md) |
| CLI help | Run: \`learn --help\` |
| Vim basics | Read: [VIM_CHEATSHEET.md](VIM_CHEATSHEET.md) |

### Feature Questions

**"Which-key menu is cluttered"**
- It's been cleaned up! Only essential commands show now

**"Lesson formatting disappears on cursor line"**
- Fixed! Anti-conceal keeps formatting visible

**"Help comment missing in code files"**
- Fixed! All new and existing empty files get help comments

**"Can't remember keybindings"**
- Press \`<Space>\` and wait - which-key shows everything
- Press \`<Space>h\` for essential shortcuts popup
- Press \`<Space>g\` for quick navigation guide

**"Can I use this on Windows?"**
- Yes! Full Windows support via PowerShell installer
- Same features as Linux/Mac

---

## 💡 Tips

- **Use interactive mode** (\`learn\`) for the best experience
- **Start with Python or C++** if you're new (most forgiving)
- **Try Rust or Go** for systems programming
- **JavaScript/TypeScript for web**, **Dart for mobile**
- **Shell for DevOps**, **SQL for databases**
- **Kotlin for Android**, **Swift for iOS**
- **Press \`<Space>h\` in Neovim** for instant help
- **Track progress** with \`learn --progress\`
- **Learn multiple languages** to see programming patterns

---

## 🚀 What's Next?

\`\`\`bash
learn
\`\`\`

Launch the interactive menu and start your learning journey!

Or jump straight in:

\`\`\`bash
learn c++ 1          # C++
learn python 1       # Python
learn typescript 1   # TypeScript
learn kotlin 1       # Kotlin
learn sql 1          # SQL
\`\`\`

Everything you need is built into the CLI and IDE.

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

## 🌟 Star This Repo!

If you find LEARN helpful, please star it on GitHub!

---

**Happy Learning! 🎓**
