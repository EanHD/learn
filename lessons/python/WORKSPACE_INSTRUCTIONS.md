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
├── python/                          # Original lessons (READ-ONLY)
│   ├── stage-1-copying-code/
│   ├── TABLE_OF_CONTENTS.md
│   └── ...
│
└── my-practice/                    # Your working copies
    ├── level-1-hello-world/
    │   ├── lesson.md              # Copied from original
    │   ├── hello.py               # Your working code
    │   └── my_notes.txt          # Your personal notes
    ├── level-2-variables/
    └── ...
```

### Option 2: Lesson-Specific Folders
```
LEARN/
├── python/                          # Original lessons
└── practice-sessions/              # Working directories
    ├── session-1-hello-world/
    │   ├── original-lesson.md     # Copied lesson
    │   ├── hello.py               # Your code
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
mkdir my-python-practice
cd my-python-practice

# Create subdirectories for each level
mkdir level-1-hello-world level-2-variables level-3-basic-math
mkdir level-4-user-input level-5-conditionals level-6-loops
mkdir level-7-functions
```

**Using File Explorer:**
1. Open your file explorer
2. Navigate to the `LEARN` directory
3. Create a new folder called `my-python-practice`
4. Inside it, create 7 subfolders: `level-1-hello-world` through `level-7-functions`

---

### Step 2: Copy Lesson Files

#### Method A: Copy Individual Lessons (Recommended)

**For Level 1:**
```bash
# Copy the lesson file
cp ../python/stage-1-copying-code/level-1-hello-world/lesson.md level-1-hello-world/

# Copy any code templates if they exist
cp ../python/stage-1-copying-code/level-1-hello-world/*.py level-1-hello-world/ 2>/dev/null || true
```

**For All Levels (Automated):**
```bash
# Copy all lesson files at once
for level in level-1-hello-world level-2-variables level-3-basic-math level-4-user-input level-5-conditionals level-6-loops level-7-functions; do
    mkdir -p "$level"
    cp "../python/stage-1-copying-code/$level/lesson.md" "$level/" 2>/dev/null || echo "Warning: Could not copy $level lesson"
done
```

#### Method B: Copy Entire Stage Folder

```bash
# Copy the entire stage (creates a backup)
cp -r python/stage-1-copying-code my-stage-1-backup

# Then work in the backup folder
cd my-stage-1-backup
```

#### Method C: Using File Explorer

1. Open two file explorer windows
2. Left window: `LEARN/python/stage-1-copying-code/`
3. Right window: `LEARN/my-python-practice/`
4. Copy `lesson.md` from each level folder to corresponding practice folder

---

### Step 3: Create Working Code Files

**For Each Level:**
```bash
# Navigate to level directory
cd level-1-hello-world

# Create your working code file
touch hello.py

# Open in your editor
vim hello.py        # or code hello.py, or your preferred editor
```

**Template for Each Level:**
```bash
# Create standard files for each lesson
cd level-1-hello-world
touch hello.py
touch notes.txt
touch experiments.py

cd ../level-2-variables
touch variables.py
touch notes.txt
touch experiments.py

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
    vim hello.py          # Create your code file
    # Copy code from lesson.md into hello.py
    ```

3. **Compile and Test:**
    ```bash
    python3 hello.py
    ```

4. **Experiment and Take Notes:**
    ```bash
    vim notes.txt        # Record what you learned
    vim experiments.py    # Try modifications
    ```

### File Organization Tips

**Keep your workspace clean:**
```
level-1-hello-world/
├── lesson.md          # Original lesson (READ-ONLY)
├── hello.py           # Your main working code
├── experiments.py     # Code experiments
├── notes.txt         # Your learning notes
├── backup.py          # Backup of working version
└── test_output.txt   # Program outputs
```

**Version control your work:**
```bash
# Initialize git in your practice folder
cd my-python-practice
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

**Install Python Interpreter:**
```bash
# Check if Python is installed
python3 --version

# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3

# macOS (usually pre-installed)
python3 --version

# Windows: Download from python.org
```

**Recommended Editors:**
- **Vim**: `vim filename.py`
- **VS Code**: `code filename.py`
- **Sublime Text**: `subl filename.py`

### Run Commands

**Basic Execution:**
```bash
python3 program.py
```

**With Python 2 compatibility check:**
```bash
python3 -m py_compile program.py
python3 program.py
```

**Interactive Python:**
```bash
python3 -i
# Or just: python3
```

---

## Progress Tracking

### Manual Progress Updates

**Update the Table of Contents:**
```bash
# Edit your progress
vim ../python/TABLE_OF_CONTENTS.md

# Mark lessons as completed
# Change [ ] to [x] for completed lessons
```

**Create Progress Log:**
```bash
# Daily progress tracking
echo "$(date): Completed Level 1 - Hello World" >> progress.log
echo "$(date): Learned print() function" >> progress.log
```

### Automated Progress Tracking

**Simple Progress Script:**
```bash
# !/bin/bash
# progress.sh

echo "=== Python Learning Progress ==="
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

**"python3: command not found" when running:**
```bash
# Install Python
sudo apt-get install python3

# Or use python instead of python3
python --version
python program.py
```

**Syntax errors:**
```bash
# Check for common issues
cat hello.py

# Common fixes:
# - Missing colon after if/for/def
# - Wrong indentation (use spaces or tabs consistently)
# - Missing quotes around strings
# - Wrong function name (print vs println)
```

**Indentation errors:**
```bash
# Python requires consistent indentation
# Use 4 spaces or tabs, but not both
python3 -m py_compile hello.py  # Check for syntax errors
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
4. Try running simpler test cases first

---

## Best Practices

### Code Organization
- [ ] Keep original lessons separate from working code
- [ ] Use meaningful filenames (`hello_v2.py`, `experiment_loops.py`)
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
1. Install Python extension
2. Configure Python interpreter
3. Set up debugging with Python debugger

**Vim Advanced Setup:**
```vim
" Add to .vimrc for Python development
autocmd FileType python setlocal tabstop=4 shiftwidth=4 expandtab
autocmd FileType python nnoremap <F5> :w<CR>:!python3 %<CR>
autocmd FileType python setlocal makeprg=python3\ -m\ py_compile\ %
```

### Virtual Environments

**Using venv:**
```bash
# Create virtual environment
python3 -m venv myenv

# Activate
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows

# Install packages
pip install package_name

# Deactivate
deactivate
```

---

## Support Resources

### Getting Help
- **Lesson Answer Keys**: Check bottom of each lesson file
- **Runtime Errors**: Compare with working examples
- **Concept Questions**: Re-read relevant lesson sections
- **Stuck on Code**: Try simpler test cases first

### External Resources
- **Python Documentation**: https://docs.python.org/3/
- **Python Tutorial**: https://docs.python.org/3/tutorial/
- **Practice Sites**: LeetCode, HackerRank, CodeSignal
- **Communities**: Stack Overflow, Reddit r/learnpython

---

## Success Checklist

**Workspace Setup:**
- [ ] Created separate practice directory
- [ ] Copied lesson files safely
- [ ] Set up development environment
- [ ] Tested Python execution works

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

*Remember: The goal is learning, not perfection. Every error message is a learning opportunity! Keep practicing and you'll master Python programming. *