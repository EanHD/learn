# Learn CLI - Documentation Hub

Welcome to the **Enhanced Learn CLI** - a full-featured, interactive learning system for programming.

## 🚀 Quick Start

### First Time Setup
```bash
bash CLI/install.sh
```

### Launch Interactive Mode
```bash
learn
```

### Open a Specific Lesson
```bash
learn c++ 1              # C++ Stage 1, Level 1
learn python 1           # Python Stage 1, Level 1
```

## 📚 Documentation

Choose the guide that fits your needs:

- **[ENHANCED_README.md](ENHANCED_README.md)** - Complete guide to all features
- **[FEATURES.md](FEATURES.md)** - Detailed feature overview and capabilities
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - Upgrading from the old CLI
- **[README.md](README.md)** - This file (index + original CLI docs)

## 🎯 What's New?

The Enhanced CLI adds:
- ✅ Interactive menu system
- ✅ Multi-language support (20 languages!)
- ✅ Advanced progress tracking with JSON
- ✅ Completion tracking
- ✅ Visual statistics and progress bars
- ✅ Smart lesson suggestions
- ✅ Session history
- ✅ System diagnostics & setup (NEW - Option 9!)
- ✅ Better error handling
- ✅ Rich terminal output with colors and tables

**All while maintaining full backward compatibility!**

## 🎮 Interactive Menu (All Options)

When you run `learn`, you get this menu:

```
🎯 MAIN MENU

  1 Start a lesson (browse by category)
  2 Continue where you left off
  3 View progress
  4 Browse all lessons
  5 Switch language
  6 Mark lesson as complete
  7 View statistics
  8 Interactive Tutorial
  9 System Diagnostics & Setup
  0 Exit
```

### Option 9: System Diagnostics & Setup

**NEW!** Manage your system setup and configuration:

```
🔧 SYSTEM DIAGNOSTICS & SETUP

  1 Run system check (verify all dependencies)
  2 Run setup wizard (first-time setup)
  3 Reset progress (start over)
  4 Show configuration
  5 Install/Reinstall dependencies
  b Back to main menu
```

Perfect for:
- 🔍 Troubleshooting setup issues
- ✅ Verifying all dependencies are installed
- 🔧 Reinstalling tools if something breaks
- 📊 Viewing your configuration and paths
- ↩️ Starting fresh if needed

## 📦 Language Requirements

The CLI automatically checks that required language runtimes are available **before opening a lesson**. If a runtime is missing, you'll see:

```
⚠️  RUNTIME NOT FOUND

Node.js is required to run javascript lessons.

Install with:
  curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt install -y nodejs

Or select Option 9 from the main menu to install all dependencies.
```

### Supported Languages & Requirements

