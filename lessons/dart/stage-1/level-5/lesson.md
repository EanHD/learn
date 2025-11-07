# Level 5: Conditional Statements

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.dart` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.dart`**

```
import 'dart:io';

void main() {
  stdout.write('Enter a number: ');
  int num = int.parse(stdin.readLineSync()!);
  
  if (num > 0) {
    print('$num is positive');
  } else if (num < 0) {
    print('$num is negative');
  } else {
    print('The number is zero');
  }
  
  if (num % 2 == 0) {
    print('$num is even');
  } else {
    print('$num is odd');
  }
}
```

---

### Success Checklist

- [ ] Created a file named `main.dart`
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
import 'dart:io';

void main() {
  stdout.write('Enter a number: ');
  int num = int.parse(stdin.readLineSync()!);
  
  if (num > 0) {
    print('$num is positive');
  } else if (num < 0) {
    print('$num is negative');
  } else {
    print('The number is zero');
  }
  
  if (num % 2 == 0) {
    print('$num is even');
  } else {
    print('$num is odd');
  }
}
```

### What This Code Does

This program demonstrates conditional statements in Dart.

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


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```
void main() {
    print("Hello, World!");
}

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard dart conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
