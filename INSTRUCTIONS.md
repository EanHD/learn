# INSTRUCTIONS FOR AI AGENTS

This document provides comprehensive guidance for AI agents working on this learning platform.
Use this as the authoritative reference for understanding project structure, adding languages,
creating lessons, and maintaining code quality.

## Project Overview

**Mission:** Teach programming through progressive, hands-on lessons with immediate feedback.

**Philosophy:** Learn by doing, not by reading. Users progress through 5 stages:

1. **Copying Code** - Muscle memory and syntax familiarity
2. **Pseudocode to Code** - Translate logic to implementation
3. **Problem to Pseudocode** - Design before coding
4. **Full Problem Solving** - Independent problem-solving
5. **Capstone Projects** - Real-world applications

**Current Support:** C/C++, Rust, Python, JavaScript, Go, Lua (210 lessons total - all complete!)
**Recently Added:** Dart, Swift, Kotlin, SQL, C#, Shell, PowerShell, TypeScript
**Framework:** 5 stages × 7 levels per language (35 lessons × 14 languages = 490 total lessons supported)

## Repository Structure

```
LEARN/
├── README.md                 # User entry point
├── START_HERE.md            # 5-minute quickstart
├── INSTRUCTIONS.md          # THIS FILE - for AI agents
├── CONTRIBUTING.md          # Contribution guidelines
├── CHANGELOG.md             # Version history
├── ROADMAP.md               # Future plans
├── LICENSE                  # MIT license
├── CODE_OF_CONDUCT.md       # Community standards
├── SECURITY.md              # Security policy
│
├── .github/                 # GitHub configuration
│   ├── workflows/           # CI/CD pipelines
│   ├── ISSUE_TEMPLATE/      # Issue forms
│   └── pull_request_template.md
│
├── .docs/                   # Internal documentation ONLY
│   ├── SETUP_DEV.md         # Developer setup
│   ├── SETUP_NVIM.md        # Neovim configuration
│   ├── VIM_CHEATSHEET.md    # Vim commands
│   └── [session notes]      # Development logs
│
├── CLI/                     # Command-line interface
│   ├── learn                # Main executable
│   ├── learn_cli.py         # Core implementation
│   ├── install.sh           # Installation script
│   └── [documentation]
│
├── MODE_VIM/                # Vim mode configuration
│   └── CONFIG/
│       └── init-learning.vim
│
├── c-c++/                   # C++ language lessons
│   ├── TABLE_OF_CONTENTS.md
│   ├── stage-1-copying-code/
│   ├── stage-2-pseudocode-to-code/
│   └── ... stage-5
│
├── rust/                    # Rust language lessons
└── [python/, javascript/, go/, lua/]  # Future languages
```

## CRITICAL: Documentation Organization

**User-facing (root):**

- README.md, START_HERE.md, CONTRIBUTING.md, CHANGELOG.md, ROADMAP.md

**Developer/internal (.docs/):**

- Setup guides, session notes, architecture docs, progress tracking

**Rule:** Never create root-level markdown files for internal/session work.
All AI session summaries, status updates, and technical notes go in `.docs/`.

## Lesson Organization

Each stage contains 7 levels ordered by progressive complexity.

### Stage Structure

```
stage-N-description/
├── TABLE_OF_CONTENTS.md
├── WORKSPACE_INSTRUCTIONS.md
├── level-1-topic/
│   ├── lesson.md
│   ├── main.cpp (or .rs)
│   └── [additional files]
├── level-2-topic/
└── ... level-7
```

## Lesson File Format

All lessons follow professional markdown format without emojis.

### Required Sections

1. **Header** - Clear title indicating stage, level, and topic
2. **Learning Goals** - Bullet list of specific skills or concepts
3. **Your Task** - Clear, step-by-step instructions
4. **How to Run** - Step-by-step commands to execute code
5. **Success Checklist** - Checkable items using `- [ ]` format
6. **Additional Content** - Explanatory sections providing context
7. **Code Review** - Break down key functions and structure
8. **Answer Key** - Placed at bottom after page break with solutions

### Formatting Guidelines

- Use standard Markdown with GitHub-flavored extensions
- No emojis - maintain professional appearance
- Code blocks with language specification
- Use Markdown tables for structured information
- Bullet points and numbered lists for clarity
- Bold for emphasis, italics for subtle notes
- Page breaks using: `<div style="page-break-after: always;"></div>`
- Professional, encouraging tone
- Progressive difficulty within stages
- Interactive elements: checklists, test cases, ideas