| Language | Runtime | Installation |
|----------|---------|--------------|
| C / C++ | GCC/G++ | `sudo apt install build-essential` |
| Rust | rustc | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| Python | Python 3 | `sudo apt install python3` |
| JavaScript | Node.js | `curl -fsSL https://deb.nodesource.com/setup_lts.x \| sudo -E bash - && sudo apt install -y nodejs` |
| TypeScript | Node.js + tsc | `npm install -g typescript` |
| Go | Go compiler | `sudo apt install golang-go` |
| Lua | Lua 5.4 | `sudo apt install lua5.4` |
| Dart | Dart SDK | `sudo apt install dart` |
| Swift | Swift | `sudo apt install swift` |
| Kotlin | Kotlin | `sudo apt install kotlin` |
| Java | JDK | `sudo apt install default-jdk` |
| C# | .NET SDK | `sudo apt install dotnet-sdk-latest` |
| Shell | Bash | Pre-installed on Linux |
| PowerShell | PowerShell Core | `sudo apt install -y powershell` |
| Zig | Zig | [Download](https://ziglang.org/download/) |
| SQL | SQLite3 | `sudo apt install sqlite3` |
| Julia | Julia | [Download](https://julialang.org/downloads/) |
| R | R language | `sudo apt install r-base` |
| PHP | PHP | `sudo apt install php-cli` |
| NoSQL | MongoDB shell | [Download](https://www.mongodb.com/try/download/shell) |

**Tip**: Use **Option 9 → Install/Reinstall dependencies** to install all runtimes at once!

---

# Original CLI Documentation

Below is the original documentation for reference. All these commands still work!

## Quick Reference

### Basic Commands

```bash
learn c++ 1              Open C++ Level 1 (Stage 1 by default)
learn rust 2             Open Rust Level 2
learn --list             List all available lessons
learn --help             Show help and examples
```

### Checking Progress

```bash
learn --info             Show your learning progress
learn --next             Get suggestion for next lesson
```

### Advanced Options

```bash
learn c++ 1 --stage 3    Jump to Stage 3, Level 1
learn c++ 1 --vscode     Open in VS Code instead of Vim
learn c++ 1 --terminal   Open in terminal pager
```

---

## Installation & Setup

### Make the Tool Executable

```bash
chmod +x ~/LEARN/CLI/learn
```

### (Optional) Add to PATH for System-Wide Access

Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$PATH:$HOME/LEARN/CLI"
```

Then reload:

```bash
source ~/.bashrc  # or source ~/.zshrc
```

After this, you can run `learn` from anywhere instead of `~/LEARN/CLI/learn`.

---

## Detailed Command Reference

### Opening Lessons

#### Open C++ Lesson

```bash
learn c++ 1              Level 1 (default: Stage 1)
learn c++ 3              Level 3
learn c++ 7              Level 7 (final level)
```

#### Open Rust Lesson

```bash
learn rust 1             Level 1
learn rust 2             Level 2
learn rust 5             Level 5
```

#### Jump to Specific Stage

```bash
learn c++ 1 --stage 1    Stage 1, Level 1 (explicit)
learn c++ 1 --stage 2    Stage 2, Level 1
learn c++ 3 --stage 3    Stage 3, Level 3
learn c++ 5 --stage 5    Stage 5, Level 5
```

#### Open in Different Modes

```bash
learn c++ 1 --vim        Open in Vim (default)
learn c++ 1 --vscode     Open in VS Code
learn c++ 1 --terminal   Open in terminal pager (less)
```

### Progress & Navigation

#### List All Lessons

```bash
learn --list
```

Shows organized list:
```
C++
==================================================

  Stage 1: Copying Code - Learn by doing
  ----------------------------------------
    Levels: 1, 2, 3, 4, 5, 6, 7

  Stage 2: Pseudocode to Code - Translate logic
  ----------------------------------------
    Levels: 1, 2, 3, 4, 5, 6, 7

  [... more stages ...]

Rust
==================================================
  [... same structure ...]
```

#### Check Your Progress

```bash
learn --info
```

Shows:
```
Your Learning Progress:
Total sessions: 15
Last session: c-c++ stage-1 level-3
```

#### Get Next Lesson Suggestion

```bash
learn --next
```

Shows intelligent suggestion based on your progress:
```
Next up: learn c++ 2  (Continue Stage 1)
```

#### Show Help

```bash
learn --help
```

Displays:
```
usage: learn [-h] [--list] [--info] [--next] [--stage STAGE] [--vim] [--vscode] [--terminal] [language] [level]

Learn programming with interactive lessons

positional arguments:
  language       Programming language (c++, rust)
  level          Level number (1-7)

options:
  -h, --help     show this help message and exit
  --list         List all available lessons
  --info         Show learning progress
  --next         Suggest next lesson
  --stage STAGE  Specific stage number (1-5)
  --vim          Open in Vim mode (default)
  --vscode       Open in VS Code
  --terminal     Open in terminal mode

Examples:
  learn c++ 1              # Open C++ Level 1 (default: vim mode)
  learn rust 2 --vim       # Rust Level 2 in Vim (split-screen)
  learn c++ 1 --vscode     # C++ Level 1 in VS Code
  learn --list             # List all lessons
  learn --next             # Suggest next lesson
  learn --info             # Show your progress
```

---

## Common Workflows

### Workflow 1: First Time Learning

```bash
# Step 1: See what's available
learn --list

# Step 2: Open first lesson
learn c++ 1

# Step 3: Inside Vim, read and code (see MODE_VIM docs for Vim commands)

# Step 4: Move to next lesson
learn c++ 2
```

### Workflow 2: Resuming Previous Session

```bash
# Check progress
learn --info
# Output: Last session: c-c++ stage-1 level-3

# Resume that lesson
learn c++ 3

# Or get suggestion
learn --next
# Output: Next up: learn c++ 4  (Continue Stage 1)

# Follow the suggestion
learn c++ 4
```

### Workflow 3: Jumping Between Stages

```bash
# Completed Stage 1, move to Stage 2
learn c++ 1 --stage 2

# Jump to Stage 3
learn c++ 1 --stage 3

# Or specific level in specific stage
learn c++ 5 --stage 4   # Stage 4, Level 5
```

### Workflow 4: Switching Languages

```bash
# Finished C++ Stage 1, start Rust
learn rust 1

# Or jump to same level in Rust
learn rust 2

# Or switch to Rust, Stage 2
learn rust 1 --stage 2
```

### Workflow 5: Using Different Editors

```bash
# Default: Vim (split-screen learning)
learn c++ 1

# Use VS Code instead
learn c++ 1 --vscode

# Use terminal pager (read-only)
learn c++ 1 --terminal

# Back to Vim
learn c++ 1 --vim
```

---

## Understanding Lesson Organization

### Structure

```
LEARN/
├── c-c++/
│   ├── stage-1/          Stage 1: Copying Code
│   │   ├── level-1/
│   │   ├── level-2/
│   │   └── ... level-7/
│   ├── stage-2/          Stage 2: Pseudocode to Code
│   │   ├── level-1/
│   │   └── ... level-7/
│   ├── stage-3/          Stage 3: Problem to Pseudocode
│   ├── stage-4/          Stage 4: Full Problem Solving
│   └── stage-5/          Stage 5: Capstone Projects
│
└── rust/                 (identical structure)
```

### The Five Stages

**Stage 1**: Learn by copying and understanding existing code
**Stage 2**: Translate pseudocode (English-like steps) into programs
**Stage 3**: Analyze problems and write your own pseudocode
**Stage 4**: Solve real-world problems completely independently
**Stage 5**: Build complete, professional-quality projects

### Lesson Content

Each lesson directory contains:

```
level-X/
├── lesson.md            The lesson content
├── solution.c           Your code workspace (C/C++)
└── solution.rs          Your code workspace (Rust)
```

---

## Command Behavior

### Lesson Discovery

When you run `learn c++ 3`:

1. CLI looks for level 3 in Stage 1 first
2. If Stage 1 exists, opens: `c-c++/stage-1/level-3/lesson.md`
3. If not found, searches other stages
4. Shows error if level 3 doesn't exist anywhere

This allows you to omit `--stage` for convenience.

### Progress Recording

Each time you open a lesson:

1. Session is recorded with timestamp
2. Language, stage, level, and mode stored
3. Data saved in `.learn-progress` file
4. `learn --info` reads this file
5. `learn --next` uses this data for suggestions

### File Creation

When opening a lesson in Vim mode:

1. If solution file doesn't exist, it's created
2. Populated with appropriate template (C or Rust)
3. Ready for you to start coding immediately

---

## Error Messages & Troubleshooting

### Error: "Lesson not found"

```bash
learn c++ 9
# Error: Lesson not found: c++ level 9
```

**Solution**: Levels only go 1-7. Try:
```bash
learn --list              # See valid levels
```

### Error: "Unknown language"

```bash
learn python 1
# Error: Unknown language: python
# Available: c++, rust
```

**Solution**: Only C++ and Rust are available:
```bash
learn c++ 1               # C++
learn rust 1              # Rust
```

### Error: "Neovim not found"

```bash
learn c++ 1
# Error: nvim not found
```

**Solution**: Install Neovim:
```bash
# Ubuntu/Debian
sudo apt install neovim

# macOS
brew install neovim
```

### Issue: Lesson appears in wrong stage

```bash
learn c++ 1
# Opens Stage 2, but you wanted Stage 1
```

**Solution**: Use `--stage` flag:
```bash
learn c++ 1 --stage 1     # Explicitly specify stage
```

### Issue: Progress not tracking

```bash
learn --info
# Shows: No progress recorded yet
```

**Solution**: Check file permissions:
```bash
ls -la ~/LEARN/.learn-progress
chmod 644 ~/LEARN/.learn-progress
```

---

## Using from Scripts

You can use the `learn` command in shell scripts:

### Example: Study 3 lessons

```bash
#!/bin/bash
learn c++ 1
learn c++ 2
learn c++ 3
```

### Example: Study all Stage 1

```bash
#!/bin/bash
for level in {1..7}; do
    echo "Opening Level $level..."
    learn c++ $level --stage 1
done
```

### Example: Track when you study

```bash
#!/bin/bash
echo "Study Session: $(date)" >> ~/LEARN/study-log.txt
learn c++ 1
echo "Session ended: $(date)" >> ~/LEARN/study-log.txt
```

---

## Advanced Usage

### Combine with Other Commands

```bash
# Count total lessons you've completed
wc -l ~/.learn-progress

# See your study history
cat ~/.learn-progress

# Search for Rust lessons you've opened
grep "rust" ~/.learn-progress

# See your most recent lessons
tail ~/.learn-progress
```

### Automate Your Study Plan

Create `~/LEARN/study-plan.sh`:

```bash
#!/bin/bash
# Study plan: 3 lessons per day for 5 days

echo "Day 1: Fundamentals"
learn c++ 1 --stage 1
learn c++ 2 --stage 1
learn c++ 3 --stage 1

echo "Day 2: More practice"
learn c++ 4 --stage 1
learn c++ 5 --stage 1
learn c++ 6 --stage 1

# ... continue for days 3-5
```

Run it:

```bash
chmod +x ~/LEARN/study-plan.sh
~/LEARN/study-plan.sh
```

---

## Quick Tips

### Tip 1: Alias for Faster Typing

Add to `~/.bashrc`:

```bash
alias learn-cpp='learn c++'
alias learn-rs='learn rust'
```

Then:

```bash
learn-cpp 1          # Same as: learn c++ 1
learn-rs 2           # Same as: learn rust 2
```

### Tip 2: Check Progress Regularly

```bash
# Daily check
learn --info

# See what's next
learn --next
```

### Tip 3: Jump Stages When Ready

```bash
# Finished Stage 1
learn c++ 1 --stage 2

# Skipped a stage? No problem
learn c++ 1 --stage 4
```

### Tip 4: Use Terminal Mode for Reading Only

```bash
# Just read without editing
learn c++ 1 --terminal

# Useful for reviewing past lessons
```

### Tip 5: Track Multiple Languages

```bash
# Study C++ first
learn c++ 1
learn c++ 2

# Then Rust
learn rust 1
learn rust 2

# Progress tracks both
learn --info
```

---

## Getting Help

### In Terminal

```bash
learn --help             Show all options
learn --list             See all lessons
learn --info             Check progress
learn --next             Get suggestion
```

### Documentation

- **Quick Reference**: `MODE_VIM/QUICK_REFERENCE.md`
- **Complete Guide**: `MODE_VIM/COMPLETE_SETUP.md`
- **Navigation Help**: `MODE_VIM/NAVIGATION_GUIDE.md`
- **All Docs**: `VIM_MODE_DOCUMENTATION_INDEX.md`

### Inside Vim

When a lesson is open:

```vim
<leader>?               Show Vim help
:call LessonInfo()      Show lesson info
:help vim               Full Vim documentation
```

---

## Summary

The `learn` CLI tool provides:

- Easy access to all 70 lessons
- Smart navigation between lessons
- Progress tracking
- Support for multiple editing modes
- Flexible learning paths
- Simple command structure

### Most Common Commands

```bash
learn c++ 1              Open a lesson
learn --list             See what's available
learn --info             Check progress
learn --next             Get suggestion
```

Start learning now:

```bash
learn c++ 1
```

For detailed documentation, see: `VIM_MODE_DOCUMENTATION_INDEX.md`

