# Split-Screen Learning Workflow

A detailed walkthrough of learning with VS Code + Vim in split-screen mode.

---

## Overview

This workflow maximizes learning efficiency with:
- **Left pane:** Lesson content (read-only reference)
- **Right pane:** Your code (where you work)
- **Bottom panel:** Terminal (compile & run)

---

## Step-by-Step Walkthrough

### 1. Open Your Workspace

```bash
cd ~/LEARN
code .
```

**Result:** VS Code opens with LEARN workspace, Vim mode active.

---

### 2. Navigate to a Lesson

**Option A: File Explorer**

1. Press `Ctrl+Shift+E` to open explorer
2. Navigate: `dart → stage-1 → level-1`
3. Click `lesson.md`

**Option B: Quick Open**

1. Press `Ctrl+P`
2. Type `lesson.md`
3. Select the one you want
4. Press Enter

**Option C: Terminal**

```bash
# In VS Code terminal (Ctrl+Shift+T)
cd dart/stage-1/level-1
code lesson.md
```

---

### 3. Set Up Split View

With `lesson.md` open:

1. **Split editor:** Press `Ctrl+\`
2. **Open code file:** Press `Ctrl+P`, type `main.dart`, Enter
3. **Move to right pane:** Press `Ctrl+l`
4. **Equalize widths:** Press `Ctrl+=`

**Your screen now looks like:**

```
╔════════════════════╦════════════════════╗
║   lesson.md        ║   main.dart        ║
║   (left)           ║   (right)          ║
╚════════════════════╩════════════════════╝
```

---

### 4. Read the Lesson (Left Pane)

**Switch to left pane:** `Ctrl+h`

**Navigate with Vim:**

```vim
gg          " Jump to top
/Learning   " Search for "Learning Goals"
n           " Next match
G           " Jump to bottom
Ctrl+d      " Scroll down half page
Ctrl+u      " Scroll up half page
```

**What to look for:**

1. **Learning Goals** - What you should learn
2. **Key Concepts** - Definitions and explanations
3. **Examples** - Reference code
4. **Exercises** - What to implement

**Optional: Preview Mode**

- Press `Ctrl+Shift+V` for rendered markdown
- Scrolls in sync with source
- Beautiful formatting

---

### 5. Write Code (Right Pane)

**Switch to right pane:** `Ctrl+l`

**Enter Insert mode:** `i`

**Example workflow for Dart:**

```dart
void main() {
  // Start typing here
  print('Hello, World!');
}
```

**Vim tips while coding:**

```vim
i           " Insert before cursor
a           " Insert after cursor
o           " New line below and insert
O           " New line above and insert

Esc         " Exit insert mode
jk          " Quick exit (if you type fast)

dd          " Delete line
yy          " Copy line
p           " Paste

u           " Undo
Ctrl+r      " Redo

:w          " Save
<Space>w    " Save (leader command)
```

**Get help from language server:**

```vim
K           " Show documentation (hover)
gd          " Go to definition
Ctrl+Space  " Trigger autocomplete
```

---

### 6. Open Terminal (Bottom Panel)

**Toggle terminal:** `Ctrl+Shift+T` or `<Space>t`

**Your screen now:**

```
╔════════════════════╦════════════════════╗
║   lesson.md        ║   main.dart        ║
║   (left)           ║   (right)          ║
╠════════════════════╩════════════════════╣
║  Terminal                               ║
║  $                                      ║
╚═════════════════════════════════════════╝
```

---

### 7. Compile & Run

**In terminal:**

**For Dart:**
```bash
dart run main.dart
```

**For C++:**
```bash
make        # or: g++ main.cpp -o main
./main
```

**For Rust:**
```bash
cargo run   # or: rustc main.rs && ./main
```

**For Python:**
```bash
python3 main.py
```

**Switch between code and terminal:**

- `Ctrl+l` - Focus code editor
- `Ctrl+j` - Focus terminal
- Or click with mouse

---

### 8. Debug & Iterate

**Typical cycle:**

1. **Write code** (right pane, Insert mode)
2. **Save:** `Esc` then `<Space>w`
3. **Run:** Switch to terminal, run command
4. **See output:** Read error messages
5. **Fix:** Switch back to code (`Ctrl+k`), fix issue
6. **Repeat:** Until it works!

**Common debug workflow:**

```vim
" In code editor
Ctrl+l      " Focus code
/error      " Search for error keyword
n           " Next occurrence
i           " Fix the code
Esc
<Space>w    " Save
Ctrl+j      " Back to terminal
↑ Enter     " Re-run last command
```

---

### 9. Reference the Lesson

**Quick peek at lesson without losing focus:**

```vim
Ctrl+h      " Switch to lesson
/example    " Find example code
yy          " Copy line
Ctrl+l      " Back to your code
p           " Paste
```

**Or use split preview:**

1. With lesson.md active: `Ctrl+Shift+V`
2. Now you have 3 panes: Source, Preview, Code
3. Read rendered lesson while coding

---

### 10. Save & Move to Next Lesson

**Save your work:**

```vim
Esc         " Exit insert mode
<Space>w    " Save file
```

**Optional: Commit to git:**

```bash
git add .
git commit -m "Completed stage-1 level-1"
```

**Open next lesson:**

**Option A: File Explorer**
- `Ctrl+Shift+E`
- Navigate to `level-2/lesson.md`

**Option B: Quick Open**
- `Ctrl+P`
- Type next lesson path

**Option C: CLI**
```bash
learn dart 2
```

---

## Advanced Workflows

### Workflow 1: Multiple Terminals

For complex projects with build watchers:

1. **Terminal 1:** Development server
   ```bash
   dart run --observe
   ```

2. **Terminal 2:** Tests
   ```bash
   dart test --watch
   ```

3. **Terminal 3:** Git commands
   ```bash
   git status
   ```

**Create splits:** `Ctrl+Shift+5` in terminal

---

### Workflow 2: Zen Mode Focus

For deep concentration:

1. Read lesson fully
2. Press `Ctrl+Shift+Z` (Zen mode)
3. Code without distractions
4. Press `Esc` `Esc` when done
5. Return to split view

---

### Workflow 3: Markdown + Code + Preview

For documentation-heavy lessons:

```
╔═══════════════╦═══════════════╗
║  lesson.md    ║  Lesson       ║
║  (source)     ║  (rendered)   ║
╠═══════════════╩═══════════════╣
║  main.dart    ║  Terminal     ║
╚═══════════════╩═══════════════╝
```

**Setup:**
1. Open lesson.md
2. `Ctrl+Shift+V` (preview side-by-side)
3. `Ctrl+\` (split below)
4. Open code file (bottom-left)
5. `Ctrl+Shift+T` (terminal bottom-right)

---

### Workflow 4: Multi-File Projects

When lesson requires multiple files:

```
╔═══════════════╦═══════════════╗
║  lesson.md    ║  main.dart    ║
╠═══════════════╬═══════════════╣
║  utils.dart   ║  Terminal     ║
╚═══════════════╩═══════════════╝
```

**Setup:**
1. Open lesson.md (top-left)
2. `Ctrl+\` split right → open main.dart
3. `Ctrl+\` split below-left → open utils.dart
4. `Ctrl+\` split below-right → terminal

**Navigate:**
- `Ctrl+h/j/k/l` to move between panes
- `Ctrl+P` to quickly open files

---

## Pro Tips

### Tip 1: Save Time with Marks

Set marks to jump between important sections:

```vim
" In lesson.md
/Key Concepts    " Find concepts section
ma               " Mark as 'a'
/Examples        " Find examples
mb               " Mark as 'b'

