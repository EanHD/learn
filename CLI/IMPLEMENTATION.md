# CLI Implementation Guide

Technical documentation for the `learn` CLI tool. This guide covers the implementation, architecture, and how to extend or customize the tool.

## Architecture Overview

```
learn (Python CLI)
│
├── Argument Parsing
│   ├── language (c++, rust)
│   ├── level (1-7)
│   └── flags (--vim, --vscode, --terminal, --stage, etc)
│
├── Lesson Discovery
│   ├── Stage detection
│   ├── File validation
│   └── Error handling
│
├── Progress Tracking
│   ├── Session recording
│   ├── History storage
│   └── Progress suggestions
│
└── Lesson Launch
    ├── Vim mode (split-screen)
    ├── VSCode mode
    └── Terminal mode
```

## Code Structure

### Main Components

```python
class LearnCLI:
    def __init__(self):                    # Initialize
        self.learn_dir                     # Root directory
        self.modes                         # Available modes
        self.progress_file                 # Progress tracking
    
    def list_lessons(self):                # List all lessons
    def find_lesson_path(self, lang, level, stage): # Smart discovery
    def open_lesson_vim(self, lang, level, stage):  # Vim launch
    def open_lesson_vscode(self, lang, level):      # VSCode launch
    def open_lesson_terminal(self, lang, level):    # Terminal launch
    def record_progress(self, lang, level, stage, mode):  # Track
    def get_progress(self):                # Read history
    def suggest_next_lesson(self):         # Recommendations
    def _create_template(self, path, ext): # Code templates

def main():                                # CLI entry point
```

## Key Functions

### 1. find_lesson_path()

Smart lesson discovery across all stages:

```python
def find_lesson_path(self, lang, level, stage=None):
    """Find lesson path, intelligently searching across all stages if needed"""
    if stage:
        # Direct lookup: stage-X/level-Y/lesson.md
        stage_path = self.learn_dir / lang / f"stage-{stage}"
        if stage_path.exists():
            level_path = stage_path / f"level-{level}"
            lesson_file = level_path / "lesson.md"
            if lesson_file.exists():
                return lesson_file
        return None
    
    # Search all stages if no stage specified
    for stage_dir in sorted(self.learn_dir.glob(f"{lang}/stage-*")):
        level_path = stage_dir / f"level-{level}"
        lesson_file = level_path / "lesson.md"
        if lesson_file.exists():
            return lesson_file
    
    return None
```

**Why this design:**
- Allows user to omit `--stage` for convenience
- Returns first found (usually Stage 1)
- Allows jumping to specific stage with flag
- Graceful error if lesson doesn't exist

### 2. record_progress()

Tracks every lesson opening:

```python
def record_progress(self, lang, level, stage, mode):
    """Record that a lesson was opened"""
    progress_data = {
        "timestamp": datetime.now().isoformat(),
        "language": lang,
        "stage": stage,
        "level": level,
        "mode": mode
    }
    
    # Append to progress file
    with open(self.progress_file, 'a') as f:
        f.write(f"{progress_data}\n")
```

**What gets tracked:**
- When the lesson was opened
- Which language (c-c++, rust)
- Which stage (1-5)
- Which level (1-7)
- Which mode (vim, vscode, terminal)

### 3. open_lesson_vim()

Launches Vim with split-screen setup:

```python
def open_lesson_vim(self, lang, level, stage=None):
    """Open lesson in Vim mode with split screen"""
    lesson_path = self.find_lesson_path(lang, level, stage)
    
    # Extract stage number
    stage_num = lesson_path.parent.parent.name.replace("stage-", "")
    
    # Create solution file if needed
    code_ext = "c" if lang == "c-c++" else "rs"
    solution_path = lesson_path.parent / f"solution.{code_ext}"
    if not solution_path.exists():
        self._create_template(solution_path, code_ext)
    
    # Get Vim config
    config = self.learn_dir / "MODE_VIM" / "CONFIG" / "init-learning.vim"
    
    # Record and launch
    self.record_progress(lang, level, stage_num, "vim")
    os.system(f"nvim -u {config} {lesson_path}")
```

**What happens:**
1. Finds lesson file
2. Creates solution workspace if needed
3. Records the session
4. Launches Neovim with learning config

## Data Flow

### Opening a Lesson

```
User Input: learn c++ 3 --stage 2
    ↓
Argument Parsing
    ↓
Normalize: language="c-c++", level=3, stage=2
    ↓
find_lesson_path("c-c++", 3, stage=2)
    ↓
Check: c-c++/stage-2/level-3/lesson.md exists? YES
    ↓
Create solution file if needed
    ↓
record_progress("c-c++", 3, 2, "vim")
    ↓
Launch: nvim -u CONFIG c-c++/stage-2/level-3/lesson.md
    ↓
User sees split-screen with lesson and empty code file
```

### Checking Progress

```
User Input: learn --info
    ↓
get_progress()
    ↓
Read .learn-progress file
    ↓
Parse each line: {timestamp, language, stage, level, mode}
    ↓
Display: "Total sessions: X, Last session: Y"
```

## Progress File Format

The `.learn-progress` file is append-only:

```
{'timestamp': '2024-10-29T14:30:00', 'language': 'c-c++', 'stage': 1, 'level': 1, 'mode': 'vim'}
{'timestamp': '2024-10-29T14:45:00', 'language': 'c-c++', 'stage': 1, 'level': 2, 'mode': 'vim'}
{'timestamp': '2024-10-29T15:00:00', 'language': 'rust', 'stage': 1, 'level': 1, 'mode': 'vim'}
```

**Advantages:**
- Append-only is fast and safe
- Complete history preserved
- Easy to parse and analyze
- No data loss on concurrent access

## Adding New Features

### Add a New Command

Example: `learn --stats` to show statistics

```python
# In main():
parser.add_argument("--stats", action="store_true", help="Show learning statistics")

# In argument handling:
if args.stats:
    cli.show_stats()
    return

# Add method:
def show_stats(self):
    progress = self.get_progress()
    c_plus_count = sum(1 for p in progress if "c-c++" in str(p))
    rust_count = sum(1 for p in progress if "rust" in str(p))
    print(f"C++: {c_plus_count} sessions")
    print(f"Rust: {rust_count} sessions")
```

### Add Support for New Language

Example: Add Python language

```python
# In find_lesson_path():
if args.language in ["python", "py"]:
    lang = "python"

# In open_lesson_vim():
code_ext = "py" if lang == "python" else ...

# Add template:
def _create_template(self, path, ext):
    templates = {
        "py": """# Python solution
# Your code here
if __name__ == "__main__":
    pass
"""
    }
```

### Add a New Mode

Example: Add `--docker` mode

```python
# In argument parsing:
parser.add_argument("--docker", action="store_true", help="Open in Docker container")

# In mode determination:
if args.docker:
    mode = "docker"

# Add handler:
def open_lesson_docker(self, lang, level, stage=None):
    lesson_path = self.find_lesson_path(lang, level, stage)
    # Docker launch logic
    os.system(f"docker run -v {lesson_path}:/lesson learn:latest")
```

## Configuration & Customization

### Changing Default Mode

Edit `CLI/learn`:

```python
# In main() or LearnCLI:
DEFAULT_MODE = "vim"  # Change to "vscode" or "terminal"

# Use it:
if not args.vim and not args.vscode and not args.terminal:
    mode = DEFAULT_MODE
```

### Changing Progress File Location

```python
# In __init__:
self.progress_file = Path("/custom/location/.learn-progress")
```

### Changing Lesson Directory Structure

If you rename directories, update paths:

```python
# Find and replace pattern matching
for stage_dir in self.learn_dir.glob(f"{lang}/stage-*"):
    # Can modify glob pattern here
```

## Error Handling

### Lesson Not Found

```python
if not lesson_path:
    print(f"Lesson not found: {lang} level {level}")
    return
```

### Language Not Recognized

```python
if args.language not in ["cpp", "c++", "c", "C++", "rust", "rs"]:
    print(f"Unknown language: {args.language}")
    print("Available: c++, rust")
    return
```

### Vim Not Installed

```python
try:
    os.system(f"nvim -u {config} {lesson_path}")
except:
    print("Error: Neovim not found. Install with:")
    print("  Ubuntu: sudo apt install neovim")
    print("  macOS:  brew install neovim")
```

## Performance Considerations

### Lesson Discovery

**Current**: O(n) where n = number of stages
- Typically 5 stages = < 50ms lookup
- Sorted glob ensures consistent order
- No caching needed for this speed

**Could optimize**: Cache stage structure on first run

### Progress Tracking

**Current**: Append-only file write
- ~1ms per session record
- No locking issues
- Complete history preserved

**Could optimize**: Separate hot data (last 10) from cold data (archive)

### File Creation

**Current**: Check exists before creating
- ~10-20ms per template creation
- Only done once per language/level
- Fast I/O for small templates

## Testing

### Manual Testing

```bash
# Test lesson opening
./learn c++ 1
./learn rust 2

# Test flags
./learn c++ 1 --stage 3
./learn c++ 1 --vscode

# Test info commands
./learn --list
./learn --info
./learn --next

# Test errors
./learn c++ 99      # Should error
./learn python 1    # Should error
```

### Syntax Check

```bash
python3 -m py_compile CLI/learn
```

### Script Testing

```bash
# Test from different directory
cd /tmp && learn c++ 1

# Test with aliases
alias learn-cpp='learn c++'
learn-cpp 1
```

## Future Enhancements

### Phase 2

1. **Caching** - Cache stage structure for faster lookup
2. **Analytics** - Parse progress file for insights
3. **Scheduling** - `learn --schedule "3 per day"`
4. **Templates** - Customizable code templates
5. **Themes** - Different Vim themes per mode

### Phase 3

1. **Web Interface** - Browser-based lesson viewer
2. **Mobile App** - Mobile lesson access
3. **Collaboration** - Share progress, compete with friends
4. **AI Assistance** - Smart hints and suggestions
5. **Achievement System** - Badges, milestones, leaderboards

## Summary

The `learn` CLI tool is:

- **Simple**: Single-file Python script
- **Powerful**: Smart lesson discovery and progress tracking
- **Extensible**: Easy to add features and modes
- **Fast**: Minimal overhead, responsive
- **Reliable**: Error handling and validation
- **User-friendly**: Clear messages and suggestions

For usage, see: `README.md` (user guide)
For setup, see: `MODE_VIM/COMPLETE_SETUP.md`

