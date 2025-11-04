#!/usr/bin/env python3
"""
Fix lesson.md files to match c-c++ gold standard.
- Add missing Answer Key sections
- Fix code fence language tags
- Add execution instructions where missing
- Remove placeholders (or mark NEEDS_AUTHOR)
- Ensure final newline
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Language-specific configurations from INSTRUCTIONS.md
LANG_CONFIG = {
    'python': {
        'ext': 'py',
        'fence': 'python',
        'run_cmd': 'python3',
        'compile': False,
    },
    'javascript': {
        'ext': 'js',
        'fence': 'javascript',
        'run_cmd': 'node',
        'compile': False,
    },
    'typescript': {
        'ext': 'ts',
        'fence': 'typescript',
        'run_cmd': 'ts-node',
        'compile': False,
    },
    'rust': {
        'ext': 'rs',
        'fence': 'rust',
        'run_cmd': './hello',
        'compile': True,
        'compile_cmd': 'rustc hello.rs -o hello',
    },
    'go': {
        'ext': 'go',
        'fence': 'go',
        'run_cmd': 'go run',
        'compile': False,
    },
    'lua': {
        'ext': 'lua',
        'fence': 'lua',
        'run_cmd': 'lua',
        'compile': False,
    },
    'java': {
        'ext': 'java',
        'fence': 'java',
        'run_cmd': 'java',
        'compile': True,
        'compile_cmd': 'javac',
    },
    'julia': {
        'ext': 'jl',
        'fence': 'julia',
        'run_cmd': 'julia',
        'compile': False,
    },
    'dart': {
        'ext': 'dart',
        'fence': 'dart',
        'run_cmd': 'dart',
        'compile': False,
    },
    'swift': {
        'ext': 'swift',
        'fence': 'swift',
        'run_cmd': 'swift',
        'compile': False,
    },
    'kotlin': {
        'ext': 'kt',
        'fence': 'kotlin',
        'run_cmd': 'kotlin',
        'compile': True,
        'compile_cmd': 'kotlinc',
    },
    'sql': {
        'ext': 'sql',
        'fence': 'sql',
        'run_cmd': 'sqlite3 <',
        'compile': False,
    },
    'csharp': {
        'ext': 'cs',
        'fence': 'csharp',
        'run_cmd': 'mono',
        'compile': True,
        'compile_cmd': 'csc',
    },
    'shell': {
        'ext': 'sh',
        'fence': 'bash',
        'run_cmd': 'bash',
        'compile': False,
    },
    'powershell': {
        'ext': 'ps1',
        'fence': 'powershell',
        'run_cmd': 'powershell -File',
        'compile': False,
    },
    'zig': {
        'ext': 'zig',
        'fence': 'zig',
        'run_cmd': './hello',
        'compile': True,
        'compile_cmd': 'zig build-exe',
    },
    'nosql': {
        'ext': 'js',
        'fence': 'javascript',
        'run_cmd': 'mongo',
        'compile': False,
    },
    'php': {
        'ext': 'php',
        'fence': 'php',
        'run_cmd': 'php',
        'compile': False,
    },
    'r': {
        'ext': 'R',
        'fence': 'r',
        'run_cmd': 'Rscript',
        'compile': False,
    },
}

class LessonFixer:
    def __init__(self, filepath: Path, language: str):
        self.filepath = filepath
        self.language = language
        self.config = LANG_CONFIG.get(language, {})
        self.content = ""
        self.modified = False

    def load(self):
        """Load file content."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def save(self):
        """Save file content if modified."""
        if self.modified:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                f.write(self.content)
            return True
        return False

    def fix_code_fences(self):
        """Add language tags to code fences."""
        if not self.config:
            return

        fence_lang = self.config.get('fence', '')

        # Find all code fence positions and determine if they're opening or closing
        lines = self.content.split('\n')
        in_fence = False
        modified_lines = []

        for i, line in enumerate(lines):
            # Check if this line is ONLY a fence marker (no language tag)
            if line.strip() == '```':
                if not in_fence:
                    # This is an opening fence - add language tag
                    prev_line = lines[i-1].lower() if i > 0 else ''
                    next_line = lines[i+1].strip() if i < len(lines)-1 else ''

                    # Detect context
                    if 'output' in prev_line or 'expected' in prev_line or 'result' in prev_line:
                        # Output block - leave plain
                        modified_lines.append(line)
                    elif next_line.startswith(('cd ', 'python', 'node', 'cargo', 'go ', 'javac', 'rustc', 'gcc', 'g++ ', 'dart ', 'swift ', 'kotlin', 'lua ', 'julia ', 'csc ', 'bash ', 'sh ', 'sqlite3')):
                        # Shell command
                        modified_lines.append('```bash')
                        self.modified = True
                    else:
                        # Code block
                        modified_lines.append(f'```{fence_lang}')
                        self.modified = True
                    in_fence = True
                else:
                    # This is a closing fence - leave as is
                    modified_lines.append(line)
                    in_fence = False
            elif line.strip().startswith('```'):
                # Already has a language tag - don't modify
                modified_lines.append(line)
                if in_fence:
                    in_fence = False
                else:
                    in_fence = True
            else:
                modified_lines.append(line)

        if self.modified:
            self.content = '\n'.join(modified_lines)

    def fix_final_newline(self):
        """Ensure file ends with newline."""
        if not self.content.endswith('\n'):
            self.content += '\n'
            self.modified = True

    def has_answer_key(self) -> bool:
        """Check if Answer Key section exists."""
        return bool(re.search(r'^##?\s+ANSWER KEY', self.content, re.IGNORECASE | re.MULTILINE))

    def add_minimal_answer_key(self):
        """Add minimal Answer Key section if missing."""
        if self.has_answer_key():
            return

        # Find the page break or end of file
        page_break_match = re.search(r'<div style="page-break-after: always;"></div>', self.content)

        if not page_break_match:
            # No page break exists, add one before answer key
            answer_key_template = f'''

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to {self.language.title()}
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**
'''
            self.content = self.content.rstrip() + answer_key_template
            self.modified = True
        else:
            # Page break exists, add answer key after it
            insert_pos = page_break_match.end()
            answer_key_template = f'''

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to {self.language.title()}
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**
'''
            self.content = self.content[:insert_pos] + answer_key_template + self.content[insert_pos:]
            self.modified = True

    def remove_placeholder_ellipsis(self):
        """Remove ... placeholders in code examples (but not in strings)."""
        # Target patterns like:
        # - ... (existing code)
        # - ... more code ...
        # But NOT in strings or comments

        patterns_to_fix = [
            (r'^\.\.\..*$', ''),  # Lines that are just ...
            (r'\n\.\.\..*?\n', '\n'),  # Lines with ... in middle
        ]

        for pattern, replacement in patterns_to_fix:
            if re.search(pattern, self.content, re.MULTILINE):
                # Mark for author review rather than auto-delete
                self.content = re.sub(
                    pattern,
                    f'{replacement}\n> **NEEDS_AUTHOR:** Removed placeholder - verify completeness\n',
                    self.content,
                    flags=re.MULTILINE
                )
                self.modified = True

    def ensure_execution_section(self):
        """Ensure 'How to Run/Compile' section exists."""
        if re.search(r'How to (Run|Compile|Execute)', self.content, re.IGNORECASE):
            return  # Already has execution instructions

        # Look for "Your Task" section
        task_match = re.search(r'(###\s+Your Task.*?)(?=\n###|\n##|$)', self.content, re.DOTALL)
        if not task_match:
            return  # Can't safely add without Your Task section

        # Build execution instructions based on language
        if not self.config:
            return

        if self.config.get('compile'):
            exec_section = f'''

### How to Compile and Run

1. **Compile the code**:
   ```bash
   {self.config.get('compile_cmd', 'compiler')} hello.{self.config['ext']}
   ```

2. **Run your program**:
   ```bash
   {self.config['run_cmd']} hello
   ```

**Expected output:**
```
Hello, World!
```
'''
        else:
            exec_section = f'''

### How to Run

1. **Run the code**:
   ```bash
   {self.config['run_cmd']} hello.{self.config['ext']}
   ```

**Expected output:**
```
Hello, World!
```
'''

        # Insert after "Your Task" section
        insert_pos = task_match.end()
        self.content = self.content[:insert_pos] + exec_section + self.content[insert_pos:]
        self.modified = True

    def fix_all(self):
        """Apply all fixes."""
        self.load()
        self.fix_code_fences()
        self.ensure_execution_section()
        self.add_minimal_answer_key()
        self.remove_placeholder_ellipsis()
        self.fix_final_newline()
        return self.save()

