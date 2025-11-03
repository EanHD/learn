# LEARN Platform - Complete Feature List

Last updated: November 2025

---

## 📚 Core Platform

### Content
- **490 Total Lessons** across 14 programming languages
- **5 Progressive Stages** from copying code to building projects
- **35 Lessons per Language** (7 levels × 5 stages)
- **14 Languages**: C++, Rust, Python, JavaScript, TypeScript, Go, Lua, Dart, Swift, Kotlin, SQL, C#, Shell, PowerShell

### Learning Methodology
- **Stage 1**: Copy working code, learn syntax
- **Stage 2**: Convert pseudocode to real code
- **Stage 3**: Design solutions to problems
- **Stage 4**: Build complete projects
- **Stage 5**: Create capstone projects

---

## 🖥️ CLI Features

### Core Commands
- `learn` - Interactive menu system
- `learn <language> <level>` - Direct lesson access
- `learn --list` - Browse all 490 lessons
- `learn --progress` - View learning statistics
- `learn --next` - Smart lesson suggestions
- `learn --complete <lang> <stage> <level>` - Mark lessons complete

### Editor Integration
- **Neovim Mode** (default) - Enhanced IDE experience
- **VS Code Mode** - Full editor integration
- **Terminal Mode** - Read-only quick view

### Progress Tracking
- Automatic session recording
- Completion tracking per language
- Total time spent learning
- Last lesson accessed
- Smart "continue learning" suggestions

### Interactive Menu
- Color-coded language selection
- Visual progress indicators
- Keyboard navigation
- Stage/level browser
- Quick mode switching

---

## 🎨 Neovim IDE Features

### Theme & Appearance
- **Nightfox Theme** - Professional dark theme with excellent contrast
- **Lualine Statusbar** - Shows file, mode, git status, diagnostics
- **Render-Markdown** - Beautiful lesson rendering with:
  - Icon headings (📌 📍 🔸 🔹)
  - Styled checkboxes (⬜ ✅)
  - Pretty links (🔗 🖼️)
  - Code blocks with borders
  - Quote styling
- **Anti-Conceal** - See raw markdown when cursor is on line

### Plugin Ecosystem (19 Plugins)
1. **nightfox.nvim** - Theme
2. **lualine.nvim** - Statusline
3. **render-markdown.nvim** - Markdown rendering
4. **nvim-treesitter** - Syntax highlighting
5. **mason.nvim** - LSP installer
6. **nvim-lspconfig** - LSP configuration
7. **nvim-cmp** - Autocompletion
8. **telescope.nvim** - Fuzzy finder
9. **flash.nvim** - Motion navigation
10. **which-key.nvim** - Command discovery
11. **toggleterm.nvim** - Terminal management
12. **zen-mode.nvim** - Distraction-free mode
13. **trouble.nvim** - Diagnostics panel
14. **nvim-colorizer.lua** - Color preview
15. **neoscroll.nvim** - Smooth scrolling
16. **Comment.nvim** - Smart commenting
17. **nvim-autopairs** - Auto close brackets
18. **gitsigns.nvim** - Git integration
19. **nvim-web-devicons** - File icons

### Language Support (Auto-Installed LSPs)
- **clangd** - C/C++
- **rust-analyzer** - Rust
- **pyright** - Python
- **ts_ls** - JavaScript/TypeScript
- **gopls** - Go
- **lua_ls** - Lua
- **dartls** - Dart

### Code Intelligence
- Auto-completion as you type
- Inline diagnostics and errors
- Go to definition (gd)
- Find references (gr)
- Rename refactoring (<Space>rn)
- Code actions (<Space>ca)
- Hover documentation (K)

### Navigation Features
- **Flash Jump** - Press `s` to jump anywhere instantly
- **Telescope Fuzzy Find** - `<Space>ff` for files, `<Space>fg` for grep
- **Buffer Switching** - `<Space>fb` to browse open files
- **Help Tags** - `<Space>fh` for Vim help search

### Window Management
- **Split Screen** - Lesson on left, code on right
- **Auto Window Balance** - Optimal sizing on startup
- **Smart Navigation**:
  - `Ctrl+h` / `Ctrl+l` - Switch windows
  - `<Space>←` / `<Space>→` - Alternative window switching
  - `Ctrl+j` / `Ctrl+k` - Vertical navigation
