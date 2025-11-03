" ==========================================
" Learning Mode Init File for Neovim
" Optimized for learning programming + Vim
" ==========================================

" ========== ESSENTIAL SETTINGS ==========

" Visual appearance
set number                      " Show line numbers
set relativenumber              " Show relative line numbers (jump easier)
set cursorline                  " Highlight current line
" set colorcolumn=80              " Visual guide at 80 character mark (can cause issues)

" Search optimization
set hlsearch                    " Highlight search results
set incsearch                   " Incremental search
set ignorecase                  " Case-insensitive search
set smartcase                   " Case-sensitive if pattern has uppercase

" Window and scrolling
set scrolloff=5                 " Keep 5 lines visible when scrolling
set sidescrolloff=5             " Horizontal scroll padding
set splitright                  " New vertical splits on right
set splitbelow                  " New horizontal splits below

" Indentation
set autoindent                  " Auto-indent new lines
set expandtab                   " Use spaces instead of tabs
set tabstop=4                   " Tab = 4 spaces
set shiftwidth=4                " Indent = 4 spaces
set softtabstop=4

" Editing
set backspace=indent,eol,start  " Better backspace
set mouse=a                     " Enable mouse (for copy/paste if needed)
set clipboard=unnamedplus       " System clipboard integration

" Appearance
set termguicolors               " True color support
silent! colorscheme habamax     " Good contrast for reading (safe fail)

" Disable features that distract from learning
set noswapfile                  " No swap files
set nobackup                    " No backup files
set noundofile                  " Don't create undo files

" ========== CUSTOM FUNCTIONS ==========

" Function to show quick navigation help
function! ShowLessonHelp()
    let help = [
        \ "=== LESSON NAVIGATION ===",
        \ "Window Movement:",
        \ "  C-h / C-l     - Left/Right windows",
        \ "  C-j / C-k     - Down/Up windows",
        \ "  C-= / C-+ / C-- - Resize windows",
        \ "",
        \ "Lesson Navigation:",
        \ "  gg            - Top of lesson",
        \ "  G             - Bottom of lesson",
        \ "  /text         - Search forward",
        \ "  ?text         - Search backward",
        \ "  n / N         - Next/prev match",
        \ "",
        \ "Marks & Jumps:",
        \ "  ma            - Mark position 'a'",
        \ "  'a            - Jump to mark 'a'",
        \ "",
        \ "Editing (code window):",
        \ "  i / a / o     - Insert/append/new line",
        \ "  dd            - Delete line",
        \ "  p             - Paste",
        \ "  :w            - Save file",
        \ "",
        \ "Terminal:",
        \ "  C-z           - Shell background",
        \ "  C-l           - New terminal",
        \ "  C-]           - Back to editing",
        \ ]
    call popup_create(help, {'line': 5, 'col': 10, 'border': [], 'highlight': 'Normal', 'maxwidth': 60})
endfunction

" Function to jump to next level
function! NextLesson()
    let current_file = expand('%:p')
    if current_file =~ 'level-\d\+/lesson.md'
        let level = str2nr(matchstr(current_file, 'level-\zs\d\+'))
        let next_level = level + 1
        if next_level <= 7
            let next_file = substitute(current_file, 'level-' . level . '/', 'level-' . next_level . '/', '')
            if filereadable(next_file)
                execute 'edit ' . next_file
                echo 'Moved to Level ' . next_level
            else
                echo 'No next level found'
            endif
        else
            echo 'Already at final level!'
        endif
    else
        echo 'Could not determine current level'
    endif
endfunction

" Function to jump to previous level
function! PrevLesson()
    let current_file = expand('%:p')
    if current_file =~ 'level-\d\+/lesson.md'
        let level = str2nr(matchstr(current_file, 'level-\zs\d\+'))
        let prev_level = level - 1
        if prev_level >= 1
            let prev_file = substitute(current_file, 'level-' . level . '/', 'level-' . prev_level . '/', '')
            if filereadable(prev_file)
                execute 'edit ' . prev_file
                echo 'Moved to Level ' . prev_level
            else
                echo 'No previous level found'
            endif
        else
            echo 'Already at first level!'
        endif
    else
        echo 'Could not determine current level'
    endif
