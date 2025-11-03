# Neovim Setup Guide

Get Neovim configured for learning and writing code in minutes.

## Quick Start

### 1. Install Neovim (if not already installed)

**Ubuntu/Debian (WSL):**
```bash
sudo apt install neovim
```

Or get the latest from: https://github.com/neovim/neovim/releases

**macOS:**
```bash
brew install neovim
```

**Windows (Direct):**
Download from: https://github.com/neovim/neovim/releases (nvim.exe)

### 2. Install Kickstart.nvim

Kickstart is a starting point for Neovim that includes everything you need:

```bash
# Clone kickstart
git clone https://github.com/nvim-kickstart/kickstart.nvim ~/.config/nvim

# First launch (will auto-install plugins)
nvim

# Wait for Packer/Lazy to finish syncing (shows at bottom)
# Press 'q' to close messages once done
```

### 3. Run the Development Setup Script

This installs all tools (C++, Rust, Python, formatters, LSPs):

```bash
cd ~/LEARN
bash setup-dev.sh
```

The script will:
- Install system dependencies (build tools, clangd, Node.js, Rust)
- Configure Rust toolchain with rust-analyzer
- Use Mason to install LSPs and formatters via Neovim
- Set up optional CLI helpers (prettier, markdownlint)

### 4. Configure Neovim for Reading & Writing

Add this to the bottom of `~/.config/nvim/init.lua`:

```lua
-- === Soft wrap & nicer reading ===
vim.opt.wrap = true            -- wrap long lines
vim.opt.linebreak = true       -- wrap at nice word boundaries
vim.opt.breakindent = true     -- preserve indent on wrapped lines
vim.opt.showbreak = "↳ "       -- visually mark wrapped continuation
vim.opt.scrolloff = 2

-- Better wrapping for prose/Markdown/text
vim.api.nvim_create_autocmd("FileType", {
  pattern = { "markdown", "text", "gitcommit" },
  callback = function()
    vim.opt_local.wrap = true
    vim.opt_local.linebreak = true
    vim.opt_local.spell = true
    vim.opt_local.conceallevel = 2
  end,
})

-- OPTIONAL: autoformat on save when Conform.nvim is present
-- This will use prettierd for Markdown/JS/TS, black for Python, etc.
pcall(function()
  require("conform").setup({
    format_on_save = function(bufnr)
      local ft = vim.bo[bufnr].filetype
      -- keep it light: only autoformat code & markdown by default
      local ok_ft = { lua=true, python=true, sh=true, javascript=true, typescript=true, markdown=true }
      if ok_ft[ft] then
        return { timeout_ms = 1500, lsp_fallback = true }
      end
    end,
  })
end)
```

## Verify Installation

Open Neovim and check:

```bash
nvim

# Inside Neovim, run these commands:
:Mason              # See all installed tools
:LspInfo           # Check active LSPs
:ConformInfo       # Check formatters
```

You should see installed tools for C++, Rust, Python, etc.

## Now You're Ready to Learn

```bash
# Start your first lesson
learn c++ 1

# Or switch to Rust
learn rust 1
```

In Neovim:
- **Left pane**: Lesson (read-only)
- **Right pane**: Your editor (blank canvas)

**Navigation:**
- `Ctrl-h` → Go to lesson
- `Ctrl-l` → Go to your editor
- `i` → Start typing
- `Esc` → Exit insert mode

## Troubleshooting

### Mason command not found
If `:Mason` doesn't work in Neovim, make sure Kickstart.nvim is properly installed:
```bash
rm -rf ~/.config/nvim
git clone https://github.com/nvim-kickstart/kickstart.nvim ~/.config/nvim
nvim  # let plugins install
```

### Rust tools not available
Re-source your shell environment:
```bash
source ~/.cargo/env
rustup update
```

### LSP not working for a language
Inside Neovim, manually install via Mason:
```
:MasonInstall clangd rust-analyzer pyright
```

### Formatters not running
Check `:ConformInfo` to see available formatters. If needed, re-run:
```bash
bash ~/LEARN/setup-dev.sh
```

## Tips

- **F1 in Neovim** - Opens help documentation
- **:help** - Full Neovim documentation
- **:LspInfo** - Shows which LSP is active for current file
- **:Mason** - Install/manage tools graphically
- **<leader>** is mapped to `<Space>` in Kickstart by default

## Next Steps

1. Complete **Stage 1** lessons (copying code)
2. Progress to **Stage 2** (understanding pseudocode)
3. Continue through all 5 stages
4. Build your capstone project

Good luck, and happy learning!

