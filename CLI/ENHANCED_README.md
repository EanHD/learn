# Enhanced Learn CLI - Complete Guide

## 🚀 Quick Start

### Interactive Mode (Recommended)
```bash
learn
```

This launches a full-featured interactive menu where you can:
- Browse and select lessons
- Track your progress
- Continue where you left off
- Switch between languages
- Mark lessons as complete
- View detailed statistics

### Command Line Mode
```bash
learn c++ 1              # Open C++ Stage 1, Level 1
learn rust 3 --stage 2   # Open Rust Stage 2, Level 3
learn python 1           # Open Python Stage 1, Level 1
learn --next             # Continue from last lesson
learn --progress         # View your progress
```

## 🎯 Features

### ✨ New in Enhanced CLI

1. **Interactive Menu System**
   - User-friendly interface
   - Easy navigation
   - Visual progress bars
   - Intuitive lesson selection

2. **Multi-Language Support**
   - C++
   - Rust
   - Python
   - JavaScript
   - Go
   - Lua

3. **Advanced Progress Tracking**
   - JSON-based progress storage
   - Completion tracking per lesson
   - Session history
   - Detailed statistics
   - Progress percentages

4. **Smart Lesson Navigation**
   - Automatic "next lesson" suggestions
   - Continue where you left off
   - Jump to any stage/level
   - Browse all lessons

5. **Flexible Editor Modes**
   - Vim (with split view)
   - VS Code
   - Terminal (read-only)

## 📚 Command Reference

### Interactive Mode

```bash
learn              # Start interactive menu
learn -i           # Explicit interactive mode
learn --interactive
```

**Interactive Menu Options:**
1. Start a lesson - Select language, stage, and level
2. Continue learning - Pick up where you left off
3. View progress - See completion stats
4. Browse all lessons - See what's available
5. Switch language - Change to different language
6. Mark lesson complete - Track completed lessons
7. View statistics - Detailed learning stats

### Direct Lesson Access

```bash
# Open specific lesson
learn <language> <level> [--stage N]

# Examples
learn c++ 1                    # C++ Stage 1, Level 1
learn rust 5 --stage 3         # Rust Stage 3, Level 5
learn python 2                 # Python Stage 1, Level 2
learn javascript 4 --stage 2   # JavaScript Stage 2, Level 4
```

### Progress Commands

```bash
learn --progress     # View your progress
learn --next         # Get next lesson suggestion
learn --list         # List all available lessons
```

### Completion Tracking

```bash
# Mark a lesson as complete
learn --complete <lang> <stage> <level>

# Examples
learn --complete c++ 1 1       # Mark C++ Stage 1, Level 1 complete
learn --complete rust 2 3      # Mark Rust Stage 2, Level 3 complete
```

### Editor Modes

```bash
learn c++ 1 --vim        # Open in Vim (default)
learn c++ 1 --vscode     # Open in VS Code
learn c++ 1 --terminal   # Open in terminal (read-only)
```

## 🗂️ Lesson Organization

### Structure
```
LEARN/
├── c-c++/
│   ├── stage-1/    # Copying Code
│   ├── stage-2/    # Pseudocode to Code
│   ├── stage-3/    # Problem to Pseudocode
│   ├── stage-4/    # Full Problem Solving
│   └── stage-5/    # Capstone Projects
├── rust/           # Same structure
├── python/         # Same structure
├── javascript/     # Same structure
├── go/             # Same structure
└── lua/            # Same structure
```

Each stage has 7 levels (lessons).

### The Five Stages

**Stage 1: Copying Code**
- Learn by understanding and copying working code
- Focus on syntax and basic patterns
- Build muscle memory

**Stage 2: Pseudocode to Code**
- Translate step-by-step instructions into real code
- Learn to think algorithmically
- Practice implementation

**Stage 3: Problem to Pseudocode**
- Analyze problems and design solutions
- Write your own pseudocode
- Plan before coding

**Stage 4: Full Problem Solving**
- Complete autonomy
- Solve real-world problems
- Apply all learned skills

