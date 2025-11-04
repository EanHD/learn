# Level 1: Simple Problem Analysis

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window**. The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 3: Problem to Pseudocode

### Today's Mission

Time to think like a programmer! You'll analyze real problems and design solutions using pseudocode before writing any code. This is the most important skill in programming.

**The Process:**
1. Read and understand the problem requirements
2. Break the problem into smaller sub-problems
3. Design an algorithm in pseudocode
4. Identify edge cases and constraints
5. Implement the solution in Zig

---

### Learning Goals

- Develop problem analysis skills
- Learn to design algorithms before coding
- Practice breaking complex problems into steps
- Master pseudocode notation and planning
- Understand edge cases and constraints

---

### Your Task

**Problem Statement:**

Create a temperature conversion tool that allows users to convert between Celsius and Fahrenheit. The program should provide a simple menu interface where users can choose the conversion direction and input the temperature value.

**Your Process:**
1. **Understand**: 
   - Input: Temperature value and conversion choice (C→F or F→C)
   - Output: Converted temperature value
   - Formulas: C to F: (C * 9/5) + 32, F to C: (F - 32) * 5/9
2. **Plan**: Write pseudocode outlining your approach
3. **Code**: Implement your design in Zig
4. **Test**: Verify with multiple test cases
5. **Refine**: Optimize and improve

**Deliverables:**
- Written pseudocode (comments in your code)
- Working Zig implementation
- Test cases showing it works (0°C = 32°F, 100°C = 212°F)

---


### How to Compile and Run

1. **Compile the code**:
   ```bash
   zig build-exe hello.zig
   ```

2. **Run your program**:
   ```bash
   ./hello hello
   ```

**Expected output:**
```
Hello, World!
```

### How to Approach This

**Step 1: Understand**
- Read all requirements carefully
- Identify inputs, outputs, and constraints
- Ask yourself: "What is the core problem?"

**Step 2: Plan**
- Sketch out your approach on paper
- List the steps needed
- Identify potential challenges

**Step 3: Implement**
- Start with a basic version
- Add features incrementally
- Test after each addition

**Step 4: Test**
- Try normal cases
- Try edge cases (empty, max, min)
- Try invalid inputs
- Verify all requirements met

**Step 5: Refine**
- Review your code
- Add comments
- Optimize if needed
- Ensure it's readable

---

### Success Checklist

- [ ] Understood the problem/requirements completely
- [ ] Designed a solution approach
- [ ] Wrote pseudocode or algorithm design
- [ ] Implemented in Zig correctly
- [ ] Tested with multiple scenarios
- [ ] Code is clean and well-commented
- [ ] All requirements met
- [ ] Program runs without errors

---

### Key Concepts

**Problem Decomposition:**
- Break big problems into smaller ones
- Solve each part individually
- Combine solutions together
- Always start simple, then expand

**Algorithm Design:**
- Clear input/output definition
- Step-by-step logic
- Consider edge cases
- Plan before coding

---

### Try This (Optional Challenges)

1. Extend the solution with additional features
2. Handle more edge cases
3. Optimize for performance
4. Add a user interface
5. Write unit tests

---

### Helpful Resources

- Review previous lessons for syntax help
- Check WORKSPACE_INSTRUCTIONS.md for setup
- Use `<Space>h` in Vim for keyboard shortcuts
- Test frequently to catch errors early

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study after attempting!)

### Solution Approach

**Problem-Solving Framework:**

1. **Input Analysis**: Temperature value and conversion direction (C→F or F→C)
2. **Output Requirements**: Converted temperature value in the target unit
3. **Process Design**: Apply conversion formulas based on user choice
4. **Edge Cases**: Invalid input values, non-numeric input

**Pseudocode Design:**
```zig
ALGORITHM: Temperature Converter
INPUT: temperature value (number), conversion choice (C or F)
OUTPUT: converted temperature value

BEGIN
    1. Display menu: Convert C to F (choice 1) or F to C (choice 2)
    2. Get user's choice
    3. Get temperature value from user
    4. IF choice is 1 (C to F)
        THEN apply formula: (C * 9/5) + 32
    5. ELSE IF choice is 2 (F to C) 
        THEN apply formula: (F - 32) * 5/9
    6. Display result
END
```

**Zig Implementation:**
```zig
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const stdin = std.io.getStdIn().reader();
    
    try stdout.print("Temperature Converter\\n", .{});
    try stdout.print("1. Celsius to Fahrenheit\\n", .{});
    try stdout.print("2. Fahrenheit to Celsius\\n", .{});
    try stdout.print("Choose (1 or 2): ", .{});
    
    var buf: [10]u8 = undefined;
    _ = try stdin.readUntilDelimiterOrEof(&buf, '\n');
    
    const choice = std.fmt.parseInt(u8, std.mem.trimRight(u8, &buf, "\n\r"), 10) catch 0;
    
    try stdout.print("Enter temperature: ", .{});
    _ = try stdin.readUntilDelimiterOrEof(&buf, '\n');
    const temp = std.fmt.parseFloat(f64, std.mem.trimRight(u8, &buf, "\n\r")) catch 0.0;
    
    var result: f64 = 0.0;
    if (choice == 1) {
        result = (temp * 9.0 / 5.0) + 32.0;
        try stdout.print("{d}°C = {d}°F\\n", .{ temp, result });
    } else if (choice == 2) {
        result = (temp - 32.0) * 5.0 / 9.0;
        try stdout.print("{d}°F = {d}°C\\n", .{ temp, result });
    } else {
        try stdout.print("Invalid choice!\\n", .{});
    }
}
```

Then translate this directly to Zig code.

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Logic error | Algorithm design flaw | Review pseudocode, trace by hand |
| Syntax error | Language rules violated | Check language documentation |
| Runtime error | Invalid operation | Add validation, handle edge cases |
| Wrong output | Misunderstanding requirements | Re-read problem carefully |

### Next Steps

1. Review your solution critically
2. Compare with best practices
3. Optimize if needed
4. Move to next level when ready
5. Keep practicing!

---

**Excellent work on this advanced challenge!**

*Continue building your skills - you're doing great!*