- **Terminal Toggle** - `<Space>t` for horizontal terminal

### Lesson Protection System
- **Read-Only Lessons** - Prevent accidental edits to lesson files
- **Insert Mode Blocking** - 10 insert keys disabled in lessons
- **Helpful Messages** - "📖 Lesson file is read-only. Use Ctrl+l to switch to code window."
- **Flash Navigation Preserved** - `s` key still works for jumping in lessons
- **Smart Detection** - Only applies to `lesson.md` files

### Code File Features
- **Auto Help Comments** - Every new file starts with:
  ```
  // Press <Esc> <Space> h for help.


  ```
- **Auto-Positioning** - Cursor starts on line 4, ready to code
- **Language-Specific** - Correct comment syntax for each language
- **Empty File Detection** - Automatically adds help to existing empty files

### Custom Popups
#### Quick Guide (`<Space>g`)
- Beautiful formatted popup
- Window navigation commands
- Lesson navigation shortcuts
- Editing basics
- Compile/run commands
- Language-specific instructions

#### Essential Shortcuts (`<Space>h`)
- Context-aware commands
- Window management
- Lesson navigation
- Editing commands
- Compile/run for current language
- Tips and tricks

### Which-Key Integration
Clean, organized command menu showing:
- **Window Navigation** - `<Space>←→` for window switching
- **Help & Guide** - `<Space>g/h` for popups
- **Find Group** - `<Space>f` prefix for search
- **Refactor Group** - `<Space>r` prefix for LSP actions
- **Code Group** - `<Space>c` prefix for code actions
- **View Group** - `<Space>x` prefix for UI toggles

All presets disabled for clean interface.

### Additional Features
- **Smooth Scrolling** - Eased cursor movement
- **Auto-Save** - Code saves when switching windows
- **Git Integration** - Show changes in sidebar
- **Color Highlighting** - See colors in CSS/HTML
- **Auto-Pairs** - Auto-close brackets and quotes
- **Smart Commenting** - `gcc` to toggle comments
- **Zen Mode** - `<Space>xz` for distraction-free writing

---

## ⚡ Key Bindings Reference

### Leader Key Commands (`<Space>`)

| Key | Action |
|-----|--------|
| `<Space>` | Open which-key menu |
| `<Space>g` | Quick Guide popup |
| `<Space>h` | Essential Shortcuts popup |
| `<Space>t` | Toggle terminal |
| `<Space>w` | Save file |
| `<Space>n` | Next lesson |
| `<Space>p` | Previous lesson |
| `<Space>i` | Show lesson info |
| `<Space>←` | Move to left window |
| `<Space>→` | Move to right window |

### Find Commands (`<Space>f`)

| Key | Action |
|-----|--------|
| `<Space>ff` | Find files |
| `<Space>fg` | Live grep search |
| `<Space>fb` | Browse buffers |
| `<Space>fh` | Help tags |

### Refactor Commands (`<Space>r`)

| Key | Action |
|-----|--------|
| `<Space>rn` | Rename symbol |
| `<Space>ro` | Toggle read-only |

### Code Commands (`<Space>c`)

| Key | Action |
|-----|--------|
| `<Space>ca` | Code action |

### View Commands (`<Space>x`)

| Key | Action |
|-----|--------|
| `<Space>xx` | Show diagnostics |
| `<Space>xz` | Toggle Zen mode |
| `<Space>xt` | Toggle terminal |

### Window Navigation

| Key | Action |
|-----|--------|
| `Ctrl+h` | Move to left window |
| `Ctrl+l` | Move to right window |
| `Ctrl+j` | Move to bottom window |
| `Ctrl+k` | Move to top window |
| `<Space>=` | Equalize windows |

### LSP Commands

| Key | Action |
|-----|--------|
| `gd` | Go to definition |
| `gr` | Find references |
| `K` | Hover documentation |
| `<Space>ca` | Code actions |
| `<Space>rn` | Rename symbol |

### Navigation

| Key | Action |
|-----|--------|
| `s` | Flash jump (leap to any location) |
| `S` | Flash treesitter jump |
| `Ctrl+d` | Page down (centered) |
| `Ctrl+u` | Page up (centered) |
| `gg` | Go to top |
| `G` | Go to bottom |
| `/` | Search |
| `n` | Next search result |
| `N` | Previous search result |

