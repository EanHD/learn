# Workspace Setup Instructions
## How to Copy Lessons for Safe Practice

### Why Copy Lessons?

The lesson files in this curriculum are **read-only educational materials**. They contain:
-  Complete working code examples
-  Detailed explanations and answer keys
-  Professional formatting and structure

** NEVER edit the original lesson files!** Instead, create working copies where you can:
- Experiment with code modifications
- Add your own comments and notes
- Make mistakes without ruining the lesson
- Practice without fear of breaking anything

---

## Recommended Workspace Structure

### Option 1: Separate Practice Folder
```
LEARN/
├── c-c++/                          # Original lessons (READ-ONLY)
│   ├── stage-1-copying-code/
│   ├── TABLE_OF_CONTENTS.md
│   └── ...
│
└── my-practice/                    # Your working copies
    ├── level-1-hello-world/
    │   ├── lesson.md              # Copied from original
    │   ├── hello.c               # Your working code
    │   └── my_notes.txt          # Your personal notes
    ├── level-2-variables/
    └── ...
```

### Option 2: Lesson-Specific Folders
```
LEARN/
├── c-c++/                          # Original lessons
└── practice-sessions/              # Working directories
    ├── session-1-hello-world/
    │   ├── original-lesson.md     # Copied lesson
    │   ├── hello.c               # Your code
    │   └── experiments/          # Additional experiments
    ├── session-2-variables/
    └── ...
```

---

## Step-by-Step Setup Instructions

### Step 1: Create Your Practice Directory

**Using Terminal/Command Line:**
```bash
# Navigate to the LEARN directory
cd /path/to/LEARN

# Create a practice workspace
mkdir my-c-practice
cd my-c-practice

# Create subdirectories for each level
mkdir level-1-hello-world level-2-variables level-3-basic-math
mkdir level-4-user-input level-5-conditionals level-6-loops
mkdir level-7-functions
```

**Using File Explorer:**
1. Open your file explorer
2. Navigate to the `LEARN` directory
3. Create a new folder called `my-c-practice`
4. Inside it, create 7 subfolders: `level-1-hello-world` through `level-7-functions`

---

### Step 2: Copy Lesson Files

#### Method A: Copy Individual Lessons (Recommended)

**For Level 1:**
```bash
# Copy the lesson file
cp ../c-c++/stage-1-copying-code/level-1-hello-world/lesson.md level-1-hello-world/

# Copy any code templates if they exist
cp ../c-c++/stage-1-copying-code/level-1-hello-world/*.c level-1-hello-world/ 2>/dev/null || true
```

**For All Levels (Automated):**
```bash
# Copy all lesson files at once
for level in level-1-hello-world level-2-variables level-3-basic-math level-4-user-input level-5-conditionals level-6-loops level-7-functions; do
    mkdir -p "$level"
    cp "../c-c++/stage-1-copying-code/$level/lesson.md" "$level/" 2>/dev/null || echo "Warning: Could not copy $level lesson"
done
```

#### Method B: Copy Entire Stage Folder

```bash
# Copy the entire stage (creates a backup)
cp -r c-c++/stage-1-copying-code my-stage-1-backup

# Then work in the backup folder
cd my-stage-1-backup
```

#### Method C: Using File Explorer

1. Open two file explorer windows
2. Left window: `LEARN/c-c++/stage-1-copying-code/`
3. Right window: `LEARN/my-c-practice/`
4. Copy `lesson.md` from each level folder to corresponding practice folder

---

### Step 3: Create Working Code Files

**For Each Level:**
```bash
# Navigate to level directory
cd level-1-hello-world

# Create your working code file
touch hello.c

# Open in your editor
vim hello.c        # or code hello.c, or your preferred editor
```

**Template for Each Level:**
```bash
# Create standard files for each lesson
cd level-1-hello-world
touch hello.c
touch notes.txt
touch experiments.c

cd ../level-2-variables
touch variables.c
touch notes.txt
touch experiments.c

# ... repeat for each level
```

---

## Working with Your Copies

### Daily Workflow

1. **Read the Lesson:**
   ```bash
   cd level-1-hello-world
   vim lesson.md        # Read the copied lesson
   ```

2. **Create Working Code:**
   ```bash
   vim hello.c          # Create your code file
   # Copy code from lesson.md into hello.c
   ```

3. **Compile and Test:**
   ```bash
   gcc hello.c -o hello
   ./hello
   ```

4. **Experiment and Take Notes:**
   ```bash
   vim notes.txt        # Record what you learned
   vim experiments.c    # Try modifications
   ```

### File Organization Tips

**Keep your workspace clean:**
```
level-1-hello-world/
├── lesson.md          # Original lesson (READ-ONLY)
├── hello.c           # Your main working code
├── experiments.c     # Code experiments
├── notes.txt         # Your learning notes
├── backup.c          # Backup of working version
└── test_output.txt   # Program outputs
```

**Version control your work:**
```bash
# Initialize git in your practice folder
cd my-c-practice
git init
git add .
git commit -m "Initial setup with lesson copies"

# Commit after each lesson
git add level-1-hello-world/
git commit -m "Completed Level 1: Hello World"
```

---

## Development Environment Setup

### Essential Tools

**Install GCC Compiler:**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install gcc

# macOS
xcode-select --install

