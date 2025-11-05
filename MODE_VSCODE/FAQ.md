# VS CODE MODE: Frequently Asked Questions

Quick answers to common questions about using VS Code with Vim for learning.

---

## General Questions

### Q: Do I need to know Vim to use this?

**A:** No! You'll learn Vim gradually as you learn programming. Start with basics:
- `i` to type
- `Esc` to stop typing
- `hjkl` to move
- `<Space>w` to save

That's enough to get started.

### Q: Can I use the mouse?

**A:** Yes! The Vim extension doesn't disable mouse support. Use the mouse whenever you want, but try keyboard shortcuts - they're faster once you learn them.

### Q: Is this better than MODE_VIM (Neovim)?

**A:** Different, not better:

| Feature | MODE_VSCODE | MODE_VIM |
|---------|-------------|----------|
| **GUI** | ✅ Rich UI | Terminal only |
| **Mouse** | ✅ Full support | Limited |
| **Speed** | Good | ⚡ Faster |
| **Plugins** | VS Code extensions | Lua plugins |
| **Learning Curve** | Gentler | Steeper |
| **Setup** | Install extension | Already done |

Choose what fits your style!

### Q: Will my code automatically save?

**A:** Yes! Auto-save is enabled with a 1-second delay. You can still manually save with `<Space>w` or `:w`.

---

## Vim Questions

### Q: How do I exit Vim mode?

**A:** You don't need to! Just press `Esc` to return to Normal mode. If you really want to disable Vim:

```
Ctrl+Shift+P → "Toggle Vim Mode"
```

### Q: I pressed something and now the screen is weird!

**A:** Common issues:

**Problem:** Cursor is a thin line
- **Cause:** You're in Insert mode
- **Fix:** Press `Esc`

**Problem:** Text is highlighted
- **Cause:** You're in Visual mode
- **Fix:** Press `Esc`

**Problem:** Everything is command-line
- **Cause:** You pressed `:`
- **Fix:** Press `Esc` or `Ctrl+C`

**Problem:** Numbers appear when I move
- **Cause:** You pressed a number accidentally
- **Fix:** Press `Esc`

### Q: What does `<leader>` mean?

**A:** It's your "prefix key" for custom commands. It's set to `<Space>` (spacebar).

So `<leader>w` means: Press `Space`, then press `w`

### Q: Can I change the leader key?

**A:** Yes! Edit `.vscode/settings.json`:

```json
{
  "vim.leader": ","  // Now comma is your leader
}
```

### Q: Typing `jk` makes me exit Insert mode. Can I disable this?

**A:** Yes! Edit `.vscode/settings.json`:

```json
{
  "vim.insertModeKeyBindings": []  // Remove the jk binding
}
```

### Q: How do I copy/paste from outside VS Code?

**A:** It's already enabled! System clipboard is on by default.

- **Copy from Vim:** `yy` (copies to system clipboard)
- **Paste in Vim:** `p` (even if you copied from browser)
- **Copy from outside:** `Ctrl+C` still works
- **Paste from outside:** `Ctrl+V` in Insert mode

---

## Setup Questions

### Q: Do I need to install anything?

**A:** Just the Vim extension:

```bash
code --install-extension vscodevim.vim
```

Everything else is optional but recommended for language support.

### Q: Where are the settings stored?

**A:** In the workspace: `LEARN/.vscode/settings.json`

Your personal settings are separate: `~/.config/Code/User/settings.json`

Workspace settings override personal settings when the LEARN folder is open.

### Q: Can I use these settings in other projects?

**A:** Yes! Copy `.vscode/` folder to any project:

```bash
cp -r ~/LEARN/.vscode ~/my-other-project/
```

### Q: How do I update the configuration?

**A:** Edit files in `.vscode/`:

- **Workspace settings:** `.vscode/settings.json`
- **Keybindings:** `.vscode/keybindings.json`
- **Extensions:** `.vscode/extensions.json`

Or use VS Code UI: `Ctrl+,` for settings, `Ctrl+K Ctrl+S` for keybindings.

---

## Layout Questions

### Q: How do I split the editor?

**A:** Multiple ways:

- Press `Ctrl+\`
- Press `<Space>s` (in Normal mode)
- Right-click editor tab → "Split Right"

### Q: How do I close a split?

**A:**
- Press `<Space>q` (in Normal mode)
- Or `Ctrl+W` (normal VS Code shortcut)
- Or click the X on the tab

### Q: How do I resize splits?

**A:**
- **Equalize:** `Ctrl+=` or `<Space>=`
- **Mouse:** Drag the divider between editors
- **Commands:** `Ctrl+Shift+P` → "View: Increase/Decrease Editor Width"

### Q: Can I have 3 or more splits?

**A:** Yes! Just keep splitting:

1. Open file 1
2. Press `Ctrl+\` to split (now 2 panes)
3. Press `Ctrl+\` again (now 3 panes)
4. Continue as needed

### Q: How do I switch between splits?

**A:**
- `Ctrl+h` - Left
- `Ctrl+l` - Right
- `Ctrl+j` - Down
- `Ctrl+k` - Up
- Or click with mouse

---

## Terminal Questions

### Q: How do I open the terminal?

**A:**
- Press `Ctrl+Shift+T`
- Or `<Space>t` (in Normal mode)
- Or View → Terminal from menu

### Q: How do I close the terminal?

**A:**
- Press `Ctrl+Shift+T` again (toggles)
- Or type `exit` in terminal
- Or click the X on terminal tab

### Q: Can I have multiple terminals?

**A:** Yes!

- Press `Ctrl+Shift+5` to split terminal
- Or click `+` button in terminal panel
- Or right-click terminal → "Split Terminal"

### Q: How do I switch between terminals?

**A:**
- Click the terminal tab
- Or use dropdown in terminal panel
- Or `Ctrl+Shift+]` to cycle

### Q: Terminal takes too much space!

**A:** Resize it:
- Drag the top border of terminal panel
- Or close it: `Ctrl+Shift+T`
- Or minimize: Click ∧ on terminal panel

---

## Lesson Questions

### Q: Why can't I edit lesson.md files?

**A:** They're read-only by design! Lessons are reference material. Write your code in the separate code files (main.cpp, main.py, etc.).

If you really need to edit a lesson:

```json
// In .vscode/settings.json, remove or comment out:
"files.readonlyInclude": {
  "**/lesson.md": true
}
```

### Q: How do I navigate between lessons?

**A:**

**Method 1:** File Explorer
- Press `Ctrl+Shift+E`
- Navigate to next lesson folder
- Open the lesson.md

**Method 2:** Quick Open
- Press `Ctrl+P`
- Type lesson name
- Press Enter

**Method 3:** CLI (from terminal)
```bash
# Use the learn command
learn c++ 2      # Next level
learn c++ 3      # Skip ahead
```

### Q: Can I preview markdown?

**A:** Yes! With lesson.md open:

- Press `Ctrl+Shift+V` for side-by-side preview
- Or `Ctrl+K V` for preview in new tab
- Or click preview icon (top-right of editor)

### Q: The markdown preview looks different from the lesson file!

**A:** That's normal! Markdown is rendered as HTML in preview. To see raw markdown, look at the source file (left pane).

---

## Language Questions

### Q: Auto-completion isn't working!

**A:**

1. Install language extension:
   - C/C++: `code --install-extension ms-vscode.cpptools`
   - Rust: `code --install-extension rust-lang.rust-analyzer`
   - Python: `code --install-extension ms-python.python`

2. Reload window: `Ctrl+Shift+P` → "Reload Window"

3. Wait a few seconds for language server to start

4. Try `Ctrl+Space` to manually trigger suggestions

### Q: "Go to Definition" doesn't work!

**A:** Language server might not be ready:

- Wait 5-10 seconds after opening a file
- Check bottom-right corner for loading indicator
- Ensure language extension is installed
- Try `Ctrl+Shift+P` → "Reload Window"

### Q: Code formatting not working!

**A:**

Press `Shift+Alt+F` to format, or enable format-on-save:

```json
{
  "editor.formatOnSave": true
}
```

Make sure language formatter is installed (should be in recommended extensions).

---

## Performance Questions

### Q: VS Code feels slow with Vim!

**A:** Try these optimizations:

```json
{
  "vim.highlightedyank.enable": false,
  "editor.cursorBlinking": "solid",
  "editor.smoothScrolling": false
}
```

### Q: Typing lags in Insert mode!

**A:** Disable expensive Vim features:

```json
{
  "vim.easymotion": false,
  "vim.sneak": false
}
```

### Q: Scrolling is slow!

**A:**

```json
{
  "editor.smoothScrolling": false,
  "editor.cursorSmoothCaretAnimation": "off"
}
```

---

## Customization Questions

### Q: Can I change the color theme?

**A:** Yes!

```
Ctrl+K Ctrl+T → Select theme
```

Popular themes:
- Tokyo Night
- One Dark Pro
- Dracula
- Material Theme

Install themes: `Ctrl+Shift+X` → Search theme name → Install

### Q: Can I make the font bigger?

**A:** Yes! Edit settings:

```json
{
  "editor.fontSize": 16,
  "editor.lineHeight": 1.8
}
```

Or use: `Ctrl+` (increase) / `Ctrl-` (decrease)

### Q: Can I customize the keybindings?

**A:** Absolutely!

```
Ctrl+K Ctrl+S → Click any binding to edit
```

Or edit `.vscode/keybindings.json` directly.

### Q: Can I disable relative line numbers?

**A:** Yes:

```json
{
  "editor.lineNumbers": "on"  // Instead of "relative"
}
```

---

## Workflow Questions

### Q: What's the recommended workflow for a lesson?

**A:**

1. Open `lesson.md` (left pane) - Read goals and concepts
2. Split editor `Ctrl+\`
3. Open code file (right pane) - Write your solution
4. Switch to code pane `Ctrl+l`
5. Code in Insert mode `i`
6. Save often `Esc` then `<Space>w`
7. Open terminal `Ctrl+Shift+T`
8. Compile and run
9. Fix errors, repeat
10. Move to next lesson

### Q: Should I use Zen Mode?

**A:** Use it when you need deep focus:

- Press `Ctrl+Shift+Z` or `<Space>z`
- Fullscreen, no distractions
- Perfect for complex problems
- Press `Esc` `Esc` to exit

Good for:
- Reading long lessons
- Debugging complex code
- Writing essays in markdown
- Deep concentration work

### Q: How do I run my code?

**A:** Depends on language:

**C++:**
```bash
make        # or: g++ main.cpp -o main
./main
```

**Rust:**
```bash
cargo run   # or: rustc main.rs && ./main
```

**Python:**
```bash
python3 main.py
```

**Dart:**
```bash
dart run main.dart
```

Or use tasks: `Ctrl+Shift+P` → "Tasks: Run Task"

---

## Troubleshooting

### Q: Nothing works after installing Vim!

**A:** Did you reload?

```
Ctrl+Shift+P → "Developer: Reload Window"
```

### Q: I can't type anything!

**A:** You're in Normal mode. Press `i` to enter Insert mode.

### Q: Ctrl+C doesn't copy!

**A:** In Vim, `Ctrl+C` exits Insert mode. For copying:

- In Normal/Visual mode: `y` (yank)
- In Insert mode: Use mouse to select, then `Ctrl+Shift+C`
- Or use `yy` in Normal mode to copy whole line

### Q: My custom settings aren't working!

**A:** Check:

1. Did you edit the **workspace** settings? (`.vscode/settings.json`)
2. Did you reload? (`Ctrl+Shift+P` → "Reload Window")
3. Are there typos in JSON? (Check bottom-right for JSON errors)
4. Did you save the file? (`Ctrl+S`)

---

## Getting More Help

- **Command Palette:** `F1` or `Ctrl+Shift+P` - Search for any command
- **Keyboard Shortcuts:** `Ctrl+K Ctrl+S` - See all keybindings
- **Documentation:** [README.md](README.md) - Full VS Code Mode guide
- **Quick Reference:** [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - All commands
- **Vim Basics:** [../VIM_CHEATSHEET.md](../VIM_CHEATSHEET.md) - Vim fundamentals

---

**Still stuck? Check the docs or try the Vim tutor: `vimtutor` in terminal!**
