# Level 3: Basic Math Operations

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.zig` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Master arithmetic operations and use Zig as your powerful calculator.

---

### Learning Goals

- Learn all basic arithmetic operators (+, -, *, /, %)
- Understand operator precedence (order of operations)
- Practice mathematical expressions
- Work with both integers and floating-point numbers

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.zig`**

```
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    const a: i32 = 10;
    const b: i32 = 3;

    try stdout.print("Addition: {}\n", .{a + b});
    try stdout.print("Subtraction: {}\n", .{a - b});
    try stdout.print("Multiplication: {}\n", .{a * b});
    try stdout.print("Division: {}\n", .{@divTrunc(a, b)});
    try stdout.print("Modulus: {}\n", .{@mod(a, b)});

    const x: f64 = 10.0;
    const y: f64 = 3.0;
    try stdout.print("Float division: {d:.2}\n", .{x / y});
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
Sum: 13
Difference: 7
Product: 30
Quotient: 3.33
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

- Arithmetic operators work like a calculator
- Order of operations matters (PEMDAS)
- Integer division vs float division produces different results
- Modulus (%) gives the remainder after division

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

    const a: i32 = 10;
    const b: i32 = 3;

    try stdout.print("Addition: {}\n", .{a + b});
    try stdout.print("Subtraction: {}\n", .{a - b});
    try stdout.print("Multiplication: {}\n", .{a * b});
    try stdout.print("Division: {}\n", .{@divTrunc(a, b)});
    try stdout.print("Modulus: {}\n", .{@mod(a, b)});

    const x: f64 = 10.0;
    const y: f64 = 3.0;
    try stdout.print("Float division: {d:.2}\n", .{x / y});
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
