# VIM MODE Integration Guide

This document shows how all VIM MODE components work together to create a seamless learning experience.

## Architecture Overview

```
LEARN/ (Root Directory)
├── CLI/
│   └── learn              Python CLI tool (main entry point)
│
├── MODE_VIM/              VIM MODE subsystem
│   ├── README.md          Overview (start here)
│   ├── COMPLETE_SETUP.md  Full setup guide
│   ├── QUICK_START.md     Quick reference
│   ├── QUICK_REFERENCE.md One-page cheat sheet
│   ├── NAVIGATION_GUIDE.md Detailed navigation
│   ├── FAQ.md             Common questions
│   ├── CONFIG/
│   │   └── init-learning.vim   Neovim configuration
│   ├── TEMPLATES/
│   │   ├── code-template.c
│   │   └── code-template.rs
│   └── WORKFLOWS/
│       └── split-screen-learning.md
│
├── c-c++/
│   └── stage-{1-5}/
│       └── level-{1-7}/
│           ├── lesson.md
│           └── solution.{c,cpp,h}
│
└── rust/
    └── stage-{1-5}/
        └── level-{1-7}/
            ├── lesson.md
            └── solution.rs
```

## Data Flow

### User Interaction

```
User Command
    ↓
"learn c++ 1"
    ↓
CLI Tool (learn)
    ↓
Finds lesson path: c-c++/stage-1/level-1/lesson.md
Creates solution file: c-c++/stage-1/level-1/solution.c
Records progress: .learn-progress
    ↓
Launches Neovim with init-learning.vim config
    ↓
Vim Opens Split Screen:
  - Left: lesson.md (read-only)
  - Right: solution.c (editable)
  - Bottom: Terminal (optional)
    ↓
User learns and codes
    ↓
"learn c++ 2" or :call NextLesson()
    ↓
(repeat)
```

## Component Interactions

### 1. CLI Tool → Lesson Discovery

The `learn` command:

1. Parses arguments: `learn c++ 1 --stage 2 --vim`
2. Normalizes language: `c++ → c-c++`
3. Searches all stages for lesson
4. Finds: `/home/eanhd/LEARN/c-c++/stage-2/level-1/lesson.md`
5. Creates solution file if needed
6. Records session in `.learn-progress`

### 2. Vim Config → Learning Environment

The `init-learning.vim` config:

1. Sets visual preferences (line numbers, colors, highlights)
2. Configures keyboard shortcuts (C-h/l for windows)
3. Defines custom functions (NextLesson, PrevLesson, etc)
4. Enables terminal integration
5. Protects lesson files (read-only by default)

### 3. Navigation Functions → Lesson Jumping

Custom Vim functions enable intelligent navigation:

**NextLesson():**
- Reads current file path
- Extracts stage and level numbers
- Increments level
- Loads next lesson if it exists
- Shows error if at final level

**PrevLesson():**
- Similar logic going backwards
- Prevents moving before Level 1

**LessonInfo():**
- Displays current stage/level in status bar
- Helps learners track progress

### 4. Progress Tracking

Each time a lesson opens:

1. CLI records: timestamp, language, stage, level, mode
2. Data written to `.learn-progress` file
3. `learn --info` reads this file
4. Displays session count and last opened lesson

## Usage Scenarios

### Scenario 1: Complete Beginner

```bash
# 1. See what's available
learn --list

# 2. Start C++ Stage 1
learn c++ 1

# 3. Read lesson (10-15 min)
# Inside Vim: gg, /, n, G

# 4. Write code (15-25 min)
# Inside Vim: C-l, i, :w

# 5. Test (5-10 min)
# Inside Vim: :terminal, gcc..., exit

# 6. Next level
# From shell: learn c++ 2
# Or from Vim: :call NextLesson()
```

### Scenario 2: Multi-Stage Learner

```bash
# Completed Stage 1, move to Stage 2
learn c++ 1 --stage 2

# Or search from CLI
learn --next           # Suggests next lesson

# Jump around as needed
learn c++ 5 --stage 4  # Jump to Stage 4, Level 5
learn rust 3           # Switch languages
```

### Scenario 3: Return to Learning Session

```bash
# Check progress
learn --info
# Output: "Last session: rust stage-2 level-3"

# Resume
learn rust 3 --stage 2

# Or just
learn rust 3           # CLI finds it across all stages
```

