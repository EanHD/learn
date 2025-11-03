# Dynamic Language-Specific Compile Commands Implementation

**Date:** November 1, 2025
**Status:** ✅ Complete
**Task:** Make Vim instructions show only the current language's compile command, not all languages

## Problem

Previously, when launching a lesson in Vim, the instruction screen showed ALL language compile commands:

```
Compile/Run (in code window):
    :!make run         -> C++ (compile + run)
    :!cargo run        -> Rust
    :!python3 %        -> Python
    :!node %           -> JavaScript
```

This was confusing for users learning Python (for example) who would see C++ commands.

## Solution

Implemented **dynamic, language-aware compile commands** in the CLI:

1. Created `_get_compile_command(language: str) -> Tuple[str, str]` method
2. Updated `open_vim()` to pass language to instruction display
3. Updated `_show_vim_instructions()` to show only the current language's command
4. Added comprehensive documentation in INSTRUCTIONS.md for agents adding new languages

## Changes Made

### 1. CLI/learn_cli.py - Added `_get_compile_command()` method

**Location:** LessonExecutor class, after `_get_lang_short_name()`

```python
def _get_compile_command(self, language: str) -> Tuple[str, str]:
    """Get compile/run command for language

    Returns: (description, vim_command)
    """
    commands = {
        "c-c++": ("C++ (compile + run)", ":!make run"),
        "rust": ("Rust", ":!cargo run"),
        "python": ("Python", ":!python3 %"),
        "javascript": ("JavaScript", ":!node %"),
        "go": ("Go", ":!go run %"),
        "lua": ("Lua", ":!lua %")
    }
    lang_desc, cmd = commands.get(language, ("Unknown", ":!echo 'Language not configured'"))
    return lang_desc, cmd
```

### 2. CLI/learn_cli.py - Updated `open_vim()` method

**Changed:** Pass `language` parameter to `_show_vim_instructions()`

```python
def open_vim(self, lesson_path: Path, language: str):
    # ... existing code ...
    self._show_vim_instructions(workspace, language)  # Added language param
```

### 3. CLI/learn_cli.py - Updated `_show_vim_instructions()` method

**Changed:** Accept language parameter and display only that language's command

```python
def _show_vim_instructions(self, workspace: Dict, language: str):
    """Show quick instructions before launching Vim"""
    lang_desc, compile_cmd = self._get_compile_command(language)

    # ... existing code ...
    print("  Compile/Run (in code window):")
    print(f"    {compile_cmd:<20} -> {lang_desc}")  # Only shows current language!
    # ... rest of code ...
```

### 4. INSTRUCTIONS.md - Enhanced language addition guide

**Added comprehensive section:** "Step 3b: Compile/Run Command Mapping"

**Key points documented:**

- Where to add compile commands (`_get_compile_command()`)
- How users see language-specific instructions in Vim
- That all 6 languages (C++, Rust, Python, JavaScript, Go, Lua) are pre-configured
- **CRITICAL NOTE:** When adding new languages, this mapping MUST be updated

**Example from documentation:**

```markdown
##### 3b. Compile/Run Command Mapping

**CRITICAL:** Add to `_get_compile_command()` in `LessonExecutor`:

When adding a new language, add entry here so students
see the correct compile command in their Vim instructions.
```

### 5. START_HERE.md - Updated user documentation

**Added section:** "Vim Instructions" explaining language-specific compile commands

Shows users they will only see their language's command:

```
learn c++ 1 --vim  → Shows: :!make run  -> C++ (compile + run)
learn python 1 --vim  → Shows: :!python3 %  -> Python
```

## Example Output

**Before (confusing - shows all languages):**

```
Compile/Run (in code window):
    :!make run         -> C++ (compile + run)
    :!cargo run        -> Rust
    :!python3 %        -> Python
    :!node %           -> JavaScript
    :!go run %         -> Go
    :!lua %            -> Lua
```

**After (clean - shows only current language):**

```
Compile/Run (in code window):
    :!python3 %        -> Python
```

## Testing

Verified that the method works for all 6 languages:

```python
languages = ["c-c++", "rust", "python", "javascript", "go", "lua"]

for lang in languages:
    desc, cmd = executor._get_compile_command(lang)
    print(f"{lang:15} -> {cmd:20} ({desc})")

# Output:
# c-c++           -> :!make run           (C++ (compile + run))
# rust            -> :!cargo run          (Rust)
# python          -> :!python3 %          (Python)
# javascript      -> :!node %             (JavaScript)
# go              -> :!go run %           (Go)
# lua             -> :!lua %              (Lua)
```

## Impact

✅ **User Experience:** Cleaner, less confusing Vim instructions
✅ **Code Quality:** Centralized compile command configuration
✅ **Maintainability:** Single source of truth for compile commands
✅ **Future-Ready:** Clear pattern documented for adding new languages

## For AI Agents Adding New Languages

When adding a new language (e.g., TypeScript, Go variants, etc.):

1. **Must update:** `_get_compile_command()` in LessonExecutor
2. **Format:** `"language-name": ("Display Name", "vim_command")`
3. **Testing:** Verify `learn --doctor` output shows new language
4. **Documentation:** Already documented in INSTRUCTIONS.md Step 3b

Example for TypeScript:

```python
commands = {
    # ... existing ...
    "typescript": ("TypeScript", ":!ts-node %"),
}
```

Then users will see:

```
Compile/Run (in code window):
    :!ts-node %        -> TypeScript
```

## Files Modified

- ✅ `CLI/learn_cli.py` - Added method, updated signatures
- ✅ `INSTRUCTIONS.md` - Enhanced language addition guide
- ✅ `START_HERE.md` - Added user documentation about vim instructions

## Backward Compatibility

✅ **No breaking changes** - All existing commands work exactly as before

## Notes

- C++ uses Makefile with `:!make run` (most common pattern)
- Other languages use direct execution (`:!python3 %`, `:!cargo run`, etc.)
- Go and Lua support added but not yet with lesson content
- Pattern is extensible for future languages
