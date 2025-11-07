-- ==========================================
-- LEARN Platform - Modern Neovim Configuration
-- Beautiful markdown rendering with Nightfox theme
-- ==========================================

-- ========== BOOTSTRAP LAZY.NVIM PLUGIN MANAGER ==========
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- ========== CORE SETTINGS ==========

-- Leader key
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Visual appearance
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.cursorline = true
vim.opt.termguicolors = true
vim.opt.signcolumn = "yes"

-- Search
vim.opt.hlsearch = true
vim.opt.incsearch = true
vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Window and scrolling
vim.opt.scrolloff = 5
vim.opt.sidescrolloff = 5
vim.opt.splitright = true
vim.opt.splitbelow = true

-- Indentation (default: 2 spaces)
vim.opt.autoindent = true
vim.opt.expandtab = true
vim.opt.tabstop = 2
vim.opt.shiftwidth = 2
vim.opt.softtabstop = 2

-- Editing
vim.opt.backspace = "indent,eol,start"
vim.opt.mouse = "a"
vim.opt.clipboard = "unnamedplus"

-- Disable swap/backup files
vim.opt.swapfile = false
vim.opt.backup = false
vim.opt.undofile = false

-- Status line
vim.opt.laststatus = 3  -- Global statusline
vim.opt.showmode = false  -- Don't show mode (lualine will)

-- Better completion experience
vim.opt.completeopt = "menu,menuone,noselect"

-- Line wrapping (disable globally, enable for markdown only)
vim.opt.wrap = false

-- Concealment (safe defaults for code, markdown will override)
vim.opt.conceallevel = 0  -- Show all by default
vim.opt.concealcursor = ""  -- Show syntax in cursor line for editing

-- ========== PLUGIN SETUP ==========

