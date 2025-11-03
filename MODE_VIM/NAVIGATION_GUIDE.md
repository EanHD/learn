# Lesson Navigation Guide - VIM MODE

This guide shows you how to seamlessly navigate through all your lessons using both Vim commands and the CLI tool.

## Quick Reference

### Navigate Between Levels (within a stage)

From inside Neovim:

```vim
:call NextLesson()        " Jump to next level (e.g., Level 1 → Level 2)
:call PrevLesson()        " Jump to previous level
:call LessonInfo()        " Show current stage/level
:call ShowLessonHelp()    " Show all keyboard commands
```

Or use leader key shortcuts:

```vim
<leader>n                 " Next lesson
<leader>p                 " Previous lesson  
<leader>i                 " Show current lesson info
<leader>?                 " Show help popup
```

### Window Navigation

```vim
C-h                       " Move to left window (lesson)
C-l                       " Move to right window (code)
C-j                       " Move to bottom window (terminal)
C-k                       " Move to top window

C-=                       " Equal-size all windows
C-+                       " Make current window wider
C-_                       " Make current window narrower
```

### Essential Vim Commands

```vim
gg                        " Jump to top of lesson
G                         " Jump to bottom of lesson
/pattern                  " Search forward for text
?pattern                  " Search backward
n                         " Go to next search result
N                         " Go to previous search result

ma                        " Mark current position as 'a'
'a                        " Jump back to mark 'a'

:w                        " Save code file
:q                        " Quit Vim
```

---

## Using the CLI Tool for Navigation

### Open a Specific Lesson

```bash
# Open C++ Level 1 (default: Vim mode)
learn c++ 1

# Open Rust Level 3
learn rust 3

# Specific stage
learn c++ 2 --stage 2     " C++, Stage 2, Level 2

# Different mode
learn c++ 1 --vscode      " Open in VS Code
learn rust 1 --terminal   " Open in terminal pager
```

### List All Lessons

```bash
learn --list
```

Shows all available lessons organized by language, stage, and level:

```
C++
==================================================

  Stage 1: Copying Code - Learn by doing
  ----------------------------------------
    Levels: 1, 2, 3, 4, 5, 6, 7

  Stage 2: Pseudocode to Code - Translate logic
  ----------------------------------------
    Levels: 1, 2, 3, 4, 5, 6, 7

  [... and so on ...]
```

### Check Your Progress

```bash
# Show learning progress so far
learn --info

# Get suggestion for next lesson
learn --next
```

---

## Complete Workflow: Start to Finish

### 1. List What's Available

```bash
learn --list
```

### 2. Open Your First Lesson

```bash
learn c++ 1
```

This opens C++ Level 1 in Vim mode with:
- Lesson text on the left (read-only)
- Empty code file on the right (ready to edit)

### 3. Navigate Inside Vim

```vim
" Read the lesson
gg                    " Go to top
G                     " Go to bottom
/learning goals       " Search for a section
n                     " Next match

" Switch to code window
C-l                   " Move right

" Write your solution
i                     " Enter insert mode
" ... type your code ...
Esc                   " Exit insert mode
:w                    " Save

" Open terminal
C-j                   " Move down (if terminal window exists)
" or
:terminal             " Create new terminal

" Compile and run
gcc solution.c -o solution && ./solution
exit                  " Exit terminal (back to editing)

" Move to next lesson when done
:call NextLesson()    " Jump to Level 2
```

### 4. Move Between Lessons

**From the command line:**

```bash
learn c++ 2           " Open Level 2
learn c++ 3           " Open Level 3
```

**From inside Vim:**

```vim
:call NextLesson()    " Go to next level
:call PrevLesson()    " Go to previous level
```

### 5. Track Your Progress

```bash
learn --info          " See total sessions and last opened lesson
```

---

## Stage Progression

Learn at your own pace through the 5 stages:

**Stage 1: Copying Code** (7 lessons)
- Learn by copying and understanding existing code
- Build a foundation of programming concepts

**Stage 2: Pseudocode to Code** (7 lessons)
- Translate pseudocode (English-like steps) into working programs
- Learn to interpret specifications

**Stage 3: Problem to Pseudocode** (7 lessons)
- Read a problem and write your own pseudocode
- Learn problem decomposition

**Stage 4: Full Problem Solving** (7 lessons)
- Complete independence: read problem → solve completely
- Professional-level autonomy

**Stage 5: Capstone Projects** (7 lessons)
- Build meaningful, complete applications
- Create portfolio-worthy projects

---

## Tips for Smooth Navigation

### 1. Bookmark Important Concepts

In Vim, mark positions for quick jumping:

```vim
ma                    " Mark current line as 'a'
mb                    " Mark current line as 'b'
'a                    " Jump back to mark 'a'
'b                    " Jump back to mark 'b'
```

Useful for:
- Bookmarking important definitions
- Marking the problem statement
- Jumping to key concepts

### 2. Use Search Efficiently

```vim
/Learning Goals       " Find the learning goals
n                     " Jump to next match
N                     " Jump to previous match

/TODO                 " Find tasks in your code
```

### 3. Split Your Study Sessions

Each level is designed to take 30-60 minutes:

```bash
# Morning: Levels 1-2
learn c++ 1
learn c++ 2

# Afternoon: Levels 3-4
learn c++ 3
learn c++ 4
```

### 4. Keep Multiple Levels Open (Advanced)

Vim supports multiple buffers:

```vim
:e ../../../level-2/solution.c    " Open another level
:bn                               " Next buffer
:bp                               " Previous buffer
C-^                               " Toggle between last two buffers
```

### 5. Save Your Session

Save your Vim workspace to resume later:

```vim
:mksession lesson1.vim            " Save current session
```

Restore it later:

```bash
nvim -S lesson1.vim
```

---

## Troubleshooting Navigation

**Q: Can't find next level?**

```vim
:call LessonInfo()            " Check current stage/level
:call NextLesson()            " Shows error if no next level exists
```

**Q: Lost track of which level I'm on?**

```vim
:call LessonInfo()            " Shows: Stage: X | Level: Y/7
:edit .                       " Shows file path in tree view
```

**Q: Want to jump to a specific stage?**

```bash
learn c++ 1 --stage 2         " Jump to Stage 2, Level 1
learn c++ 3 --stage 4         " Jump to Stage 4, Level 3
```

**Q: How do I go back to previous session?**

```bash
learn --info                  " See your last opened lesson
learn c++ 3                   " Open that same lesson again
```

---

## Advanced: Custom Navigation Shortcuts

Add these to your Neovim config for even faster navigation:

```vim
" Jump to stage 2
nnoremap <leader>s2 :call JumpToStage(2)<CR>

" Bookmark important sections
nnoremap <leader>b1 ma
nnoremap <leader>b2 mb
nnoremap <leader>b3 mc

" Quick lesson restart
nnoremap <leader>restart :edit!<CR>
```

---

## Summary

You have multiple ways to navigate:

1. **CLI commands** - Best for switching between lessons: `learn c++ 1`, `learn rust 2`
2. **Vim commands** - Best while learning: `:call NextLesson()`, `C-h/l` for windows
3. **Keyboard shortcuts** - Fastest once you memorize them: `<leader>n`, `C-l`
4. **Search** - Best for finding concepts: `/pattern`, `n`, `N`

Mix and match based on your workflow!