### Editing

| Key | Action |
|-----|--------|
| `i` | Insert mode |
| `a` | Append mode |
| `o` | New line below |
| `O` | New line above |
| `Esc` | Return to normal mode |
| `gcc` | Toggle line comment |
| `gc` (visual) | Toggle block comment |
| `:w` | Save file |
| `:q` | Quit |
| `:wq` | Save and quit |

### Terminal Mode

| Key | Action |
|-----|--------|
| `<Space>t` | Toggle terminal |
| `Ctrl+\` `Ctrl+n` | Exit terminal mode |
| `Esc` (terminal) | Exit terminal mode |

---

## 🔧 Technical Features

### Workspace Management
- **Automatic Directory Creation** - `~/.local/share/learn/workspaces/`
- **Language-Specific Workspaces** - Organized by language/stage/level
- **Starter Files** - Pre-configured with build systems:
  - C++: Makefile, .clang-format
  - Rust: Cargo.toml
  - JavaScript: package.json
  - Python: requirements.txt (where needed)

### File Management
- **Smart File Detection** - Automatically finds lesson and code files
- **Extension Mapping** - Correct file extensions for all 14 languages
- **Template System** - Language-specific code templates
- **Help Comment Injection** - Automatic help text in all new files

### Progress System
- **JSON Storage** - `.learn-progress.json` in home directory
- **Session Tracking** - Timestamp, language, stage, level, mode
- **Statistics** - Total sessions, time estimates, completion rates
- **Smart Suggestions** - Next lesson recommendations based on history

### Configuration
- **Lua-Based** - Modern Neovim configuration
- **Lazy.nvim** - Fast plugin manager with lazy loading
- **Modular Design** - Easy to customize and extend
- **Auto-Bootstrap** - Plugins install automatically on first run

---

## 🎯 Unique Features

### What Makes LEARN Different

1. **Integrated Learning Environment** - Everything in one place
2. **490 Lessons** - Most comprehensive multi-language curriculum
3. **Progressive Difficulty** - Carefully designed learning path
4. **Smart Protection** - Can't accidentally break lessons
5. **Context-Aware Help** - Help system knows your language and stage
6. **Beautiful UI** - Professional IDE feel, not just a text editor
7. **Zero Configuration** - Works out of the box
8. **Offline-First** - All lessons locally available
9. **Progress Tracking** - Know where you are and where you've been
10. **Multi-Language** - Learn patterns across 14 languages

---

## 📊 Statistics

- **490 Total Lessons**
- **14 Languages**
- **19 Neovim Plugins**
- **7 LSP Servers**
- **~1100 Lines** of Neovim configuration
- **~1500 Lines** of Python CLI code
- **Zero Cost** - Completely free and open source

---

## 🚀 Performance

- **Fast Startup** - Lazy loading keeps Neovim snappy
- **LSP Auto-Install** - Language servers install on demand
- **Smart Caching** - Compiled plugins for speed
- **Minimal Resource Usage** - Efficient even on older hardware
- **Instant Switching** - Jump between lessons in milliseconds

---

## 🔒 Safety & Protection

- **Lesson Protection** - Read-only to prevent accidents
- **Git-Friendly** - User data in `.gitignore`
- **Backup-Safe** - Old configs backed up automatically
- **Non-Destructive** - Installer preserves existing setups
- **Recoverable** - Progress tracking prevents lost work

---

## 🆘 Help System

- **Built-In Popups** - Context-aware help (`<Space>h`)
- **Which-Key Integration** - Discover commands as you type
- **Quick Guide** - Navigation reference (`<Space>g`)
- **Help Comments** - Reminder in every code file
- **Comprehensive Docs** - README, guides, cheatsheets
- **Clear Error Messages** - Helpful feedback throughout

---

## 🌟 Coming Soon

(Features planned or in development)

- Web-based progress dashboard
- Lesson completion badges
- Community solutions sharing
- Additional languages (Java, PHP, etc.)
- Video lesson integration
- Interactive exercises
- Unit test integration
- AI-powered hints

---

## 📝 Notes

This feature list is current as of November 2025. For the latest updates, check the GitHub repository at https://github.com/EanHD/learn

---

**Feature requests?** Open an issue on GitHub!
