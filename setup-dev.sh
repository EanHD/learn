#!/usr/bin/env bash
set -euo pipefail

echo "==> Learning Environment Setup"
echo "==> Detecting distro (assuming Debian/Ubuntu on WSL)…"
if ! command -v apt >/dev/null 2>&1; then
  echo "This script expects apt (Debian/Ubuntu). Exiting." >&2
  exit 1
fi

echo "==> Updating apt and installing base packages…"
sudo apt update
sudo apt install -y \
  build-essential curl git unzip pkg-config ripgrep fd-find \
  python3 python3-pip python3-venv \
  clangd

# Some distros call fd 'fdfind'
if ! command -v fd >/dev/null 2>&1 && command -v fdfind >/dev/null 2>&1; then
  sudo update-alternatives --install /usr/bin/fd fd /usr/bin/fdfind 10
fi

echo "==> Installing Node.js LTS (for some tools & formatters)…"
if ! command -v node >/dev/null 2>&1; then
  curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
  sudo apt install -y nodejs
fi

echo "==> Installing Rust (rustup + rust-analyzer)…"
if ! command -v rustup >/dev/null 2>&1; then
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
  # shellcheck disable=SC1090
  source "$HOME/.cargo/env"
else
  echo "Rust already installed, updating..."
fi
rustup toolchain install stable
rustup default stable
rustup component add rust-analyzer 2>/dev/null || true

echo "==> Installing Neovim…"
if ! command -v nvim >/dev/null 2>&1; then
  echo "Installing Neovim..."
  sudo apt install -y neovim
else
  echo "Neovim already installed: $(nvim --version | head -1)"
fi

echo "==> Installing Kickstart.nvim…"
NVIM_CONF="${HOME}/.config/nvim/init.lua"
KICKSTART_ALT="${HOME}/.config/nvim/kickstart"
if [ -f "$NVIM_CONF" ]; then
  echo "Kickstart already installed at ${NVIM_CONF}"
elif [ -d "$KICKSTART_ALT" ]; then
  echo "Kickstart found at ${KICKSTART_ALT}, copying to ~/.config/nvim…"
  rm -rf "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim
  cp -r "$KICKSTART_ALT" "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim
  echo "Kickstart configured."
else
  echo "Cloning Kickstart.nvim to ${XDG_CONFIG_HOME:-$HOME/.config}/nvim…"
  git clone https://github.com/nvim-lua/kickstart.nvim.git "${XDG_CONFIG_HOME:-$HOME/.config}"/nvim
  echo "Kickstart installed successfully."
fi

echo "==> Creating LazyVim plugins spec for Mason packages…"
CUSTOM_PLUGINS_DIR="${HOME}/.config/nvim/lua/custom/plugins"
mkdir -p "$CUSTOM_PLUGINS_DIR"

# Create the mason-config.lua spec file
cat > "${CUSTOM_PLUGINS_DIR}/mason-config.lua" << 'EOF'
return {
  {
    "williamboman/mason.nvim",
    opts = {
      ensure_installed = {
        "clangd",       -- C/C++
        "rust-analyzer", -- Rust
        "pyright",      -- Python LSP
        "tsserver",     -- TypeScript/JavaScript LSP
        "marksman",     -- Markdown LSP
        "prettierd",    -- Fast Prettier daemon (Markdown/JS/TS)
        "black",        -- Python formatter
        "shfmt",        -- Shell formatter
        "stylua",       -- Lua formatter
      },
    },
  },
  {
    "williamboman/mason-lspconfig.nvim",
    opts = {
      ensure_installed = {
        "clangd",
        "rust_analyzer",
        "pyright",
        "ts_ls",
        "marksman",
      },
    },
  },
  {
    "stevearc/conform.nvim",
    opts = {
      formatters_by_ft = {
        cpp = { "clangd" },
        c = { "clangd" },
        rust = { "rustfmt" },
        python = { "black" },
        javascript = { "prettierd" },
        typescript = { "prettierd" },
        markdown = { "prettierd" },
        shell = { "shfmt" },
        lua = { "stylua" },
      },
    },
  },
}
EOF

echo "Created ${CUSTOM_PLUGINS_DIR}/mason-config.lua"

echo "==> Installing Mason packages via Neovim…"
# Open Neovim headless, sync plugins, install Mason packages, then quit
nvim --headless \
  '+MasonInstall clangd rust-analyzer pyright tsserver marksman prettierd black shfmt stylua' \
  '+qa' \
  2>/dev/null || true

echo "==> Installing global CLI helpers (optional)…"
sudo npm -g install prettier markdownlint-cli || true

echo "==> Done!"
echo
echo "What was configured:"
echo "- System: build-essential, clangd, Node LTS, Rust + rust-analyzer"
echo "- Neovim: Installed (or verified existing)"
echo "- Kickstart.nvim: Cloned to ~/.config/nvim"
echo "- LazyVim specs: Created at ~/.config/nvim/lua/custom/plugins/mason-config.lua"
echo "- Mason packages installed: clangd, rust-analyzer, pyright, tsserver, marksman, prettierd, black, shfmt, stylua"
echo
echo "Next steps:"
echo "1) Open Neovim once (nvim) to let Kickstart/lazy.nvim finish syncing."
echo "2) Check :Mason to confirm all tools are installed."
echo "3) Check :LspInfo to verify LSPs are attached."
echo "4) See SETUP_NVIM.md for word-wrap configuration."
echo
