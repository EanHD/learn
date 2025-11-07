# Level 1: Calculator Application

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window**. The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 4: Full Problem Solving

### Today's Mission

Now you're building real applications! This stage combines everything you've learned to create complete, working programs that solve real-world problems.

**The Process:**
1. Analyze the application requirements
2. Design the architecture and data flow
3. Implement features one by one
4. Test thoroughly with various inputs
5. Refine and optimize the solution

---

### Learning Goals

- Build complete, working applications
- Integrate multiple programming concepts
- Handle real-world requirements
- Practice debugging and testing
- Create user-friendly interfaces

---

### Your Task

**Application Requirements:**

Build a complete Calculator Application that supports basic arithmetic operations (addition, subtraction, multiplication, division). The calculator should provide a menu interface for users to select operations and input numbers.

**Application Specifications:**
- Support +, -, *, / operations
- Handle division by zero errors gracefully
- Allow users to perform multiple calculations in one session
- Validate numeric input and handle errors
- Display results with appropriate formatting
- Provide clear user interface with menu options

**Specific Features:**
- Menu system with operation choices
- Input validation and error handling
- Continuous operation until user exits
- Clear formatting of results

**Implementation Notes:**
- Use a main loop that continues until user chooses to exit
- Implement each operation in separate functions
- Handle potential errors like division by zero
- Format floating-point results appropriately

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

**Application Design:**
- Modular code is easier to debug
- User experience matters
- Error handling is not optional
- Test early and often

**Best Practices:**
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- Meaningful variable names
- Comments for complex logic

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

**Application Architecture:**

A complete calculator application has these components:

1. **Input Layer**: Menu selection and number input using `std.io`
2. **Validation Layer**: Check numeric input and division by zero
3. **Processing Layer**: Arithmetic operations in separate functions
4. **Output Layer**: Display results formatted properly
5. **Error Handling**: Manage division by zero and invalid input

**Zig Implementation:**
```zig
const std = @import("std");

// Function to perform addition
fn add(x: f64, y: f64) f64 {
    return x + y;
}

// Function to perform subtraction
fn subtract(x: f64, y: f64) f64 {
    return x - y;
}

// Function to perform multiplication
fn multiply(x: f64, y: f64) f64 {
    return x * y;
}

// Function to perform division with error checking
fn divide(x: f64, y: f64) !f64 {
    if (y == 0) {
        return error.DivisionByZero;
    }
    return x / y;
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const stdin = std.io.getStdIn().reader();
    
    var continue_calc: bool = true;
    var input_buf: [100]u8 = undefined;
    
    while (continue_calc) {
        // Display menu
        try stdout.print("\\n--- Calculator ---\\n", .{});
        try stdout.print("1. Add (+)\\n", .{});
        try stdout.print("2. Subtract (-)\\n", .{});
        try stdout.print("3. Multiply (*)\\n", .{});
        try stdout.print("4. Divide (/)\\n", .{});
        try stdout.print("5. Exit\\n", .{});
        try stdout.print("Choose operation (1-5): ", .{});
        
        // Get user choice
        _ = try stdin.readUntilDelimiterOrEof(&input_buf, '\n');
        const choice = std.fmt.parseInt(u8, std.mem.trimRight(u8, &input_buf, "\n\r"), 10) catch 0;
        
        if (choice == 5) {
            continue_calc = false;
            try stdout.print("Goodbye!\\n", .{});
            break;
        }
        
        if (choice < 1 or choice > 4) {
            try stdout.print("Invalid choice. Please select 1-5.\\n", .{});
            continue;
        }
        
        // Get numbers
        try stdout.print("Enter first number: ", .{});
        _ = try stdin.readUntilDelimiterOrEof(&input_buf, '\n');
        const num1 = std.fmt.parseFloat(f64, std.mem.trimRight(u8, &input_buf, "\n\r")) catch 0.0;
        
        try stdout.print("Enter second number: ", .{});
        _ = try stdin.readUntilDelimiterOrEof(&input_buf, '\n');
        const num2 = std.fmt.parseFloat(f64, std.mem.trimRight(u8, &input_buf, "\n\r")) catch 0.0;
        
        // Perform operation
        var result: f64 = 0.0;
        switch (choice) {
            1 => result = add(num1, num2),
            2 => result = subtract(num1, num2),
            3 => result = multiply(num1, num2),
            4 => {
                result = divide(num1, num2) catch {
                    try stdout.print("Error: Division by zero!\\n", .{});
                    continue;
                };
            },
            else => try stdout.print("Invalid operation\\n", .{}),
        }
        
        // Display result
        try stdout.print("Result: {d}\\n", .{result});
    }
}
```

Build incrementally - get one feature working before adding the next.

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
