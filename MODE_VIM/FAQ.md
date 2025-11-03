# FAQ: Vim Mode Learning

Common questions and answers for learning in Vim mode.

## Getting Started

**Q: Do I need to know Vim already?** 
A: No! This mode teaches Vim as you learn programming. Start with [QUICK_START.md](../QUICK_START.md).

**Q: My Vim config is different. Will it work?** 
A: The `init-learning.vim` config is standalone, so it won't affect your normal config. It's optimized just for learning.

**Q: Can I use my existing Vim config instead?** 
A: Yes, but you might lose some learning optimizations. Copy the settings from `init-learning.vim` to your config.

**Q: I use VS Code. Can I still learn?** 
A: Yes! See [MODE_VSCODE/](../MODE_VSCODE/) (coming soon) or skip to the VS Code specific guides.

---

## Using the Split-Screen Setup

**Q: How do I split the window?** 
A: Inside Vim, type `:vsplit` to split vertically. See [WORKFLOWS/split-screen-learning.md](../WORKFLOWS/split-screen-learning.md).

**Q: The windows are too narrow. How do I resize?** 
A: Use `C-w =` to equal-size, or `C-w >` to widen the current window.

**Q: How do I switch between windows?** 
A: Press `C-h` (left) or `C-l` (right). These are mapped in the learning config.

**Q: Can I have more than 2 windows?** 
A: Yes! Use `:split` and `:vsplit` repeatedly. But 2 is usually best for learning.

**Q: How do I close a window?** 
A: Press `:q` to close the current window, or `:qa` to close all.

---

## Searching and Navigation in Lessons

**Q: How do I find a specific concept in the lesson?** 
A: Use `/` to search. Type `/pattern` and press Enter.

**Q: How do I jump to the next occurrence?** 
A: After searching, press `n` to go to the next match, `N` for previous.

**Q: How do I get back to the top of the lesson?** 
A: Press `gg` (go to beginning) or `G` to go to the end.

**Q: How do I jump to line 50?** 
A: Type `:50` and press Enter.

**Q: Can I mark an important section to jump back to?** 
A: Yes! Type `ma` to mark (using 'a'), then `'a` to jump back to that mark.

---

## Editing and Coding

**Q: How do I start typing code?** 
A: Press `i` to enter insert mode, then type. Press `Esc` to exit.

**Q: How do I delete a line?** 
A: In normal mode, press `dd`.

**Q: How do I undo a mistake?** 
A: Press `u` to undo. Press `C-r` to redo.

**Q: How do I save my code?** 
A: Type `:w` (write) and press Enter.

**Q: How do I save and quit?** 
A: Type `:wq` and press Enter.

---

## Compiling and Testing

**Q: How do I compile my C code from Vim?** 
A: Type `:terminal` to open a terminal, then run `gcc solution.c -o solution && ./solution`.

**Q: How do I compile Rust?** 
A: Same as C, but use `rustc solution.rs -o solution && ./solution`.

**Q: How do I go back to editing after running code?** 
A: Inside the terminal, press `Exit` or `Ctrl-d`, then return to the editor.

**Q: Can I compile without opening a terminal?** 
A: Not easily in default Vim, but the terminal buffer approach works great.

**Q: How do I re-run the last command?** 
A: In terminal, press the up arrow to recall previous commands.

---

## Saving Your Workspace

**Q: How do I save the window layout I set up?** 
A: Type `:mksession my-lesson.vim` to save the current session.

**Q: How do I restore a saved session?** 
A: Start Vim with `nvim -S my-lesson.vim`.

**Q: Can I have one session per lesson?** 
A: Yes! You can name them like `lesson-1.vim`, `lesson-2.vim`, etc.

**Q: Where are sessions saved?** 
A: By default, in your current directory. You can specify a path: `:mksession ~/sessions/lesson1.vim`.

---

## Macros and Efficiency

**Q: What's a macro?** 
A: A recorded sequence of commands that you can replay. Great for repetitive tasks.

**Q: How do I record a macro?** 
A: Type `qa` to start recording macro 'a', do your commands, then type `q` to stop.

**Q: How do I replay a macro?** 
A: Type `@a` to play macro 'a', or `5@a` to play it 5 times.

**Q: Can I record in the lesson (read-only) buffer?** 
A: Macros are for editing, which you can't do in read-only mode. Record in the code editor (right window).

---

## Read-Only Lesson Files

**Q: Why can't I edit the lesson?** 
A: It's set to read-only to prevent accidents. This is intentional!

**Q: How do I temporarily edit the lesson?** 
A: Type `:set noreadonly` to unlock, then `:set readonly` to lock again.

**Q: But I want to take notes in the lesson.** 
A: Better idea: use the code file (right window) to write comments and notes there instead.

---

## Keyboard Shortcuts Reference

