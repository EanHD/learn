# Enhanced Learn CLI - Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      User Interface                          │
│  ┌────────────────────┐         ┌────────────────────────┐  │
│  │  Interactive Mode  │         │   Command-Line Mode    │  │
│  │   (Menu System)    │         │  (Direct Commands)     │  │
│  └────────┬───────────┘         └──────────┬─────────────┘  │
│           │                                 │                 │
│           └─────────────┬───────────────────┘                 │
│                         ▼                                     │
│              ┌──────────────────────┐                         │
│              │  InteractiveCLI      │                         │
│              │  (Main Coordinator)  │                         │
│              └──────────┬───────────┘                         │
└─────────────────────────┼─────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌───────────────┐  ┌──────────────┐  ┌──────────────┐
│ ProgressTracker│  │LessonManager │  │LessonExecutor│
│  (Data Layer)  │  │ (Discovery)  │  │  (Actions)   │
└───────┬───────┘  └──────┬───────┘  └──────┬───────┘
        │                 │                 │
        │                 │                 │
        ▼                 ▼                 ▼
┌────────────────────────────────────────────────────┐
│              File System & Resources               │
│  ┌──────────┐  ┌──────────┐  ┌─────────────────┐  │
│  │Progress  │  │ Lessons  │  │ Solution Files  │  │
│  │  JSON    │  │   MD     │  │   (cpp,rs,etc)  │  │
│  └──────────┘  └──────────┘  └─────────────────┘  │
└────────────────────────────────────────────────────┘
```

## Component Details

### User Interface Layer

#### Interactive Mode
```
┌──────────────────────────────┐
│      Main Menu               │
├──────────────────────────────┤
│  1. Start a lesson           │
│  2. Continue learning         │
│  3. View progress            │
│  4. Browse all lessons       │
│  5. Switch language          │
│  6. Mark lesson complete     │
│  7. View statistics          │
│  0. Exit                     │
└──────────────────────────────┘
```

**Flow:**
1. User selects option
2. Submenu for details (if needed)
3. Action executed
4. Feedback displayed
5. Return to menu

#### Command-Line Mode
```
learn <command> [options]
    │
    ├─→ Direct lesson access
    ├─→ Progress queries
    ├─→ Completion marking
    └─→ Information display
```

### Application Layer

#### InteractiveCLI Class
**Role:** Main coordinator and UI controller

```
InteractiveCLI
├── run_interactive_mode()
│   └─→ Main menu loop
├── _select_language_and_lesson()
│   └─→ Lesson selection flow
├── _open_lesson()
│   └─→ Coordinates opening
├── _view_progress()
│   └─→ Display statistics
├── _continue_learning()
│   └─→ Smart resume
└── _mark_lesson_complete()
    └─→ Completion tracking
```

### Data Layer

#### ProgressTracker Class
**Role:** Progress management and statistics

```
ProgressTracker
├── _load_progress()
│   └─→ Load JSON file
├── _save_progress()
│   └─→ Save JSON file
├── mark_lesson_opened()
│   └─→ Record session
├── mark_lesson_completed()
│   └─→ Mark complete
├── get_next_lesson()
│   └─→ Suggest next
└── get_completion_stats()
    └─→ Calculate stats
```

**Data Flow:**
```
User Action
    ↓
mark_lesson_opened()
    ↓
Load JSON → Update Data → Save JSON
    ↓
Session Recorded
```

#### LessonManager Class
**Role:** Lesson discovery and information

```
LessonManager
├── _discover_languages()
│   └─→ Scan directories
├── find_lesson()
│   └─→ Locate lesson file
├── list_all_lessons()
│   └─→ Get all lessons
└── get_lesson_file_extension()
    └─→ File extension map
```

**Discovery Flow:**
```
Startup
    ↓
Scan LEARN/
    ↓
For each language dir:
    ├─→ Check stages
    ├─→ Check levels
    └─→ Build lesson map
    ↓
