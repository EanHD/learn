# Complete Developer Setup

Get your full development environment configured in 10 minutes.

## What You'll Get

- **C++ Development** - clangd LSP, compiler, formatter
- **Rust Development** - rust-analyzer, cargo, formatter
- **Python Development** - pyright LSP, black formatter
- **Neovim** - Kickstart configuration with Mason tools management
- **Formatters & Tools** - prettier, shfmt, stylua, markdownlint

All ready to use with the `learn` command.

## Prerequisites

You need:
1. **Linux/WSL** (Ubuntu/Debian-based)
2. **Neovim** (0.9+) - [Install here](https://github.com/neovim/neovim/releases)
3. **Git**

## One-Command Setup

```bash
# 1. Install Neovim (if needed)
sudo apt install neovim

# 2. Setup Kickstart (one time)
git clone https://github.com/nvim-kickstart/kickstart.nvim ~/.config/nvim

# 3. Run the setup script
cd ~/LEARN
bash setup-dev.sh

# 4. Open Neovim to finalize
nvim
```

Then check inside Neovim:
```vim
:Mason           # See installed tools
:LspInfo        # Check active language servers
```

## What the Script Does

### Dependencies
- **build-essential** - C/C++ compiler and tools
- **clangd** - C/C++ language server
- **ripgrep, fd** - Fast file searching
- **python3, pip** - Python environment
- **Node.js LTS** - Formatter engines
- **Rust** - Full Rust toolchain with rust-analyzer

### Tools (via Mason)
- clangd - C/C++ LSP
- rust-analyzer - Rust LSP
- pyright - Python LSP
- tsserver - JavaScript/TypeScript LSP
- marksman - Markdown LSP
- prettierd - Fast formatter
- black - Python formatter
- shfmt - Shell formatter
- stylua - Lua formatter

## Verify It Worked

Inside Neovim:

```vim
# Check all tools
:Mason

# See which LSP is active
:LspInfo

# List available formatters
:ConformInfo

# Verify Kickstart loaded
:PlugStatus
```

All should show installed tools in green.

## Troubleshooting

### "command not found: nvim"
Install Neovim: `sudo apt install neovim`

### "Mason not available"
Make sure Kickstart is installed: 
```bash
git clone https://github.com/nvim-kickstart/kickstart.nvim ~/.config/nvim
```

### "Can't find rustup"
The script sets up Rust but needs a fresh shell:
```bash
source ~/.cargo/env
```

### Mason tools won't install
Try manually inside Neovim:
```vim
:MasonInstall clangd rust-analyzer pyright
```

## Now Start Learning

```bash
# First lesson
learn c++ 1

# Or Rust
learn rust 1
```

See `START_HERE.md` for learning paths.

## For More Details

- **Neovim Configuration** - See `SETUP_NVIM.md`
- **Learning Guide** - See `README.md`
- **CLI Tool Help** - Run `learn --help`
- **Vim Mode** - Check `MODE_VIM/` directory

## What's Different from Stock Neovim?

| Feature | Stock | Ours |
|---------|-------|------|
| LSP support | Manual | Auto (Mason) |
| Formatters | Manual | Auto (Conform) |
| Themes | Basic | Kickstart curated |
| Defaults | Minimal | Dev-friendly |
| C++ support | None | clangd + formatting |
| Rust support | None | rust-analyzer + formatting |
| Python support | None | pyright + black |

## Performance Notes

- First Neovim launch takes ~10 seconds (plugins loading)
- LSP startup: ~2 seconds per language
- After first launch: <1 second

All very manageable for learning.

## Support

If things don't work:

1. Check `SETUP_NVIM.md` for detailed Neovim setup
2. Read error messages carefully
3. Verify tools with `:Mason` inside Neovim
4. Run the script again

Most issues resolve by re-running `bash setup-dev.sh`.

## Next

✓ Setup complete!

Now read `START_HERE.md` and run:
```bash
learn c++ 1
```

Happy learning!

