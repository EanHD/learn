# Get Started Learning to Code

Learn programming through **hands-on lessons** in **20 programming languages**.

**490 lessons** across **5 stages**. Start coding in **under 5 minutes**.

## 🚀 Quick Start

### Option 1: Interactive Mode (Recommended)

```bash
learn
```

Launches an **interactive menu** to browse lessons, check progress, and start learning.

### Option 2: Jump to a Specific Lesson

```bash
learn open c++ 1 1       # C++ Stage 1, Level 1
learn open python 1 2    # Python Stage 1, Level 2
learn open typescript 1 1    # TypeScript Stage 1, Level 1
learn open kotlin 1 1    # Kotlin Stage 1, Level 1
```

### Option 3: First Time? Run the Setup Wizard

```bash
learn init
```

This checks your system, installs dependencies, and creates your workspace.

## 📋 Common Commands

| Command | What It Does |
|---------|-------------|
| `learn` | Interactive menu |
| `learn browse` | Browse languages by category ⭐ NEW |
| `learn tip` | Get random programming tips ⭐ NEW |
| `learn open c++ 1 1` | Open C++ Stage 1, Level 1 |
| `learn list` | See all 490 lessons |
| `learn progress` | View your progress |
| `learn next` | Continue where you left off |
| `learn doctor` | Check system dependencies |
| `learn --help` | Full command reference |

## 🎯 What You'll Learn

| Stage | What It Is |
|-------|-----------|
| 1 | Copy working code, learn syntax |
| 2 | Turn pseudocode into real code |
| 3 | Design solutions to small problems |
| 4 | Build full projects from scratch |
| 5 | Create your own capstone |

**Languages available:** C/C++, Rust, Go, Zig, JavaScript, TypeScript, Python, PHP, Dart, Swift, Kotlin, SQL, NoSQL, R, Julia, Shell, PowerShell, Lua, Java, C#

**7 lessons per stage** × **5 stages** × **20 languages** = **490 total lessons**

## 🎮 Choose Your Editor

By default, lessons open in **Neovim** with split-screen view (lesson on left, code on right).

**Or pick your favorite:**

```bash
learn open c++ 1 1 --vim        # Neovim split-screen (default)
learn open c++ 1 1 --vscode     # VS Code
learn open c++ 1 1 --terminal   # Read-only terminal view
```

**Vim Instructions:**
When you launch Vim, you'll see language-specific compile/run commands:

```text
Compile/Run (in code window):
    :!make run         -> C++ (compile + run)
```

For other languages:

- **Rust:** `:!cargo run`
- **Python:** `:!python3 %`
- **JavaScript:** `:!node %`
- **Go:** `:!go run %`
- **Lua:** `:!lua %`

## ⚠️ System Check

If something doesn't work, run:

```bash
learn doctor
```

This checks for missing tools (Neovim, compilers, LSP servers) and shows you how to fix them.

## 💡 Pro Tips

- **First time?** Start with: `learn init`
- **Explore languages:** `learn browse` to see categories
- **Get inspired:** `learn tip` for random programming wisdom
- **Stuck?** Read the lesson again. Solutions are at the bottom.
- **Fast learner?** Jump to advanced: `learn open c++ 5 1`
- **Check progress:** `learn progress`
- **Next lesson:** `learn next`
- **Mark as complete:** `learn complete c++ 1 1`

## 📖 Documentation

- **Full tutorial:** Read `README.md`
- **Command help:** Run `learn --help`
- **Vim/Neovim tips:** See `.docs/VIM_CHEATSHEET.md`
- **Troubleshooting:** See `.docs/SETUP_DEV.md`
- **Contributing:** See `CONTRIBUTING.md`

## Your Learning Journey

Learn → Practice → Build → Master

### Week 1: Foundations (Stage 1)

```bash
learn open c++ 1 1    # Variables, syntax, basics
```

### Week 2: Logic (Stage 2)

```bash
learn open c++ 2 1    # Conditionals, loops, functions
```

### Week 3-4: Problem Solving (Stages 3-4)

```bash
learn open c++ 3 1    # Design and build
```

### Week 5-6: Mastery (Stage 5)

```bash
learn open c++ 5 1    # Your own project
```

## 🎓 By the End, You'll Have

- Written 35+ programs
- Learned fundamentals of your chosen language(s)
- Built real projects from scratch
- Developed problem-solving skills
- A foundation to continue learning independently

## Ready to Start?

```bash
learn init
```

Then explore:

```bash
learn browse          # See all language categories
learn open c++ 1 1    # Or jump right in
```

You've got this. Start now.

---

**Questions?** Run `learn --help` or see `README.md`

**Found a bug?** File an issue on GitHub with details

**Want to contribute?** See `CONTRIBUTING.md`
