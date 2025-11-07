# Level 5: Conditional Statements

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.ps1` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Add decision-making to your programs with if/else statements.

---

### Learning Goals

- Understand conditional logic and boolean expressions
- Master if, else if, and else statements
- Practice with comparison and logical operators
- Create programs that make intelligent decisions

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.ps1`**

```
$num = [int](Read-Host "Enter a number")

if ($num -gt 0) {
    Write-Host "$num is positive"
} elseif ($num -lt 0) {
    Write-Host "$num is negative"
} else {
    Write-Host "The number is zero"
}

if ($num % 2 -eq 0) {
    Write-Host "$num is even"
} else {
    Write-Host "$num is odd"
}
```

---

### Success Checklist

- [ ] Created a file named `main.ps1`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study after attempting!)

### The Complete Code

```
$num = [int](Read-Host "Enter a number")

if ($num -gt 0) {
    Write-Host "$num is positive"
} elseif ($num -lt 0) {
    Write-Host "$num is negative"
} else {
    Write-Host "The number is zero"
}

if ($num % 2 -eq 0) {
    Write-Host "$num is even"
} else {
    Write-Host "$num is odd"
}
```

### What This Code Does

This program demonstrates conditional statements in PowerShell.

### Key Concepts

- **Conditional Statements**: Making decisions in code
- **if/else**: Testing conditions and executing different code
- **Comparison Operators**: `>`, `<`, `==`, `!=`, `>=`, `<=`
- **Logical Operators**: Combining conditions with AND, OR, NOT

### Line-by-Line Breakdown

The code makes decisions based on input:

1. **Get Number**: Read a number from the user
2. **Test Positive/Negative**: Check if number is > 0, < 0, or = 0
3. **Display Result**: Show whether it's positive, negative, or zero
4. **Test Even/Odd**: Check if number divides evenly by 2
5. **Display Parity**: Show whether the number is even or odd

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Type error | Wrong data type | Ensure variables are correct type |
| Runtime error | Code runs but crashes | Check your logic and data flow |

### Bonus Knowledge

- You can chain multiple if/else statements together
- Every if can have an optional else clause
- Conditions are evaluated top to bottom
- Use else for "catch-all" cases

---

**Excellent work! You've mastered conditional statements!**

*Continue to the next level to keep building your skills!*
