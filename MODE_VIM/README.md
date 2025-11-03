# VIM MODE: Professional Learning IDE

**Learn programming in a beautiful, professional Neovim environment.**

---

## ✨ What You Get

When you run \`learn c++ 1\`, you get a full IDE experience:

- 🎨 **Nightfox Theme** - Beautiful dark theme
- 📖 **Smart Markdown** - Lessons render with icons and formatting  
- 🔒 **Protected Lessons** - Can't accidentally edit lesson files
- ⚡ **19 Plugins** - LSP, completion, fuzzy find, and more
- 🪟 **Split Screen** - Lesson on left, code on right
- 💬 **Help System** - Press \`<Space>h\` for instant help
- 📍 **Auto-Positioning** - Cursor starts ready to code

---

## 🚀 Quick Start

```bash
# Open any lesson
learn c++ 1
learn python 1
learn rust 1
```

**You'll see:**

```
╔═══════════════════╦═══════════════════╗
║   lesson.md       ║   main.cpp        ║
║   (left)          ║   (right)         ║
║                   ║                   ║
║  📌 Heading       ║  // Press <Esc>   ║
║                   ║  // <Space> h     ║
║  🔸 Bullet        ║  // for help.     ║
║                   ║                   ║
║  ⬜ Unchecked     ║  ▊               ║
║  ✅ Checked       ║                   ║
║                   ║                   ║
║  (read-only)      ║  (editable)       ║
╚═══════════════════╩═══════════════════╝
```

---

## ⚡ Essential Keybindings

**Press \`<Space>\` and wait** - see ALL commands instantly!

### Getting Help
| Key | Action |
|-----|--------|
| \`<Space>h\` | Essential Shortcuts popup |
| \`<Space>g\` | Quick Guide popup |
| \`<Space>\` | See all commands (which-key) |

### Window Navigation
| Key | Action |
|-----|--------|
| \`Ctrl+h\` | Move to left window (lesson) |
| \`Ctrl+l\` | Move to right window (code) |
| \`<Space>←\` | Alternative: move left |
| \`<Space>→\` | Alternative: move right |

### File Operations
| Key | Action |
|-----|--------|
| \`<Space>w\` | Save file |
| \`<Space>ff\` | Find files (Telescope) |
| \`<Space>fg\` | Live grep search |
| \`<Space>fb\` | Browse buffers |

### Terminal
| Key | Action |
|-----|--------|
| \`<Space>t\` | Toggle terminal |
| \`Esc\` (in terminal) | Exit terminal mode |

### Lesson Navigation
| Key | Action |
|-----|--------|
| \`<Space>n\` | Next lesson |
| \`<Space>p\` | Previous lesson |
| \`<Space>i\` | Show lesson info |

### Navigation
| Key | Action |
|-----|--------|
| \`s\` | Flash jump anywhere |
| \`Ctrl+d\` | Page down |
| \`Ctrl+u\` | Page up |
| \`gg\` | Go to top |
| \`G\` | Go to bottom |

### Editing Basics
| Key | Action |
|-----|--------|
| \`i\` | Enter insert mode |
| \`Esc\` | Return to normal mode |
| \`o\` | New line below |
| \`gcc\` | Toggle line comment |
| \`:w\` | Save |
| \`:q\` | Quit |

---

## 🎨 Features Explained

### Nightfox Theme
Professional dark theme with excellent syntax highlighting. Easy on the eyes for long coding sessions.

### Smart Markdown Rendering
Lessons display beautifully:
- **Headings**: 📌 📍 🔸 🔹
- **Checkboxes**: ⬜ ✅
- **Links**: 🔗 Images: 🖼️
- **Code blocks** with borders
- **Anti-conceal**: See raw markdown when cursor is on line

### Protected Lessons
- Lesson files are read-only
- Can't accidentally enter insert mode
- Try pressing \`i\` in a lesson - you'll get a helpful message!
- Flash navigation (\`s\`) still works for jumping around

### Help Comments
Every new code file starts with:
```cpp
// Press <Esc> <Space> h for help.


