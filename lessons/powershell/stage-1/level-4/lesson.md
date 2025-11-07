# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.ps1` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Make your programs interactive by reading input from users.

---

### Learning Goals

- Learn how to read user input
- Understand input/output operations
- Practice with different data types from user
- Create interactive programs that respond to users

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.ps1`**

```
$name = Read-Host "Enter your name"
$age = [int](Read-Host "Enter your age")

Write-Host "Hello, $name!"
Write-Host "You are $age years old."
Write-Host "Next year you'll be $($age + 1)."
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
$name = Read-Host "Enter your name"
$age = [int](Read-Host "Enter your age")

Write-Host "Hello, $name!"
Write-Host "You are $age years old."
Write-Host "Next year you'll be $($age + 1)."
```

### What This Code Does

This program demonstrates user input in PowerShell.

### Key Concepts

- **User Input**: Reading data from the user
- **Input Methods**: Language-specific ways to get user input
- **Type Conversion**: Converting string input to numbers
- **String Concatenation**: Combining text with variables

### Line-by-Line Breakdown

The code creates an interactive program:

1. **Prompt for Name**: Ask the user for their name
2. **Read Name**: Store the user's input
3. **Prompt for Age**: Ask the user for their age
4. **Read Age**: Store and convert the age to a number
5. **Greet User**: Display personalized greeting
6. **Show Age**: Display the age back to the user
7. **Calculate**: Show age + 1 (next year's age)

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Type error | Wrong data type | Ensure variables are correct type |
| Runtime error | Code runs but crashes | Check your logic and data flow |

### Bonus Knowledge

- Always validate user input in production code
- Different languages have different input methods
- Type conversion can fail if user enters invalid data
- Consider what happens if user enters unexpected input

---

**Excellent work! You've mastered user input!**

*Continue to the next level to keep building your skills!*
