# Level 7: Functions

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.zig` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Organize your code into reusable functions/methods.

---

### Learning Goals

- Understand function concepts and modularity
- Learn to define and call functions
- Practice with parameters and return values
- Create organized, maintainable code

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.zig`**

```
const std = @import("std");

fn greet(name: []const u8) !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello, {s}!\n", .{name});
}

fn add(a: i32, b: i32) i32 {
    return a + b;
}

fn factorial(n: i32) i64 {
    var result: i64 = 1;
    var i: i32 = 1;
    while (i <= n) : (i += 1) {
        result *= i;
    }
    return result;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    try greet("Alice");
    try greet("Bob");

    const sum = add(5, 3);
    try stdout.print("5 + 3 = {}\n", .{sum});

    try stdout.print("5! = {}\n", .{factorial(5)});
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
Result: 15
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

- Functions organize code into reusable blocks
- Parameters pass data into functions
- Return values send data back from functions
- Functions make code more maintainable and testable

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

fn greet(name: []const u8) !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello, {s}!\n", .{name});
}

fn add(a: i32, b: i32) i32 {
    return a + b;
}

fn factorial(n: i32) i64 {
    var result: i64 = 1;
    var i: i32 = 1;
    while (i <= n) : (i += 1) {
        result *= i;
    }
    return result;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    try greet("Alice");
    try greet("Bob");

    const sum = add(5, 3);
    try stdout.print("5 + 3 = {}\n", .{sum});

    try stdout.print("5! = {}\n", .{factorial(5)});
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