### Scenario 4: Advanced Vim User

```bash
# Start lesson
learn c++ 1

# Inside Vim: use custom functions
:call NextLesson()         # Next
:call PrevLesson()         # Previous
:call LessonInfo()         # Current status

# Use marks for bookmarking
ma                         # Mark position A
'a                         # Jump back

# Record macros
qa ... q                   # Record
@a                         # Play

# Multiple buffers
:e ../../../level-2/solution.c
:bn / :bp                  # Navigate buffers
```

## Key Features Enabled by Integration

### 1. Seamless Transitions

No context-switching between tools:
- Lesson viewing in Vim (not external markdown viewer)
- Code editing in Vim (not VSCode)
- Compilation in Vim terminal (not external shell)

### 2. Intelligent Navigation

- CLI finds lessons across all stages automatically
- Vim functions handle sequential level progression
- Progress tracking remembers where you left off

### 3. Customizable Experience

Users can choose:
- Mode: `--vim` (default), `--vscode`, `--terminal`
- Language: C++, Rust
- Stage: Can jump directly to any stage
- Navigation: CLI or Vim commands

### 4. Learning Preservation

- Progress files track all sessions
- Vim sessions can be saved/restored
- Code templates standardize starting points
- Configuration is reusable across all lessons

## Customization Points

### 1. Modify Vim Config

Edit `/home/eanhd/LEARN/MODE_VIM/CONFIG/init-learning.vim`:

```vim
" Add custom keybindings
nnoremap <leader>x :call MyFunction()<CR>

" Modify colors
colorscheme dracula     " Instead of habamax

" Change indent size
set tabstop=2           " Instead of 4
```

### 2. Add Custom Functions

In the same config file:

```vim
function! MyCustomFunction()
    echo "Custom behavior here"
endfunction

nnoremap <leader>c :call MyCustomFunction()<CR>
```

### 3. Extend CLI Tool

Edit `/home/eanhd/LEARN/CLI/learn`:

```python
# Add new mode
def open_lesson_custom_mode(self, lang, level):
    # Custom implementation
    pass

# Add new flag
parser.add_argument("--custom", action="store_true")
```

## Performance Considerations

### CLI Tool

- Lesson discovery: O(n) where n = number of stages
  - Typically finds lesson in <50ms
- Progress tracking: Append-only file
  - Fast writes, minimal overhead

### Vim Config

- Functions execute on-demand (not auto)
- No background processes
- Minimal memory overhead
- Config loads once per session

### Overall

- First lesson load: ~500ms (Vim startup + config)
- Subsequent lessons: ~200ms (Vim + file loading)
- No impact on editing performance

## Troubleshooting Integration

### Issue: CLI can't find lesson

```bash
# Check lesson exists
ls ~/LEARN/c-c++/stage-1/level-1/lesson.md

# Use absolute path
learn --list | grep "Stage 1"
```

### Issue: Vim functions not working

```vim
# Check config loaded
:scriptnames | grep init-learning.vim

# Test function
:call LessonInfo()

# If error, check config syntax
:set nocompatible
:syntax on
```

### Issue: Progress not tracking

```bash
# Check progress file
cat ~/.learn-progress

# Or check file permissions
ls -la ~/LEARN/.learn-progress
```

### Issue: Wrong stage being opened

```bash
# Use --stage flag explicitly
learn c++ 1 --stage 3

# Check all stages
learn --list | grep "Level 1"
```

## Future Enhancements

### Planned

1. **MODE_VSCODE** - VS Code-optimized learning
2. **Compilation integration** - Auto-compile on save
3. **Testing framework** - Run lesson tests automatically
4. **Achievement system** - Track completion of stages
5. **Difficulty ratings** - Feedback from learners

### Architecture Ready For

- Multiple programming languages (add new dirs)
- Different learning frameworks (new MODE_* dirs)
- Progress analytics (parse .learn-progress)
- Collaborative features (share progress)

## Summary

VIM MODE integrates:
- **CLI tool** for easy lesson access
- **Vim configuration** for optimized environment
- **Custom functions** for intelligent navigation
- **Progress tracking** for resuming sessions
- **Professional documentation** for support

All components work together to create a distraction-free, efficient learning experience that teaches both programming AND Vim mastery simultaneously.