### File Structure Per Level

```bash
level-N-topic/
├── lesson.md           (Main instructional document)
├── main.cpp            (C++ code file)
└── [additional files]  (Data, headers, etc.)
```

## Code Examples

All code examples should:

- Use proper syntax highlighting
- Include comments explaining logic
- Follow language conventions
- Progress in complexity through levels
- Be complete and runnable

## Progress Tracking

Each stage root includes TABLE_OF_CONTENTS.md that:

- Lists all 7 levels
- Shows completion status
- Can be manually updated or automated

Users can also use:

- `learn --info` - Check progress
- `learn --list` - See all lessons
- `learn --next` - Get suggestion

## CLI Tool (learn)

Located in `/home/eanhd/LEARN/CLI/learn` - Python executable

### Key Features

- `learn <language> <level>` - Open lesson
- `learn --list` - Show all 70 lessons
- `learn --info` - Display progress
- `learn --next` - Get recommendation
- `--stage` flag to jump stages
- `--vim`, `--vscode`, `--terminal` modes

### CLI Documentation

Complete CLI documentation in `CLI/`:

- `README.md` - User guide with commands
- `IMPLEMENTATION.md` - Technical architecture
- `TROUBLESHOOTING.md` - Problem solutions
- `INDEX.md` - Navigation guide

## Vim Mode - Tab & Indentation Configuration

The `.vimrc` file at the repository root configures Vim for all lessons with language-specific tab settings.

### Default Tab Settings

**DEFAULT: 2 spaces** (Most languages)

- JavaScript, Lua, Go, Shell scripts

**4 spaces** (Language-specific conventions)

- C/C++ (Google style)
- Python (PEP 8)
- Rust (community standard)

**Tab characters** (Language requirement)

- Go (Go enforces tab characters)

### Configuration Details

**File:** `.vimrc` (repository root)

**Settings applied automatically:**

```vim
set tabstop=2           " Display tabs as 2 spaces
set softtabstop=2       " Backspace deletes 2 spaces
set shiftwidth=2        " Auto-indent uses 2 spaces
set expandtab           " Use spaces (not tab chars)
set autoindent          " Auto-indent on new line

" Language-specific overrides
autocmd FileType c,cpp set tabstop=4 shiftwidth=4 softtabstop=4
autocmd FileType python set tabstop=4 shiftwidth=4 softtabstop=4
autocmd FileType rust set tabstop=4 shiftwidth=4 softtabstop=4
autocmd FileType go set tabstop=4 shiftwidth=4 noexpandtab
```

**How it works:**

1. User launches lesson with `learn launch`
2. CLI loads `.vimrc` with `-u` flag
3. All tab settings applied automatically per language
4. No student configuration needed!

### Why This Matters

Consistent indentation across all students helps with:

- Code review and grading
- Professional coding habits
- Language convention learning
- Copy-paste accuracy

## Extending the System

### Adding New Lessons

1. Create new level directory: `level-N-topic/`
2. Create `lesson.md` following format above
3. Create `main.cpp` (or `.rs`) with complete working code
4. Include all required sections
5. Move any implementation notes to `/.docs/`
6. Update stage TABLE_OF_CONTENTS.md

### Adding New Languages

Follow this comprehensive checklist when adding a new programming language:

#### Step 1: Directory Structure

```bash
<language>/
├── TABLE_OF_CONTENTS.md          # Overview of all lessons
├── WORKSPACE_INSTRUCTIONS.md      # Language-specific setup
├── stage-1-copying-code/
│   ├── level-1-hello-world/
│   │   ├── lesson.md
│   │   └── main.<ext>
│   ├── level-2-variables/
│   ├── level-3-basic-math/
│   ├── level-4-user-input/
│   ├── level-5-conditionals/
│   ├── level-6-loops/
│   └── level-7-functions/
├── stage-2-pseudocode-to-code/
├── stage-3-problem-to-pseudocode/
├── stage-4-full-problem-solving/
└── stage-5-capstone/
```

#### Step 2: Language Metadata

Create `<language>/.language-config.json`:

