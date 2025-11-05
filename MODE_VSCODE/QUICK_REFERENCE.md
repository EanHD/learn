# VS CODE MODE: Quick Reference

All essential keybindings and commands in one place.

---

## Vim Modes

| Mode | Indicator | Purpose | How to Enter |
|------|-----------|---------|--------------|
| **Normal** | `NORMAL` | Navigation & commands | Press `Esc` or `jk` |
| **Insert** | `INSERT` | Typing text | Press `i`, `a`, `o` |
| **Visual** | `VISUAL` | Selecting text | Press `v`, `V`, `Ctrl+v` |
| **Command** | `:` | Ex commands | Press `:` |

---

## Essential Vim Motions

### Basic Movement

| Key | Action |
|-----|--------|
| `h` `j` `k` `l` | Left, Down, Up, Right |
| `w` | Next word start |
| `b` | Previous word start |
| `e` | Next word end |
| `0` | Start of line |
| `^` | First non-blank character |
| `$` | End of line |
| `gg` | Top of file |
| `G` | Bottom of file |
| `{` `}` | Previous/next paragraph |
| `Ctrl+d` | Half page down |
| `Ctrl+u` | Half page up |
| `Ctrl+f` | Full page down |
| `Ctrl+b` | Full page up |

### Line Jumping (with Relative Numbers)

| Key | Action |
|-----|--------|
| `5j` | Jump 5 lines down |
| `10k` | Jump 10 lines up |
| `3w` | Jump 3 words forward |
| `:42` | Jump to line 42 |

### Entering Insert Mode

| Key | Action |
|-----|--------|
| `i` | Insert before cursor |
| `a` | Insert after cursor |
| `I` | Insert at start of line |
| `A` | Insert at end of line |
| `o` | New line below |
| `O` | New line above |
| `s` | Delete char and insert |
| `S` | Delete line and insert |

### Exiting Insert Mode

| Key | Action |
|-----|--------|
| `Esc` | Return to Normal mode |
| `jk` | Quick exit to Normal mode |
| `Ctrl+[` | Alternative exit |

---

## Editing Commands (Normal Mode)

### Delete (Cut)

| Key | Action |
|-----|--------|
| `x` | Delete character under cursor |
| `dw` | Delete word |
| `dd` | Delete line |
| `D` | Delete to end of line |
| `d$` | Delete to end of line |
| `d0` | Delete to start of line |
| `dap` | Delete paragraph |

### Copy (Yank)

| Key | Action |
|-----|--------|
| `yw` | Yank word |
| `yy` | Yank line |
| `Y` | Yank line |
| `y$` | Yank to end of line |
| `yap` | Yank paragraph |

### Paste

| Key | Action |
|-----|--------|
| `p` | Paste after cursor |
| `P` | Paste before cursor |

### Change

| Key | Action |
|-----|--------|
| `cw` | Change word |
| `cc` | Change line |
| `C` | Change to end of line |
| `ciw` | Change inner word |
| `ci"` | Change inside quotes |
| `ci(` | Change inside parentheses |

### Undo/Redo

| Key | Action |
|-----|--------|
| `u` | Undo |
| `Ctrl+r` | Redo |

### Repeat

| Key | Action |
|-----|--------|
| `.` | Repeat last change |

---

## Visual Mode

### Enter Visual Mode

| Key | Action |
|-----|--------|
| `v` | Character-wise visual |
| `V` | Line-wise visual |
| `Ctrl+v` | Block-wise visual |

### Visual Mode Operations

| Key | Action |
|-----|--------|
| `d` or `x` | Delete selection |
| `y` | Yank selection |
| `c` | Change selection |
| `>` | Indent right |
| `<` | Indent left |
| `~` | Toggle case |
| `u` | Lowercase |
| `U` | Uppercase |

---

## Search & Replace

### Search

| Key | Action |
|-----|--------|
| `/text` | Search forward for "text" |
| `?text` | Search backward for "text" |
| `n` | Next match |
| `N` | Previous match |
| `*` | Search word under cursor (forward) |
| `#` | Search word under cursor (backward) |

### Replace

| Command | Action |
|---------|--------|
| `:s/old/new` | Replace first on line |
| `:s/old/new/g` | Replace all on line |
| `:%s/old/new/g` | Replace all in file |
| `:%s/old/new/gc` | Replace all with confirmation |

---

## Leader Commands (Space)

**Leader Key**: `<Space>` in Normal mode

### File Operations

| Keys | Action |
|------|--------|
| `<Space>w` | Save file |
| `<Space>q` | Close editor |
| `<Space>ff` | Quick Open (find files) |
| `<Space>fg` | Find in files (search) |

### Window & Layout

| Keys | Action |
|------|--------|
| `<Space>e` | Toggle file explorer |
| `<Space>t` | Toggle terminal |
| `<Space>s` | Split editor |
| `<Space>=` | Equalize editor widths |
| `<Space>z` | Toggle Zen mode |

### Code Actions

| Keys | Action |
|------|--------|
| `<Space>c` | Comment line (Visual mode) |

---

## Window Navigation

### Switch Between Windows

| Key | Action |
|-----|--------|
| `Ctrl+h` | Move to left window |
| `Ctrl+j` | Move down |
| `Ctrl+k` | Move up |
| `Ctrl+l` | Move to right window |

### Resize Windows

| Key | Action |
|-----|--------|
| `Ctrl+=` | Equalize widths |

---

## VS Code Shortcuts

### Essential

