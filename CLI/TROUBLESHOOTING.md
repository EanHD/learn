# CLI Troubleshooting Guide

Common issues when using the `learn` command and how to fix them.

## Installation Issues

### Issue: Command not found

```bash
learn c++ 1
# bash: learn: command not found
```

**Solution 1**: Use full path

```bash
~/LEARN/CLI/learn c++ 1
# or
python3 ~/LEARN/CLI/learn c++ 1
```

**Solution 2**: Make executable

```bash
chmod +x ~/LEARN/CLI/learn
```

**Solution 3**: Add to PATH

```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$PATH:$HOME/LEARN/CLI"

# Reload
source ~/.bashrc
```

### Issue: Permission denied

```bash
./learn c++ 1
# bash: ./learn: Permission denied
```

**Fix**: Make executable

```bash
chmod +x ~/LEARN/CLI/learn
```

### Issue: Python not found

```bash
./learn c++ 1
# env: python3: No such file or directory
```

**Fix**: Install Python 3

```bash
# Ubuntu/Debian
sudo apt install python3

# macOS
brew install python3
```

---

## Lesson Opening Issues

### Issue: Lesson not found

```bash
learn c++ 8
# Lesson not found: c++ level 8
```

**Why**: Levels only go 1-7 (7 lessons per stage)

**Fix**: Use valid level

```bash
learn c++ 7               # Maximum level
learn --list              # See all available
```

### Issue: Unknown language

```bash
learn java 1
# Unknown language: java
# Available: c++, rust
```

**Why**: Only C++ and Rust are supported

**Fix**: Use supported language

```bash
learn c++ 1
learn rust 1
```

### Issue: File not found error

```bash
learn c++ 1
# Error: /home/user/LEARN/c-c++/stage-1/level-1/lesson.md not found
```

**Why**: Lesson files don't exist or wrong location

**Fix**: Verify structure

```bash
cd ~/LEARN
ls -la c-c++/stage-1/level-1/
# Should show: lesson.md

# If missing, recreate
# See: MODE_VIM/COMPLETE_SETUP.md
```

### Issue: Lesson opens wrong stage

```bash
learn c++ 3
# Opens: c-c++/stage-2/level-3/lesson.md
# Expected: c-c++/stage-1/level-3/lesson.md
```

**Why**: Level 3 exists in Stage 2 but not Stage 1

**Fix**: Specify stage explicitly

```bash
learn c++ 3 --stage 1     # Force Stage 1
```

---

## Editor/Mode Issues

### Issue: Neovim not found

```bash
learn c++ 1 --vim
# Error: Neovim not found
```

**Why**: Vim not installed

**Fix**: Install Neovim

```bash
# Ubuntu/Debian
sudo apt install neovim

# macOS
brew install neovim

# Verify
nvim --version
```

### Issue: VS Code not found

```bash
learn c++ 1 --vscode
# Error: code command not found
```

**Why**: VS Code not installed or not in PATH

**Fix**: Install VS Code

```bash
# Ubuntu/Debian
sudo apt install code

# macOS
brew install visual-studio-code

# Add to PATH if needed
export PATH="$PATH:/path/to/code"
```

### Issue: Terminal mode not working

```bash
learn c++ 1 --terminal
# Error: less not found
```

**Why**: `less` pager not available

**Fix**: Install less or use alternatives

```bash
# Ubuntu/Debian
sudo apt install less

# Or use alternatives
learn c++ 1 --vim        # Use Vim instead
```

### Issue: Vim config error

```bash
learn c++ 1
# Error: Unable to read config: init-learning.vim not found
```

**Why**: Vim config file missing

**Fix**: Restore config

```bash
# Check if it exists
ls ~/LEARN/MODE_VIM/CONFIG/init-learning.vim

# If missing, re-create it
# See: MODE_VIM/README.md
```

---

## Progress Tracking Issues

### Issue: Progress not saving

```bash
learn --info
# No progress recorded yet
```

**Why**: File permissions or directory issues

**Fix**: Check file and directory

```bash
# Check progress file exists
ls -la ~/.learn-progress

# Check directory writable
touch ~/.learn-progress

# Check learn directory writable
ls -la ~/LEARN/.learn-progress
```

### Issue: Progress shows wrong data

```bash
learn --info
# Shows incorrect sessions or language
```

**Why**: Corrupted progress file

**Fix**: Reset progress file

```bash
# Backup old progress
cp ~/LEARN/.learn-progress ~/LEARN/.learn-progress.bak

# Clear and start fresh
rm ~/LEARN/.learn-progress

# Next session will create new file
learn c++ 1
```

### Issue: learn --next not working

```bash
learn --next
# (no suggestion shown)
```