require("lazy").setup({
  -- Nightfox theme
  {
    "EdenEast/nightfox.nvim",
    priority = 1000,
    config = function()
      require("nightfox").setup({
        options = {
          compile_path = vim.fn.stdpath("cache") .. "/nightfox",
          compile_file_suffix = "_compiled",
          transparent = false,  -- Solid background
          terminal_colors = true,
          dim_inactive = false,
          module_default = true,
          styles = {
            comments = "italic",
            conditionals = "NONE",
            constants = "NONE",
            functions = "NONE",
            keywords = "bold",
            numbers = "NONE",
            operators = "NONE",
            strings = "NONE",
            types = "NONE",
            variables = "NONE",
          },
        },
      })
      -- Load the nightfox colorscheme
      vim.cmd("colorscheme nightfox")
    end,
  },

  -- Lualine statusline
  {
    "nvim-lualine/lualine.nvim",
    dependencies = { "nvim-tree/nvim-web-devicons", "EdenEast/nightfox.nvim" },
    config = function()
      require("lualine").setup({
        options = {
          theme = "onedark",
          section_separators = { right = "", left = "" },
          component_separators = { right = "", left = "" },
          icons_enabled = true,
          globalstatus = true,
        },
        sections = {
          lualine_a = { "mode" },
          lualine_b = { "branch", "diff", "diagnostics" },
          lualine_c = {
            {
              "filename",
              path = 1,  -- Relative path
              symbols = {
                modified = " [+]",
                readonly = " [RO]",
                unnamed = "[No Name]",
              },
            },
          },
          lualine_x = { "encoding", "fileformat", "filetype" },
          lualine_y = { "progress" },
          lualine_z = { "location" },
        },
      })
    end,
  },

  -- Better markdown rendering (conceals ** ### etc.)
  {
    "MeanderingProgrammer/render-markdown.nvim",
    dependencies = { "nvim-treesitter/nvim-treesitter", "nvim-tree/nvim-web-devicons" },
    ft = { "markdown" },
    config = function()
      require("render-markdown").setup({
        -- Render markdown beautifully
        render_modes = { 'n', 'c' },  -- Only render in normal and command mode (not when cursor is on line)
        anti_conceal = {
          enabled = true,  -- Keep original markdown visible on cursor line
        },
        heading = {
          enabled = true,
          sign = true,
          icons = { "📌 ", "📍 ", "🔸 ", "🔹 ", "▪️ ", "▫️ " },
          width = "full",
          backgrounds = {
            "RenderMarkdownH1Bg",
            "RenderMarkdownH2Bg",
            "RenderMarkdownH3Bg",
            "RenderMarkdownH4Bg",
            "RenderMarkdownH5Bg",
            "RenderMarkdownH6Bg",
          },
        },
        code = {
          enabled = true,
          sign = true,
          style = "language",
          width = "block",
          left_pad = 2,
          right_pad = 2,
          border = "thin",
        },
        bullet = {
          enabled = true,
          icons = { "🔹 ", "🔸 ", "▪️ ", "▫️ " },
          highlight = "RenderMarkdownBullet",
        },
        checkbox = {
          enabled = true,
          unchecked = { icon = "⬜ " },
          checked = { icon = "✅ " },
        },
        quote = {
          enabled = true,
          icon = "┃",
        },
        link = {
          enabled = true,
          image = "🖼️ ",
          hyperlink = "🔗 ",
        },
      })
    end,
  },

  -- Treesitter for better syntax highlighting
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    config = function()
      require("nvim-treesitter.configs").setup({
        ensure_installed = {
          "c", "cpp", "rust", "python", "javascript", "typescript",
          "go", "lua", "dart", "kotlin", "bash", "markdown", "markdown_inline"
        },
        highlight = {
          enable = true,
          additional_vim_regex_highlighting = false,
        },
        indent = { enable = true },
      })
    end,
  },

  -- Icons
  {
    "nvim-tree/nvim-web-devicons",
    config = function()
      require("nvim-web-devicons").setup({ default = true })
    end,
  },

  -- Zen Mode - Distraction-free writing/reading
  {
    "folke/zen-mode.nvim",
    cmd = "ZenMode",
    keys = {
      { "<leader>z", "<cmd>ZenMode<cr>", desc = "Toggle Zen Mode" },
    },
    config = function()
      require("zen-mode").setup({
        window = {
          width = 90,
          options = {
            number = false,
            relativenumber = false,
            signcolumn = "no",
            cursorline = false,
          },
        },
      })
    end,
  },

  -- Indent Blankline - Show indentation guides
  {
    "lukas-reineke/indent-blankline.nvim",
    main = "ibl",
    config = function()
      require("ibl").setup({
        indent = {
          char = "│",
          tab_char = "│",
        },
        scope = { enabled = false },
        exclude = {
          filetypes = { "markdown", "help", "dashboard", "lazy" },
        },
      })
    end,
  },

  -- ToggleTerm - Terminal integration
  {
    "akinsho/toggleterm.nvim",
    version = "*",
    keys = {
      { "<leader>t", "<cmd>ToggleTerm direction=horizontal<cr>", desc = "Toggle Terminal" },
    },
    config = function()
      require("toggleterm").setup({
        size = function(term)
          if term.direction == "horizontal" then
            return 15
          elseif term.direction == "vertical" then
            return vim.o.columns * 0.4
          end
        end,
        open_mapping = [[<c-\>]],
        direction = "float",
        float_opts = {
          border = "curved",
        },
      })
    end,
  },

  -- Which-Key - Show available keybindings
  {
    "folke/which-key.nvim",
    event = "VeryLazy",
    config = function()
      local wk = require("which-key")
      wk.setup({
        plugins = {
          spelling = true,
          presets = {
            operators = false,
            motions = false,
            text_objects = false,
            windows = false,
            nav = false,
            z = false,
            g = false,
          },
        },
        win = {
          border = "rounded",
        },
      })

      -- Custom highlight for which-key descriptions (purple like popup tips)
      vim.api.nvim_set_hl(0, "WhichKeyDesc", { fg = "#c678dd" })

      -- Register main LEARN platform keybindings with proper grouping
      wk.add({
        -- Window Navigation (using arrow-like keys)
        { "<leader><Left>", "<C-w>h", desc = "← Move to left window" },
        { "<leader><Right>", "<C-w>l", desc = "→ Move to right window" },

        -- Help & Guide
        { "<leader>g", desc = "Quick Guide Popup" },
        { "<leader>h", desc = "Essential Shortcuts" },
        { "<leader>t", desc = "Toggle Terminal" },
        { "<leader>w", desc = "Save file" },        -- Find/Search group
        { "<leader>f", group = "Find" },
        { "<leader>ff", desc = "Find files" },
        { "<leader>fg", desc = "Live grep" },
        { "<leader>fb", desc = "Buffers" },
        { "<leader>fh", desc = "Help tags" },

        -- Run command (standalone, no submenu)
        { "<leader>r", desc = "🚀 Run/Compile code" },

        -- Code actions
        { "<leader>c", group = "Code" },
        { "<leader>ca", desc = "Code action" },

        -- View/UI group
        { "<leader>x", group = "View" },
        { "<leader>xx", desc = "Diagnostics (Trouble)" },
        { "<leader>xz", "<cmd>ZenMode<cr>", desc = "Toggle Zen mode" },
        { "<leader>xt", "<cmd>ToggleTerm<cr>", desc = "Toggle terminal" },
      })
    end,
  },

  -- Smooth Scrolling
  {
    "karb94/neoscroll.nvim",
    config = function()
      require("neoscroll").setup({
        mappings = { "<C-u>", "<C-d>", "<C-b>", "<C-f>", "zt", "zz", "zb" },
        hide_cursor = true,
        easing_function = "quadratic",
      })
    end,
  },

  -- Better Quickfix/Location List
  {
    "folke/trouble.nvim",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    keys = {
      { "<leader>xx", "<cmd>Trouble diagnostics toggle<cr>", desc = "Diagnostics (Trouble)" },
    },
    config = function()
      require("trouble").setup()
    end,
  },

  -- Highlight Colors in Code
  {
    "NvChad/nvim-colorizer.lua",
    ft = { "css", "html", "javascript", "typescript", "lua" },
    config = function()
      require("colorizer").setup({
        user_default_options = {
          RGB = true,
          RRGGBB = true,
          names = false,
          css = true,
        },
      })
    end,
  },

  -- Auto-pairs for brackets
  {
    "windwp/nvim-autopairs",
    event = "InsertEnter",
    config = function()
      require("nvim-autopairs").setup({
        check_ts = true,
        ts_config = {
          lua = { "string" },
          javascript = { "template_string" },
        },
      })
    end,
  },

  -- Better commenting
  {
    "numToStr/Comment.nvim",
    keys = {
      { "gcc", mode = "n", desc = "Comment toggle current line" },
      { "gc", mode = { "n", "o" }, desc = "Comment toggle linewise" },
      { "gc", mode = "x", desc = "Comment toggle linewise (visual)" },
      { "gbc", mode = "n", desc = "Comment toggle current block" },
      { "gb", mode = { "n", "o" }, desc = "Comment toggle blockwise" },
      { "gb", mode = "x", desc = "Comment toggle blockwise (visual)" },
    },
    config = function()
      require("Comment").setup()
    end,
  },

  -- Flash - Jump to any location quickly
  {
    "folke/flash.nvim",
    event = "VeryLazy",
    keys = {
      { "s", mode = { "n", "x", "o" }, function() require("flash").jump() end, desc = "Flash" },
      { "S", mode = { "n", "x", "o" }, function() require("flash").treesitter() end, desc = "Flash Treesitter" },
    },
    config = function()
      require("flash").setup()
    end,
  },

  -- Telescope - Fuzzy finder
  {
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    keys = {
      { "<leader>ff", function() require("telescope.builtin").find_files() end, desc = "Find files" },
      { "<leader>fg", function() require("telescope.builtin").live_grep() end,  desc = "Live grep" },
      { "<leader>fb", function() require("telescope.builtin").buffers() end,    desc = "Buffers" },
      { "<leader>fh", function() require("telescope.builtin").help_tags() end,  desc = "Help tags" },
    },
  },

  -- Telescope FZF extension for speed
  {
    "nvim-telescope/telescope-fzf-native.nvim",
    build = "cmake -S. -Bbuild -DCMAKE_BUILD_TYPE=Release && cmake --build build --config Release && cmake --install build --prefix build",
    config = function()
      require("telescope").load_extension("fzf")
    end,
  },

  -- Mason - LSP installer
  {
    "williamboman/mason.nvim",
    build = ":MasonUpdate",
    config = function()
      require("mason").setup()
    end,
  },

  -- Mason LSP config - Auto-install language servers
  {
    "williamboman/mason-lspconfig.nvim",
    dependencies = { "neovim/nvim-lspconfig" },
    config = function()
      local lsp = require("lspconfig")
      require("mason-lspconfig").setup({
        ensure_installed = {
          "lua_ls",           -- Lua
          "pyright",          -- Python
          "ts_ls",            -- TypeScript/JavaScript
          "gopls",            -- Go
          "clangd",           -- C/C++
          "rust_analyzer",    -- Rust
          "bashls",           -- Shell/Bash
        },
        handlers = {
          function(server) lsp[server].setup({}) end,
        },
      })
    end,
    keys = {
      { "K",  vim.lsp.buf.hover,        desc = "Hover docs" },
      { "gd", vim.lsp.buf.definition,   desc = "Go to definition" },
      { "gr", vim.lsp.buf.references,   desc = "Find references" },
      -- { "<leader>rn", vim.lsp.buf.rename, desc = "Rename symbol" },  -- Disabled to avoid conflict with <leader>r
      { "<leader>ca", vim.lsp.buf.code_action, desc = "Code action" },
    },
  },

})