Return available lessons
```

#### LessonExecutor Class
**Role:** Lesson opening and file management

```
LessonExecutor
├── open_vim()
│   └─→ Neovim with split
├── open_vscode()
│   └─→ VS Code
├── open_terminal()
│   └─→ Less pager
└── _create_solution_template()
    └─→ Generate template
```

**Execution Flow:**
```
Open Lesson Request
    ↓
Check solution file exists?
    ├─→ No: Create template
    └─→ Yes: Use existing
    ↓
Launch editor
    ├─→ Vim: nvim + split
    ├─→ VS Code: code
    └─→ Terminal: less
```

## Data Flow Diagrams

### Opening a Lesson

```
User: learn c++ 1
    ↓
InteractiveCLI.main()
    ↓
Parse arguments
    ↓
InteractiveCLI._open_lesson()
    ↓
┌─────────────────────────────────────┐
│  1. LessonManager.find_lesson()     │
│     └─→ Returns lesson path          │
│                                      │
│  2. ProgressTracker.mark_opened()   │
│     └─→ Records session              │
│                                      │
│  3. LessonExecutor.open_vim()       │
│     ├─→ Check solution file          │
│     ├─→ Create if needed             │
│     └─→ Launch nvim                  │
└─────────────────────────────────────┘
    ↓
Lesson opened in editor
```

### Viewing Progress

```
User: learn --progress
    ↓
InteractiveCLI._view_progress()
    ↓
┌─────────────────────────────────────┐
│  For each language:                 │
│    ├─→ ProgressTracker.             │
│    │   get_completion_stats()       │
│    │   └─→ Count complete/total      │
│    │                                 │
│    └─→ Display:                      │
│        ├─→ Completed lessons         │
│        ├─→ Percentage                │
│        └─→ Progress bar              │
└─────────────────────────────────────┘
    ↓
Progress displayed
```

### Getting Next Lesson

```
User: learn --next
    ↓
InteractiveCLI._continue_learning()
    ↓
┌─────────────────────────────────────┐
│  1. Get last session language       │
│     └─→ From sessions array          │
│                                      │
│  2. ProgressTracker.get_next_lesson()│
│     └─→ Find first incomplete        │
│                                      │
│  3. Suggest to user                 │
│     └─→ Display suggestion           │
│                                      │
│  4. Confirm and open                │
│     └─→ If yes, open lesson          │
└─────────────────────────────────────┘
    ↓
Next lesson suggested/opened
```

### Marking Complete

```
User: learn --complete c++ 1 1
    ↓
InteractiveCLI (completion handler)
    ↓
ProgressTracker.mark_lesson_completed()
    ↓
┌─────────────────────────────────────┐
│  1. Load progress JSON              │
│                                      │
│  2. Navigate to lesson:             │
│     languages → c-c++ → stage_1 →   │
│     level_1                          │
│                                      │
│  3. Set completed = true            │
│     Add completed_at timestamp      │
│                                      │
│  4. Save progress JSON              │
└─────────────────────────────────────┘
    ↓
✅ Lesson marked complete
```

## Storage Architecture

### Progress File Structure

```json
.learn-progress.json
├── languages
│   └── {language}
│       └── stage_{N}
│           └── level_{N}
│               ├── opened_count
│               ├── first_opened
│               ├── last_opened
│               ├── completed
│               └── completed_at
├── sessions []
│   └── {session}
│       ├── timestamp
│       ├── language
│       ├── stage
│       ├── level
│       └── mode
├── started
└── last_accessed
```

### Lesson File Structure

```
LEARN/
└── {language}/
    └── stage-{N}/
        └── level-{N}/
            ├── lesson.md       # Lesson content
            ├── solution.{ext}  # User code (auto-created)
            └── README.md       # Optional
