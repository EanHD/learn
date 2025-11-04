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

" Function to detect language from file type or path
function! DetectLanguage()
    let current_file = expand('%:p')
    " Check file type
    if &filetype != ''
        return &filetype
    endif
    " Try to detect from path
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

" Function to get run command for current language
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
    return get(commands, lang, 'No run command defined for this language')
endfunction

" Function to show quick navigation help (dynamic based on language)
function! ShowLessonHelp()
    let run_cmd = GetRunCommand()
    let lang = DetectLanguage()
    let help = [
        \ "=== " . toupper(lang) . " LESSON NAVIGATION ===",
        \ "",
        \ "RUN CODE:",
        \ "  <Space>r      - Run: " . run_cmd,
        \ "",
        \ "Window Movement:",
        \ "  C-h / C-l     - Left/Right windows",
        \ "  C-j / C-k     - Down/Up windows",
        \ "  C-= / C-+ / C-- - Resize windows",
        \ "",
        \ "Lesson Navigation:",
        \ "  <Space>n      - Next lesson (switches to code)",
        \ "  <Space>p      - Previous lesson (switches to code)",
        \ "  gg            - Top of lesson",
        \ "  G             - Bottom of lesson",
        \ "  /text         - Search forward",
        \ "  ?text         - Search backward",
        \ "",
        \ "Editing (code window):",
        \ "  i / a / o     - Insert/append/new line",
        \ "  dd            - Delete line",
        \ "  p             - Paste",
        \ "  <Space>w      - Save file",
        \ "",
        \ "Other:",
        \ "  <Space>i      - Lesson info",
        \ "  <Space>m      - Mark complete",
        \ ]
    call popup_create(help, {'line': 3, 'col': 5, 'border': [], 'highlight': 'Normal', 'maxwidth': 70})
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
                wincmd l                " Switch to code window
                echo 'Moved to Level ' . next_level . ' - Code window active'
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
                wincmd l                " Switch to code window
                echo 'Moved to Level ' . prev_level . ' - Code window active'
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
nnoremap <leader>h :call ShowLessonHelp()<CR>
nnoremap <leader>? :call ShowLessonHelp()<CR>

" Run current code
nnoremap <leader>r :execute '!'.GetRunCommand()<CR>

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