-- ========== CUSTOM QUICK NAVIGATION GUIDE POPUP ==========

do
  (function()
      -- Create the popup functionality
      local M = {}
      local popup_win = nil
      local popup_buf = nil

      -- Check if JetBrainsMono Nerd Font is available, fallback to default
      local function get_font_family()
        -- Try to detect JetBrainsMono Nerd Font
        if vim.fn.has("gui_running") == 1 then
          return "JetBrainsMono Nerd Font"
        end
        return nil -- Use terminal default
      end

      -- Create the guide content
      local function create_guide_content()
        local lines = {
          "╔══════════════════════════════════════════════════════════════════════════╗",
          "║                   🎓 LEARN PLATFORM - Quick Navigation Guide             ║",
          "╚══════════════════════════════════════════════════════════════════════════╝",
          "",
          "📚 LESSON NAVIGATION",
          "   <Space>n  →  Next lesson",
          "   <Space>p  →  Previous lesson",
          "   <Space>i  →  Show lesson info (stage/level)",
          "",
          "🔍 FIND & SEARCH",
          "   <Space>ff →  Find files (fuzzy search)",
          "   <Space>fg →  Live grep (search in all files)",
          "   <Space>fb →  List open buffers",
          "   <Space>fh →  Help tags (search documentation)",
          "",
          "💻 CODE INTELLIGENCE (works in code files only)",
          "   K         →  Hover documentation (place cursor on code)",
          "   gd        →  Go to definition",
          "   gr        →  Find references",
          "   <Space>rn →  Rename symbol",
          "   <Space>ca →  Code actions",
          "",
          "🎨 FOCUS & DISPLAY",
          "   <Space>z  →  Zen Mode (distraction-free reading)",
          "   <Space>g  →  Toggle this Quick Guide popup",
          "   <Space>h  →  Show detailed help message",
          "   <Space>H  →  Open Vim help (vertical split)",
          "",
          "💻 TERMINAL & EDITING",
          "   <Space>t  →  Toggle floating terminal",
          "   <Space>th →  Toggle horizontal terminal",
          "   Ctrl+\\    →  Quick terminal toggle",
          "   gcc       →  Comment/uncomment current line",
          "   gc        →  Comment/uncomment selection (visual mode)",
          "",
          "⚡ QUICK NAVIGATION",
          "   s+[char]  →  Flash jump to any word on screen",
          "   S         →  Flash jump using syntax tree",
          "   Ctrl+hjkl →  Navigate between windows (h=left j=down k=up l=right)",
          "   <Space> =  →  Equalize all window sizes",
          "   <Space> .  →  Make current window wider",
          "   <Space> ,  →  Make current window narrower",
          "",
          "💾 FILE OPERATIONS",
          "   <Space>w  →  Save file",
          "   <Space>ro →  Toggle read-only mode",
          "   <Space>xx →  Show diagnostics/errors list",
          "",
          "💡 TIP: Press <Esc>, q, or <Space>g to close this guide",
          "════════════════════════════════════════════════════════════════════════════",
        }
        return lines
      end

      -- Toggle the popup window
      function M.toggle_guide()
        if popup_win and vim.api.nvim_win_is_valid(popup_win) then
          -- Close the popup
          vim.api.nvim_win_close(popup_win, true)
          if popup_buf and vim.api.nvim_buf_is_valid(popup_buf) then
            vim.api.nvim_buf_delete(popup_buf, { force = true })
          end
          popup_win = nil
          popup_buf = nil
        else
          -- Create the popup
          local content = create_guide_content()

          -- Calculate popup size
          local width = 80
          local height = #content + 2
          local row = math.floor((vim.o.lines - height) / 2)
          local col = math.floor((vim.o.columns - width) / 2)

          -- Create buffer
          popup_buf = vim.api.nvim_create_buf(false, true)
          vim.api.nvim_buf_set_lines(popup_buf, 0, -1, false, content)

          -- Make buffer read-only
          vim.api.nvim_buf_set_option(popup_buf, "modifiable", false)
          vim.api.nvim_buf_set_option(popup_buf, "readonly", true)
          vim.api.nvim_buf_set_option(popup_buf, "buftype", "nofile")
          vim.api.nvim_buf_set_option(popup_buf, "bufhidden", "wipe")
          vim.api.nvim_buf_set_option(popup_buf, "filetype", "learn-guide")

          -- Create floating window with rounded borders
          local opts = {
            relative = "editor",
            width = width,
            height = height,
            row = row,
            col = col,
            style = "minimal",
            border = "rounded",
            title = " Quick Guide ",
            title_pos = "center",
          }

          popup_win = vim.api.nvim_open_win(popup_buf, true, opts)

          -- Set window options for better appearance
          vim.api.nvim_win_set_option(popup_win, "winblend", 10)
          vim.api.nvim_win_set_option(popup_win, "cursorline", false)

          -- Set up keymaps to close the popup
          local close_popup = function()
            M.toggle_guide()
          end

          -- Close on Esc or Space+g
          vim.api.nvim_buf_set_keymap(popup_buf, "n", "<Esc>", "", {
            callback = close_popup,
            noremap = true,
            silent = true
          })
          vim.api.nvim_buf_set_keymap(popup_buf, "n", "<leader>g", "", {
            callback = close_popup,
            noremap = true,
            silent = true
          })
          vim.api.nvim_buf_set_keymap(popup_buf, "n", "q", "", {
            callback = close_popup,
            noremap = true,
            silent = true
          })

          -- Highlight groups for beautiful, vibrant appearance
          vim.api.nvim_set_hl(0, "LearnGuideTitle", { fg = "#61afef", bold = true, bg = "#2c313c" })
          vim.api.nvim_set_hl(0, "LearnGuideSection", { fg = "#e5c07b", bold = true })
          vim.api.nvim_set_hl(0, "LearnGuideKey", { fg = "#98c379", bold = true })
          vim.api.nvim_set_hl(0, "LearnGuideDescription", { fg = "#abb2bf" })
          vim.api.nvim_set_hl(0, "LearnGuideBorder", { fg = "#56b6c2" })
          vim.api.nvim_set_hl(0, "LearnGuideTip", { fg = "#c678dd", italic = true })
          vim.api.nvim_set_hl(0, "LearnGuideHeader", { fg = "#56b6c2", bold = true })

          -- Apply syntax highlighting with more visual impact
          -- Header box (lines 0-2)
          vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideHeader", 0, 0, -1)
          vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideTitle", 1, 0, -1)
          vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideHeader", 2, 0, -1)

          for i = 1, #content do
            local line = content[i]

            -- Highlight section headers (with emojis)
            if line:match("^[🎓📚🔍💻🎨⚡💾💡]") then
              vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideSection", i - 1, 0, -1)

            -- Highlight command lines with arrows
            elseif line:match("→") then
              local arrow_pos = line:find("→")
              -- Highlight everything before the arrow as keybinding (green)
              if arrow_pos then
                vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideKey", i - 1, 0, arrow_pos - 1)
                -- Highlight description after arrow (gray)
                vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideDescription", i - 1, arrow_pos + 2, -1)
              end

            -- Highlight the tip line
            elseif line:match("^💡") then
              vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideTip", i - 1, 0, -1)

            -- Highlight bottom border
            elseif line:match("^═+$") then
              vim.api.nvim_buf_add_highlight(popup_buf, -1, "LearnGuideHeader", i - 1, 0, -1)
            end
          end
        end
      end

    -- Make the function globally available
    _G.LearnGuide = M
  end)()
