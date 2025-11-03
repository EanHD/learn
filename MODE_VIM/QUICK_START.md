# QUICK START: Vim Mode in 5 Minutes

Get your Neovim learning environment running **right now**.

## Step 1: Copy the Learning Config (1 minute)

```bash
# Create config directory if needed
mkdir -p ~/.config/nvim

# Copy the learning-optimized config
cp MODE_VIM/CONFIG/init.vimrc-learning ~/.config/nvim/init-learning.vim
```

## Step 2: Open Your First Lesson (2 minutes)

```bash
# Navigate to your lessons
cd ~/LEARN

# Open Neovim with learning config
nvim -u init-learning.vim c-c++/stage-1/level-1/lesson.md
```

You'll see the lesson in a nice, readable format with:
- Proper syntax highlighting
- Line numbers (for referencing code)
- Good colors for reading
- Vim optimizations for learning

## Step 3: Set Up Your Split Screen (2 minutes)

**You're now in Neovim with the lesson open. Do this:**

```vim
" Create a vertical split for your code file
:vsplit ../../../solution.c

" Make both windows visible and equal size
:wincmd =

" Go to right window (code editor)
:wincmd l

" Insert a basic template
:read MODE_VIM/TEMPLATES/code-template.c
```

**What you see now:**

```

 
 Lesson (READ) Code (EDIT) 
 
 Learning Goals #include <stdio.h> 
 - Understand... 
 - Learn how... int main() { 
 // Your code 
 Key Concepts: return 0; 
 - Variables are... } 
 

```

## Step 4: Start Coding (optional, but fun)

While viewing the lesson on the left, code on the right:

```vim
" You're in the right buffer (code editor)
" Type your solution based on the lesson

i
// My solution starts here
printf("Hello, World!\n");

" Save when done
:w

" Switch to left window to review concepts
C-w h

" Search for a specific concept in the lesson
/important_concept

" Back to coding
C-w l

" Compile and test
:terminal
gcc solution.c -o solution && ./solution
```

## Essential Commands You'll Use

**Navigation:**
- `C-w l` → Move to right window (code)
- `C-w h` → Move to left window (lesson)
- `C-w =` → Make windows equal width
- `gg` → Jump to top of lesson
- `G` → Jump to bottom of lesson

**Searching:**
- `/pattern` → Search forward in lesson
- `?pattern` → Search backward
- `n` → Next match
- `N` → Previous match

**Editing (right window only):**
- `i` → Insert mode
- `a` → Append
- `dd` → Delete line
- `p` → Paste
- `:w` → Save file

**Terminal:**
- `:terminal` → Open a terminal buffer
- `gcc solution.c -o solution && ./solution` → Compile and run

---

## Your First 15-Minute Learning Session

```bash
# 1. Start (30 seconds)
cd ~/LEARN
nvim -u init-learning.vim c-c++/stage-1/level-1/lesson.md

# 2. Inside Neovim (15 minutes of this):
:vsplit ../../../solution.c " Split screen
:wincmd = " Equal sizing
:wincmd l " Focus code side

# 3. Read the lesson on the left
C-w h " Go left
/Learning Goals " Find section
gg " Go to top
G " Go to bottom

# 4. Write code on the right
C-w l " Go right
i " Start typing
" ... write your code based on lesson ...
:w " Save

# 5. Test it
:terminal " Open terminal
gcc solution.c -o solution && ./solution " Run code
exit " Close terminal

# 6. Done!
" You just learned programming + Vim simultaneously 
```

---

## Customizing Your Config

The `init-learning.vim` includes good defaults, but you can customize:

```bash
# View/edit the learning config
nvim ~/.config/nvim/init-learning.vim

# Some key settings already enabled:
set number # Line numbers
set relativenumber # Relative line numbers (jump '5j' for 5 lines)
set colorcolumn=80 # Visual guide at 80 chars
set cursorline # Highlight current line
set scrolloff=5 # Keep 5 lines visible when scrolling
set hlsearch # Highlight search results
set ignorecase # Case-insensitive search
```

---

## Troubleshooting

**Q: Init file not found?**
```bash
# Make sure you're in the right directory
pwd # Should show: /home/your-user/LEARN

# Try absolute path
nvim -u ~/.config/nvim/init-learning.vim c-c++/stage-1/level-1/lesson.md
```

**Q: Lesson looks ugly/hard to read?**
```bash
# Try with your regular Neovim config + learning tweaks
nvim c-c++/stage-1/level-1/lesson.md

# Then in Vim:
:set readonly " Make lesson read-only
:set colorcolumn=
:set number
```

**Q: Can't compile?**
```bash
# Make sure GCC is installed
gcc --version

# If not:
sudo apt install build-essential # Ubuntu/Debian
brew install gcc # macOS
```

**Q: Want to use Rust instead?**
```vim
:vsplit ../../../solution.rs
" Then compile with:
:terminal
rustc solution.rs -o solution && ./solution
```

---

## Next Level: Add These to Your Workflow

Once you're comfortable, try:

1. **Macros** — Record complex edits:
 ```vim
 qa " Start recording macro 'a'
 " ... your commands ...
 q " Stop
 @a " Play macro 'a'
 ```

2. **Marks** — Jump back to important concepts:
 ```vim
 ma " Mark current position 'a'
 `a " Jump back to mark 'a'
 ```

3. **Buffers** — Keep multiple files open:
 ```vim
 :e another-file.c " Edit another file
 :bn / :bp " Next/previous buffer
 C-^ " Toggle between last two buffers
 ```

4. **Session Management** — Save your workspace:
 ```vim
 :mksession lesson1.vim " Save current session
 nvim -S lesson1.vim " Restore later
 ```

---

## Learn More

- **More workflows:** See [WORKFLOWS/](WORKFLOWS/) folder
- **Vim tips:** See [TIPS/](TIPS/) folder 
- **Advanced setups:** Check [CONFIG/](CONFIG/) for example configs
- **Language-specific:** See [c-c++/](c-c++/) or [rust/](rust/) folders

---

## Checklist

- [ ] Config copied to ~/.config/nvim/init-learning.vim
- [ ] Can open lesson with `nvim -u ~/.config/nvim/init-learning.vim`
- [ ] Can create vertical split with `:vsplit solution.c`
- [ ] Can navigate between windows with `C-w h/l`
- [ ] Can open terminal with `:terminal`
- [ ] Can compile and run code
- [ ] Ready to start learning! 

---

**Stuck?** Check the [FAQ](FAQ.md) or see [WORKFLOWS/](WORKFLOWS/) for more detailed guides.

**Ready to learn?** Open `c-c++/stage-1/level-1/lesson.md` and start! 

