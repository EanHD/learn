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
├── go/                          # Original lessons (READ-ONLY)
│   ├── stage-1-copying-code/
│   ├── TABLE_OF_CONTENTS.md
│   └── ...
│
└── my-go-practice/                    # Your working copies
    ├── level-1-hello-world/
    │   ├── lesson.md              # Copied from original
    │   ├── hello.go              # Your working code
    │   └── my_notes.txt          # Your personal notes
    ├── level-2-variables/
    └── ...
```

### Option 2: Lesson-Specific Folders
```
LEARN/
├── go/                          # Original lessons
└── practice-sessions/              # Working directories
    ├── session-1-hello-world/
    │   ├── original-lesson.md     # Copied lesson
    │   ├── hello.go              # Your code
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
mkdir my-go-practice
cd my-go-practice

# Create subdirectories for each level
mkdir level-1-hello-world level-2-variables level-3-basic-math
mkdir level-4-user-input level-5-conditionals level-6-loops
mkdir level-7-functions
```

**Using File Explorer:**
1. Open your file explorer
2. Navigate to the `LEARN` directory
3. Create a new folder called `my-go-practice`
4. Inside it, create 7 subfolders: `level-1-hello-world` through `level-7-functions`

---

### Step 2: Copy Lesson Files

#### Method A: Copy Individual Lessons (Recommended)

**For Level 1:**
```bash
# Copy the lesson file
cp ../go/stage-1-copying-code/level-1-hello-world/lesson.md level-1-hello-world/