# Windows: Install MinGW or use WSL
```

**Recommended Editors:**
- **Vim**: `vim filename.c`
- **VS Code**: `code filename.c`
- **Sublime Text**: `subl filename.c`

### Build Commands

**Basic Compilation:**
```bash
gcc program.c -o program
./program
```

**With Warnings:**
```bash
gcc -Wall -Wextra program.c -o program
```

**Debug Build:**
```bash
gcc -g program.c -o program
gdb ./program
```

---

## Progress Tracking

### Manual Progress Updates

**Update the Table of Contents:**
```bash
# Edit your progress
vim ../c-c++/TABLE_OF_CONTENTS.md

# Mark lessons as completed
# Change [ ] to [x] for completed lessons
```

**Create Progress Log:**
```bash
# Daily progress tracking
echo "$(date): Completed Level 1 - Hello World" >> progress.log
echo "$(date): Learned printf() and basic compilation" >> progress.log
```

### Automated Progress Tracking

**Simple Progress Script:**
```bash
# !/bin/bash
# progress.sh

echo "=== C/C++ Learning Progress ==="
echo "Date: $(date)"
echo ""

completed=0
total=7

for level in level-1-hello-world level-2-variables level-3-basic-math level-4-user-input level-5-conditionals level-6-loops level-7-functions; do
    if [ -f "$level/notes.txt" ] && [ -s "$level/notes.txt" ]; then
        echo " $level - COMPLETED"
        ((completed++))
    else
        echo "⏳ $level - IN PROGRESS"
    fi
done

echo ""
echo "Progress: $completed/$total levels completed ($((completed*100/total))%)"
```

---

## Troubleshooting

### Common Issues

**"Permission denied" when compiling:**
```bash
# Make sure you're in the right directory
pwd
ls -la

# Check file permissions
chmod +x hello.c  # Not needed for .c files
gcc hello.c -o hello
```

**"No such file or directory":**
```bash
# Check if file exists
ls -la hello.c

# Check current directory
pwd

# Navigate correctly
cd level-1-hello-world
```

**Compilation errors:**
```bash
# Check for typos in code
cat hello.c

# Common fixes:
# - Missing semicolon
# - Wrong quotes (" vs ')
# - Missing include
# - Wrong function name
```

### Getting Help

**Check the Original Lesson:**
- Answer keys are at the bottom of each lesson
- Common errors and solutions included
- Detailed explanations provided

**Debugging Steps:**
1. Read the error message carefully
2. Check line numbers mentioned
3. Compare with working examples in lesson
4. Try compiling simpler versions first

---

## Best Practices

### Code Organization
- [ ] Keep original lessons separate from working code
- [ ] Use meaningful filenames (`hello_v2.c`, `experiment_loops.c`)
- [ ] Comment your experimental code
- [ ] Save working versions before major changes

### Learning Habits
- [ ] Read lessons completely before coding
- [ ] Take notes on concepts you find difficult
- [ ] Experiment with code modifications
- [ ] Review completed lessons periodically
- [ ] Don't rush - understanding > speed

### Backup Strategy
- [ ] Commit to git after each successful lesson
- [ ] Keep backup copies of working code
- [ ] Don't overwrite working versions
- [ ] Save different approaches for comparison

---

## Advanced Setup (Optional)

### Integrated Development Environment

**VS Code Setup:**
1. Install C/C++ extension
2. Configure tasks.json for building
3. Set up debugging with gdb

**Vim Advanced Setup:**
```vim
" Add to .vimrc for C/C++ development
autocmd FileType c,cpp setlocal tabstop=4 shiftwidth=4 expandtab
autocmd FileType c,cpp nnoremap <F5> :w<CR>:!gcc % -o %< && ./%<<CR>
autocmd FileType c,cpp setlocal makeprg=gcc\ -Wall\ -o\ %<\ %
```

### Build Systems

**Simple Makefile:**
```makefile
CC=gcc
CFLAGS=-Wall -Wextra -g

all: hello variables math input conditionals loops functions

hello: level-1-hello-world/hello.c
    $(CC) $(CFLAGS) $< -o $@

variables: level-2-variables/variables.c
    $(CC) $(CFLAGS) $< -o $@

# ... add rules for other programs

clean:
    rm -f */*.o hello variables math input conditionals loops functions
```

---

## Support Resources

### Getting Help
- **Lesson Answer Keys**: Check bottom of each lesson file
- **Compilation Errors**: Compare with working examples
- **Concept Questions**: Re-read relevant lesson sections
- **Stuck on Code**: Try simpler test cases first

### External Resources
- **C Reference**: `man gcc`, `man printf`
- **Online Communities**: Stack Overflow, Reddit r/learnprogramming
- **Practice Sites**: LeetCode, HackerRank, CodeSignal
- **Documentation**: cppreference.com, cprogramming.com

---

## Success Checklist

**Workspace Setup:**
- [ ] Created separate practice directory
- [ ] Copied lesson files safely
- [ ] Set up development environment
- [ ] Tested compilation works

**Learning Habits:**
- [ ] Read lessons before coding
- [ ] Take personal notes
- [ ] Experiment with modifications
- [ ] Track progress regularly

**Code Management:**
- [ ] Keep originals and working copies separate
- [ ] Use version control
- [ ] Backup working code
- [ ] Document experiments

---

*Remember: The goal is learning, not perfection. Every compilation error is a learning opportunity! Keep practicing and you'll master C/C++ programming. *