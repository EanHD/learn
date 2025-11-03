# Learn CLI - Quick Reference Card

## Installation
```bash
bash CLI/install.sh       # Run installer
source ~/.bashrc          # Reload shell
```

## Basic Commands
```bash
learn                     # Interactive menu (recommended!)
learn c++ 1               # Open C++ Stage 1, Level 1
learn rust 3 --stage 2    # Open Rust Stage 2, Level 3
learn python 1            # Open Python Stage 1, Level 1
learn --help              # Show help
```

## Progress & Navigation
```bash
learn --progress          # View progress with stats
learn --next              # Get next lesson suggestion
learn --list              # List all available lessons
learn --complete c++ 1 1  # Mark lesson as complete
```

## Editor Modes
```bash
learn c++ 1               # Vim (default)
learn c++ 1 --vim         # Vim (explicit)
learn c++ 1 --vscode      # VS Code
learn c++ 1 --terminal    # Terminal (read-only)
```

## Interactive Mode Menu
```
1. Start a lesson         → Select language, stage, level
2. Continue learning      → Pick up where you left off
3. View progress         → See completion stats
4. Browse all lessons    → See what's available
5. Switch language       → Change languages
6. Mark lesson complete  → Track completion
7. View statistics       → Detailed stats
0. Exit                  → Quit
```

## Languages
```bash
learn c++ 1              # C++
learn rust 1             # Rust
learn python 1           # Python
learn javascript 1       # JavaScript / js
learn go 1               # Go
learn lua 1              # Lua
```

## Aliases
```
c++, cpp       → C++
rust, rs       → Rust
python, py     → Python
javascript, js → JavaScript
go             → Go
lua            → Lua
```

## Stage & Level
```bash
--stage N                # Stage number (1-5)
N                        # Level number (1-7)

# Examples
learn c++ 1 --stage 1    # Stage 1, Level 1
learn c++ 5 --stage 3    # Stage 3, Level 5
learn rust 7             # Stage 1, Level 7 (default stage)
```

## The Five Stages
```
Stage 1: Copying Code          → Learn syntax
Stage 2: Pseudocode to Code    → Translate logic
Stage 3: Problem to Pseudocode → Design solutions
Stage 4: Full Problem Solving  → Complete autonomy
Stage 5: Capstone Projects     → Professional work
```

## Typical Workflows

### First-Time User
```bash
learn                    # Launch interactive
# Select: 1 → 1 (C++) → 1 → 1 → 1 (Vim)
learn --complete c++ 1 1 # Mark complete
learn --next             # Get next
```

### Daily Learning
```bash
learn --next             # Continue from yesterday
# Complete lesson
learn --complete c++ 1 2
learn --progress         # Check stats
```

### Multi-Language
```bash
learn c++ 1              # C++ version
learn --complete c++ 1 1
learn rust 1             # Same concept, Rust
learn --complete rust 1 1
learn --progress         # Compare progress
```

### Exploration
```bash
learn --list             # See all lessons
learn python 1           # Try Python
learn javascript 1       # Try JavaScript
```

## File Structure
```
LEARN/
├── .learn-progress.json      # Your progress (JSON)
├── .learn-progress           # Old progress (text)
├── c-c++/stage-N/level-N/
│   ├── lesson.md            # Lesson content
│   └── solution.cpp         # Your code
├── rust/stage-N/level-N/
│   ├── lesson.md
│   └── solution.rs
└── [python|javascript|go|lua]/
    └── ... same structure
```

## Progress File
**Location:** `LEARN/.learn-progress.json`

**View manually:**
```bash
cat LEARN/.learn-progress.json | python3 -m json.tool
```

**View in CLI:**
```bash
learn --progress
```

## Common Errors

### "Command not found"
```bash
bash CLI/install.sh
source ~/.bashrc
```

### "Lesson not found"
```bash
learn --list             # Check available lessons
```

### "nvim not found"
```bash
sudo apt install neovim  # Ubuntu/Debian
brew install neovim      # macOS
# Or use: learn c++ 1 --vscode
```

## Tips

💡 Use interactive mode for discovery: `learn`
💡 Use commands for speed: `learn c++ 1`
💡 Mark lessons complete: `learn --complete`
💡 Check progress often: `learn --progress`
💡 Try multiple languages: same concepts, different syntax
💡 Jump stages if experienced: `--stage 3`
💡 Solutions in lesson files: scroll to bottom

## Statistics

📊 Total lessons: **210+**
📊 Languages: **6**
📊 Stages: **5**
📊 Levels per stage: **7**

## Key Features

✅ Interactive menu
✅ Multi-language support
✅ Progress tracking
✅ Completion tracking  
✅ Statistics & analytics
✅ Smart suggestions
✅ Auto-generated templates
✅ Session history
✅ Three editor modes
✅ Visual progress bars

## Getting Help

```bash
learn --help             # CLI help
learn                    # Interactive menu (most intuitive)
```

**Documentation:**
- `CLI/ENHANCED_README.md` - Complete guide
- `CLI/FEATURES.md` - Feature details
- `CLI/MIGRATION_GUIDE.md` - Upgrading guide
- `CLI/QUICK_REFERENCE.md` - This file

## Example Session

```bash
# Morning
learn                    # Interactive mode
# Option 2: Continue learning
# Opens: C++ Stage 1, Level 3
# Complete the lesson
learn --complete c++ 1 3

# Afternoon  
learn --progress         # Check stats
# C++: 3/35 lessons (8.6%)
# [██░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 8.6%

learn --next             # What's next?
# Next: learn c++ 4

learn c++ 4              # Open lesson 4
# Complete it
learn --complete c++ 1 4

# Evening
learn --progress         # Review progress
# C++: 4/35 lessons (11.4%)
```

## Start Learning Now!

```bash
learn
```

**That's it!** Everything else you'll learn from the interactive menus and lessons.

---

**Print this reference card and keep it handy while learning!**