```json
{
  "name": "Python",
  "display_name": "Python",
  "file_extension": "py",
  "compiler": "python3",
  "run_command": "python3 {file}",
  "build_command": null,
  "test_command": "pytest",
  "format_command": "black {file}",
  "lsp": "pyright",
  "formatter": "black",
  "total_lessons": 35
}
```

#### Step 3: CLI Integration

Update `CLI/learn_cli.py` with these changes:

##### 3a. Language Registration

Add language to `LessonManager.languages` dict and related methods:

```python
# In LessonManager.__init__
self.languages = {
    "c-c++": {...},
    "rust": {...},
    "python": {  # NEW
        "name": "Python",
        "extension": "py",
        "stages": 5
    }
}

# In get_lesson_file_extension() - map to file extension
extension_map = {
    "c-c++": "cpp", "c++": "cpp",
    "rust": "rs",
    "python": "py",  # NEW
    "javascript": "js", "js": "js",
    "go": "go",
    "lua": "lua"
}

# In _get_lang_short_name() - map to short name for workspaces
mapping = {
    "c-c++": "cpp",
    "rust": "rust",
    "python": "python",  # NEW
    "javascript": "js",
    "go": "go",
    "lua": "lua",
    "dart": "dart",
    "swift": "swift",
    "kotlin": "kotlin",
    "sql": "sql",
    "c#": "csharp",
    "csharp": "csharp",
    "shell": "shell",
    "powershell": "powershell",
    "typescript": "typescript"
}
```

##### 3b. Compile/Run Command Mapping

**CRITICAL:** Add to `_get_compile_command()` in `LessonExecutor`:

```python
def _get_compile_command(self, language: str) -> Tuple[str, str]:
    """Get compile/run command for language

    Returns: (description, vim_command)

    IMPORTANT: When adding a new language, add entry here so students
    see the correct compile command in their Vim instructions.
    """
    commands = {
        "c-c++": ("C++ (compile + run)", ":!make run"),
        "rust": ("Rust", ":!cargo run"),
        "python": ("Python", ":!python3 %"),
        "javascript": ("JavaScript", ":!node %"),
        "go": ("Go", ":!go run %"),
        "lua": ("Lua", ":!lua %"),
        "dart": ("Dart", ":!dart %"),
        "swift": ("Swift", ":!swift %"),
        "kotlin": ("Kotlin", ":!kotlinc % -include-runtime -d main.jar && java -jar main.jar"),
        "sql": ("SQL", ":!sqlite3 < %"),
        "c#": ("C#", ":!csc % && ./%.exe"),
        "csharp": ("C#", ":!csc % && ./%.exe"),
        "shell": ("Shell", ":!bash %"),
        "powershell": ("PowerShell", ":!powershell -File %"),
        "typescript": ("TypeScript", ":!ts-node %")
    }
    lang_desc, cmd = commands.get(language, ("Unknown", ":!echo 'Language not configured'"))
    return lang_desc, cmd
```

This ensures that when users launch Vim for your language, they see:

```text
Compile/Run (in code window):
    :<command>  -> <Language Name>
```

Only showing the command for their current language (not all languages).

##### 3c. Workspace Template Creation

**CRITICAL:** Create COMPLETELY BLANK files for students to type EVERYTHING from scratch!

Create `_create_<lang>_workspace()` method:

```python
def _create_python_workspace(self, workspace_dir: Path):
    """Create Python workspace with COMPLETELY BLANK file

    IMPORTANT: File must be 100% BLANK. Students learn by typing
    EVERYTHING from the lesson - even basic structure. This forces
    them to practice every keystroke and learn Vim simultaneously.

    DO NOT pre-fill ANYTHING - not even comments or function stubs!
    """
    main_py = workspace_dir / "main.py"
    main_py.write_text("")  # Completely blank - student types everything

    # Add optional supporting files (requirements.txt, Makefile, etc.)
    # But the main code file MUST be blank!
    requirements = workspace_dir / "requirements.txt"
    requirements.write_text("")

# Then update _create_workspace() dispatcher:
elif language == "python":
    main_file = workspace_dir / "main.py"
    if not main_file.exists():
        self._create_python_workspace(workspace_dir)
```

**Template Guidelines:**

- ✅ **DO**: Create completely blank files (`write_text("")`)
- ✅ **DO**: Let students type EVERYTHING from scratch
- ✅ **DO**: Add supporting files (Makefile, package.json, Cargo.toml)
- ❌ **DON'T**: Include ANY code - not even comments
- ❌ **DON'T**: Pre-fill structure, imports, or function stubs
- ❌ **DON'T**: Add "Your code here" comments

