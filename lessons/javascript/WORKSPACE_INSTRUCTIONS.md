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
├── javascript/                          # Original lessons (READ-ONLY)
│   ├── stage-1-copying-code/
│   ├── TABLE_OF_CONTENTS.md
│   └── ...
│
└── my-js-practice/                    # Your working copies
    ├── level-1-hello-world/
    │   ├── lesson.md              # Copied from original
    │   ├── hello.js              # Your working code
    │   └── my_notes.txt          # Your personal notes
    ├── level-2-variables/
    └── ...
```

### Option 2: Lesson-Specific Folders
```
LEARN/
├── javascript/                          # Original lessons
└── practice-sessions/              # Working directories
    ├── session-1-hello-world/
    │   ├── original-lesson.md     # Copied lesson
    │   ├── hello.js              # Your code
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
mkdir my-js-practice
cd my-js-practice

# Create subdirectories for each level
mkdir level-1-hello-world level-2-variables level-3-basic-math
mkdir level-4-user-input level-5-conditionals level-6-loops
mkdir level-7-functions
```

**Using File Explorer:**
1. Open your file explorer
2. Navigate to the `LEARN` directory
3. Create a new folder called `my-js-practice`
4. Inside it, create 7 subfolders: `level-1-hello-world` through `level-7-functions`

---

### Step 2: Copy Lesson Files

#### Method A: Copy Individual Lessons (Recommended)

**For Level 1:**
```bash
# Copy the lesson file
cp ../javascript/stage-1-copying-code/level-1-hello-world/lesson.md level-1-hello-world/

