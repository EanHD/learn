# Migration Guide: Old CLI → Enhanced CLI

## Overview

The Enhanced CLI maintains full backward compatibility while adding powerful new features. Your existing workflows continue to work, and you can adopt new features at your own pace.

## What Changed?

### Old CLI (Still Works)
```bash
learn c++ 1              ✅ Still works
learn rust 3 --vim       ✅ Still works  
learn --list             ✅ Still works
learn --info             ⚠️  Changed to --progress
learn --next             ✅ Still works
```

### Enhanced CLI (New Features)
```bash
learn                    🆕 Interactive menu
learn --progress         🆕 Enhanced progress view
learn --complete         🆕 Mark lessons complete
learn python 1           🆕 More languages
learn javascript 2       🆕 More languages
learn go 1               🆕 More languages
```

## Key Differences

### 1. Progress Tracking

**Old System:**
- Text file: `.learn-progress`
- Simple append-only log
- Dictionary-string format

**New System:**
- JSON file: `.learn-progress.json`
- Structured data
- Completion tracking
- Detailed statistics

**Migration:**
Your old progress file is preserved. The new system creates a separate JSON file for enhanced tracking.

### 2. Commands

| Old Command | New Command | Status |
|------------|-------------|--------|
| `learn --info` | `learn --progress` | Renamed (--info deprecated) |
| `learn --list` | `learn --list` | Enhanced with more languages |
| `learn --next` | `learn --next` | Enhanced with smarter logic |
| N/A | `learn` | New: Interactive mode |
| N/A | `learn --complete` | New: Completion tracking |

### 3. Language Support

**Old:**
- C++
- Rust

**New:**
- C++
- Rust
- Python
- JavaScript
- Go
- Lua

## Migration Steps

### Step 1: No Action Required

The enhanced CLI works immediately with your existing setup. No migration needed.

```bash
# Your existing commands still work
learn c++ 1
learn rust 2
```

### Step 2: Try Interactive Mode (Optional)

```bash
# Launch new interactive interface
learn
```

Explore the menu options:
1. Start a lesson
2. Continue learning
3. View progress
4. Browse all lessons
5. Switch language
6. Mark lesson complete
7. View statistics

### Step 3: Update Your Workflow (Optional)

**Old Workflow:**
```bash
learn c++ 1
# Do lesson
learn c++ 2
# Do lesson
learn --info
```

**Enhanced Workflow:**
```bash
learn c++ 1
learn --complete c++ 1 1    # Mark complete
learn --next                # Get suggestion
learn --progress            # View stats with progress bars
```

### Step 4: Explore New Languages (Optional)

```bash
# Try Python
learn python 1

# Try JavaScript
learn javascript 1

# View all available
learn --list
```

## Compatibility Matrix

| Feature | Old CLI | Enhanced CLI | Notes |
|---------|---------|--------------|-------|
| Open C++ lesson | ✅ | ✅ | Same syntax |
| Open Rust lesson | ✅ | ✅ | Same syntax |
| Open Python lesson | ❌ | ✅ | New feature |
| Vim mode | ✅ | ✅ | Enhanced split view |
| VS Code mode | ✅ | ✅ | Same |
| Terminal mode | ✅ | ✅ | Same |
| List lessons | ✅ | ✅ | Enhanced output |
| View progress | ⚠️ | ✅ | Changed to --progress |
| Next suggestion | ✅ | ✅ | Smarter logic |
| Interactive menu | ❌ | ✅ | New feature |
| Completion tracking | ❌ | ✅ | New feature |
| Statistics | ❌ | ✅ | New feature |
| Progress bars | ❌ | ✅ | New feature |
| JSON progress | ❌ | ✅ | New feature |

## Troubleshooting

### Issue: `learn --info` doesn't work

**Solution:**
```bash
# Use the new command
learn --progress
```

### Issue: Don't see new languages

**Solution:**
```bash
# Check what's available
learn --list

# Languages need lesson directories
# Make sure python/, javascript/, go/, lua/ exist
```

### Issue: Old progress not showing

**Solution:**
Old progress is in `.learn-progress` (text file).
New progress is in `.learn-progress.json` (JSON file).

They're separate but both preserved. The new system builds its own tracking.

### Issue: Missing features in command mode

**Solution:**
Some features are only in interactive mode:
```bash
# Launch interactive mode to access all features
learn
```

## Recommended Migration Path

### Week 1: Familiarity
- Keep using your existing commands
- Try `learn` once to see interactive mode
- Use `learn --list` to see new languages

### Week 2: Exploration
- Use `learn --progress` instead of `learn --info`
- Try `learn --next` for suggestions
- Experiment with one new language

### Week 3: Adoption
- Start using interactive mode regularly
- Begin marking lessons complete
- Track progress with `learn --progress`

### Week 4: Full Integration
- Use interactive mode as primary interface
- Track all completions
- Explore multiple languages
- Review statistics regularly

## Best Practices

### 1. Use Interactive Mode for Discovery

```bash
# When unsure what to do next
learn
```

### 2. Use Command Line for Speed

```bash
# When you know exactly what you want
learn c++ 5 --stage 2
```

### 3. Mark Lessons Complete

```bash
# Helps with progress tracking
learn --complete c++ 1 1
```

### 4. Check Progress Regularly

```bash
# Stay motivated
learn --progress
```

### 5. Explore New Languages

```bash
# Learn same concepts in different languages
learn c++ 1
learn rust 1
learn python 1
```

## FAQ

**Q: Do I have to migrate?**
A: No. The old CLI still works. New features are optional.

**Q: Will my old progress be lost?**
A: No. Old progress file is preserved. New system tracks separately.

**Q: Can I use both old and new commands?**
A: Yes. They work together seamlessly.

**Q: What happens to my existing workflow?**
A: It continues to work without changes.

**Q: Should I delete the old progress file?**
A: No need. It doesn't interfere and serves as a backup.

**Q: How do I know which version I'm using?**
A: If you see interactive menus and progress bars, you're using the enhanced CLI.

**Q: Can I go back to the old CLI?**
A: The old CLI is now just a wrapper around the enhanced CLI. But all your old commands still work the same way.

## Summary

✅ **Backward Compatible** - All old commands work
✅ **No Action Required** - Works immediately
✅ **Optional Adoption** - Use new features at your pace
✅ **Data Preserved** - Old progress files kept
✅ **Enhanced Features** - Available when you want them

**Start exploring:**
```bash
learn
```

or keep using your existing workflow:
```bash
learn c++ 1
```

Both work perfectly!