**Why?** Students learn by typing EVERYTHING from the lesson files.
This forces them to:

1. Practice every single keystroke
2. Learn Vim muscle memory
3. Remember syntax through repetition
4. Build confidence from a truly blank canvas

Pre-filling ANYTHING defeats the core learning methodology!

##### 3d. Language Metadata (Optional but Recommended)

Create `<language>/.language-config.json`:

```json
{
  "name": "Python",
  "display_name": "Python",
  "file_extension": "py",
  "compiler": "python3",
  "run_command": "python3 {file}",
  "build_command": null,
  "test_command": "pytest",
  "format_command": "black {file}",
  "lsp": "pyright",
  "formatter": "black",
  "total_lessons": 35
}
```

This file helps other tools (IDEs, scripts) understand language setup.

#### Step 4: System Dependencies

Update `SystemChecker` in `learn_cli.py`:

```python
# In SystemChecker.check_all()
python_ok = self._check_command("python3", "--version")
self.checks.append({
    "name": "Python 3",
    "status": "OK" if python_ok else "MISSING",
    "fix": "sudo apt install python3 python3-pip" if not python_ok else None
})
```

#### Step 5: Documentation Updates

1. **README.md**: Add language to supported list
2. **START_HERE.md**: Add example (`learn python 1`)
3. **ROADMAP.md**: Move from planned to implemented
4. **CHANGELOG.md**: Add entry under [Unreleased]
5. **CLI/FEATURES.md**: Document language-specific features

#### Step 6: Content Creation

Create 35 lessons (5 stages × 7 levels):

**Stage 1 (Copying Code):**

- Level 1: Hello World
- Level 2: Variables
- Level 3: Basic Math
- Level 4: User Input
- Level 5: Conditionals
- Level 6: Loops
- Level 7: Functions

**Stage 2-5:** Follow existing pattern from C++/Rust

#### Step 7: Testing Checklist

- [ ] `learn --list` shows new language
- [ ] `learn <lang> 1` opens first lesson
- [ ] Workspace scaffolding creates correct files
- [ ] `learn --run <lang> 1 1` compiles/runs successfully
- [ ] LSP autocomplete works in Neovim
- [ ] Formatter works on save
- [ ] `learn --doctor` checks language dependencies
- [ ] Progress tracking works for new language

#### Step 8: Community Announcement

After testing, create PR with:

- All 35 lessons
- CLI integration complete
- Documentation updated
- Tests passing
- Examples in PR description

### Enhancing CLI

1. Edit `CLI/learn` (Python)
2. Follow existing code patterns
3. Add tests for new features
4. Update `CLI/README.md` with new commands
5. Document technical changes in `CLI/IMPLEMENTATION.md`
6. Move design notes to `/.docs/`

## User-Facing vs Internal Docs

### User-Facing (Root Level)

Simple, inviting, noob-friendly:

- `README.md` - Overview and quick start
- `START_HERE.md` - First-time learning guide
- `VIM_CHEATSHEET.md` - Vim reference for users
- `SUGGESTIONS.md` - Ideas and features

### Internal (/.docs/ Hidden)

Complex documentation goes here:

- Implementation summaries
- Status documents
- Architecture notes
- Session records
- Development plans

### AI Agent Only

- `INSTRUCTIONS.md` - This file only for AI agents

## Quality Standards

All lessons must:

- Be complete and runnable as-is
- Have answer keys with detailed explanations
- Include success checklists
- Progress in difficulty
- Use consistent formatting
- Maintain professional tone
- Encourage learning

## Documentation Standards

All documentation must:

- Use clear, professional language
- Avoid jargon for user-facing docs
- Include examples and code snippets
- Have proper markdown formatting
- Be free of emojis
- Be well-organized with clear headers
- Include tables of contents for longer docs

## Performance Considerations

- Lessons should load quickly in text editors
- Answer keys should be scrollable (page break)
- CLI tool should respond in under 1 second
- Progress files should be minimal (< 1 KB)

## Future Enhancements

Potential additions tracked in `/.docs/`:

- MODE_VSCODE configuration
- Automated compilation integration
- Test framework integration
- Web-based lesson viewer
- Community contributions