### Movement
- `gg` — Go to top
- `G` — Go to bottom
- `j` — Down line
- `k` — Up line
- `h` — Left
- `l` — Right
- `w` — Next word
- `b` — Previous word

### Searching
- `/pattern` — Search forward
- `?pattern` — Search backward
- `n` — Next match
- `N` — Previous match

### Editing
- `i` — Insert mode
- `a` — Append
- `dd` — Delete line
- `p` — Paste
- `u` — Undo
- `C-r` — Redo
- `C-h` — Backspace in insert mode

### Windows
- `C-w h` — Move left
- `C-w l` — Move right
- `C-w j` — Move down
- `C-w k` — Move up
- `C-w =` — Equal width
- `C-w >` — Widen
- `C-w <` — Narrow

### Buffers
- `:bn` — Next buffer
- `:bp` — Previous buffer
- `C-^` — Toggle last buffer
- `:ls` — List buffers

### Macros & Marks
- `ma` — Mark 'a'
- `'a` — Jump to mark
- `qa` — Start macro
- `q` — Stop macro
- `@a` — Play macro

### File Operations
- `:w` — Save
- `:wq` — Save & quit
- `:q` — Quit
- `:q!` — Quit without saving

---

## Terminal Integration

**Q: Can I compile without leaving Vim?** 
A: Yes! Use `:terminal` to open an embedded terminal.

**Q: How do I toggle between code editing and terminal?** 
A: Press `C-w j` to go to terminal, `C-w k` to go back to editor.

**Q: Can I split code and terminal side-by-side?** 
A: Yes! Use `:vsplit` before opening terminal, or `:split` for horizontal.

---

## Performance & Troubleshooting

**Q: Vim is slow with large lesson files.** 
A: This shouldn't happen. Try: `:set syntax=off` or close other buffers with `:bd`.

**Q: My colors look weird.** 
A: Check your terminal supports true color: `:set termguicolors`. Or try a different colorscheme: `:colorscheme default`.

**Q: Terminal output looks messed up.** 
A: Try scrolling with `C-u` and `C-d`, or type `reset` in terminal.

**Q: I can't paste from terminal to code.** 
A: Make sure clipboard is enabled: `:set clipboard=unnamedplus`.

---

## Learning Progression

**Q: Should I learn all the Vim commands at once?** 
A: No! Learn them naturally as you encounter them. Start with: `hjkl`, `i/Esc`, `/n`, `:w`, `C-w`.

**Q: What's the minimum Vim to know to start?** 
A: Movement (`hjkl`), insert (`i`), exit insert (`Esc`), save (`:w`), search (`/`), windows (`C-w`).

**Q: How long until I'm fast with Vim?** 
A: ~3 hours of actual use. After 1 week, you'll be significantly faster than GUI editors.

---

## Customization

**Q: Can I change the colorscheme?** 
A: Yes! Edit `init-learning.vim` and change the `colorscheme` line.

**Q: Can I add my own keybindings?** 
A: Yes! Edit `init-learning.vim` and add your mappings.

**Q: Can I use my own plugins?** 
A: Yes, but the learning config is minimal on purpose. Add plugins carefully.

**Q: Where do I make permanent changes?** 
A: Edit `~/.config/nvim/init-learning.vim` or copy settings to your main `init.vim`.

---

## Advanced Topics

**Q: Can I use Vim plugins like fzf or telescope?** 
A: Yes, but they're optional. The learning config works without them.

**Q: Can I use LSP (language server) for autocomplete?** 
A: Not in the basic learning config, but you can add it if you know how.

**Q: Can I integrate with git?** 
A: Yes! Use `:terminal` and run git commands, or use a plugin like vim-fugitive.

**Q: Can I automate lesson progress tracking?** 
A: Yes, the CLI tool (coming soon) handles this.

---

## Philosophy Questions

**Q: Why Vim instead of VS Code for learning?** 
A: Vim skills transfer anywhere. VS Code is IDE-specific. Vim is universal.

**Q: Is Vim hard to learn?** 
A: The basics (`hjkl`, `i`, `:w`) take ~1 hour. Advanced stuff is optional.

**Q: Will learning Vim slow down my programming?** 
A: Yes, for the first few hours. No, after that—you'll be faster.

**Q: What if I hate Vim?** 
A: Use [MODE_VSCODE/](../MODE_VSCODE/) instead (coming soon).

---

## Getting Help

**Stuck?** Check:
1. [QUICK_START.md](../QUICK_START.md) — 5-minute setup
2. [WORKFLOWS/split-screen-learning.md](../WORKFLOWS/split-screen-learning.md) — Your exact workflow
3. [TIPS/](../TIPS/) folder — Specific techniques
4. `:help` inside Vim — Built-in documentation
5. Type `:LessonNav` — Quick command reference

---

**Ready to learn?** → Start with [QUICK_START.md](../QUICK_START.md) 