def get_language_from_path(filepath: Path) -> str:
    """Extract language from file path."""
    parts = filepath.parts
    for part in parts:
        if part in LANG_CONFIG:
            return part
    # Special cases
    if 'c-c++' in parts:
        return 'cpp'
    return None

def main():
    """Main execution."""
    import sys

    root_dir = Path(__file__).parent

    # Get language filter from command line
    target_language = sys.argv[1] if len(sys.argv) > 1 else None

    # Find all lesson.md files (excluding c-c++)
    lessons = []
    for lang_dir in root_dir.iterdir():
        if not lang_dir.is_dir():
            continue
        if lang_dir.name == 'c-c++':
            continue
        if lang_dir.name.startswith('.'):
            continue

        # Filter by language if specified
        if target_language and lang_dir.name != target_language:
            continue

        for lesson in lang_dir.rglob('lesson.md'):
            lessons.append(lesson)

    print(f"Found {len(lessons)} lessons to process")
    if target_language:
        print(f"Processing only: {target_language}")

    fixed_count = 0
    for i, lesson_path in enumerate(sorted(lessons), 1):
        language = get_language_from_path(lesson_path)
        if not language:
            print(f"  Skipping {lesson_path} - unknown language")
            continue

        fixer = LessonFixer(lesson_path, language)
        if fixer.fix_all():
            fixed_count += 1
            print(f"  [{i}/{len(lessons)}] Fixed: {lesson_path.relative_to(root_dir)}")
        else:
            print(f"  [{i}/{len(lessons)}] OK: {lesson_path.relative_to(root_dir)}")

    print(f"\nComplete! Fixed {fixed_count}/{len(lessons)} files")

if __name__ == '__main__':
    main()
