# Level 2: Variables and Data Types

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.zig` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Learn how to store and work with different types of data in Zig.

---

### Learning Goals

- Understand variables and data types
- Learn to declare and initialize variables
- Practice with numbers, strings, and other types
- Display variable values to the screen

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.zig`**

```
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    // Integer variables
    const age: i32 = 25;
    const score: i32 = 100;

    // Floating point
    const price: f64 = 29.99;

    // String
    const name = "Alex";

    // Display
    try stdout.print("Name: {s}\n", .{name});
    try stdout.print("Age: {}\n", .{age});
    try stdout.print("Price: ${d:.2}\n", .{price});
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
Name: Alex
Age: 25
Price: $29.99
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

- Variables store data for later use
- Different data types (integers, floats, strings) serve different purposes
- You can perform operations on variables
- Displaying variables shows their current values

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

    // Integer variables
    const age: i32 = 25;
    const score: i32 = 100;

    // Floating point
    const price: f64 = 29.99;

    // String
    const name = "Alex";

    // Display
    try stdout.print("Name: {s}\n", .{name});
    try stdout.print("Age: {}\n", .{age});
    try stdout.print("Price: ${d:.2}\n", .{price});
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
