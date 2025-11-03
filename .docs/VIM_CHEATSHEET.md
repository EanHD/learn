# Vim Cheatsheet for Programming
## Essential Commands for C/C++ Development

### Why Vim for Programming?
Vim is a powerful text editor that keeps your hands on the keyboard, making coding faster and more efficient. This cheatsheet focuses on commands you'll use daily when programming in C/C++.

---

## Quick Start

### Opening Files
```bash
vim filename.c          # Open file
vim -O file1.c file2.c  # Open files side-by-side
vim +10 filename.c      # Open file at line 10
```

### Vim Modes
- **Normal Mode**: Default mode for navigation and commands (press `Esc`)
- **Insert Mode**: For typing text (`i`, `a`, `o`, etc.)
- **Visual Mode**: For selecting text (`v`, `V`, `Ctrl+v`)
- **Command Mode**: For executing commands (`:`)

---

## ⌨ Essential Movement Commands

### Basic Movement (Normal Mode)
```
h     ←    Left
j     ↓    Down
k     ↑    Up
l     →    Right

0          Beginning of line
$          End of line
gg         Beginning of file
G          End of file
```

### Word Movement
```
w          Next word
b          Previous word
e          End of word

W, B, E    Same but ignore punctuation
```

### Line Movement
```
10j        Down 10 lines
5k         Up 5 lines
:10        Go to line 10
```

### Screen Movement
```
Ctrl+u     Up half screen
Ctrl+d     Down half screen
Ctrl+b     Up full screen
Ctrl+f     Down full screen

H          Top of screen
M          Middle of screen
L          Bottom of screen
```

---

## Editing Commands

### Insert Mode Entry
```
i          Insert before cursor
a          Append after cursor
I          Insert at beginning of line
A          Append at end of line

o          Open new line below
O          Open new line above
```

### Deleting Text
```
x          Delete character under cursor
X          Delete character before cursor

dd         Delete entire line
5dd        Delete 5 lines

dw         Delete word
d$         Delete to end of line
d0         Delete to beginning of line

D          Delete to end of line (same as d$)
```

### Copying (Yanking) and Pasting
```
yy         Yank (copy) current line
5yy        Yank 5 lines

yw         Yank word
y$         Yank to end of line

p          Paste after cursor
P          Paste before cursor
```

### Undo/Redo
```
u          Undo last change
Ctrl+r     Redo last undone change

U          Undo all changes to current line
```

---

## Search and Replace

### Searching
```
/pattern   Search forward for pattern
?pattern   Search backward for pattern

n          Next occurrence
N          Previous occurrence

*          Search for word under cursor
# Search backward for word under cursor
```

### Search and Replace
```
:s/old/new/           Replace first occurrence in line
:s/old/new/g          Replace all occurrences in line
:%s/old/new/g         Replace all occurrences in file
:%s/old/new/gc        Replace all with confirmation

:.,$s/old/new/g       Replace from current line to end
:1,10s/old/new/g      Replace lines 1-10
```

### Case Sensitivity
```
:set ignorecase       Ignore case in searches
:set noignorecase     Case sensitive searches
```

---

## Visual Mode Selections

### Visual Mode Entry
```
v          Character-wise visual mode
V          Line-wise visual mode
Ctrl+v     Block-wise visual mode
```

### Visual Mode Operations
```
d          Delete selection
y          Yank selection
c          Change selection
>          Indent selection
<          Unindent selection
```

---

## Programming-Specific Commands

### Code Navigation
```
%          Jump to matching bracket: (), [], {}
gd         Go to definition (local)
gD         Go to global definition

]]         Next function start
[[         Previous function start
```

### Indentation
```
>>         Indent current line
<<         Unindent current line
==         Auto-indent current line

5>>        Indent 5 lines
```

### Comments (C/C++ specific)
```
gcc        Comment/uncomment current line
5gcc       Comment/uncomment 5 lines
```

*Note: Comment commands require vim-commentary plugin*

---

## File Operations

### Saving and Quitting
```
:w         Write (save) file
:wq        Write and quit
:x         Write and quit (same as :wq)
:q         Quit (fails if unsaved)
:q!        Quit without saving
:wq!       Force write and quit

ZZ         Write and quit (same as :wq)
ZQ         Quit without saving (same as :q!)
```

### Multiple Files
```
:ls        List open buffers
:bnext     Next buffer
:bprev     Previous buffer
:buffer N  Switch to buffer N

:split     Horizontal split
:vsplit    Vertical split
Ctrl+w w   Switch between splits
Ctrl+w q   Close current split
```

---

## Useful Commands for Programming

### Line Operations
```
J          Join current line with next
gJ         Join without adding space

.          Repeat last command
;          Repeat last f/F/t/T command
,          Repeat last f/F/t/T command backward
```

### Case Changes
```
~          Toggle case of character
guu        Make line lowercase
gUU        Make line uppercase
g~~        Toggle case of line
```

### Number Operations
```
Ctrl+a     Increment number under cursor
Ctrl+x     Decrement number under cursor
```

---

## Configuration for Programming

