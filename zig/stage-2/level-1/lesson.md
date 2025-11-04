# Level 1: Basic Algorithm Translation

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window**. The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 2: Pseudocode to Code

### Today's Mission

You've mastered the basics! Now you'll learn to translate written algorithms (pseudocode) into working Zig code. This is how professional programmers plan before coding.

**The Process:**
1. Read and understand the pseudocode algorithm
2. Identify the programming concepts needed
3. Translate each step into Zig syntax
4. Test and verify the implementation

---

### Learning Goals

- Master the translation of pseudocode to Zig
- Understand algorithm design patterns
- Practice with common programming patterns
- Build confidence in problem decomposition
- Learn to spot and fix logic errors

---

### Your Task

**Study the pseudocode algorithm below, then implement it in Zig:**

```zig
ALGORITHM: Greeting Generator

BEGIN
    INPUT: user's name (string)
    
    PROCESSING:
        1. Create a personalized greeting message
        2. Append the current date to the message  
        3. Calculate the length of the greeting
    
    OUTPUT: 
        - Display the personalized greeting
        - Show the length of the message
        - Print a border of asterisks matching the greeting length
END
```

**Implementation Steps:**
1. Declare variables to store the user's name and greeting
2. Implement the greeting message concatenation in Zig
3. Calculate string length using Zig's string functions
4. Print the greeting, length, and border of asterisks
5. Test with different names to verify functionality

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
- [ ] Implemented in Zig correctly
- [ ] Tested with multiple scenarios
- [ ] Code is clean and well-commented
- [ ] All requirements met
- [ ] Program runs without errors

---

### Key Concepts

**Pseudocode Translation:**
- Pseudocode is language-independent
- Focus on logic, not syntax
- One pseudocode line may become multiple code lines
- Test your understanding before coding

**Common Patterns:**
- Loops for repetition
- Conditionals for decisions
- Variables for data storage
- Functions for organization

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

**Pseudocode to Code Translation:**

The key is understanding what each pseudocode statement represents in Zig:

1. **Input**: `INPUT: user's name` → `std.io.getStdIn().reader()` for reading
2. **Assignment**: `SET x TO 5` → `x = 5` (or `var x: type = 5`)
3. **String operations**: `append text` → `std.fmt.allocPrint()` for concatenation
4. **Output**: `PRINT value` → `std.io.getStdOut().writer().print()`
5. **Calculation**: `calculate length` → `string.len` property

**Zig Implementation:**
```zig
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    
    // Sample name (in a complete program, you'd get user input)
    const name = "Alex";
    
    // Create personalized greeting
    var greeting = try std.fmt.allocPrint(std.heap.page_allocator, "Hello, {s}! Welcome!", .{name});
    defer std.heap.page_allocator.free(greeting);
    
    // Calculate length
    const greeting_length = greeting.len;
    
    // Print greeting
    try stdout.print("{s}\n", .{greeting});
    try stdout.print("Message length: {d} characters\n", .{greeting_length});
    
    // Print border of asterisks
    var i: usize = 0;
    while (i < greeting_length) : (i += 1) {
        try stdout.print("*", .{});
    }
    try stdout.print("\n", .{});
}
```

This translates the pseudocode algorithm into proper Zig syntax.

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