**Stage 5: Capstone Projects**
- Build complete applications
- Professional-quality code
- Portfolio-worthy projects

## 📊 Progress Tracking

### Progress File

Progress is stored in `.learn-progress.json` with:
- Session history
- Lesson completion status
- Timestamps
- Statistics

### View Your Progress

**Interactive Mode:**
- Option 3: View progress
- Option 7: View statistics

**Command Line:**
```bash
learn --progress
```

**Manual Inspection:**
```bash
cat ~/.../LEARN/.learn-progress.json | python3 -m json.tool
```

### Mark Lessons Complete

**Interactive Mode:**
- Option 6: Mark lesson as complete

**Command Line:**
```bash
learn --complete c++ 1 1
```

## 🎨 Editor Modes

### Vim Mode (Default)

**Features:**
- Split-screen layout
- Lesson on left, code on right
- Full Vim capabilities
- Auto-creates solution file with template

**Usage:**
```bash
learn c++ 1              # Default is Vim
learn c++ 1 --vim        # Explicit Vim mode
```

### VS Code Mode

**Features:**
- Opens entire lesson directory
- Access to all files
- VS Code extensions available
- Integrated terminal

**Usage:**
```bash
learn c++ 1 --vscode
```

### Terminal Mode

**Features:**
- Read-only viewing
- Uses `less` pager
- No file editing
- Great for review

**Usage:**
```bash
learn c++ 1 --terminal
```

## 🔧 Installation

### Make Executable

```bash
chmod +x ~/LEARN/CLI/learn
chmod +x ~/LEARN/CLI/learn_cli.py
```

### Add to PATH

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$PATH:$HOME/LEARN/CLI"
```

Reload:
```bash
source ~/.bashrc
```

### Verify Installation

```bash
learn --help
```

## 💡 Usage Examples

### Example 1: First-Time User

```bash
# Launch interactive mode
learn

# Select option 1 (Start a lesson)
# Choose language: 1 (C++)
# Stage: 1
# Level: 1
# Mode: 1 (Vim)

# Read lesson, write code, practice
# Exit Vim with :q

# Continue to next lesson
learn

# Select option 2 (Continue learning)
```

### Example 2: Experienced User

```bash
# Jump directly to specific lesson
learn rust 5 --stage 3

# Mark it complete when done
learn --complete rust 3 5

# Check progress
learn --progress

# Get next suggestion
learn --next
```

### Example 3: Multiple Languages

```bash
# Work on C++ lessons
learn c++ 1
learn c++ 2
learn c++ 3

# Switch to Python
learn python 1
learn python 2

# View progress across all languages
learn --progress
```

### Example 4: Browse and Select

```bash
# See all available lessons
learn --list

# Interactive browsing
learn
# Option 4: Browse all lessons
```

## 📈 Progress Tracking Features

### Automatic Tracking

Every time you open a lesson, the CLI automatically tracks:
- Timestamp
- Language
- Stage and level
- Editor mode used
- Number of times opened

### Completion Tracking

Mark lessons as complete to:
- Track your learning journey
- See completion percentages
- Get accurate "next lesson" suggestions
- View detailed statistics

### Statistics View

See:
- Total lessons available per language
- Lessons completed
- Completion percentage
- Visual progress bars
- Session count
- Learning start date
- Last accessed lesson

## 🎯 Workflows

### Workflow 1: Linear Learning Path

```bash
# Day 1
learn c++ 1
learn --complete c++ 1 1

# Day 2
learn --next    # Suggests c++ Stage 1, Level 2
learn --complete c++ 1 2

# Continue...
```

### Workflow 2: Multi-Language Learning

```bash
# Morning: C++
learn c++ 1
learn --complete c++ 1 1

# Afternoon: Rust (same concepts)
learn rust 1
learn --complete rust 1 1

# Evening: Review progress
learn --progress
```

### Workflow 3: Stage-Based Progression

```bash
# Complete Stage 1
learn c++ 1 --stage 1
learn c++ 2 --stage 1
# ... through level 7