### Essential .vimrc Settings
```vim
syntax on                    " Syntax highlighting
set number                   " Line numbers
set relativenumber           " Relative line numbers
set autoindent               " Auto indentation
set smartindent              " Smart indentation
set tabstop=4                " Tab width
set shiftwidth=4             " Indentation width
set expandtab                " Use spaces instead of tabs
set hlsearch                 " Highlight search results
set incsearch                " Incremental search
set ignorecase               " Case insensitive search
set smartcase                " Case sensitive if uppercase used
set showmatch                " Show matching brackets
set cursorline               " Highlight current line
set background=dark          " Dark background
```

### C/C++ Specific Settings
```vim
autocmd FileType c,cpp setlocal tabstop=4 shiftwidth=4 expandtab
autocmd FileType c,cpp setlocal commentstring=//\ %s
autocmd FileType c,cpp setlocal makeprg=gcc\ -o\ %<\ %
```

---

## Advanced Commands

### Macros
```
qa         Start recording macro 'a'
q          Stop recording
@a         Play macro 'a'
@@         Repeat last macro
5@a        Play macro 'a' 5 times
```

### Marks
```
ma         Set mark 'a' at current position
`a         Jump to mark 'a'
'a         Jump to beginning of line with mark 'a'
:marks     List all marks
```

### Registers
```
"ayy       Yank current line to register 'a'
"ap        Paste from register 'a'
:registers List all registers
```

### Command History
```
:          Enter command mode
↑/↓        Navigate command history
q:         Open command history window
```

---

## Debugging Commands

### Syntax Checking
```
:make      Run make (compile)
:copen     Open quickfix window
:cnext     Next error
:cprev     Previous error
:clist     List all errors
```

### Spell Checking
```
:set spell    Enable spell checking
]s           Next misspelled word
[s           Previous misspelled word
z=           Suggestions for current word
zg           Add word to dictionary
```

---

## Learning Vim

### Getting Help
```
:help        General help
:help topic  Help on specific topic
:help i      Insert mode help
:help motion  Movement commands help
Ctrl+]       Follow link in help
Ctrl+T       Go back in help
```

### Vim Tutor
```bash
vimtutor    # Interactive Vim tutorial
```

### Practice Commands
```
vim filename.c
iHello World!<Esc>
:wq
```

---

## Vim for C/C++ Workflow

### Typical Programming Session
1. **Open file**: `vim program.c`
2. **Navigate**: Use `h/j/k/l` or search `/function_name`
3. **Edit**: Press `i` to insert, make changes
4. **Save**: `:w`
5. **Compile**: `:make` or `:terminal gcc program.c -o program`
6. **Test**: `:terminal ./program`
7. **Fix errors**: Use quickfix window `:copen`

### Efficient Coding Habits
- Stay in Normal mode as much as possible
- Use relative numbers for quick line jumps
- Learn to use `.` to repeat commands
- Master search and replace for refactoring
- Use macros for repetitive tasks

---

## Custom Commands for C/C++

### Compile and Run
Add to `.vimrc`:
```vim
autocmd FileType c,cpp nnoremap <F5> :w<CR>:!gcc % -o %< && ./%<<CR>
autocmd FileType c,cpp nnoremap <F6> :w<CR>:make<CR>
```

Now `F5` compiles and runs C/C++ programs!

### Header Guards
```vim
function! AddHeaderGuard()
    let guard = substitute(toupper(expand('%:t')), '\.', '_', 'g') . '_'
    call append(0, '#ifndef ' . guard)
    call append(1, '#define ' . guard)
    call append(line('$'), '#endif /* ' . guard . ' */')
endfunction
```

---

## Pro Tips

1. **Learn one command at a time** - Don't try to memorize everything
2. **Use Vim's help system** - `:help` is your best friend
3. **Practice daily** - Muscle memory takes time
4. **Customize your .vimrc** - Make Vim work for you
5. **Learn visual mode** - Great for refactoring
6. **Master search/replace** - Essential for programming
7. **Use plugins** - vim-commentary, vim-fugitive, etc.

### Common Mistakes to Avoid
- Forgetting to press `Esc` to exit insert mode
- Using arrow keys instead of `h/j/k/l`
- Not using search for navigation
- Overusing the mouse
- Not learning visual mode

---

## Practice Exercises

### Beginner
1. Open a C file and move around using `h/j/k/l`
2. Insert text at different positions (`i`, `a`, `I`, `A`)
3. Delete words and lines (`dw`, `dd`)
4. Search for a function name (`/main`)
5. Replace all occurrences of a variable (`:%s/old/new/g`)

### Intermediate
1. Use visual mode to select and modify code blocks
2. Record and play back a macro for repetitive tasks
3. Use marks to jump between important locations
4. Split windows and edit multiple files
5. Use the quickfix window for compilation errors

### Advanced
1. Set up custom key mappings for frequent tasks
2. Use Vim's built-in completion features
3. Integrate with external tools (ctags, cscope)
4. Create custom commands for project-specific tasks
5. Master Vim's regular expressions for complex searches

---

*Remember: Vim has a steep learning curve, but the productivity gains are worth it! Start with the basics and gradually add more commands to your repertoire.*

**Happy Vimming! **