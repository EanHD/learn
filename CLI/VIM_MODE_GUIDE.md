# Enhanced Vim Mode - User Guide

## Overview

The Learn CLI now features an **enhanced Vim learning mode** with automatic split-screen layout, flash instructions, and helpful shortcuts designed specifically for learning programming.

## What's New

✅ **Pre-Launch Instructions** - See navigation guide before entering Vim
✅ **Auto Split-Screen** - Lesson on left, code on right  
✅ **Flash Help Popup** - Auto-appears after 1.5 seconds
✅ **Smart Status Line** - Shows which window you're in
✅ **Auto-Save** - Code saves when switching windows
✅ **Read-Only Lesson** - Prevents accidental lesson edits
✅ **Quick Shortcuts** - All essential commands at your fingertips

## Launch Experience

### Step 1: Pre-Launch Instructions

When you run `learn c++ 1 --vim`, you'll see:

```
======================================================================
  🚀 LAUNCHING VIM LEARNING MODE
======================================================================

📖 QUICK NAVIGATION GUIDE:

   Windows:
     Ctrl-w h / Ctrl-w l    → Switch between lesson and code
    Ctrl-w =           → Balance window sizes

  Lesson Navigation:
    j / k              → Scroll down/up
    Ctrl-d / Ctrl-u    → Page down/up
    gg / G             → Top/Bottom

  Editing (in code window):
    i                  → Insert mode
    Esc                → Normal mode
    :w                 → Save file

  Help:
    <Space>?           → Show full help
    :q                 → Quit

💡 TIP: Lesson is on the LEFT, your code is on the RIGHT
======================================================================

Press ENTER to launch Vim...
```

### Step 2: Vim Opens

After pressing ENTER:
- Vim launches with split-screen layout
- Lesson (read-only) on the LEFT
- Your code workspace on the RIGHT
- Windows balanced automatically

### Step 3: Welcome Message

You'll immediately see:
```
📚 Learning Mode | Press <Space>? for help | :q to quit
```

### Step 4: Quick Help (Auto-Appears)

After 1.5 seconds, a help message automatically flashes on screen with all essential commands.

## Window Layout

```
┌─────────────────────────┬─────────────────────────┐
│                         │                         │
│   📖 LESSON             │   ✏️  CODE              │
│   (Read-Only)           │   (Your Workspace)      │
│                         │                         │
│   - Learn concepts      │   - Write your code     │
│   - Read instructions   │   - Practice exercises  │
│   - View examples       │   - Test solutions      │
│                         │                         │
│   Scroll with j/k       │   Edit with i           │
│   Search with /text     │   Save with :w          │
│                         │                         │
└─────────────────────────┴─────────────────────────┘
```

## Essential Commands

### Switch Between Windows

| Command | Action |
|---------|--------|
| `Ctrl-h` | Go to LEFT window (lesson) |
| `Ctrl-l` | Go to RIGHT window (code) |
| `Ctrl-w =` | Balance window sizes |

**Tip:** These are the MOST IMPORTANT commands to remember!

### Navigate Lesson (Left Window)

| Command | Action |
|---------|--------|
| `j` / `k` | Move down/up one line |
| `Ctrl-d` | Page down (half page) |
| `Ctrl-u` | Page up (half page) |
| `gg` | Go to top of file |
| `G` | Go to bottom of file |
| `/text` | Search forward for "text" |
| `n` | Next search result |

### Edit Code (Right Window)

| Command | Action |
|---------|--------|
| `i` | Enter INSERT mode (start typing) |
| `a` | Append after cursor |
| `o` | Open new line below |
| `Esc` | Exit INSERT mode (back to NORMAL) |
| `:w` | Save your code |
| `dd` | Delete current line |
| `p` | Paste |
| `u` | Undo |
| `Ctrl-r` | Redo |

### Quick Actions

| Command | Action |
|---------|--------|
| `<Space>?` | Show quick help |
| `:q` | Quit (must save first with `:w`) |
| `:wq` | Save and quit |
| `:q!` | Quit without saving |

## Status Line

The bottom status line shows:

```
📖  lesson.md [RO]                                    1:1
```

Or when in code window:

```
✏️   solution.cpp                                    5:15
```

**Legend:**
- 📖 = You're in the LESSON window
- ✏️ = You're in the CODE window
- `[RO]` = Read-only (lesson)
- `1:1` = Line:Column position

## Features

### 1. Auto-Split Layout

When you open a lesson, Vim automatically:
- Creates a vertical split
- Opens lesson on the left
- Opens your code file on the right
- Balances the window sizes
- Focuses on the lesson first

**No manual setup required!**

### 2. Read-Only Lesson

The lesson file is automatically set to read-only to prevent accidental edits.

**Want to add notes?**
- Press `<Space>e` to toggle edit mode
- Press again to lock it back

### 3. Auto-Save

Your code automatically saves when you switch from the code window to the lesson window.

**No more lost work!**

### 4. Smart Shortcuts

All essential commands are mapped to easy-to-remember keys:
- Window navigation: `Ctrl-h/l`
- Quick help: `<Space>?`
- Quick save: `:w`

### 5. Enhanced Status Line

Always know which window you're in with the emoji indicators:
- 📖 = Lesson (read)
- ✏️ = Code (edit)