" Later, jump instantly:
'a               " Jump to concepts
'b               " Jump to examples
```

### Tip 2: Use Visual Mode for Examples

Copy example code from lesson:

```vim
Ctrl+h           " Switch to lesson
/example         " Find example
V                " Visual line mode
5j               " Select 5 lines
y                " Yank (copy)
Ctrl+l           " Switch to code
p                " Paste
```

### Tip 3: Keep Terminal History

Don't close terminal between lessons:

- Terminal history persists
- Use ↑ to recall commands
- Saves retyping `dart run`, `make`, etc.

### Tip 4: Leverage Language Server

```vim
" In your code
K                " Hover docs (what does this function do?)
gd               " Jump to definition
Ctrl+o           " Jump back
gr               " Find all references
```

### Tip 5: Use Macros for Repetitive Tasks

```vim
qa               " Record macro 'a'
i                " Insert mode
// TODO:        " Type comment
Esc              " Normal mode
j                " Next line
q                " Stop recording

@a               " Run macro (adds TODO comment)
10@a             " Run 10 times
```

---

## Common Patterns

### Pattern: Read → Code → Test → Fix

```vim
" 1. Read
Ctrl+h           " Lesson pane
gg               " Top
/Exercise        " Find exercise

" 2. Code
Ctrl+l           " Code pane
i                " Insert mode
" ... type code ...
Esc
<Space>w         " Save

" 3. Test
Ctrl+j           " Terminal
↑ Enter          " Rerun last command

" 4. Fix (if errors)
Ctrl+k           " Back to code
/error_line      " Find error
cw               " Change word
Esc
<Space>w         " Save
Ctrl+j           " Terminal
↑ Enter          " Test again
```

### Pattern: Compare Example to Your Code

```vim
" Split lesson and code side-by-side
Ctrl+h           " Lesson
/Example         " Find example
Ctrl+l           " Your code

" Compare by eye, or:
Ctrl+h           " Back to lesson
V                " Visual mode
10j              " Select example
y                " Copy
Ctrl+l           " Your code
o                " New line
p                " Paste
" Now compare directly
dd               " Delete when done
```

---

## Troubleshooting Workflows

### Problem: Lost track of which pane is which

**Solution:**
- Look at filename in tab
- Status bar shows current file
- Or press `Ctrl+Shift+E` to see file tree

### Problem: Terminal output scrolled away

**Solution:**
- Scroll up in terminal with mouse
- Or `Ctrl+Shift+T` to close/reopen
- Or split terminal and keep both outputs

### Problem: Code and lesson widths uneven

**Solution:**
- Press `Ctrl+=` to equalize
- Or drag divider with mouse
- Or close sidebar: `Ctrl+Shift+B`

---

## Summary: Essential Keys

| Action | Key | When |
|--------|-----|------|
| Switch left | `Ctrl+h` | Any pane |
| Switch right | `Ctrl+l` | Any pane |
| Switch down | `Ctrl+j` | Any pane |
| Switch up | `Ctrl+k` | Any pane |
| Split editor | `Ctrl+\` | Editor |
| Equalize | `Ctrl+=` | Editor |
| Toggle terminal | `Ctrl+Shift+T` | Anytime |
| Insert mode | `i` | Normal mode |
| Normal mode | `Esc` or `jk` | Insert mode |
| Save | `<Space>w` | Normal mode |
| Quick Open | `Ctrl+P` | Anytime |

---

**Master this workflow and you'll learn faster than ever! 🚀**
