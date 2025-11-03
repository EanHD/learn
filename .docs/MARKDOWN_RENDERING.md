# Beautiful Markdown Rendering in LEARN Platform

## Quick Reference Card

**Essential Shortcuts:**
- `<Space>` then wait → See all keybindings
- `<Space>z` → Zen Mode (focus reading)
- `<Space>t` → Floating terminal
- `<Space>n/p` → Next/Previous lesson
- `s` + chars → Flash jump anywhere
- `gcc` → Comment line

**On First Launch:** Plugins auto-install (30-60 seconds), then instant forever!

---

## Overview

The LEARN platform now uses a modern Neovim configuration with beautiful markdown rendering and 14 powerful plugins. Lessons display with clean formatting, hiding raw markdown syntax like `**`, `###`, and `[]()`.

### What You Get

✨ **Visual Beauty**: OneDark theme with powerline statusbar
🎯 **Focus Mode**: Zen Mode for distraction-free reading
💻 **Integrated Terminal**: Test code without leaving Neovim
⚡ **Fast Navigation**: Flash jump + smooth scrolling
🤖 **Smart Typing**: Auto-pairs, easy commenting, color preview
📚 **Learning Aids**: Which-Key help system, indentation guides

## What Changed

### Visual Improvements

**Before:**
```
# Level 1: Hello World
## Stage 1: Copying Code
**Learning Goals**
- Understand the basic structure
```

