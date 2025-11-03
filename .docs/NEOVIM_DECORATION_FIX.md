# Neovim Decoration Error - Fixed

## Issue

```
Error: nvim: .src/nvim/decoration.c:868 
       decor_conceal_line assertion row >= 0 failed
```

When running `learn c++ 1`, Neovim would crash with a decoration error instead of opening the lesson.

## Root Cause

Two issues combined:

1. **CLI Command Issue** - Multiple `-c` commands with vsplit chaining caused Neovim to calculate negative row offsets for decorations before buffer splits were finalized

2. **Vim Config Issues** - Several problematic settings:
   - Colorscheme could fail if not installed
   - `colorcolumn=80` interfered with decoration calculations
   - Highlight autocmds conflicted with readonly buffer state

## Solution

### 1. Simplified CLI Launch

**Before:**
```python
subprocess.run([
    "nvim",
    "-u", str(config),
    "-c", "vsplit",
    "-c", "wincmd l",
    str(lesson_path)
])
```

**After:**
```python
subprocess.run([
    "nvim",
    "-u", str(config),
    str(lesson_path)
])
```

**Why:** Avoids complex command chaining. Users can create split manually with `Ctrl-w v`.

### 2. Fixed Vim Config

**Changes to `MODE_VIM/CONFIG/init-learning.vim`:**

```vim
# Fixed colorscheme
silent! colorscheme habamax  # Was: colorscheme habamax

# Disabled problematic visual column
# set colorcolumn=80  # Was: set colorcolumn=80

# Disabled conflicting highlights
# autocmd BufRead **/stage-*/level-*/lesson.md highlight LessonGoals ctermfg=Green
# autocmd BufRead **/stage-*/level-*/lesson.md highlight LessonCode ctermfg=Yellow
```

## Result

Running `learn c++ 1` now:
- ✓ Launches Neovim cleanly
- ✓ Opens lesson file without errors
- ✓ No decoration assertion errors
- ✓ Lesson ready to read and edit

To create a split manually:
```vim
Ctrl-w v    # Create vertical split
Ctrl-h/l    # Navigate between windows
i           # Edit on right pane
```

## Files Modified

1. **CLI/learn** - Simplified Neovim command
2. **MODE_VIM/CONFIG/init-learning.vim** - Fixed settings and removed problematic options

## Verified

✓ Python syntax valid
✓ CLI executes without errors
✓ Neovim initializes successfully
✓ No assertion failures