endfunction

" Function to show current lesson info
function! LessonInfo()
    let current = expand('%:p')
    let matches = matchlist(current, '.*/\(stage-\d\+\)/level-\(\d\+\)')
    if len(matches) > 0
        echo 'Stage: ' . matches[1] . ' | Level: ' . matches[2] . '/7'
    endif
endfunction

" Function to mark lesson complete
function! LessonMarkComplete()
    let line = 'COMPLETED at: ' . strftime('%Y-%m-%d %H:%M:%S')
    call append(line('$'), line)
    echo 'Lesson marked complete!'
endfunction

" Function to toggle read-only on current buffer
function! ToggleReadOnly()
    if &readonly
        set noreadonly
        echo "Buffer is now editable"
    else
        set readonly
        echo "Buffer is now read-only"
    endif
endfunction

" ========== KEYMAPPINGS FOR LEARNING ==========

" Quick navigation between windows
nnoremap <C-h> <C-w>h           " Ctrl-h to go left
nnoremap <C-l> <C-w>l           " Ctrl-l to go right
nnoremap <C-j> <C-w>j           " Ctrl-j to go down
nnoremap <C-k> <C-w>k           " Ctrl-k to go up

" Quick window resizing
nnoremap <C-=> <C-w>=           " Equal width
nnoremap <C-+> <C-w>>           " Wider
nnoremap <C-_> <C-w><           " Narrower

" Lesson navigation
nnoremap <leader>n :call NextLesson()<CR>
nnoremap <leader>p :call PrevLesson()<CR>
nnoremap <leader>i :call LessonInfo()<CR>
nnoremap <leader>? :call ShowLessonHelp()<CR>

" Toggle read-only mode
nnoremap <leader>ro :call ToggleReadOnly()<CR>

" Mark lesson complete
nnoremap <leader>m :call LessonMarkComplete()<CR>

" Quick terminal
nnoremap <leader>t :terminal<CR>

" Quick save in code window
nnoremap <leader>w :w<CR>

" Quick search navigation
nnoremap <leader>/ /
nnoremap <leader>? ?

" ========== STATUS LINE ==========

" Show useful info in status line
set laststatus=2
set statusline=%f\ %m\ \|\ %l:%c\ \|\ %{&fileencoding}\ %Y

" ========== ABBREVIATIONS FOR TEMPLATES ==========

" Common C template
iabbrev <buffer> <buffer> _C_MAIN int main() {<CR>    return 0;<CR>}<Esc>

" Common Rust template
iabbrev <buffer> <buffer> _RUST_MAIN fn main() {<CR>    println!(\"Hello!\");<CR>}<Esc>

" ========== AUTO COMMANDS ==========

" Create a split for blank canvas when opening lesson files (done after VimEnter for safety)
autocmd VimEnter **/stage-*/level-*/lesson.md vsplit | enew | wincmd h

" Make lesson files read-only by default
autocmd BufRead **/stage-*/level-*/lesson.md setlocal readonly nomodifiable

" Highlight certain patterns in lesson files (commented out - can cause decoration issues)
" autocmd BufRead **/stage-*/level-*/lesson.md highlight LessonGoals ctermfg=Green
" autocmd BufRead **/stage-*/level-*/lesson.md highlight LessonCode ctermfg=Yellow

" ========== CONVENIENCE COMMANDS ==========

" :LessonMode to enter learning mode for a specific lesson
command! -nargs=+ LessonMode execute 'vsplit <args>' | wincmd l | execute 'edit ../solution.c' | wincmd =

" ========== INIT COMPLETE ==========

echo "Learning Mode initialized! Use Ctrl-h/l to move between windows."
echo "Use :LessonNav to see quick commands, or :help for more."

