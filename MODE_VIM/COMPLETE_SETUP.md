# Complete VIM MODE Setup & Learning Guide

This guide walks you through setting up and using VIM MODE for a seamless, professional learning experience.

## What is VIM MODE?

VIM MODE combines the power of Neovim with structured programming lessons. You learn **programming AND Vim** simultaneously in a split-screen environment:

- **Left pane**: Lesson content (read-only) with learning goals, concepts, and examples
- **Right pane**: Your code editor (write your solutions here)
- **Bottom pane**: Terminal for compilation and testing

Everything happens within Neovim. No context-switching to external editors or markdown viewers.

## Installation

> **🪟 Windows Users:** See **[WINDOWS_SETUP.md](WINDOWS_SETUP.md)** for complete Windows installation guide including Chocolatey, CMake, and MinGW setup.

### Step 1: Ensure Neovim is Installed

```bash
nvim --version
```

If not installed:

```bash
# Ubuntu/Debian
sudo apt install neovim

# macOS
brew install neovim

# Windows (PowerShell as Admin)
choco install neovim

# Or visit: https://neovim.io/
```

### Step 2: Ensure Compilers and Build Tools are Installed

For C++:

```bash
gcc --version  # or clang
```

For Rust:

```bash
rustc --version
```

For Neovim plugins (CMake required):

```bash
cmake --version
```

If missing:

```bash
# Ubuntu/Debian
sudo apt install build-essential rustc cmake

# macOS
brew install gcc rust cmake

# Windows (PowerShell as Admin)
choco install mingw rust cmake
```

**Windows users:** CMake and MinGW are **required** for telescope-fzf-native plugin. See [WINDOWS_SETUP.md](WINDOWS_SETUP.md).

### Step 3: Make the CLI Tool Executable

```bash
chmod +x ~/LEARN/CLI/learn
```

Optional: Add to PATH for system-wide access:

```bash
# Add this line to ~/.bashrc or ~/.zshrc
export PATH="$PATH:$HOME/LEARN/CLI"

# Then reload
source ~/.bashrc  # or source ~/.zshrc
```

After this, you can run `learn` from anywhere instead of `python3 ~/LEARN/CLI/learn`.

## Your First Lesson (5 minutes)

### 1. Navigate to Learn Directory

```bash
cd ~/LEARN
```

### 2. List Available Lessons

```bash
learn --list
```

This shows all 70 lessons organized by:
- Language (C++, Rust)
- Stage (1-5)
- Level (1-7 per stage)

### 3. Open Your First Lesson

```bash
learn c++ 1
```

This opens C++ Stage 1, Level 1 in Neovim with your learning config automatically applied.

### 4. Understand the Layout

Inside Neovim, you'll see:

```
 Lesson (LEFT)            Code (RIGHT)
 
 Learning Goals           #include <stdio.h>
 ================         
 - Understand variables   int main() {
 - Practice declarations    // Your code here
                            return 0;
 Key Concepts             }
 - Variables hold data...
 
 
 Terminal (optional, open with :terminal)
```

### 5. Start Learning

**In the LEFT pane (lesson):**

- Read the learning goals
- Understand the concepts
- Review examples

Use Vim navigation:
- `gg` to jump to top
- `G` to jump to bottom
- `/text` to search
- `n` to find next match

**In the RIGHT pane (code):**

- Press `C-l` to move right
- Press `i` to enter insert mode
- Write your code solution
- Press `Esc` then `:w` to save

**In the TERMINAL:**

- Press `:terminal` to open terminal
- Compile: `gcc solution.c -o solution && ./solution`
- Or for Rust: `rustc solution.rs -o solution && ./solution`
- Press `exit` to return to editor

## Navigation Reference

### Between Lessons

Using CLI (from terminal):

```bash
learn c++ 2             # Move to Level 2
learn c++ 3             # Move to Level 3
learn rust 1            # Switch languages
learn c++ 1 --stage 2   # Jump to Stage 2, Level 1
```

Using Vim (inside editor):

```vim
:call NextLesson()      # Jump to next level
:call PrevLesson()      # Jump to previous level
:call LessonInfo()      " Show current stage/level
```

### Window Navigation

```vim
C-h                     " Move to LEFT pane (lesson)
C-l                     " Move to RIGHT pane (code)
C-j                     " Move to BOTTOM pane (terminal)
C-k                     " Move up

C-=                     " Make windows equal size
C-+                     " Make current window wider
C-_                     " Make current window narrower
```

### Essential Editing

```vim
i                       " Start typing (insert mode)
Esc                     " Stop typing (normal mode)
:w                      " Save your code
dd                      " Delete a line
p                       " Paste
/pattern                " Search for text
n                       " Go to next match
```

## Typical Learning Session

**Time: 30-60 minutes per lesson**

1. **Open lesson** (1 min):

   ```bash
   learn c++ 1
   ```

2. **Read & understand** (10-15 min):

   ```vim
   gg                    " Jump to top
   /Learning Goals       " Find what you need to learn
   G                     " Go to bottom to see examples
   ```