# Copy any code templates if they exist
cp ../javascript/stage-1-copying-code/level-1-hello-world/*.js level-1-hello-world/ 2>/dev/null || true
```

**For All Levels (Automated):**
```bash
# Copy all lesson files at once
for level in level-1-hello-world level-2-variables level-3-basic-math level-4-user-input level-5-conditionals level-6-loops level-7-functions; do
    mkdir -p "$level"
    cp "../javascript/stage-1-copying-code/$level/lesson.md" "$level/" 2>/dev/null || echo "Warning: Could not copy $level lesson"
done
```

#### Method B: Copy Entire Stage Folder

```bash
# Copy the entire stage (creates a backup)
cp -r javascript/stage-1-copying-code my-stage-1-backup

# Then work in the backup folder
cd my-stage-1-backup
```

#### Method C: Using File Explorer

1. Open two file explorer windows
2. Left window: `LEARN/javascript/stage-1-copying-code/`
3. Right window: `LEARN/my-js-practice/`
4. Copy `lesson.md` from each level folder to corresponding practice folder

---

### Step 3: Create Working Code Files

**For Each Level:**
```bash
# Navigate to level directory
cd level-1-hello-world

# Create your working code file
touch hello.js

# Open in your editor
vim hello.js        # or code hello.js, or your preferred editor
```

**Template for Each Level:**
```bash
# Create standard files for each lesson
cd level-1-hello-world
touch hello.js
touch notes.txt
touch experiments.js

cd ../level-2-variables
touch variables.js
touch notes.txt
touch experiments.js

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
   vim hello.js          # Create your code file
   # Copy code from lesson.md into hello.js
   ```

3. **Execute and Test:**
   ```bash
   node hello.js
   ```

4. **Experiment and Take Notes:**
   ```bash
   vim notes.txt        # Record what you learned
   vim experiments.js    # Try modifications
   ```

### File Organization Tips

**Keep your workspace clean:**
```
level-1-hello-world/
├── lesson.md          # Original lesson (READ-ONLY)
├── hello.js           # Your main working code
├── experiments.js     # Code experiments
├── notes.txt         # Your learning notes
├── backup.js          # Backup of working version
└── test_output.txt   # Program outputs
```

**Version control your work:**
```bash
# Initialize git in your practice folder
cd my-js-practice
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

**Install Node.js:**
```bash
# Using package manager (Ubuntu/Debian)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Using package manager (macOS)
brew install node

# Using package manager (Windows)
# Download from nodejs.org or use Chocolatey: choco install nodejs
```

**Recommended Editors:**
- **Vim**: `vim filename.js`
- **VS Code**: `code filename.js`
- **Sublime Text**: `subl filename.js`

### Execution Commands

**Basic Execution:**
```bash
node program.js
```

**With ES6+ features:**
```bash
node --experimental-modules program.js
```

**Debug with Node:**
```bash
node --inspect program.js
```

---

## Progress Tracking

### Manual Progress Updates

**Update the Table of Contents:**
```bash
# Edit your progress
vim ../javascript/TABLE_OF_CONTENTS.md

# Mark lessons as completed
# Change [ ] to [x] for completed lessons
```

**Create Progress Log:**
```bash
# Daily progress tracking
echo "$(date): Completed Level 1 - Hello World" >> progress.log
echo "$(date): Learned console.log() and basic execution" >> progress.log
```

### Automated Progress Tracking

**Simple Progress Script:**
```bash
#!/bin/bash
# progress.sh

echo "=== JavaScript Learning Progress ==="
echo "Date: $(date)"
echo ""

completed=0
total=7

for level in level-1-hello-world level-2-variables level-3-basic-math level-4-user-input level-5-conditionals level-6-loops level-7-functions; do
    if [ -f "$level/notes.txt" ] && [ -s "$level/notes.txt" ]; then
        echo "✓ $level - COMPLETED"
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

**"Command 'node' not found":**
```bash
# Check if Node.js is installed
which node
node --version

# Install Node.js if needed
# Follow installation instructions above
```

**"No such file or directory":**
```bash
# Check if file exists
ls -la hello.js

# Check current directory
pwd

# Navigate correctly
cd level-1-hello-world
```

**Runtime errors:**
```bash
# Check for typos in code
cat hello.js

# Common fixes:
# - Missing semicolon
# - Wrong quotes (" vs ')
# - Missing parentheses
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
4. Try running simpler versions first

---

## Best Practices

### Code Organization
- [ ] Keep original lessons separate from working code
- [ ] Use meaningful filenames (`hello_v2.js`, `experiment_loops.js`)
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
1. Install JavaScript (ES6) extension pack
2. Configure tasks.json for building
3. Set up debugging with Node.js

**Vim Advanced Setup:**
```vim
" Add to .vimrc for JavaScript development
autocmd FileType javascript setlocal tabstop=2 shiftwidth=2 expandtab
autocmd FileType javascript nnoremap <F5> :w<CR>:!node %<CR>
autocmd FileType javascript setlocal makeprg=node\\ %
```

### Build Systems

**Simple Package.json:**
```json
{
  "name": "js-learning",
  "version": "1.0.0",
  "description": "JavaScript learning project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "level1": "node level-1-hello-world/hello.js",
    "level2": "node level-2-variables/variables.js"
  },
  "devDependencies": {}
}
```

---

## Support Resources

### Getting Help
- **Lesson Answer Keys**: Check bottom of each lesson file
- **Runtime Errors**: Compare with working examples
- **Concept Questions**: Re-read relevant lesson sections
- **Stuck on Code**: Try simpler test cases first

### External Resources
- **JavaScript Reference**: MDN Web Docs, JavaScript.info
- **Online Communities**: Stack Overflow, Reddit r/learnjavascript
- **Practice Sites**: LeetCode, HackerRank, CodeSignal
- **Documentation**: developer.mozilla.org

---

## Success Checklist

**Workspace Setup:**
- [ ] Created separate practice directory
- [ ] Copied lesson files safely
- [ ] Set up development environment
- [ ] Tested execution works

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

*Remember: The goal is learning, not perfection. Every runtime error is a learning opportunity! Keep practicing and you'll master JavaScript programming. *