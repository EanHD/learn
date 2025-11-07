# Level 5: Conditional Statements

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.zig` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.zig`**

```
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const stdin = std.io.getStdIn().reader();

    try stdout.print("Enter your score (0-100): ", .{});

    var buf: [10]u8 = undefined;
    const input = try stdin.readUntilDelimiter(&buf, '\n');
    const score = try std.fmt.parseInt(i32, input, 10);

    if (score >= 90) {
        try stdout.print("Grade: A - Excellent!\n", .{});
    } else if (score >= 80) {
        try stdout.print("Grade: B - Good job!\n", .{});
    } else if (score >= 70) {
        try stdout.print("Grade: C - Passing\n", .{});
    } else if (score >= 60) {
        try stdout.print("Grade: D - Needs improvement\n", .{});
    } else {
        try stdout.print("Grade: F - Study harder!\n", .{});
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
[Output depends on conditions - varies based on input]
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

- Conditional statements let programs make decisions
- Comparison operators (==, !=, <, >, <=, >=) test relationships
- Logical operators (AND, OR, NOT) combine conditions
- Programs can respond differently based on conditions

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

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const stdin = std.io.getStdIn().reader();

    try stdout.print("Enter your score (0-100): ", .{});

    var buf: [10]u8 = undefined;
    const input = try stdin.readUntilDelimiter(&buf, '\n');
    const score = try std.fmt.parseInt(i32, input, 10);

    if (score >= 90) {
        try stdout.print("Grade: A - Excellent!\n", .{});
    } else if (score >= 80) {
        try stdout.print("Grade: B - Good job!\n", .{});
    } else if (score >= 70) {
        try stdout.print("Grade: C - Passing\n", .{});
    } else if (score >= 60) {
        try stdout.print("Grade: D - Needs improvement\n", .{});
    } else {
        try stdout.print("Grade: F - Study harder!\n", .{});
    }
}
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
