" LEARN Platform Vim Configuration
" Optimized for learning programming with focus on visibility and keystroke practice

" ============================================================================
" CORE INDENTATION & SPACING (DEFAULT: 2 SPACES)
" ============================================================================

set tabstop=2           " Tab character displays as 2 spaces
set softtabstop=2       " Backspace deletes 2 spaces (soft tabs)
set shiftwidth=2        " Auto-indent uses 2 spaces
set expandtab           " Use spaces instead of tab characters
set autoindent          " Auto-indent on new line

" ============================================================================
" LANGUAGE-SPECIFIC SETTINGS
" ============================================================================

" C/C++ - 4 spaces
autocmd FileType c,cpp set tabstop=4 shiftwidth=4 softtabstop=4

" Rust - 4 spaces
autocmd FileType rust set tabstop=4 shiftwidth=4 softtabstop=4

" Python - 4 spaces (PEP 8)
autocmd FileType python set tabstop=4 shiftwidth=4 softtabstop=4

" Go - Tab characters (Go convention)
autocmd FileType go set tabstop=4 shiftwidth=4 noexpandtab

" Kotlin - 4 spaces
autocmd FileType kotlin set tabstop=4 shiftwidth=4 softtabstop=4

" C# - 4 spaces
autocmd FileType cs set tabstop=4 shiftwidth=4 softtabstop=4

" Swift - 2 spaces
autocmd FileType swift set tabstop=2 shiftwidth=2 softtabstop=2

" Dart - 2 spaces
autocmd FileType dart set tabstop=2 shiftwidth=2 softtabstop=2

" TypeScript - 2 spaces
autocmd FileType typescript set tabstop=2 shiftwidth=2 softtabstop=2

" PowerShell - 4 spaces
autocmd FileType ps1 set tabstop=4 shiftwidth=4 softtabstop=4

" SQL - 2 spaces
autocmd FileType sql set tabstop=2 shiftwidth=2 softtabstop=2

" Shell/Bash - 2 spaces
autocmd FileType sh set tabstop=2 shiftwidth=2 softtabstop=2

" Lua - 2 spaces
autocmd FileType lua set tabstop=2 shiftwidth=2 softtabstop=2

" ============================================================================
" VISIBILITY & LEARNING FEATURES
" ============================================================================

set number              " Show line numbers
set cursorline          " Highlight current line
set showmatch           " Highlight matching brackets
set hlsearch            " Highlight search results
set incsearch           " Incremental search

" ============================================================================
" SYNTAX & APPEARANCE
" ============================================================================

syntax on               " Enable syntax highlighting
set background=dark     " Dark background

" ============================================================================
" TERMINAL OUTPUT & SHELL SETTINGS
" ============================================================================

" Ensure proper terminal output flushing for shell commands
set shell=/bin/bash
set shellcmdflag=-ic
set shellredir=>
set term=xterm-256color

" ============================================================================
" SPLIT WINDOW CONFIGURATION (FOR VIM LESSON MODE)
" ============================================================================

" Equal window sizes after split
autocmd VimResized * wincmd =

" ============================================================================
" LEARNING MODE TIPS (DISPLAYED ON STARTUP)
" ============================================================================

" Display learning tips
if has('autocmd')
  augroup LearningTips
    autocmd!
    autocmd VimEnter * call DisplayLearningTips()
  augroup END
endif

function! DisplayLearningTips()
  echo ""
  echo "📚 LEARN PLATFORM VIM - TAB SETTINGS: 2 SPACES (Most Languages)"
  echo "   C++ / Python / Rust: 4 spaces | Go: Tab characters"
  echo ""
  echo "💡 TIPS:"
  echo "   • i / a        → Insert mode"
  echo "   • Esc          → Normal mode"
  echo "   • :w           → Save"
  echo "   • gg / G       → Jump to top/bottom"
  echo ""
endfunction

" ============================================================================
" LANGUAGE-SPECIFIC RUN COMMANDS
" ============================================================================

function! DetectLanguage()
    let current_file = expand('%:p')
    if &filetype != ''
        return &filetype
    endif
    if current_file =~ '/python/'
        return 'python'
    elseif current_file =~ '/java/'
        return 'java'
    elseif current_file =~ '/javascript/'
        return 'javascript'
    elseif current_file =~ '/c-c++/'
        return 'cpp'
    elseif current_file =~ '/shell/'
        return 'bash'
    elseif current_file =~ '/sql/'
        return 'sql'
    elseif current_file =~ '/go/'
        return 'go'
    elseif current_file =~ '/rust/'
        return 'rust'
    elseif current_file =~ '/php/'
        return 'php'
    elseif current_file =~ '/r/'
        return 'r'
    elseif current_file =~ '/julia/'
        return 'julia'
    elseif current_file =~ '/typescript/'
        return 'typescript'
    elseif current_file =~ '/lua/'
        return 'lua'
    elseif current_file =~ '/powershell/'
        return 'powershell'
    elseif current_file =~ '/zig/'
        return 'zig'
    elseif current_file =~ '/nosql/'
        return 'nosql'
    elseif current_file =~ '/csharp/'
        return 'csharp'
    elseif current_file =~ '/dart/'
        return 'dart'
    elseif current_file =~ '/kotlin/'
        return 'kotlin'
    elseif current_file =~ '/swift/'
        return 'swift'
    endif
    return 'unknown'
endfunction

function! GetRunCommand()
    let lang = DetectLanguage()
    let commands = {
        \ 'python': 'python3 main.py',
        \ 'java': 'javac Main.java && java Main',
        \ 'javascript': 'node main.js',
        \ 'cpp': 'make run',
        \ 'c': 'make run',
        \ 'bash': 'bash main.sh',
        \ 'sh': 'bash main.sh',
        \ 'sql': 'sqlite3 < main.sql',
        \ 'go': 'go run main.go',
        \ 'rust': 'cargo run --release',
        \ 'php': 'php main.php',
        \ 'r': 'Rscript main.r',
        \ 'julia': 'julia main.jl',
        \ 'typescript': 'ts-node main.ts',
        \ 'lua': 'lua main.lua',
        \ 'powershell': 'pwsh ./main.ps1',
        \ 'zig': 'zig build run',
        \ 'nosql': 'mongo < main.js',
        \ 'csharp': 'dotnet run',
        \ 'dart': 'dart main.dart',
        \ 'kotlin': 'kotlin -J-Xms128m -J-Xmx768m MainKt',
        \ 'swift': 'swift main.swift',
        \ }
    return get(commands, lang, 'echo "No run command defined"')
endfunction

function! ShowDynamicHelp()
    let run_cmd = GetRunCommand()
    let lang = DetectLanguage()
    echo ""
    echo "=== " . toupper(lang) . " LESSON HELP ==="
    echo ""
    echo "RUN CODE: :!" . run_cmd
    echo "or use:   <Space>r"
    echo ""
    echo "NAVIGATION:"
    echo "  <Space>n/p    - Next/Previous lesson"
    echo "  <Space>h      - Show this help"
    echo "  Ctrl+h/l      - Switch windows"
    echo ""
endfunction

" Run command mapping
nnoremap <leader>r :execute '!'.GetRunCommand()<CR>
nnoremap <leader>h :call ShowDynamicHelp()<CR>