**Why**: Progress file empty or corrupted

**Fix**: Open some lessons first

```bash
learn c++ 1
learn c++ 2

# Now try
learn --next
```

---

## Performance Issues

### Issue: Lesson opens slowly

```bash
learn c++ 1
# Takes 10+ seconds to open
```

**Why**: Slow disk or system load

**Fix**: Wait for system, or:

```bash
# Close other applications
# Clear cache
sync; sleep 1

# Try again
learn c++ 1
```

### Issue: --list command slow

```bash
learn --list
# Takes several seconds
```

**Why**: Large directory tree or slow disk

**Fix**: Results are still correct, just takes time
- First run caches structure
- Subsequent runs are faster

---

## Advanced Troubleshooting

### Debug with Python directly

Run CLI with Python for better error messages:

```bash
python3 ~/LEARN/CLI/learn c++ 1 -v
```

### Check Python version

```bash
python3 --version
# Should be 3.6+
```

### Verify syntax

```bash
python3 -m py_compile ~/LEARN/CLI/learn
# If no output, syntax is OK
# If error, syntax problem
```

### Check lesson structure

```bash
# Verify lesson exists
file ~/LEARN/c-c++/stage-1/level-1/lesson.md

# Check it has content
wc -l ~/LEARN/c-c++/stage-1/level-1/lesson.md

# View first 10 lines
head -10 ~/LEARN/c-c++/stage-1/level-1/lesson.md
```

### Check CLI is correct

```bash
# Verify it's the learn command, not something else
which learn

# Show first line (should be #!/usr/bin/env python3)
head -1 ~/LEARN/CLI/learn

# Show size
wc -l ~/LEARN/CLI/learn
# Should be 300+ lines
```

---

## Getting More Help

### Check built-in help

```bash
learn --help              Show all options
learn --list              See all lessons
learn                     Show default help
```

### Check documentation

```bash
# CLI usage guide
less ~/LEARN/CLI/README.md

# CLI implementation details
less ~/LEARN/CLI/IMPLEMENTATION.md

# Complete learning guide
less ~/LEARN/MODE_VIM/COMPLETE_SETUP.md

# All documentation index
less ~/LEARN/VIM_MODE_DOCUMENTATION_INDEX.md
```

### Check logs

```bash
# See all sessions ever opened
cat ~/LEARN/.learn-progress

# Count sessions
wc -l ~/LEARN/.learn-progress

# See last 10 sessions
tail ~/LEARN/.learn-progress

# See specific language
grep "rust" ~/LEARN/.learn-progress
```

### File system check

```bash
# List all lessons
find ~/LEARN -name "lesson.md" | wc -l
# Should show: 70 (35 C++, 35 Rust)

# Check directory structure
tree ~/LEARN -L 3 | head -30

# Find missing lessons
find ~/LEARN -type d -name "level-*" | wc -l
# Should show: 70
```

---

## Report Issues

When reporting issues, include:

1. **What you ran**:
   ```bash
   learn c++ 1 --vim
   ```

2. **What you expected**: Lesson to open in Vim

3. **What happened**: Error message (copy-paste)

4. **System info**:
   ```bash
   python3 --version
   nvim --version
   uname -a
   ```

5. **Relevant files**:
   ```bash
   ls ~/LEARN/c-c++/stage-1/level-1/
   cat ~/LEARN/.learn-progress
   ```

---

## Quick Checklist

When troubleshooting, verify:

- [ ] Python 3 installed: `python3 --version`
- [ ] CLI executable: `ls -la ~/LEARN/CLI/learn`
- [ ] In correct directory: `pwd` shows `~/LEARN`
- [ ] Lesson exists: `ls ~/LEARN/c-c++/stage-1/level-1/lesson.md`
- [ ] Vim installed (for vim mode): `nvim --version`
- [ ] Vim config exists: `ls ~/LEARN/MODE_VIM/CONFIG/init-learning.vim`
- [ ] Progress file writable: `touch ~/LEARN/.learn-progress`
- [ ] No typos in command: `learn c++ 1` (not `lern`, `learrn`, etc)

---

## Still Stuck?

1. Check all items in the checklist above
2. Review the README.md in this directory
3. Read IMPLEMENTATION.md for technical details
4. See MODE_VIM/COMPLETE_SETUP.md for full setup guide
5. Visit MODE_VIM/FAQ.md for common questions

---

**Most Common Fix**: Many issues are solved by:

```bash
chmod +x ~/LEARN/CLI/learn
```

**Second Most Common Fix**: Test with full path:

```bash
python3 ~/LEARN/CLI/learn c++ 1
```

If that works, add to PATH (see Installation Issues section).

