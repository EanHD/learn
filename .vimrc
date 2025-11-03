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