end

-- ========== LANGUAGE-SPECIFIC INDENTATION ==========

local indent_group = vim.api.nvim_create_augroup("IndentSettings", { clear = true })

-- 4 spaces
vim.api.nvim_create_autocmd("FileType", {
  group = indent_group,
  pattern = { "c", "cpp", "rust", "python", "kotlin", "cs", "ps1" },
  callback = function()
    vim.opt_local.tabstop = 4
    vim.opt_local.shiftwidth = 4
    vim.opt_local.softtabstop = 4
  end,
})

-- Tab characters for Go
vim.api.nvim_create_autocmd("FileType", {
  group = indent_group,
  pattern = "go",
  callback = function()
    vim.opt_local.expandtab = false
    vim.opt_local.tabstop = 4
    vim.opt_local.shiftwidth = 4
  end,
})

-- ========== CODE FILE AUTO-POSITIONING ==========

-- Position cursor on line 4 when opening code files with help comment
vim.api.nvim_create_autocmd({"BufReadPost", "BufNewFile"}, {
  pattern = {"*.cpp", "*.c", "*.rs", "*.py", "*.js", "*.ts", "*.go", "*.lua", "*.dart", "*.swift", "*.kt"},
  callback = function(args)
    -- Small delay to ensure file is fully loaded and all windows are set up
    vim.defer_fn(function()
      -- Get the buffer number from the autocmd event
      local bufnr = args.buf
      local first_line = vim.api.nvim_buf_get_lines(bufnr, 0, 1, false)[1]

      -- Check if file has the help comment at the top
      if first_line and first_line:match("Press") and first_line:match("Space") and first_line:match("help") then
        local line_count = vim.api.nvim_buf_line_count(bufnr)
        if line_count >= 4 then
          -- Find the window showing this buffer and position cursor there
          for _, win in ipairs(vim.api.nvim_list_wins()) do
            if vim.api.nvim_win_get_buf(win) == bufnr then
              vim.api.nvim_win_set_cursor(win, {4, 0})
              break
            end
          end
        end
      end
    end, 100)  -- Increased delay to 100ms for split-screen scenario
  end,
})

