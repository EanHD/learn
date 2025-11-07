# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.zig` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Make your programs interactive by reading input from users.

---

### Learning Goals

- Learn how to read user input in Zig
- Understand input/output operations
- Practice with different data types from user
- Create interactive programs that respond to users

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.zig`**

```
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const stdin = std.io.getStdIn().reader();
    
    var name_buf: [100]u8 = undefined;
    
    try stdout.print("Enter your name: ", .{});
    const name = try stdin.readUntilDelimiter(&name_buf, '\n');
    
    try stdout.print("Hello, {s}!\n", .{name});
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
[Interactive - output varies based on user input]
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

- Programs can read input from users
- Input makes programs interactive and dynamic
- Different methods exist for different data types
- Always validate user input in real programs

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