# Copy any code templates if they exist
cp ../go/stage-1-copying-code/level-1-hello-world/*.go level-1-hello-world/ 2>/dev/null || true
```

**For All Levels (Automated):**
```bash
# Copy all lesson files at once
for level in level-1-hello-world level-2-variables level-3-basic-math level-4-user-input level-5-conditionals level-6-loops level-7-functions; do
    mkdir -p "$level"
    cp "../go/stage-1-copying-code/$level/lesson.md" "$level/" 2>/dev/null || echo "Warning: Could not copy $level lesson"
done
```

#### Method B: Copy Entire Stage Folder

```bash
# Copy the entire stage (creates a backup)
cp -r go/stage-1-copying-code my-stage-1-backup

# Then work in the backup folder
cd my-stage-1-backup
```

#### Method C: Using File Explorer

1. Open two file explorer windows
2. Left window: `LEARN/go/stage-1-copying-code/`
3. Right window: `LEARN/my-go-practice/`
4. Copy `lesson.md` from each level folder to corresponding practice folder

---

### Step 3: Create Working Code Files

**For Each Level:**
```bash
# Navigate to level directory
cd level-1-hello-world

# Create your working code file
touch hello.go

# Open in your editor
vim hello.go        # or code hello.go, or your preferred editor
```

**Template for Each Level:**
```bash
# Create standard files for each lesson
cd level-1-hello-world
touch hello.go
touch notes.txt
touch experiments.go

cd ../level-2-variables
touch variables.go
touch notes.txt
touch experiments.go

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
   vim hello.go          # Create your code file
   # Copy code from lesson.md into hello.go
   ```

3. **Compile and Test:**
   ```bash
   go run hello.go
   # or
   go build hello.go
   ./hello
   ```

4. **Experiment and Take Notes:**
   ```bash
   vim notes.txt        # Record what you learned
   vim experiments.go    # Try modifications
   ```

### File Organization Tips

**Keep your workspace clean:**
```
level-1-hello-world/
├── lesson.md          # Original lesson (READ-ONLY)
├── hello.go           # Your main working code
├── experiments.go     # Code experiments
├── notes.txt         # Your learning notes
├── backup.go          # Backup of working version
└── test_output.txt   # Program outputs
```

**Version control your work:**
```bash
# Initialize git in your practice folder
cd my-go-practice
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

**Install Go:**
```bash
# Using package manager (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install golang

# Using package manager (macOS)
brew install go

# Using package manager (Windows)
# Use Chocolatey: choco install golang
# Or download from golang.org
```

**Recommended Editors:**
- **Vim**: `vim filename.go`
- **VS Code**: `code filename.go` (with Go extension)
- **GoLand**: Specialized Go IDE

### Build Commands

**Basic Execution:**
```bash
go run program.go
```

**Build and Run Separately:**
```bash
go build program.go
./program    # On Linux/macOS
# or
./program.exe    # On Windows
```

**With debugging:**
```bash
go run -gcflags="-N -l" program.go
```

---

## Progress Tracking

### Manual Progress Updates

**Update the Table of Contents:**
```bash
# Edit your progress
vim ../go/TABLE_OF_CONTENTS.md

# Mark lessons as completed
# Change [ ] to [x] for completed lessons
```

**Create Progress Log:**
```bash
# Daily progress tracking
echo "$(date): Completed Level 1 - Hello World" >> progress.log
echo "$(date): Learned fmt.Println() and basic compilation" >> progress.log
```

### Automated Progress Tracking

**Simple Progress Script:**
```bash
#!/bin/bash
# progress.sh

echo "=== Go Learning Progress ==="
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

**"Command 'go' not found":**
```bash
# Check if Go is installed
which go
go version

# Install Go if needed
# Follow installation instructions above
```

**"No such file or directory":**
```bash
# Check if file exists
ls -la hello.go

# Check current directory
pwd

# Navigate correctly
cd level-1-hello-world
```

**Compilation errors:**
```bash
# Check for typos in code
cat hello.go

# Common fixes:
# - Missing package declaration
# - Wrong quotes (" vs ')
# - Missing semicolon (in some cases)
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
- [ ] Use meaningful filenames (`hello_v2.go`, `experiment_loops.go`)
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
1. Install Go extension
2. Configure tasks.json for building
3. Set up debugging with Delve (dlv)

**Vim Advanced Setup:**
```vim
" Add to .vimrc for Go development
let g:go_fmt_command = "goimports"
autocmd FileType go nmap <Leader>b :<S-Left>go build<CR>
autocmd FileType go nmap <Leader>r :<S-Left>go run %
autocmd FileType go nmap <Leader>t :<S-Left>go test<CR>
```

### Build Systems

**Simple Makefile:**
```makefile
GO=go
GOCMD=$(GO)
GOBUILD=$(GOCMD) build
GOCLEAN=$(GOCMD) clean
GOTEST=$(GOCMD) test
GOGET=$(GOCMD) get

BINARY_NAME=my-program
BINARY_UNIX=$(BINARY_NAME)_unix

all: hello variables math input conditionals loops functions

hello:
	$(GOBUILD) -o level-1-hello-world/hello level-1-hello-world/hello.go

variables:
	$(GOBUILD) -o level-2-variables/variables level-2-variables/variables.go

# ... add rules for other programs

clean:
	$(GOCLEAN)
	rm -f level-1-hello-world/hello level-2-variables/variables

.PHONY: all clean
```

---

## Support Resources

### Getting Help
- **Lesson Answer Keys**: Check bottom of each lesson file
- **Compilation Errors**: Compare with working examples
- **Concept Questions**: Re-read relevant lesson sections
- **Stuck on Code**: Try simpler test cases first

### External Resources
- **Go Reference**: Golang.org, Effective Go, Go by Example
- **Online Communities**: Stack Overflow, Reddit r/golang
- **Practice Sites**: Exercism.io, Go Playground, Codewars
- **Documentation**: golang.org/pkg/

---

## Success Checklist

**Workspace Setup:**
- [ ] Created separate practice directory
- [ ] Copied lesson files safely
- [ ] Set up development environment
- [ ] Tested compilation and execution works

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

*Remember: The goal is learning, not perfection. Every compilation error is a learning opportunity! Keep practicing and you'll master Go programming. *