-- ========== MARKDOWN-SPECIFIC SETTINGS ==========

vim.api.nvim_create_autocmd("FileType", {
  pattern = "markdown",
  callback = function()
    -- Enable concealment for markdown but keep formatting visible on cursor line
    vim.opt_local.conceallevel = 2
    vim.opt_local.concealcursor = "i"  -- Don't conceal on cursor line

    -- Make lesson files truly read-only and prevent insert mode
    if vim.fn.expand("%:p"):match("lesson%.md$") then
      vim.opt_local.readonly = true
      vim.opt_local.modifiable = false

      -- Helper function to show read-only message
      local function show_readonly_msg()
        vim.notify("📖 Lesson file is read-only. Use Ctrl+l to switch to code window.", vim.log.levels.WARN)
      end

      -- Prevent insert mode in lesson files WITH helpful message
      vim.keymap.set("n", "i", show_readonly_msg, { buffer = true, silent = false })
      vim.keymap.set("n", "I", show_readonly_msg, { buffer = true, silent = false })
      vim.keymap.set("n", "a", show_readonly_msg, { buffer = true, silent = false })
      vim.keymap.set("n", "A", show_readonly_msg, { buffer = true, silent = false })
      vim.keymap.set("n", "o", show_readonly_msg, { buffer = true, silent = false })
      vim.keymap.set("n", "O", show_readonly_msg, { buffer = true, silent = false })
      vim.keymap.set("n", "c", show_readonly_msg, { buffer = true, silent = false })
      vim.keymap.set("n", "C", show_readonly_msg, { buffer = true, silent = false })

      -- Preserve Flash navigation
      vim.keymap.set("n", "s", function() require("flash").jump() end, { buffer = true, desc = "Flash jump" })
      vim.keymap.set("n", "S", function() require("flash").treesitter() end, { buffer = true, desc = "Flash treesitter" })

      -- Additional guard: if someone bypasses the keymaps and enters insert mode
      vim.api.nvim_create_autocmd("InsertEnter", {
        buffer = 0,
        callback = function()
          vim.cmd("stopinsert")
          show_readonly_msg()
          return true
        end,
      })
    end

    -- Better word wrapping
    vim.opt_local.wrap = true
    vim.opt_local.linebreak = true
    vim.opt_local.breakindent = true
  end,
})

-- ========== KEYMAPPINGS ==========

local map = vim.keymap.set

