# Workspace Instructions for Shell

## Overview

When you start a lesson in the LEARN CLI, a workspace directory is automatically created for you. This document explains how to use it.

## Workspace Location

Your Shell workspaces are stored in:

```
~/.local/share/learn/workspaces/shell/
```

Each lesson has its own directory:

```
~/.local/share/learn/workspaces/shell/stage-<N>/level-<M>/
```

## What's in Your Workspace

### Directory Structure

```
stage-<N>/level-<M>/
├── lesson.md          # The lesson (opened automatically)
├── main.shell    # Your Shell code file
└── [other files]      # Additional resources
```

### Files You'll See

- **lesson.md** - Your lesson content (opened in Vim alongside your code)
- **main.shell** - Blank file where you write your solution

## Using the Workspace

### Opening a Lesson

1. Run the LEARN CLI:
   ```bash
   learn
   ```

2. Select Shell

3. Choose your stage and level

4. Choose your mode:
   - **Vim** (recommended) - Lesson + code side-by-side
   - **VS Code** - Full editor experience
   - **Terminal** - Just open the directory

### In Vim Mode

When you choose Vim:

- **Left pane**: Your lesson (read-only)
- **Right pane**: Your code editor (`main.shell`)
- **Navigation**: Arrow keys or Vim commands
- **Exit**: Type `:wq` to save and quit both panes

### Writing Your Solution

1. Read the lesson in the left pane
2. Click into the right pane (your code)
3. Write your Shell code
4. Save with `:w` in Vim
5. Run your code from the terminal (instructions in lesson)

## Running Your Code

From within your workspace directory:

```bash
# The exact command depends on your lesson
# Check your lesson.md for specific instructions
```

The lesson will tell you exactly how to run your specific code.

## Organizing Your Work

### Keeping Track

- Each level has its own workspace
- Your code is automatically saved when you exit Vim
- You can return to any lesson at any time

### Going Back to Previous Lessons

To revisit a previous lesson:

```bash
learn
```

Then select the language, stage, and level again. Your workspace will open.

### Backing Up Your Work

To save your work outside the LEARN system:

```bash
cp -r ~/.local/share/learn/workspaces/shell/ ~/my-learn-backup/
```

## Troubleshooting

### "Workspace not found"

The workspace directory structure may not exist yet. The LEARN CLI will create it automatically when you open a lesson.

### Can't run my code

1. Check the lesson instructions - they show the exact command
2. Make sure you saved your file (`:w` in Vim)
3. Verify the file is in the correct directory
4. Check for syntax errors in your code

### Vim is confusing

- Check `VIM_CHEATSHEET.md` in the root LEARN directory
- Basic commands: `i` (insert), `Esc` (normal), `:w` (save), `:q` (quit)
- Practice with one lesson at a time!

### I accidentally deleted my code

Unfortunately, there's no automatic backup. Consider using Git:

```bash
cd ~/.local/share/learn/workspaces/shell/
git init
git add .
git commit -m "Backup"
```

This creates a local repository you can revert from if needed.

## Best Practices

1. **Read the lesson first** - Understand before coding
2. **Type slowly** - Focus on syntax, not speed
3. **Test frequently** - Run your code after each section
4. **Follow the pattern** - Each lesson teaches incrementally
5. **Experiment** - Once you understand, try variations

## Tips for Success

- **Save often**: `:w` in Vim frequently
- **Check output**: Does your output match the expected result?
- **Read errors**: Error messages tell you what's wrong
- **Reference lessons**: Look back at previous lessons if stuck
- **Take breaks**: Programming is mentally intensive

## Moving Forward

Once you complete a level:

1. Review what you learned
2. Understand why each part of the code works
3. Try modifying the solution
4. Move to the next level

Each level builds on the previous one. Master the fundamentals first!

## Getting Help

- **Lesson stuck?** - Read the "Hints" section in your lesson
- **Vim confused?** - Check `VIM_CHEATSHEET.md`
- **Language specific?** - Check official Shell documentation
- **Logic issue?** - Write pseudocode first, then translate to code

---

## Quick Reference

### Common Shell Commands

(Check your specific lesson for language-specific commands)

### Vim Essentials

- `i` - Enter insert mode
- `Esc` - Return to normal mode
- `:w` - Save
- `:q` - Quit
- `:wq` - Save and quit

### Terminal Essentials

```bash
cd ~/.local/share/learn/workspaces/shell/stage-X/level-Y
ls                    # List files
cat main.shell   # View your code
vim main.shell   # Edit your code
```

---

Happy learning with Shell!
