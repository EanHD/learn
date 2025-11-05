# EDITOR ALIGNMENT GUIDE

Cross-platform consistency for Vim, Neovim, and VS Code.

---

## Overview

The LEARN platform provides three ways to learn programming:

1. **Plain Vim** (`.vimrc`)
2. **Neovim** (MODE_VIM - `init-learning.lua`)
3. **VS Code** (MODE_VSCODE - `.vscode/settings.json`)

All three maintain consistent settings for a unified learning experience.

---

## Synchronized Settings

### Indentation & Spacing

| Language | Tab Size | Setting | Location |
|----------|----------|---------|----------|
| Default | 2 | `set shiftwidth=2` | .vimrc, init.lua |
| C/C++ | 4 | `autocmd FileType c,cpp` | .vimrc |
| | 4 | `[cpp]` block | .vscode/settings.json |
| Rust | 4 | `autocmd FileType rust` | .vimrc |
| | 4 | `[rust]` block | .vscode/settings.json |
| Python | 4 | `autocmd FileType python` | .vimrc |
| | 4 | `[python]` block | .vscode/settings.json |
| Go | Tab | `set noexpandtab` | .vimrc |
| | Tab | `expandSpaces: false` | .vscode/settings.json |
| Dart | 2 | `autocmd FileType dart` | .vimrc |
| | 2 | `[dart]` block | .vscode/settings.json |
| Swift | 2 | `autocmd FileType swift` | .vimrc |
| | 2 | `[swift]` block | .vscode/settings.json |
| TypeScript | 2 | `autocmd FileType typescript` | .vimrc |
| | 2 | `[typescript]` block | .vscode/settings.json |

### Leader Key

| Editor | Leader | Key | Configuration |
|--------|--------|-----|---------------|
| Vim | `<Space>` | `let mapleader = " "` | `.vimrc` |
| Neovim | `<Space>` | `vim.g.mapleader = " "` | `init-learning.lua` |
| VS Code | `<Space>` | `"vim.leader": "<space>"` | `.vscode/settings.json` |

### Core Display Settings

| Setting | Value | Location |
|---------|-------|----------|
| Line numbers | Relative | `.vimrc`: `set relativenumber` |
| | | `init-learning.lua`: `vim.opt.relativenumber = true` |
| | | `.vscode/settings.json`: `"editor.lineNumbers": "relative"` |
| Cursor line | On | `.vimrc`: `set cursorline` |
| | | `init-learning.lua`: `vim.opt.cursorline = true` |
| Cursor style | Block | `.vimrc`: not set (Vim default) |
| | | `init-learning.lua`: not set (default) |
| | | `.vscode/settings.json`: `"editor.cursorStyle": "block"` |
| Font | JetBrains Mono | All three editors |
| Font size | 14 | `.vimrc`: N/A (terminal size) |
| | | `init-learning.lua`: N/A (terminal size) |
| | | `.vscode/settings.json`: `"editor.fontSize": 14` |

### Search & Navigation

| Setting | Vim | Neovim | VS Code |
|---------|-----|--------|---------|
| Highlight search | `hlsearch` | `hlsearch = true` | Auto via Vim extension |
| Incremental search | `incsearch` | `incsearch = true` | Auto via Vim extension |
| Ignore case | `ignorecase` | `ignorecase = true` | Auto via Vim extension |
| Smart case | `smartcase` | `smartcase = true` | Auto via Vim extension |

### Keybindings for Commands

#### Save
- **Vim/Neovim**: `:w` or `<Space>w`
- **VS Code**: `<Space>w` via leader mapping

#### Toggle Terminal
- **Vim/Neovim**: `:terminal` or `<Space>t`
- **VS Code**: `Ctrl+Shift+T` or `<Space>t` via leader

#### Next/Previous Lesson
- **Vim/Neovim**: `<Space>n` / `<Space>p`
- **VS Code**: Manual navigation (use Ctrl+P for quick open)

#### Run Program
- **Vim/Neovim**: `<Space>r` (calls `GetRunCommand()`)
- **VS Code**: `Ctrl+Shift+R` (runs VS Code task)

---

## Language-Specific Run Commands

All three editors support running code for these languages:

```
C++       → make run
Rust      → cargo run --release
Python    → python3 main.py
Go        → go run main.go
Dart      → dart main.dart
JavaScript→ node main.js
TypeScript→ ts-node main.ts
Java      → javac Main.java && java Main
```

**Location:**
- Vim: `.vimrc` - `GetRunCommand()` function (line 172-196)
- Neovim: `init-learning.lua` - Handled by tasks
- VS Code: `.vscode/tasks.json` - Predefined tasks

---

## Consistency Checks

### ✅ All Three Match

- **Default tab size**: 2 spaces
- **Leader key**: `<Space>`
- **Line numbers**: Relative
- **Language-specific overrides**: C++/Python/Rust/Go custom sizes
- **Font**: JetBrains Mono Nerd Font (when available)
- **Search behavior**: Incremental, case-smart
- **Read-only lessons**: `lesson.md` protected

### ⚠️ Platform-Specific Differences

| Feature | Vim | Neovim | VS Code |
|---------|-----|--------|---------|
| Plugin system | Vim built-in | Lazy.nvim | Extensions |
| Visual theme | Terminal | Nightfox | VS Code theme |
| Markdown rendering | Built-in | render-markdown.nvim | Built-in |
| LSP | Via coc/vim-lsp | Mason + LSP | Built-in |
| Statusline | Lightline/airline | Lualine | Built-in |

---

## Adding New Settings

When adding a new setting, update all three:

### Template

**For .vimrc:**
```vim
" Setting name
autocmd FileType newlang set tabstop=X shiftwidth=X softtabstop=X
```

**For init-learning.lua:**
```lua
-- Language-specific indentation
vim.api.nvim_create_autocmd("FileType", {
  pattern = "newlang",
  callback = function()
    vim.opt.tabstop = X
    vim.opt.shiftwidth = X
    vim.opt.softtabstop = X
  end,
})
```

**For .vscode/settings.json:**
```json
"[newlang]": {
  "editor.tabSize": X,
  "editor.insertSpaces": true
}
```

---

## Verification

To verify alignment:

1. **Check tab sizes**:
   - Vim: `:set tabstop?`
   - Neovim: `:lua print(vim.opt.tabstop:get())`
   - VS Code: Go to Settings, search "Tab Size"

2. **Check leader key**:
   - Vim: `:let mapleader`
   - Neovim: `:lua print(vim.g.mapleader)`
   - VS Code: Check `.vscode/settings.json` → `vim.leader`

3. **Check line numbers**:
   - Vim: `:set number?` and `:set relativenumber?`
   - Neovim: `:lua print(vim.opt.relativenumber:get())`
   - VS Code: Check `.vscode/settings.json` → `editor.lineNumbers`

---

## Update History

- **2025-01-04**: Initial alignment guide created
- **All settings**: Verified and synchronized across platforms
- **Language support**: All 20+ supported languages configured

---

## Related Files

- **Vim config**: `.vimrc`
- **Neovim config**: `MODE_VIM/CONFIG/init-learning.lua`
- **VS Code config**: `.vscode/settings.json`
- **VS Code keybindings**: `.vscode/keybindings.json`
- **Vim documentation**: `MODE_VIM/README.md`
- **VS Code documentation**: `MODE_VSCODE/README.md`

---

**Keep these three files in sync for the best learning experience across all editors!**