-- Window navigation
map("n", "<C-h>", "<C-w>h", { desc = "Move to left window" })
map("n", "<C-j>", "<C-w>j", { desc = "Move to bottom window" })
map("n", "<C-k>", "<C-w>k", { desc = "Move to top window" })
map("n", "<C-l>", "<C-w>l", { desc = "Move to right window" })

-- Window resizing (terminal-safe keys)
map("n", "<leader>=", "<C-w>=", { desc = "Equalize windows" })
map("n", "<leader>.", "<C-w>>", { desc = "Wider" })
map("n", "<leader>,", "<C-w><", { desc = "Narrower" })

-- Quick save
map("n", "<leader>w", ":w<CR>", { desc = "Save file" })

-- Toggle readonly (disabled to avoid conflict with <leader>r for run/compile)
-- map("n", "<leader>ro", function()
--   vim.opt_local.readonly = not vim.opt_local.readonly:get()
--   vim.opt_local.modifiable = not vim.opt_local.modifiable:get()
--   print("Readonly: " .. tostring(vim.opt_local.readonly:get()))
-- end, { desc = "Toggle readonly" })

-- Clear search highlighting
map("n", "<Esc>", ":noh<CR>", { silent = true, desc = "Clear search highlight" })

-- Better scrolling
map("n", "<C-d>", "<C-d>zz", { desc = "Scroll down and center" })
map("n", "<C-u>", "<C-u>zz", { desc = "Scroll up and center" })

-- Terminal (ToggleTerm handles <leader>t, so just add exit mapping)
map("t", "<Esc>", "<C-\\><C-n>", { desc = "Exit terminal mode" })

-- ========== LESSON NAVIGATION FUNCTIONS ==========

-- Function to get current lesson info
local function get_lesson_info()
  local path = vim.fn.expand("%:p")
  local stage = path:match("stage%-(%d+)")
  local level = path:match("level%-(%d+)")

  if stage and level then
    return { stage = tonumber(stage), level = tonumber(level) }
  end
  return nil
end

-- Jump to next lesson
map("n", "<leader>n", function()
  local info = get_lesson_info()
  if not info then
    print("Not in a lesson file")
    return
  end

  local next_level = info.level + 1
  if next_level > 7 then
    print("Already at last level!")
    return
  end

  local current_path = vim.fn.expand("%:p")
  local next_path = current_path:gsub("level%-" .. info.level .. "/", "level%-" .. next_level .. "/")

  if vim.fn.filereadable(next_path) == 1 then
    vim.cmd("edit " .. next_path)
    vim.cmd("wincmd l")  -- Switch to right window (code window)
    print("Moved to Level " .. next_level .. " - Code window active")
  else
    print("Next lesson not found")
  end
end, { desc = "Next lesson (switches to code window)" })

-- Jump to previous lesson
map("n", "<leader>p", function()
  local info = get_lesson_info()
  if not info then
    print("Not in a lesson file")
    return
  end

  local prev_level = info.level - 1
  if prev_level < 1 then
    print("Already at first level!")
    return
  end

  local current_path = vim.fn.expand("%:p")
  local prev_path = current_path:gsub("level%-" .. info.level .. "/", "level%-" .. prev_level .. "/")

  if vim.fn.filereadable(prev_path) == 1 then
    vim.cmd("edit " .. prev_path)
    vim.cmd("wincmd l")  -- Switch to right window (code window)
    print("Moved to Level " .. prev_level .. " - Code window active")
  else
    print("Previous lesson not found")
  end
end, { desc = "Previous lesson (switches to code window)" })

-- Show lesson info
map("n", "<leader>i", function()
  local info = get_lesson_info()
  if info then
    print(string.format("Stage %d | Level %d/7", info.stage, info.level))
  else
    print("Not in a lesson file")
  end
end, { desc = "Show lesson info" })

-- Function to detect language from file path
local function detect_language()
  local current_file = vim.fn.expand("%:p")
  
  if current_file:match("/python/") then return "python"
  elseif current_file:match("/java/") then return "java"
  elseif current_file:match("/javascript/") then return "javascript"
  elseif current_file:match("/c%-c++/") then return "cpp"
  elseif current_file:match("/shell/") then return "bash"
  elseif current_file:match("/sql/") then return "sql"
  elseif current_file:match("/go/") then return "go"
  elseif current_file:match("/rust/") then return "rust"
  elseif current_file:match("/php/") then return "php"
  elseif current_file:match("/r/") then return "r"
  elseif current_file:match("/julia/") then return "julia"
  elseif current_file:match("/typescript/") then return "typescript"
  elseif current_file:match("/lua/") then return "lua"
  elseif current_file:match("/powershell/") then return "powershell"
  elseif current_file:match("/zig/") then return "zig"
  elseif current_file:match("/nosql/") then return "nosql"
  elseif current_file:match("/csharp/") then return "csharp"
  elseif current_file:match("/dart/") then return "dart"
  elseif current_file:match("/kotlin/") then return "kotlin"
  elseif current_file:match("/swift/") then return "swift"
  else return "unknown" end
end

