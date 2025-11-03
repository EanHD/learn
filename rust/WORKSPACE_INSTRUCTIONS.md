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
├── rust/                          # Original lessons (READ-ONLY)
│   ├── stage-1-copying-code/
│   ├── TABLE_OF_CONTENTS.md
│   └── ...
│
└── my-practice/                    # Your working copies
    ├── level-1-hello-world/
    │   ├── lesson.md              # Copied from original
    │   ├── hello.rs               # Your working code
    │   └── my_notes.txt          # Your personal notes
    ├── level-2-variables/
    └── ...
```

### Option 2: Lesson-Specific Folders
```
LEARN/
├── rust/                          # Original lessons
└── practice-sessions/              # Working directories
    ├── session-1-hello-world/
    │   ├── original-lesson.md     # Copied lesson
    │   ├── hello.rs               # Your code
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
mkdir my-rust-practice
cd my-rust-practice

# Create subdirectories for each level
mkdir level-1-hello-world level-2-variables level-3-basic-math
mkdir level-4-user-input level-5-conditionals level-6-loops
mkdir level-7-functions
```

**Using File Explorer:**
1. Open your file explorer
2. Navigate to the `LEARN` directory
3. Create a new folder called `my-rust-practice`
4. Inside it, create 7 subfolders: `level-1-hello-world` through `level-7-functions`

---

### Step 2: Copy Lesson Files

#### Method A: Copy Individual Lessons (Recommended)

**For Level 1:**
```bash
# Copy the lesson file
cp ../rust/stage-1-copying-code/level-1-hello-world/lesson.md level-1-hello-world/

# Copy any code templates if they exist
cp ../rust/stage-1-copying-code/level-1-hello-world/*.rs level-1-hello-world/ 2>/dev/null || true
```

**For All Levels (Automated):**
```bash
# Copy all lesson files at once
for level in level-1-hello-world level-2-variables level-3-basic-math level-4-user-input level-5-conditionals level-6-loops level-7-functions; do
    mkdir -p "$level"
    cp "../rust/stage-1-copying-code/$level/lesson.md" "$level/" 2>/dev/null || echo "Warning: Could not copy $level lesson"
done
```

#### Method B: Copy Entire Stage Folder

```bash
# Copy the entire stage (creates a backup)
cp -r rust/stage-1-copying-code my-stage-1-backup

# Then work in the backup folder
cd my-stage-1-backup
```

#### Method C: Using File Explorer

1. Open two file explorer windows
2. Left window: `LEARN/rust/stage-1-copying-code/`
3. Right window: `LEARN/my-rust-practice/`
4. Copy `lesson.md` from each level folder to corresponding practice folder

---

### Step 3: Create Working Code Files

**For Each Level:**
```bash
# Navigate to level directory
cd level-1-hello-world

# Create your working code file
touch hello.rs

# Open in your editor
vim hello.rs        # or code hello.rs, or your preferred editor
```

**Template for Each Level:**
```bash
# Create standard files for each lesson
cd level-1-hello-world
touch hello.rs
touch notes.txt
touch experiments.rs

cd ../level-2-variables
touch variables.rs
touch notes.txt
touch experiments.rs

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
   vim hello.rs          # Create your code file
   # Copy code from lesson.md into hello.rs
   ```

3. **Compile and Test:**
   ```bash
   rustc hello.rs -o hello
   ./hello
   ```

4. **Experiment and Take Notes:**
   ```bash
   vim notes.txt        # Record what you learned
   vim experiments.rs    # Try modifications
   ```

### File Organization Tips

**Keep your workspace clean:**
```
level-1-hello-world/
├── lesson.md          # Original lesson (READ-ONLY)
├── hello.rs           # Your main working code
├── experiments.rs     # Code experiments
├── notes.txt         # Your learning notes
├── backup.rs          # Backup of working version
└── test_output.txt   # Program outputs
```

**Version control your work:**
```bash
# Initialize git in your practice folder
cd my-rust-practice
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

**Install Rust Compiler:**
```bash
# Using rustup (recommended)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Verify installation
rustc --version
cargo --version
```

**Recommended Editors:**
- **Vim**: `vim filename.rs`
- **VS Code**: `code filename.rs`
- **Sublime Text**: `subl filename.rs`

### Build Commands

**Basic Compilation:**
```bash
rustc program.rs -o program
./program
```

**With Cargo (Recommended):**
```bash
# Create a new project
cargo new my_project
cd my_project

# Build and run
cargo build
cargo run
```

**Debug Build:**
```bash
rustc -g program.rs -o program
# Use debugger if available
```

---

## Progress Tracking

### Manual Progress Updates

**Update the Table of Contents:**
```bash
# Edit your progress
vim ../rust/TABLE_OF_CONTENTS.md

# Mark lessons as completed
# Change [ ] to [x] for completed lessons
```

**Create Progress Log:**
```bash
# Daily progress tracking
echo "$(date): Completed Level 1 - Hello World" >> progress.log
echo "$(date): Learned println!() and basic compilation" >> progress.log
```

### Automated Progress Tracking

**Simple Progress Script:**
```bash
# !/bin/bash
# progress.sh

echo "=== Rust Learning Progress ==="
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

**"rustc: command not found" when compiling:**
```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

# Check installation
rustc --version
```

**Compilation errors:**
```bash
# Check for syntax errors
cat hello.rs

# Common fixes:
# - Missing semicolon
# - Wrong macro usage (println! vs print!)
# - Missing main function
# - Wrong variable declaration
```

**"Permission denied" when running:**
```bash
# Make executable (usually not needed for Rust)
chmod +x hello

# Or recompile
rustc hello.rs -o hello
./hello
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
- [ ] Use meaningful filenames (`hello_v2.rs`, `experiment_loops.rs`)
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
1. Install Rust extension
2. Configure tasks.json for building
3. Set up debugging with LLDB

**Vim Advanced Setup:**
```vim
" Add to .vimrc for Rust development
autocmd FileType rust setlocal tabstop=4 shiftwidth=4 expandtab
autocmd FileType rust nnoremap <F5> :w<CR>:!rustc % -o %< && ./%<<CR>
autocmd FileType rust setlocal makeprg=rustc\ -o\ %<\ %
```

### Build Systems

**Cargo Configuration:**
```toml
# Cargo.toml
[package]
name = "my-rust-practice"
version = "0.1.0"
edition = "2021"

[dependencies]
# Add dependencies as needed
```

**Simple Makefile:**
```makefile
RUSTC=rustc
RUSTFLAGS=-Wall

all: hello variables math input conditionals loops functions

hello: level-1-hello-world/hello.rs
    $(RUSTC) $(RUSTFLAGS) $< -o $@

variables: level-2-variables/variables.rs
    $(RUSTC) $(RUSTFLAGS) $< -o $@

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
- **The Rust Book**: https://doc.rust-lang.org/book/
- **Rust by Example**: https://doc.rust-lang.org/rust-by-example/
- **Practice Sites**: LeetCode, HackerRank, CodeSignal
- **Communities**: Stack Overflow, Reddit r/rust

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

*Remember: The goal is learning, not perfection. Every compilation error is a learning opportunity! Keep practicing and you'll master Rust programming. *