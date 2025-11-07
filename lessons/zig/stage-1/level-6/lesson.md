# Level 6: Loops

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.zig` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.zig`**

```
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    // For loop
    try stdout.print("Counting 1 to 10:\n", .{});
    var i: i32 = 1;
    while (i <= 10) : (i += 1) {
        try stdout.print("{} ", .{i});
    }
    try stdout.print("\n", .{});

    // While loop
    try stdout.print("\nCountdown:\n", .{});
    var count: i32 = 5;
    while (count > 0) {
        try stdout.print("{}\n", .{count});
        count -= 1;
    }
    try stdout.print("Blastoff!\n", .{});

    // Multiplication table
    const num: i32 = 7;
    try stdout.print("\n{} times table:\n", .{num});
    i = 1;
    while (i <= 10) : (i += 1) {
        try stdout.print("{} × {} = {}\n", .{num, i, num * i});
    }
}
```

---

### How to Run

**Method 1 (Vim - Recommended):**
```
<Space>r
```

**Method 2 (Terminal):**
```
zig build-exe main.zig
./main
```

**Expected output:**
```
1 2 3 4 5 6 7 8 9 10
```


---

### Success Checklist

- [ ] Created a file named `main.zig`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

### What Just Happened?

You just created a real Zig program! Here's what makes it work:

- Loops repeat code efficiently
- For loops work well when you know the count
- While loops continue until a condition is false
- Break and continue control loop execution

---

### Try This (Optional Challenges)

1. Modify the values and see what changes
2. Add your own variations to the code
3. Combine concepts from previous lessons
4. Break something on purpose, then fix it!

---

### Pro Tips

- Zig has no hidden control flow
- Memory safety without garbage collection
- Compile-time code execution

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

The code you copied demonstrates fundamental Zig concepts:

**Key Components:**
- Syntax rules specific to Zig
- How data is stored and manipulated
- Input/output operations
- Program flow and structure

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Runtime error | Code runs but crashes | Check your logic and data types |
| Unexpected output | Logic error | Review your algorithm step-by-step |
| Compilation error | Code won't compile | Fix syntax before running |

### Bonus Knowledge

- Zig has a rich ecosystem of libraries and tools
- Understanding these basics prepares you for advanced topics
- Practice is key - try writing similar programs from scratch
- Every expert programmer started exactly where you are now!

### Real-World Applications

This concept is used in:
1. Professional software development
2. Web applications and mobile apps
3. Data analysis and scientific computing
4. Automation and scripting
5. Game development

---

**Excellent work! You've mastered a fundamental concept!**

*Ready for the next challenge? Keep going!*