## Typical Workflow

### 1. Read the Lesson
```
1. Press ENTER at pre-launch screen
2. Vim opens with lesson visible (left window)
3. Read the lesson using j/k or Ctrl-d/u
4. Use /text to search for specific topics
```

### 2. Write Code
```
1. Press Ctrl-w l to switch to code window (right)
2. Press i to enter INSERT mode
3. Type your code
4. Press Esc when done
5. Press :w to save
```

### 3. Test and Refine
```
1. Open terminal: :term
2. Compile and run your code
3. Switch back: Ctrl-w w
4. Press Ctrl-h to read lesson again
5. Press Ctrl-l to edit code again
```

### 4. Finish
```
1. Make sure code is saved (:w)
2. Type :q to quit
```

## Tips & Tricks

### Tip 1: Learn These 3 Commands First

Master these and you'll be 80% effective:
1. `Ctrl-w h` / `Ctrl-w l` - Switch windows
2. `i` - Start editing
3. `:wq` - Save and quit

### Tip 2: Use Visual Mode

Select code to copy:
1. Press `v` to start visual selection
2. Move with `j/k` to select lines
3. Press `y` to yank (copy)
4. Press `p` to paste

### Tip 3: Split Terminal

Open a terminal without leaving Vim:
1. Type `:term`
2. Terminal opens in new split
3. Type your command
4. Press `Ctrl-\ Ctrl-n` to exit terminal mode
5. Type `:q` to close terminal

### Tip 4: Search and Replace

Replace text in your code:
1. Type `:%s/old/new/g`
2. Replaces all "old" with "new"
3. Add `c` flag for confirmation: `:%s/old/new/gc`

### Tip 5: Multiple Files

Open another file:
1. Type `:e filename.cpp`
2. Or `:split filename.cpp` for horizontal split
3. Use `Ctrl-w w` to cycle through windows

## Troubleshooting

### Help popup doesn't appear?
- It appears after 1.5 seconds
- Press `<Space>?` to show it manually

### Can't edit lesson?
- Lessons are read-only by default (good!)
- Press `<Space>e` to toggle if you need to add notes

### Code not saving?
- Make sure you're in the code window (Ctrl-l)
- Type `:w` to save manually
- Or it auto-saves when switching windows

### Window sizes unbalanced?
- Press `Ctrl-w =` to balance them

### Lost in windows?
- Look at the status line:
  - 📖 = Lesson window
  - ✏️ = Code window

### Want bigger text?
- Zoom in terminal: `Ctrl-+` (in your terminal app)
- Or increase font size in terminal settings

## Vim Basics Reminder

### Modes in Vim

**NORMAL mode** (default):
- Navigate
- Run commands
- Cannot type text

**INSERT mode** (press `i`):
- Type text like normal editor
- Press `Esc` to exit

**VISUAL mode** (press `v`):
- Select text
- Press `y` to copy, `d` to delete

### Why These Modes?

Vim is designed for efficiency:
- NORMAL mode: Fast navigation
- INSERT mode: Typing
- Separate modes = Powerful shortcuts

**New to Vim?** Don't worry!
- `i` to start typing
- `Esc` to stop typing
- That's 90% of what you need!

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════╗
║           VIM LEARNING MODE - QUICK REFERENCE          ║
╠═══════════════════════════════════════════════════════╣
║  SWITCH WINDOWS:                                       ║
║    Ctrl-w h      → Lesson (left)                       ║
║    Ctrl-w l      → Code (right)                        ║
║                                                        ║
║  NAVIGATE LESSON:                                      ║
║    j/k           → Down/Up                             ║
║    Ctrl-d/u      → Page down/up                        ║
║    gg / G        → Top/Bottom                          ║
║                                                        ║
║  EDIT CODE:                                            ║
║    i             → Insert mode                         ║
║    Esc           → Normal mode                         ║
║    :w            → Save                                ║
║    :q            → Quit                                ║
║                                                        ║
║  HELP:                                                 ║
║    <Space>?      → Show help                           ║
╚═══════════════════════════════════════════════════════╝
```

## Advanced Features

### Available (for advanced users):

- `:split` - Horizontal split
- `:vsplit` - Vertical split
- `:tabnew` - New tab
- Window resizing with `Ctrl-w >` and `Ctrl-w <`
- Marks: `ma` to set mark 'a', `'a` to jump back
- Registers: `"ay` to yank to register 'a'
- Macros: `qa` to record, `@a` to replay

### Not needed for learning:

The enhanced mode is designed to work out of the box. Advanced features are available if you want to explore, but the basic setup is perfect for learning.

## Summary

**The Enhanced Vim Mode gives you:**

✅ Instant split-screen setup (lesson + code)
✅ Pre-launch instructions
✅ Flash help that auto-appears
✅ Simple navigation (Ctrl-h/l)
✅ Auto-save protection
✅ Visual status indicators
✅ Everything configured perfectly for learning

**Just:**
1. Launch: `learn c++ 1`
2. Press ENTER
3. Start learning!

**That's it! Everything else is automatic.**

---

**Still have questions?**
- Press `<Space>?` in Vim for quick help
- See `VIM_CHEATSHEET.md` for more Vim basics
- Check `CLI/TROUBLESHOOTING.md` for common issues

Happy learning! 🚀