```

## Interaction Patterns

### Pattern 1: Interactive Session

```
┌─────────────────────────┐
│  User launches: learn   │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Display main menu      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  User selects option    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Execute action         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Show feedback          │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Return to menu         │
└────────┬────────────────┘
         │
         └─────────┐
                   │ (loop until exit)
```

### Pattern 2: Command Execution

```
┌─────────────────────────┐
│  User: learn c++ 1      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Parse command          │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Validate inputs        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Execute directly       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Show result & exit     │
└─────────────────────────┘
```

## Class Relationships

```
┌─────────────────────────────────────────────┐
│              InteractiveCLI                 │
│  - learn_dir: Path                          │
│  - progress: ProgressTracker                │
│  - lesson_mgr: LessonManager                │
│  - executor: LessonExecutor                 │
│                                              │
│  + run_interactive_mode()                   │
│  + _select_language_and_lesson()            │
│  + _open_lesson()                           │
│  + _view_progress()                         │
└───┬─────────────────────────────────────────┘
    │
    │ creates and uses
    │
    ├──────────────────┬────────────────────┐
    │                  │                    │
    ▼                  ▼                    ▼
┌──────────────┐  ┌─────────────┐  ┌─────────────┐
│ProgressTracker  │LessonManager│  │LessonExecutor│
│                 │             │  │             │
│ + mark_opened() │ + find()    │  │ + open_vim()│
│ + mark_complete()│+ list()    │  │ + open_vscode│
│ + get_next()    │ + discover()│  │ + template()│
│ + get_stats()   │             │  │             │
└──────────────┘  └─────────────┘  └─────────────┘
```

## Error Handling Flow

```
User Action
    ↓
Try:
    ├─→ Execute operation
    │
    └─→ Success → Continue
    
Except:
    ├─→ Lesson not found
    │   └─→ Show available lessons
    │
    ├─→ Invalid language
    │   └─→ Show valid languages
    │
    ├─→ File error
    │   └─→ Show error + suggestion
    │
    └─→ Other error
        └─→ Show generic error
        
Always:
    └─→ Return gracefully
```

## Scalability

### Adding New Languages

```
1. Create directory structure:
   LEARN/newlang/stage-1/level-1/

2. Add lessons (lesson.md files)

3. Update LessonManager:
   - Add to _discover_languages()
   - Add display name
   - Add file extension
   
4. Update LessonExecutor:
   - Add solution template

Done! Language available immediately.
```

### Adding New Features

```
1. Add method to appropriate class:
   - Data feature → ProgressTracker
   - Lesson feature → LessonManager
   - UI feature → InteractiveCLI

2. Add menu option (if interactive):
   - Update _print_main_menu()
   - Add handler method

3. Add command flag (if CLI):
   - Update argparse
   - Add handler in main()

4. Update documentation

Done! Feature integrated.
```

## Performance Considerations

### Optimization Points

1. **Lesson Discovery**
   - Cached after first scan
   - Only scans when needed
   - Fast path resolution

2. **Progress Loading**
   - Loads once at startup
   - Cached in memory
   - Saves only when changed

3. **File Operations**
   - Minimal disk reads
   - Atomic writes
   - Efficient JSON parsing

4. **UI Rendering**
   - Clear screen only when needed
   - Minimal redraws
   - Fast menu display

## Security Considerations

1. **File Safety**
   - Never overwrites user code
   - Validates paths
   - Safe JSON operations

2. **Input Validation**
   - Sanitizes user input
   - Range checking
   - Type validation

3. **Data Integrity**
   - Atomic file writes
   - Backup-friendly format
   - Corruption recovery

## Summary

The Enhanced Learn CLI is built with:

✅ **Clean Architecture** - Modular, maintainable
✅ **Clear Data Flow** - Predictable, debuggable
✅ **Robust Error Handling** - Graceful, helpful
✅ **Efficient Performance** - Fast, responsive
✅ **Secure Operations** - Safe, validated
✅ **Scalable Design** - Extensible, flexible

**Result:** A professional, production-ready learning system.
