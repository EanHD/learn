# LEARN - Quick Reference Card

## Essential Commands

### Launch Interactive Menu
```bash
learn
```
Browse all lessons, track progress, and start learning interactively.

---

### Explore & Learn

**Browse by category:** ⭐ NEW
```bash
learn browse               # Show all categories
learn browse --category web    # Jump to web languages
learn browse --guided      # Get extra tips
```

**Get inspired:** ⭐ NEW
```bash
learn tip                  # Random programming wisdom
```

**Open a lesson:**
```bash
learn open python 1 1      # Python Stage 1, Level 1
learn open java 1 1        # Java Stage 1, Level 1
learn open rust 2 3        # Rust Stage 2, Level 3
```

**Choose your editor:**
```bash
learn open python 1 1 --vim       # Neovim (default)
learn open python 1 1 --vscode    # VS Code
learn open python 1 1 --terminal  # Terminal view
```

---

### Track Progress

```bash
learn progress             # View your stats
learn next                 # Get next recommended lesson
learn complete python 1 1  # Mark lesson as done
```

---

### System Commands

```bash
learn doctor               # Check dependencies
learn init                 # First-time setup
learn config --show        # View settings
learn list                 # List all 490 lessons
learn --help               # Show all commands
```

---

## 20 Languages by Category

| Category | Languages |
|----------|-----------|
| **Core** 🧠 | C/C++, Rust, Go, Zig |
| **Web** 💻 | JavaScript, TypeScript, Python, PHP |
| **Mobile** 📱 | Swift, Kotlin, Dart |
| **Data** 🧮 | SQL, NoSQL, R, Julia |
| **Scripting** ⚙️ | Shell, PowerShell, Lua |
| **Enterprise** �� | Java, C# |

---

## Learning Path: 5 Stages

1. **Copy Code** - Learn syntax by typing working examples
2. **Pseudocode** - Convert logic descriptions to real code
3. **Design** - Plan solutions before coding
4. **Build** - Complete projects from scratch
5. **Capstone** - Create your own full-featured project

**Time estimate:** 60-90 hours total

---

## First Time?

1. Run `learn` to see the interactive menu
2. Pick a language from any category
3. Start with **Stage 1, Level 1**
4. Copy code and press `<Space>r` to run
5. Check help with `<Space>h`

---

## Useful Commands

```bash
learn list                 # Show all 490 lessons
learn list --language java # Filter by language
learn doctor               # Check system setup
learn config --show        # View settings
learn config --editor vim  # Change default editor
```

---

## Files and Setup

Each language has:

- `TABLE_OF_CONTENTS.md` - Complete course overview
- `WORKSPACE_INSTRUCTIONS.md` - Setup and how to run code
- 35 lessons (5 stages × 7 levels)

Install language tools before starting:

```bash
learn doctor               # Check what's missing
learn doctor --fix         # Show install commands
```

---

**Happy Learning!**

For full details, see [START_HERE.md](START_HERE.md) or [README.md](README.md)
