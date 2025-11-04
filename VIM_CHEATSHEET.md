# Quick Reference Card

Keep this handy while learning!

## Open Lessons (CLI)

```
learn c++ 1             Open C++ Level 1
learn rust 2            Open Rust Level 2
learn c++ 1 --stage 3   Open C++ Stage 3, Level 1
learn --list            List all lessons
learn --info            Show your progress
learn --next            Get suggestion for next lesson
```

## Window Navigation (Vim)

```
C-h                     Move left
C-l                     Move right
C-j                     Move down
C-k                     Move up
C-=                     Equal size windows
C-+                     Wider window
C-_                     Narrower window
```

## Lesson Navigation (Vim)

```
<leader>n               Next lesson
<leader>p               Previous lesson
<leader>i               Show current lesson info
<leader>?               Show help popup
```

## Essential Vim Commands

```
gg                      Top of file
G                       Bottom of file
/text                   Search forward
?text                   Search backward
n                       Next match
N                       Previous match

i / a / o               Insert / Append / New line
dd                      Delete line
p                       Paste
:w                      Save file
:q                      Quit
```

## Marks (Bookmark Positions)

```
ma                      Mark position as 'a'
mb                      Mark position as 'b'
'a                      Jump to mark 'a'
'b                      Jump to mark 'b'
```

## Terminal (Inside Vim)

```
:terminal               Open terminal
C-j                     Focus terminal window
exit                    Exit terminal

Inside terminal:
gcc solution.c -o solution && ./solution  (Compile C++)
rustc solution.rs -o solution && ./solution  (Compile Rust)
python3 solution.py     (Run Python)
```

## File Operations

```
:e filename             Open file
:w                      Save file
:q                      Quit
:q!                     Quit without saving
:wq                     Save and quit
```

---

## Typical Learning Session

1. Open lesson:           `learn c++ 1`
2. Read lesson (left):    `gg`, `/`, `G`, `n`
3. Switch to code (right):`C-l`
4. Write solution:        `i`, type code, `Esc`, `:w`
5. Open terminal:         `:terminal`
6. Compile/run:           `gcc solution.c -o solution && ./solution`
7. Next lesson:           `:call NextLesson()` or `learn c++ 2`

---

## Pro Tips

- Use marks to bookmark important sections: `ma`, then `'a` to return
- Search for "Learning Goals" to quickly find what to focus on
- Keep terminal open during coding for quick testing
- Use `C-^` in Vim to toggle between last two files
- Session management: `:mksession lesson1.vim` to save, `nvim -S lesson1.vim` to restore