**After:**
- Headings display with colors and icons (no ###)
- Bold text shows in color (no **)
- Bullets use pretty symbols (●, ○, ◆)
- Code blocks have borders
- Checkboxes show as ☑ and ☐

### Configuration Files

1. **`MODE_VIM/CONFIG/init-learning.lua`** (NEW)
   - Modern Lua-based Neovim config
   - OneDark theme
   - Lualine statusline
   - Markdown rendering with concealment
   - All 14 language indentation rules

2. **`CLI/learn_cli.py`** (UPDATED)
   - Now loads `init-learning.lua` instead of `.vimrc`
   - Uses `-u` flag to specify custom config

## Features & Plugins

### 🎨 Theme: OneDark
- Beautiful dark color scheme with powerline separators
- Optimized for reading code and markdown
- Better contrast and readability
- Custom markdown syntax highlighting

### 📊 Statusline: Lualine
- Clean, informative status bar with powerline arrows ( )
- Shows current mode, file, location
- Git branch and changes
- File encoding and type

### 📝 Markdown Rendering
- **Concealment Level 2**: Hides markdown syntax (**, ###, etc.)
- **Heading Icons**: Different icons for each level (󰲡, 󰲣, 󰲥)
- **Code Blocks**: Bordered, syntax-highlighted with language labels
- **Checkboxes**: Visual ☑ and ☐ instead of `[x]` and `[ ]`
- **Bullets**: Pretty symbols (●, ○, ◆, ◇) instead of `-` or `*`
- **Links**: Underlined with icons (󰌹, 󰥶)

### 🌲 Treesitter: Syntax Highlighting
- Advanced syntax highlighting for all 14 languages
- Better code structure understanding
- Enables semantic-aware plugins
- Markdown and markdown_inline support for beautiful lesson rendering

### 🧘 Zen Mode
**Keybinding:** `<Space>z`
- Distraction-free reading/writing mode
- Hides line numbers, status bars, and UI elements
- Centers content with comfortable width (90 columns)
- Perfect for focusing on lessons without distractions

### 📏 Indent Blankline
- Visual indentation guides (vertical lines)
- Helps track code structure and nesting
- Automatically disabled for markdown (keeps lessons clean)
- Shows hierarchy in nested code

### 💻 ToggleTerm: Better Terminal
**Keybindings:** `<Space>t`, `<Space>th`, `Ctrl+\`
- Floating terminal window (beautiful curved borders)
- Horizontal split option
- Quick toggle without leaving Neovim
- Test your code instantly without switching applications

### ⌨️ Which-Key: Keybinding Helper
**Usage:** Press `<Space>` and wait ~500ms
- Shows all available keybindings in a popup
- Great for discovering features
- Organized by category (Navigation, Terminal, etc.)
- Never forget shortcuts again!

### 🌊 Neoscroll: Smooth Scrolling
- Smooth animated scrolling with Ctrl+d/u/f/b
- Better visual feedback when navigating
- Makes reading long lessons more pleasant
- Configurable easing (quadratic animation)

### 🔍 Trouble: Better Diagnostics
**Keybinding:** `<Space>xx`
- Beautiful error/warning viewer
- Shows all diagnostics in one place
- Better than default quickfix window
- Jump to errors quickly

### 🎨 Colorizer: See Colors
- Shows actual colors for hex codes (#61afef, #e06c75)
- Works in CSS, HTML, JavaScript, TypeScript
- Instant visual feedback for color values
- No more guessing what colors look like

### 🔗 Auto-pairs: Smart Brackets
- Automatically closes brackets: `(`, `{`, `[`
- Closes quotes: `"`, `'`, `` ` ``
- Works with treesitter for context-aware pairing
- Speeds up coding significantly

### 💬 Comment.nvim: Easy Commenting
**Keybindings:** `gcc`, `gc` (visual mode), `gbc`
- Toggle comments on current line (gcc)
- Comment visual selections (select + gc)
- Language-aware (C++: //, Python: #, etc.)
- Block comments support (gbc)

### ⚡ Flash: Lightning Navigation
**Keybindings:** `s`, `S`
- Jump to any visible word with `s` + character(s)
- Jump using syntax tree with `S`
- Type more chars to narrow down matches
- Much faster than manual cursor movement

### Language Support
All 14 languages configured with proper indentation:
- C++, Rust, Python, Kotlin, C#, PowerShell: 4 spaces
- JavaScript, TypeScript, Dart, Swift, Lua, Shell, SQL: 2 spaces
- Go: Tab characters (Go convention)

## Complete Keybindings Reference

### 📚 Lesson Navigation
- `<Space>i` - Show current lesson info (Stage X, Level Y)
- `<Space>n` - Jump to next lesson
- `<Space>p` - Jump to previous lesson

### 🪟 Window Management
- `<Ctrl>h` - Move to left window
- `<Ctrl>j` - Move to bottom window
- `<Ctrl>k` - Move to top window
- `<Ctrl>l` - Move to right window
- `<Ctrl>=` - Equal window sizes
- `<Ctrl>+` - Increase width
- `<Ctrl>_` - Decrease width

### 💾 File Operations
- `<Space>w` - Save file
- `<Space>ro` - Toggle readonly mode
- `<Esc>` - Clear search highlighting

### 🧘 Focus & Display
- `<Space>z` - Toggle Zen Mode (distraction-free)
- Press `<Space>` and wait - Show all keybindings (Which-Key)

### 💻 Terminal
- `<Space>t` - Open floating terminal
- `<Space>th` - Open horizontal terminal
- `<Ctrl>\` - Quick terminal toggle
- `<Esc>` (in terminal) - Exit terminal mode to normal mode

### 💬 Commenting
- `gcc` - Toggle comment on current line
- `gc` (visual mode) - Comment/uncomment selection
- `gbc` - Toggle block comment

### ⚡ Quick Navigation (Flash)
- `s` + char(s) - Jump to any word (type chars to narrow)
- `S` - Jump using syntax tree (smart navigation)

### 🌊 Scrolling
- `<Ctrl>d` - Scroll down half page (smooth)
- `<Ctrl>u` - Scroll up half page (smooth)
- `<Ctrl>f` - Scroll forward full page
- `<Ctrl>b` - Scroll backward full page
- `zt` - Put cursor line at top
- `zz` - Put cursor line at center
- `zb` - Put cursor line at bottom

### 🔍 Diagnostics & Errors
- `<Space>xx` - Toggle Trouble (show all errors/warnings)

### 💡 Pro Tips
- Press `<Space>` and wait ~500ms to see Which-Key menu with all shortcuts
- Use `s` + 2-3 characters for precise Flash jumps
- Zen Mode (`<Space>z`) is perfect for reading lessons
- Terminal toggle (`Ctrl+\`) works from any mode

## First Run Setup

When you first run `learn` with Vim mode, Neovim will automatically:

1. Install lazy.nvim (plugin manager)
2. Download and install plugins:
   - onedark.nvim
   - lualine.nvim
   - render-markdown.nvim
   - nvim-treesitter
   - nvim-web-devicons

**This takes 30-60 seconds on first run only!**

You'll see installation progress in Neovim. Once complete, the plugins are cached and load instantly on subsequent runs.

## How It Works

### Markdown Concealment

Neovim's `conceallevel` is set to 2, which means:
- Markdown syntax is hidden by default
- Cursor line shows raw syntax (for editing)
- Moving away hides syntax again

Example:
```markdown
When you type:
**This is bold**

You see:
This is bold (in red/bold, no **)
```

### Render Markdown Plugin

The `render-markdown.nvim` plugin enhances concealment with:
- Custom heading backgrounds and icons
- Bordered code blocks with language tags
- Pretty bullets and checkboxes
- Link decorations

### Treesitter

Provides accurate syntax highlighting for all 14 languages, plus markdown and markdown_inline for beautiful lesson rendering.

## Troubleshooting

### Plugins Not Installing

If plugins don't auto-install on first run:

```bash
# Open Neovim manually
nvim -u /home/eanhd/LEARN/MODE_VIM/CONFIG/init-learning.lua

# Then inside Neovim, run:
:Lazy sync
```

### Markdown Not Rendering

Check concealment level:
```vim
:set conceallevel?
```

Should show `conceallevel=2`. If not:
```vim
:set conceallevel=2
```

### Theme Not Loading

Ensure OneDark is installed:
```vim
:Lazy
```

Look for `onedark.nvim` in the plugin list.

### Want to Use Old Config?

The old Vimscript config is still available at:
`MODE_VIM/CONFIG/init-learning.vim`

To use it, edit `CLI/learn_cli.py` and change:
```python
lua_init_path = Path(__file__).parent.parent / "MODE_VIM" / "CONFIG" / "init-learning.vim"
```

## Customization

### Change Theme Style

Edit `init-learning.lua`, find the OneDark setup, and change style:
```lua
style = "dark",  -- Options: 'dark', 'darker', 'cool', 'deep', 'warm', 'warmer'
```

### Adjust Concealment

To show more/less markdown syntax:
```lua
vim.opt.conceallevel = 2  -- Options: 0 (show all), 1 (some), 2 (most), 3 (all)
```

### Modify Keybindings

All keybindings are at the bottom of `init-learning.lua`. Example:
```lua
map("n", "<leader>w", ":w<CR>", { desc = "Save file" })
```

Change `<leader>w` to any key you prefer.

## Benefits

1. **Cleaner Reading Experience**: No visual noise from markdown syntax
2. **Professional Look**: Color-coded headings, pretty bullets, icons
3. **Better Focus**: Students focus on content, not formatting
4. **Modern Tools**: Latest Neovim plugins for best experience
5. **Fast Performance**: Lua-based config loads quickly
6. **Consistent Style**: OneDark theme across all lessons

## Technical Details

### Plugin Manager: Lazy.nvim
- Fast, modern plugin manager
- Lazy-loads plugins (fast startup)
- Auto-updates and manages dependencies

### Data Location
Plugins installed to: `~/.local/share/nvim/lazy/`

### Config Location
Custom config: `/home/eanhd/LEARN/MODE_VIM/CONFIG/init-learning.lua`

### CLI Integration
The CLI's `open_vim()` method loads the config with:
```bash
nvim -u /path/to/init-learning.lua -O lesson.md main.cpp
```

## Plugin Summary

| Plugin | Purpose | Key Feature |
|--------|---------|-------------|
| OneDark | Theme | Beautiful dark colors |
| Lualine | Statusline | Clean info bar with powerline |
| Render-markdown | Markdown display | Hides syntax, shows pretty formatting |
| Treesitter | Syntax highlighting | Smart code understanding |
| Zen Mode | Focus mode | Distraction-free reading |
| Indent Blankline | Visual guides | See code structure |
| ToggleTerm | Terminal | Float/split terminal in Neovim |
| Which-Key | Help system | Shows keybindings on demand |
| Neoscroll | Smooth scrolling | Animated page movement |
| Trouble | Diagnostics | Beautiful error viewer |
| Colorizer | Color preview | See hex colors visually |
| Auto-pairs | Smart typing | Auto-close brackets/quotes |
| Comment.nvim | Commenting | Easy code comments |
| Flash | Navigation | Lightning-fast jumps |

## Future Enhancements

Possible additions:
- Additional colorschemes (catppuccin, tokyonight, gruvbox)
- LSP code completion for all 14 languages
- Git integration (gitsigns.nvim)
- Markdown table formatting
- Inline LaTeX rendering for math equations
- File explorer (nvim-tree or oil.nvim)
- Fuzzy finder (telescope.nvim)

---

**Ready to learn with beautiful markdown and powerful tools!** 🎨✨