-- Get run command for current language
local function get_run_command()
  local lang = detect_language()
  
  local commands = {
    python = "python3 main.py",
    java = "javac Main.java && java Main",
    javascript = "node main.js",
    cpp = "make run",
    c = "make run",
    bash = "bash main.sh",
    sh = "bash main.sh",
    sql = "sqlite3 < main.sql",
    go = "go run main.go",
    rust = "cargo run --release",
    php = "php main.php",
    r = "Rscript main.r",
    julia = "julia main.jl",
    typescript = "ts-node main.ts",
    lua = "lua main.lua",
    powershell = "pwsh ./main.ps1",
    zig = "zig build run",
    nosql = "mongo < main.js",
    csharp = "dotnet run",
    dart = "dart main.dart",
    kotlin = "kotlin -J-Xms128m -J-Xmx768m MainKt",
    swift = "swift main.swift",
  }
  
  return commands[lang] or "echo 'No run command defined'"
end

-- Get compile/run command based on file extension (fallback if language detection fails)
local function get_compile_command()
  local current_file = vim.fn.expand("%:t")  -- Current file name
  local workspace_path = vim.fn.getcwd()

  -- Try to detect the code file if we're in lesson
  local code_file = current_file
  if current_file == "lesson.md" or current_file == "" then
    local possible_files = {
      "main.cpp", "main.c", "main.cc", "solution.cpp",
      "main.rs", "solution.rs",
      "main.py", "solution.py",
      "main.js", "solution.js",
      "main.ts", "solution.ts",
      "main.go", "solution.go",
      "main.lua", "solution.lua",
      "main.dart", "solution.dart",
      "main.swift", "solution.swift",
      "main.kt", "solution.kt",
      "main.sql", "solution.sql",
      "main.cs", "solution.cs",
      "main.sh", "solution.sh",
      "main.ps1", "solution.ps1"
    }
    for _, file in ipairs(possible_files) do
      if vim.fn.filereadable(workspace_path .. "/" .. file) == 1 then
        code_file = file
        break
      end
    end
  end

  -- First try to get from language detection
  local lang = detect_language()
  local run_cmd = get_run_command()
  if run_cmd ~= "echo 'No run command defined'" then
    return ":!" .. run_cmd, lang:upper()
  end

  -- Fallback to file extension detection
  if code_file:match("%.cpp$") or code_file:match("%.cc$") then
    return ":!make run", "C++"
  elseif code_file:match("%.c$") then
    return ":!make run", "C"
  elseif code_file:match("%.rs$") then
    return ":!cargo run --release", "Rust"
  elseif code_file:match("%.py$") then
    return ":!python3 %", "Python"
  elseif code_file:match("%.js$") then
    return ":!node %", "JavaScript"
  elseif code_file:match("%.ts$") then
    return ":!ts-node %", "TypeScript"
  elseif code_file:match("%.go$") then
    return ":!go run %", "Go"
  elseif code_file:match("%.lua$") then
    return ":!lua %", "Lua"
  elseif code_file:match("%.dart$") then
    return ":!dart %", "Dart"
  elseif code_file:match("%.swift$") then
    return ":!swift %", "Swift"
  elseif code_file:match("%.kt$") then
    return ":!kotlinc % -include-runtime -d main.jar && java -jar main.jar", "Kotlin"
  elseif code_file:match("%.sql$") then
    return ":!sqlite3 < %", "SQL"
  elseif code_file:match("%.cs$") then
    return ":!csc % && mono %.exe", "C#"
  elseif code_file:match("%.sh$") then
    return ":!bash %", "Shell"
  elseif code_file:match("%.ps1$") then
    return ":!powershell -File %", "PowerShell"
  else
    return ":!echo 'Unknown file type'", "Unknown"
  end
end

-- Essential shortcuts popup (like <Space>g but with basics)
map("n", "<leader>h", function()
  -- Get compile command dynamically
  local compile_cmd, lang_name = get_compile_command()
  
  -- Get language-specific run command
  local run_cmd = get_run_command()
  local current_lang = detect_language()

  -- Create popup content with dynamic language info
  local content = {
    "╔══════════════════════════════════════════════════════════════════════╗",
    "║                 " .. current_lang:upper() .. " LESSON - ESSENTIAL SHORTCUTS                   ║",
    "╚══════════════════════════════════════════════════════════════════════╝",
    "   Press <Esc>, q, or <Space>h to close this menu",
    "",
    "🪟 WINDOWS:",
    "   Ctrl+h / Ctrl+l  →  Switch between lesson and code",
    "   Ctrl+w =         →  Balance window sizes",
    "",
    "📚 LESSON NAVIGATION:",
    "   <Space>n / p     →  Next/Previous lesson (switches to code)",
    "   j / k            →  Scroll down/up",
    "   gg / G           →  Jump to top/bottom",
    "",
    "✏️  EDITING (in code window):",
    "   i                →  Insert mode",
    "   Esc              →  Return to normal mode",
    "   :w               →  Save file",
    "",
    "🔧 RUN COMMAND (" .. lang_name .. "):",
    "   <Space>r         →  Run: " .. run_cmd,
    "",
    "💡 TIP: Lesson is on the LEFT, your code is on the RIGHT",
    "═════════════════════════════════════════════════════════════════════════",
  }

  -- Create buffer
  local buf = vim.api.nvim_create_buf(false, true)
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, content)
  vim.api.nvim_buf_set_option(buf, "modifiable", false)
  vim.api.nvim_buf_set_option(buf, "buftype", "nofile")

  -- Calculate popup size and position
  local width = 75
  local height = #content + 2
  local row = math.floor((vim.o.lines - height) / 2)
  local col = math.floor((vim.o.columns - width) / 2)

  -- Open floating window
  local win = vim.api.nvim_open_win(buf, true, {
    relative = "editor",
    width = width,
    height = height,
    row = row,
    col = col,
    style = "minimal",
    border = "rounded",
    title = " Essential Help ",
    title_pos = "center",
  })

  vim.api.nvim_win_set_option(win, "winblend", 10)

  -- Close on Esc, Space+h, or q
  local close = function()
    if vim.api.nvim_win_is_valid(win) then
      vim.api.nvim_win_close(win, true)
    end
    if vim.api.nvim_buf_is_valid(buf) then
      vim.api.nvim_buf_delete(buf, { force = true })
    end
  end

  vim.api.nvim_buf_set_keymap(buf, "n", "<Esc>", "", { callback = close, noremap = true, silent = true })
  vim.api.nvim_buf_set_keymap(buf, "n", "<leader>h", "", { callback = close, noremap = true, silent = true })
  vim.api.nvim_buf_set_keymap(buf, "n", "q", "", { callback = close, noremap = true, silent = true })