3. **Write code** (10-20 min):

   ```vim
   C-l                   " Move to code pane
   i                     " Start typing
   " ... write your solution ...
   Esc                   " Done editing
   :w                    " Save
   ```

4. **Test your code** (5-10 min):

   ```vim
   :terminal             " Open terminal
   gcc solution.c -o solution && ./solution
   exit                  " Exit terminal
   ```

5. **Move to next lesson** (1 min):

   ```bash
   learn c++ 2
   ```

Or from inside Vim:

```vim
:call NextLesson()
```

## Progress Tracking

Check your learning progress:

```bash
learn --info
```

Shows:
- Total number of sessions completed
- Last lesson you opened

This helps you remember where you left off.

## The Five Stages

### Stage 1: Copying Code (7 lessons)

**Goal**: Learn by copying and understanding existing code
- Copy provided code
- Run it to see results
- Understand what each line does
- Begin recognizing patterns

### Stage 2: Pseudocode to Code (7 lessons)

**Goal**: Translate English-like instructions to code
- Read pseudocode (step-by-step English)
- Translate each step to actual code
- Develop logic translation skills
- Start writing without examples

### Stage 3: Problem to Pseudocode (7 lessons)

**Goal**: Read a problem and write your own solution plan
- Analyze the problem
- Break it into steps (pseudocode)
- Implement the pseudocode as code
- Learn problem decomposition

### Stage 4: Full Problem Solving (7 lessons)

**Goal**: Complete independence
- Read a problem
- Solve it completely on your own
- No pseudocode provided
- Professional-level autonomy

### Stage 5: Capstone Projects (7 lessons)

**Goal**: Build complete, meaningful applications
- Design a full project
- Plan multiple features
- Implement production-ready code
- Create portfolio-worthy projects

## Advanced Tips

### Save Your Session

Before closing, save your Vim session:

```vim
:mksession mylessonX.vim
```

Restore it later:

```bash
nvim -S mylessonX.vim
```

### Bookmark Important Concepts

Mark positions for quick jumping:

```vim
ma                      " Mark position as 'a'
'a                      " Jump back to 'a'
```

Use marks to return to important definitions or examples.

### Multiple Buffers

Keep multiple files open:

```vim
:e ../../../level-2/solution.c    " Open another level
:bn                               " Next buffer
:bp                               " Previous buffer
C-^                               " Toggle between last two
```

### Record Macros

Record complex editing patterns:

```vim
qa                      " Start recording macro 'a'
" ... type your commands ...
q                       " Stop recording
@a                      " Play macro 'a'
```

## Troubleshooting

**Q: Lesson looks hard to read?**

```bash
# Reopen with simpler config
nvim c-c++/stage-1/level-1/lesson.md

# Then in Vim:
:set number
:set relativenumber
```

**Q: Can't compile?**

Make sure compiler is installed:

```bash
gcc --version
rustc --version
```

**Q: Lost in navigation?**

```bash
# Check where you are
learn --list            " See all lessons
learn --info            " See what you've done
```

**Q: Want to start over?**

Just open any lesson again:

```bash
learn c++ 1             " Jump to Level 1
```

## Next Steps

1. Complete **Stage 1**: Focus on understanding code patterns
2. Complete **Stage 2**: Practice translating instructions
3. Complete **Stage 3**: Start designing your own solutions
4. Complete **Stage 4**: Code completely independently
5. Complete **Stage 5**: Build impressive projects!

Each stage takes roughly 1-2 weeks with consistent 1-hour daily sessions.

## Quick Commands Cheat Sheet

```bash
# CLI Commands
learn --list            List all lessons
learn --info            Show your progress
learn --next            Get suggestion
learn c++ 1             Open C++ Level 1
learn rust 2 --stage 3  Open Rust Stage 3, Level 2
learn c++ 1 --vscode    Open in VS Code instead
learn c++ 1 --terminal  Open in terminal pager

# Vim Navigation (inside editor)
C-h/C-l                 Move left/right between panes
C-j/C-k                 Move down/up between panes
C-= / C-+ / C-_         Resize panes

# Vim Lesson Control
<leader>n               Next lesson
<leader>p               Previous lesson
<leader>i               Show lesson info
<leader>?               Show help

# Essential Vim
gg / G                  Top/bottom of file
/text / ?text           Search forward/backward
i / Esc                 Insert mode on/off
:w / :q                 Save/quit
:terminal               Open terminal
```

## Support

For questions or issues:

1. Check [NAVIGATION_GUIDE.md](NAVIGATION_GUIDE.md) for detailed navigation help
2. Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for command reference
3. Check [FAQ.md](FAQ.md) for common questions
4. Look at [WORKFLOWS/split-screen-learning.md](WORKFLOWS/split-screen-learning.md) for detailed examples

## Ready to Start?

Open your first lesson:

```bash
learn c++ 1
```

Welcome to VIM MODE. Happy learning!