▊  // Your cursor starts here (line 4)
```

### Auto-Positioning
When you open a code file with a help comment, your cursor automatically starts on line 4, ready to code.

### Which-Key Menu
Press \`<Space>\` and wait - you'll see ALL available commands organized by category:
- **Window Navigation**: \`←\` \`→\`
- **Help & Guide**: \`g\` \`h\` \`t\` \`w\`
- **Find**: \`ff\` \`fg\` \`fb\` \`fh\`
- **Refactor**: \`rn\` \`ro\`
- **Code**: \`ca\`
- **View**: \`xx\` \`xz\` \`xt\`

No more memorizing keybindings!

### LSP Support
7 language servers auto-install on first use:
- **C/C++**: clangd
- **Rust**: rust-analyzer
- **Python**: pyright
- **JavaScript/TypeScript**: ts_ls
- **Go**: gopls
- **Lua**: lua_ls
- **Dart**: dartls

You get:
- Auto-completion
- Go to definition (\`gd\`)
- Find references (\`gr\`)
- Hover docs (\`K\`)
- Rename (\`<Space>rn\`)
- Code actions (\`<Space>ca\`)

### Telescope Fuzzy Finder
- \`<Space>ff\` - Find files by name
- \`<Space>fg\` - Search all file contents
- \`<Space>fb\` - Browse open buffers
- \`<Space>fh\` - Search Vim help

### Flash Navigation
Press \`s\` and type 2 characters - jump instantly to any visible location. Works even in read-only lesson files!

### Terminal Integration
Press \`<Space>t\` to toggle a horizontal terminal. Perfect for compiling and running code.

### Zen Mode
Press \`<Space>xz\` for distraction-free writing/reading. Perfect for focusing on complex lessons.

---

## 🎓 Learning Workflow

### Your First Lesson

1. **Open a lesson**:
   ```bash
   learn c++ 1
   ```

2. **Read the lesson** (left pane):
   - Use \`j/k\` to scroll
   - Press \`s\` to flash jump
   - \`Ctrl+d/u\` for page down/up

3. **Write code** (right pane):
   - Press \`Ctrl+l\` to switch
   - You'll see the help comment
   - Cursor starts on line 4
   - Type normally!

4. **Get help anytime**:
   - Press \`<Space>h\` - Essential shortcuts
   - Press \`<Space>g\` - Quick guide
   - Press \`<Space>\` - See all commands

5. **Compile and run**:
   - Press \`<Space>t\` for terminal
   - Run \`:!make run\` (C++)
   - Or \`:!cargo run\` (Rust)
   - Or \`:!python3 %\` (Python)

6. **Save and continue**:
   - \`<Space>w\` to save
   - \`<Space>n\` for next lesson
   - \`:q\` to quit

### Pro Tips

- **Don't memorize everything** - Press \`<Space>\` to see commands
- **Use Flash (\`s\`)** - Fastest way to move around
- **Telescope is your friend** - \`<Space>ff\` to find anything
- **Terminal stays open** - Keep compilation output visible
- **Zen mode for focus** - \`<Space>xz\` when you need to concentrate
- **LSP makes you faster** - \`gd\` to jump to definitions

---

## 🛠️ Configuration

Your Neovim config is at: \`~/.config/nvim/init.lua\`

It includes:
- Nightfox theme
- 19 plugins
- Custom keybindings
- LSP configuration
- Markdown rendering
- Lesson protection
- Help system

**Want to customize?** Edit \`init.lua\` directly. It's well-commented!

---

## 🔧 Plugins Used

| Plugin | Purpose |
|--------|---------|
| nightfox.nvim | Theme |
| lualine.nvim | Statusline |
| render-markdown.nvim | Beautiful lessons |
| nvim-treesitter | Syntax highlighting |
| mason.nvim | LSP installer |
| nvim-lspconfig | LSP setup |
| nvim-cmp | Autocompletion |
| telescope.nvim | Fuzzy finder |
| flash.nvim | Jump navigation |
| which-key.nvim | Command discovery |
| toggleterm.nvim | Terminal |
| zen-mode.nvim | Distraction-free |
| trouble.nvim | Diagnostics |
| nvim-colorizer.lua | Color preview |
| neoscroll.nvim | Smooth scrolling |
| Comment.nvim | Smart comments |
| nvim-autopairs | Auto-close brackets |
| gitsigns.nvim | Git integration |
| nvim-web-devicons | File icons |

---

## 🆘 Troubleshooting

**Q: Which-key shows too many commands**
- Fixed! Only essential commands show now.

**Q: Lesson formatting disappears on cursor line**
- Fixed! Anti-conceal keeps it visible.

**Q: Help comment missing in code files**
- Fixed! All files get help comments automatically.

**Q: Can't remember keybindings**
- Press \`<Space>\` and wait!
- Or press \`<Space>h\` for shortcuts popup
- Or press \`<Space>g\` for navigation guide

**Q: LSP not working**
- It auto-installs on first use
- Wait a few seconds for Mason to finish
- Check \`:Mason\` to see status

**Q: Terminal won't close**
- Press \`Esc\` first to exit terminal mode
- Then use \`<Space>t\` to toggle

**Q: Want to customize?**
- Edit \`~/.config/nvim/init.lua\`
- All settings are documented

---

## 📖 More Resources

- [Main README](../README.md) - Platform overview
- [FEATURES.md](../FEATURES.md) - Complete feature list
- [VIM_CHEATSHEET.md](../VIM_CHEATSHEET.md) - Quick Vim reference
- [CLI Documentation](../CLI/README.md) - CLI commands

---

## 💡 Remember

- **\`<Space>h\`** - Essential shortcuts (your best friend!)
- **\`<Space>g\`** - Quick guide
- **\`<Space>\`** - See all commands
- **\`s\`** - Flash jump anywhere
- **\`Ctrl+h/l\`** - Switch windows

**Happy Learning! 🎓**