end, { desc = "Show dynamic help for current language" })

-- Toggle Quick Navigation Guide Popup
map("n", "<leader>g", function()
  if _G.LearnGuide then
    _G.LearnGuide.toggle_guide()
  end
end, { desc = "Toggle Quick Guide popup" })

-- Run/Compile current file (dynamically detects language)
map("n", "<leader>r", function()
  local compile_cmd, lang_name = get_compile_command()
  if compile_cmd == ":!echo 'Unknown file type'" then
    vim.notify("⚠️  Cannot compile/run: Unknown file type", vim.log.levels.WARN)
    return
  end

  -- Show what we're doing
  vim.notify("🔨 Compiling/Running " .. lang_name .. " code...", vim.log.levels.INFO)

  -- Save file first
  vim.cmd("write")

  -- Execute the command (remove :! prefix for vim.cmd)
  local cmd = compile_cmd:gsub("^:!", "!")
  vim.cmd(cmd)
end, { desc = "Compile and run current file" })

-- ========== STARTUP MESSAGE ==========

vim.api.nvim_create_autocmd("VimEnter", {
  once = true,
  callback = function()
    vim.defer_fn(function()
      -- Display helpful guide
      print("╔════════════════════════════════════════════════════════════════════════════╗")
      print("║              🎓 LEARN PLATFORM - Enhanced Vim Mode Guide                   ║")
      print("╚════════════════════════════════════════════════════════════════════════════╝")
      print("")
      print("📚 LESSON NAVIGATION:")
      print("  <Space>n          Next lesson")
      print("  <Space>p          Previous lesson")
      print("  <Space>i          Show lesson info (stage/level)")
      print("")
      print("🎨 FOCUS & DISPLAY:")
      print("  <Space>g          Quick Guide popup (pretty navigation help!)")
      print("  <Space>z          Toggle Zen Mode (distraction-free reading)")
      print("  Ctrl + h/j/k/l    Navigate between windows")
      print("")
      print("💻 CODING HELPERS:")
      print("  <Space>t          Toggle floating terminal")
      print("  <Space>th         Toggle horizontal terminal")
      print("  Ctrl + \\          Quick terminal toggle")
      print("  gcc               Comment/uncomment current line")
      print("  gc (visual)       Comment/uncomment selection")
      print("")
      print("🔍 FIND & CODE INTELLIGENCE:")
      print("  <Space>ff         Find files (fuzzy)")
      print("  <Space>fg         Live grep (search in files)")
      print("  <Space>fb         List open buffers")
      print("  K                 Hover documentation")
      print("  gd                Go to definition")
      print("  gr                Find references")
      print("  <Space>rn         Rename symbol")
      print("")
      print("⚡ QUICK ACTIONS:")
      print("  s + [char]        Flash jump to any word (type chars to narrow)")
      print("  S                 Flash jump using syntax tree")
      print("  <Space>w          Save file")
      print("  <Space>ro         Toggle read-only mode")
      print("  <Space>xx         Show diagnostics/errors")
      print("  <Space>=/./ ,     Equalize/wider/narrower windows")
      print("  <Space>H          Open Vim help (vertical split)")
      print("")
      print("💡 TIPS:")
      print("  • Press <Space>g for a beautiful popup with ALL shortcuts!")
      print("  • Press <Space>h anytime to show this help guide again")
      print("  • Press <Space> and wait to see all available keybindings (Which-Key)")
      print("  • Markdown syntax (**, ###) is hidden for clean reading")
      print("  • Auto-pairs: brackets/quotes close automatically")
      print("  • Smooth scrolling enabled with Ctrl+d/u")
      print("  • LSP servers auto-install on first use of each language")
      print("  • Install a Nerd Font in your terminal for proper icons")
      print("")
      print("Type ':help' for Vim basics • <Space>g for Quick Guide popup • Enjoy! 🚀")
      print("════════════════════════════════════════════════════════════════════════════")
    end, 100)
  end,
})
