# Level 6: Loops

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.dart` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Learn to repeat actions efficiently using loops.

---

### Learning Goals

- Understand loop concepts and iteration
- Master for loops and while loops
- Practice with loop control (break, continue)
- Create programs that handle repetitive tasks

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.dart`**

```
void main() {
  print('Counting 1 to 10:');
  for (int i = 1; i <= 10; i++) {
    stdout.write('$i ');
  }
  print('');

  print('\nMultiplication table for 7:');
  for (int i = 1; i <= 10; i++) {
    print('7 × $i = ${7 * i}');
  }

  print('\nCountdown from 5:');
  int count = 5;
  while (count > 0) {
    print(count);
    count--;
  }
  print('Liftoff!');
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
void main() {
  print('Counting 1 to 10:');
  for (int i = 1; i <= 10; i++) {
    stdout.write('$i ');
  }
  print('');

  print('\nMultiplication table for 7:');
  for (int i = 1; i <= 10; i++) {
    print('7 × $i = ${7 * i}');
  }

  print('\nCountdown from 5:');
  int count = 5;
  while (count > 0) {
    print(count);
    count--;
  }
  print('Liftoff!');
}
```

### What This Code Does

This program demonstrates loops in Dart.

### Key Concepts

- **Loops**: Repeating code multiple times
- **For Loops**: Loop with a counter (1 to 10)
- **While Loops**: Loop while a condition is true
- **Loop Control**: Managing when loops start and stop

### Line-by-Line Breakdown

The code uses loops for repetition:

1. **Counting Loop**: Count from 1 to 10 and display
2. **Multiplication Table**: Use a loop to show 7 times table
3. **Countdown Loop**: While loop that counts down
4. **Display Each**: Print each number in the sequence

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Type error | Wrong data type | Ensure variables are correct type |
| Runtime error | Code runs but crashes | Check your logic and data flow |

### Bonus Knowledge

- For loops are best when you know how many iterations
- While loops are best when condition-based looping is needed
- Infinite loops occur when conditions never become false
- Always ensure your loops will eventually terminate

---

**Excellent work! You've mastered loops!**

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