| Key | Action |
|-----|--------|
| `Ctrl+Shift+T` | Toggle terminal |
| `Ctrl+Shift+B` | Toggle sidebar |
| `Ctrl+Shift+Z` | Toggle Zen mode |
| `Ctrl+\` | Split editor |
| `Ctrl+P` | Quick Open |
| `Ctrl+Shift+P` or `F1` | Command Palette |

### Terminal

| Key | Action |
|-----|--------|
| `Ctrl+Shift+T` | Open/close terminal |
| `Ctrl+Shift+5` | Split terminal |
| `Ctrl+Shift+C` | Copy (in terminal) |
| `Ctrl+Shift+V` | Paste (in terminal) |

### Markdown

| Key | Action |
|-----|--------|
| `Ctrl+Shift+V` | Open preview to side |
| `Ctrl+K V` | Open preview |

---

## Code Navigation (Language Server)

### Jump Around

| Key | Action |
|-----|--------|
| `gd` | Go to definition |
| `gr` | Find references |
| `gi` | Go to implementation |
| `K` | Show hover documentation |

### Intellisense

| Key | Action |
|-----|--------|
| `Ctrl+Space` | Trigger suggestions |
| `Tab` | Accept suggestion |
| `Esc` | Dismiss suggestions |

### Diagnostics

| Key | Action |
|-----|--------|
| `F8` | Next problem |
| `Shift+F8` | Previous problem |

---

## Multi-Cursor & Selection

| Key | Action |
|-----|--------|
| `Alt+Click` | Add cursor |
| `Ctrl+Alt+Down` | Add cursor below |
| `Ctrl+Alt+Up` | Add cursor above |
| `Ctrl+D` | Select next occurrence |
| `Ctrl+Shift+L` | Select all occurrences |

---

## Text Objects

Use with `d` (delete), `c` (change), `y` (yank), `v` (visual)

### Inner Objects (i)

| Command | Action |
|---------|--------|
| `iw` | Inner word |
| `i"` | Inside double quotes |
| `i'` | Inside single quotes |
| `i(` or `ib` | Inside parentheses |
| `i{` or `iB` | Inside braces |
| `i[` | Inside brackets |
| `it` | Inside HTML tag |

### Around Objects (a)

| Command | Action |
|---------|--------|
| `aw` | Around word (includes space) |
| `a"` | Around double quotes |
| `a'` | Around single quotes |
| `a(` or `ab` | Around parentheses |
| `a{` or `aB` | Around braces |
| `a[` | Around brackets |
| `at` | Around HTML tag |

### Examples

| Command | Effect |
|---------|--------|
| `diw` | Delete inner word |
| `ci"` | Change inside quotes |
| `ya(` | Yank around parentheses |
| `vi{` | Select inside braces |
| `dap` | Delete around paragraph |

---

## Marks & Jumps

### Set Marks

| Key | Action |
|-----|--------|
| `ma` | Set mark 'a' |
| `mA` | Set global mark 'A' |

### Jump to Marks

| Key | Action |
|-----|--------|
| `'a` | Jump to mark 'a' |
| `''` | Jump to previous position |
| `Ctrl+o` | Jump to older position |
| `Ctrl+i` | Jump to newer position |

---

## Macros

| Key | Action |
|-----|--------|
| `qa` | Record macro in register 'a' |
| `q` | Stop recording |
| `@a` | Play macro 'a' |
| `@@` | Replay last macro |
| `5@a` | Play macro 'a' 5 times |

---

## Ex Commands

Type `:` in Normal mode, then:

| Command | Action |
|---------|--------|
| `:w` | Save |
| `:q` | Quit |
| `:wq` or `:x` | Save and quit |
| `:q!` | Quit without saving |
| `:e file.txt` | Open file |
| `:bn` | Next buffer |
| `:bp` | Previous buffer |
| `:bd` | Close buffer |
| `:sp file` | Split horizontally |
| `:vsp file` | Split vertically |
| `:!command` | Run shell command |
| `:noh` | Clear search highlighting |

---

## Learning Path

### Day 1-3: Basics
- `hjkl` movement
- `i` and `Esc`
- `<Space>w` to save
- `dd`, `yy`, `p`

### Week 1: Core Motions
- `w`, `b`, `e`
- `0`, `$`
- `gg`, `G`
- `f`, `t`
- Number + motion: `5j`, `3w`

### Week 2-3: Editing
- `c`, `d`, `y` with motions
- Text objects: `ciw`, `di"`, `ya{`
- Visual mode: `v`, `V`
- Undo/redo: `u`, `Ctrl+r`

### Week 4+: Advanced
- Search: `/`, `n`, `*`
- Replace: `:%s/old/new/g`
- Marks: `ma`, `'a`
- Macros: `qa`, `@a`

---

## Tips

1. **Don't memorize everything** - Learn gradually
2. **Practice daily** - Muscle memory takes time
3. **Use relative numbers** - They're perfect for Vim
4. **Start simple** - Master `hjkl`, `i`, `Esc` first
5. **Use `.` to repeat** - Most powerful command
6. **Think in text objects** - `ciw`, `di(`, `ya{`
7. **Use `<Space>` commands** - Easier than `:` commands
8. **Learn one new thing daily** - Steady progress

---

## Getting Help

- **In VS Code**: `F1` → Search for command
- **Vim help**: `:help command`
- **Keybindings**: `Ctrl+K Ctrl+S`
- **Documentation**: [README.md](README.md)
- **Vim basics**: [../VIM_CHEATSHEET.md](../VIM_CHEATSHEET.md)

---

**Print this page and keep it nearby while learning!**
