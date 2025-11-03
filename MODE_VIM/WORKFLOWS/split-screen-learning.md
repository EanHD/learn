# Split-Screen Learning: Your Exact Workflow

This guide documents **exactly** the workflow you're already doing, but optimized for Neovim.

## The Setup You Want

```

 NEOVIM 

 
 lesson.md (LEFT) solution.c/rs (RIGHT) 
 
 
 Learning Goals #include <stdio.h> 
 
 - Understand variables int main() { 
 - Learn how to declare them // Your code here 
 - Practice with examples printf("Hello\n"); 
 return 0; 
 Key Concepts } 
 
 Variables are containers for... // Your testing happens 
 
 (keyboard navigation) (live editing) 
 - gg to top - Type your solution 
 - G to bottom - Compile when ready 
 - / to search - Tab to switch windows 
 - n to next match 
 

 :terminal 

 $ gcc solution.c -o solution && ./solution 
 Hello 
 $ 

```

## Step-by-Step: Your First Lesson

### 1. Start Neovim with Learning Config

```bash
cd ~/LEARN
nvim -u MODE_VIM/CONFIG/init-learning.vim c-c++/stage-1/level-1/lesson.md
```

**You'll see:**
- Lesson open in Neovim
- Line numbers enabled
- Good color scheme for reading
- Ready to split

### 2. Create the Split (VS Your Markdown Viewer)

Instead of opening a separate markdown viewer, use Neovim's split:

```vim
:vsplit
:wincmd l " Focus right window
:e ../../solution.c " Open/create code file
:wincmd = " Equal width
```

**Result:** You now have lesson and code side-by-side in ONE terminal window.

**Advantages:**
- No alt-tabbing between windows
- Both visible at all times
- Share clipboard between them
- Single terminal session
- Save window layout as a session

### 3. Navigate Lesson (Left Window)

You're viewing a lesson. Common navigation:

```vim
" Move to left window
C-h

" Jump to top
gg

" Search for concept
/Learning Goals

" Next occurrence
n

" Mark this spot for later review
ma

" Jump to next concept
}

" Go back to mark
'a

" View a specific line
:50 " Jump to line 50
```

### 4. Code (Right Window)

Read the concept on the left, implement on the right:

```vim
" Move to right window
C-l

" Enter insert mode and start coding
i

" Type your solution based on the lesson
#include <stdio.h>

int main() {
 printf("Hello, World!\n");
 return 0;
}

" Exit insert mode
Esc

" Save
:w

" Back to lesson to verify you understood
C-h
/important_concept
```

### 5. Compile and Test (Terminal)

When you want to test:

```vim
:terminal

$ gcc solution.c -o solution && ./solution
Hello, World!
$ 
```

You can now:
- See output immediately
- Edit code above it
- Edit lesson above terminal
- All in one window

### 6. Common Workflow Patterns

#### Pattern 1: Read → Code → Test

```vim
" Read section
C-h " Go left
/pattern " Find section
n n n " Read through examples

" Code it
C-l " Go right
i " Insert mode
" ... write code ...
Esc :w " Save

" Test it
:terminal
gcc solution.c -o solution && ./solution

" Fix if needed (back up and edit)
C-l
" Edit code
```

#### Pattern 2: Multiple Concepts (Using Marks)

```vim
" Read first concept
C-h
/Concept 1
ma " Mark A

" Read second concept
/Concept 2
mb " Mark B

" Code first concept
C-l
i
" ... code for concept 1 ...
Esc :w

" Review concept 1 again?
C-h
'a " Jump back to mark A

" Review concept 2?
'b " Jump to mark B
```

#### Pattern 3: Side-by-Side Comparison

```vim
" Lesson shows example on left
" You implement on right

C-h " Look at left
5j " Read example

C-l " Implement on right
i
" Type similar code but different values
Esc :w

" Compare?
C-h " Check example again
" ... verify your approach ...

C-l " Adjust if needed
```

## Pro Tips for Split-Screen Learning

### Tip 1: Window Sizing