# Move to Stage 2
learn c++ 1 --stage 2
```

### Workflow 4: Jump Around

```bash
# Skip ahead if experienced
learn rust 1 --stage 3

# Go back if needed
learn rust 5 --stage 1

# Browse what's available
learn --list
```

## 🔍 Troubleshooting

### CLI Not Found

```bash
# Check if in PATH
echo $PATH | grep LEARN

# Add to PATH
export PATH="$PATH:$HOME/LEARN/CLI"
```

### Lesson Not Found

```bash
# Verify lesson exists
learn --list

# Check language name
# Use: c++, rust, python, javascript, go, lua
```

### Progress Not Saving

```bash
# Check file permissions
ls -la ~/LEARN/.learn-progress.json

# Create if missing
touch ~/LEARN/.learn-progress.json
```

### Vim Not Opening

```bash
# Install Neovim
sudo apt install neovim  # Ubuntu/Debian
brew install neovim      # macOS

# Or use different mode
learn c++ 1 --vscode
learn c++ 1 --terminal
```

## 🆚 Old vs New CLI

### Old CLI Features
- Basic lesson opening
- Simple progress file
- Limited language support (C++, Rust)
- Manual navigation
- Basic commands

### New CLI Additions
✨ Interactive menu system
✨ Multi-language support (6 languages)
✨ JSON-based progress tracking
✨ Completion tracking
✨ Statistics and analytics
✨ Smart lesson suggestions
✨ Visual progress bars
✨ Session history
✨ Improved navigation
✨ Better error handling

## 🚀 Tips & Tricks

### Tip 1: Start with Interactive Mode

```bash
learn    # Easiest way to get started
```

### Tip 2: Use --next for Continuity

```bash
learn --next    # Always know what to do next
```

### Tip 3: Mark Lessons Complete

```bash
learn --complete c++ 1 1    # Track your progress
```

### Tip 4: Review Progress Regularly

```bash
learn --progress    # Stay motivated
```

### Tip 5: Try Multiple Languages

```bash
# Learn same concepts in different languages
learn c++ 1
learn rust 1
learn python 1
```

### Tip 6: Use Appropriate Mode

```bash
--vim       # Best for focused learning
--vscode    # Best for larger projects
--terminal  # Best for quick review
```

## 📱 Quick Reference Card

```
COMMANDS
├── learn                    Interactive mode
├── learn <lang> <level>     Open lesson
├── learn --next             Continue learning
├── learn --progress         View progress
├── learn --list             List lessons
├── learn --complete         Mark complete
└── learn --help             Show help

LANGUAGES
├── c++, cpp
├── rust, rs
├── python, py
├── javascript, js
├── go
└── lua

STAGES
├── 1: Copying Code
├── 2: Pseudocode to Code
├── 3: Problem to Pseudocode
├── 4: Full Problem Solving
└── 5: Capstone Projects

MODES
├── --vim        Vim editor (default)
├── --vscode     VS Code
└── --terminal   Read-only view
```

## 🎓 Getting Started Guide

### Step 1: Installation
```bash
chmod +x ~/LEARN/CLI/learn
export PATH="$PATH:$HOME/LEARN/CLI"
```

### Step 2: First Lesson
```bash
learn
# Select: 1 (Start a lesson)
# Select: 1 (C++)
# Stage: 1
# Level: 1
# Mode: 1 (Vim)
```

### Step 3: Complete and Continue
```bash
# After completing lesson
learn --complete c++ 1 1

# Move to next
learn --next
```

### Step 4: Track Progress
```bash
learn --progress
```

## 📝 Notes

- Progress file: `.learn-progress.json`
- Solution files auto-created with templates
- All modes support all languages
- Progress tracked automatically
- Completion tracking is manual (intentional)
- Interactive mode recommended for beginners
- Command line mode great for scripts/automation

## 🎉 What's Next?

Start learning now:
```bash
learn
```

Everything you need is built into the CLI!

Happy learning! 🚀
