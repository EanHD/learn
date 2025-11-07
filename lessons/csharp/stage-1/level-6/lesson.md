# Level 6: Loops

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.cs` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.cs`**

```
using System;

class Program {
 static void Main() {
 Console.WriteLine("Counting 1 to 10:");
 for (int i = 1; i <= 10; i++) {
 Console.Write($"{i} ");
 }
 Console.WriteLine();
 
 Console.WriteLine("\nMultiplication table for 7:");
 for (int i = 1; i <= 10; i++) {
 Console.WriteLine($"7 × {i} = {7 * i}");
 }
 
 Console.WriteLine("\nCountdown from 5:");
 int count = 5;
 while (count > 0) {
 Console.WriteLine(count);
 count--;
 }
 Console.WriteLine("Liftoff!");
 }
}
```

---

### Success Checklist

- [ ] Created a file named `main.cs`
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
using System;

class Program {
 static void Main() {
 Console.WriteLine("Counting 1 to 10:");
 for (int i = 1; i <= 10; i++) {
 Console.Write($"{i} ");
 }
 Console.WriteLine();
 
 Console.WriteLine("\nMultiplication table for 7:");
 for (int i = 1; i <= 10; i++) {
 Console.WriteLine($"7 × {i} = {7 * i}");
 }
 
 Console.WriteLine("\nCountdown from 5:");
 int count = 5;
 while (count > 0) {
 Console.WriteLine(count);
 count--;
 }
 Console.WriteLine("Liftoff!");
 }
}
```

### What This Code Does

This program demonstrates loops in C#.

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
| Compilation error | Code won't compile | Fix syntax before running |

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


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard csharp conventions with proper imports and main function
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