```vim
" Make left window bigger (for reading)
20<C-w>> " Make right window 20 wider

" Make right window bigger (for coding)
20<C-w>< " Make right window 20 narrower

" Equal again
C-w =
```

### Tip 2: Maximize One Window Temporarily

```vim
" Focus on lesson
C-h
C-w _ " Maximize height of left

" Back to normal
C-w =

" Focus on code
C-l
C-w _ " Maximize height of right

" Back to normal
C-w =
```

### Tip 3: Use Buffers Instead of Splits

Some prefer buffers over splits:

```vim
" Instead of :vsplit, you could:
:e solution.c " Open in same window

" Switch between buffers
C-^ " Toggle between last two files
:bn / :bp " Next/previous buffer
:ls " List open buffers

" But splits are probably better for learning
```

### Tip 4: Save Your Layout as a Session

```vim
" After you set up your perfect layout:
:mksession my-lesson-session.vim

" Later, restore:
nvim -S my-lesson-session.vim

" Or within Vim:
:source my-lesson-session.vim
```

### Tip 5: Record Macros for Repeated Tasks

```vim
" Record: "Use 4-space tabs in code file"
qa " Start recording macro 'a'
:set tabstop=4
:set shiftwidth=4
:set expandtab
q " Stop recording

" Play it
@a " Play macro 'a'
```

## Your Ideal 1-Hour Learning Session

### Timeline

```
0:00 - 0:05 Open Neovim with split setup
0:05 - 0:15 Read Stage 1 Level 1 concepts
0:15 - 0:40 Code your solution based on lesson
0:40 - 0:50 Compile, test, fix bugs
0:50 - 0:55 Review: did you understand? Can you explain to someone?
0:55 - 1:00 Mark complete, save session
```

### Commands You'll Type

```bash
# Start
cd ~/LEARN
nvim -u MODE_VIM/CONFIG/init-learning.vim c-c++/stage-1/level-1/lesson.md

# Inside Vim (first time)
:vsplit ../../solution.c
:wincmd =
:set readonly " Make lesson read-only

# During learning
C-h " Jump to lesson
C-l " Jump to code
/pattern " Search lesson
n " Next match
i " Edit code
Esc :w " Save code

# Testing
:terminal
gcc solution.c -o solution && ./solution
exit

# Saving
:mksession lesson1-complete.vim
:wq
```

## Comparison: Your Old vs. New Workflow

### Before (Two Windows)
```

 Markdown Viewer Neovim 
 (Separate app) (Separate app) 
 Hard to sync Alt+Tab constantly 

```

### After (Vim Mode)
```

 NEOVIM (Single Application) 

 Lesson (Left) Code (Right) 
 Native Vim rendering Native Vim editing 
 Keyboard-driven Keyboard-driven 

 Terminal (Testing) 

```

**Improvements:**
- Single application (no context switching)
- Better window management
- Keyboard-driven (faster)
- Native Vim features (marks, macros, sessions)
- Terminal integration
- Vim learning as a bonus

## Next Steps

1. **Try it:** Follow "Your First Lesson" above
2. **Customize:** Adjust window sizes to your preference
3. **Optimize:** Use tips from "Pro Tips" section
4. **Master:** Add macros and marks to your workflow
5. **Accelerate:** Your Vim and programming skills grow together

## FAQ for This Workflow

**Q: Can I have more than 2 windows?** 
A: Yes! `:split` and `:vsplit` create more splits. But 2 is usually ideal for learning.

**Q: What if I mess up the code file?** 
A: Press `u` to undo. Vim has unlimited undo history.

**Q: How do I keep this layout consistent?** 
A: Save it as a session with `:mksession` and restore with `nvim -S`.

**Q: Can I use this with other languages?** 
A: Yes! Works with C, C++, Rust, Python, etc. Just change file extensions.

**Q: What if I want to compile Rust?** 
A: Use `:terminal` then `rustc solution.rs -o solution && ./solution`.

**Q: Can I use tmux instead?** 
A: Yes! But Vim splits are simpler for this use case.

---

**Ready?** Go to [QUICK_START.md](../QUICK_START.md) to set up your first session! 

