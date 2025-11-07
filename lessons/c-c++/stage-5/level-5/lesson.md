# Level 5: Team Collaboration & Code Review

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.c` for C or `main.cpp` for C++). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

> **LANGUAGE CHOICE:** Remember, you can use **either C or C++** for this level. Choose what works best for your project!

## Stage 5: Capstone - Professional Development

### Today's Mission

Learn to **collaborate professionally** and **review code** like production teams do.

---

### Learning Goals

- [ ] Participate in **peer code reviews**
- [ ] Provide **constructive feedback**
- [ ] Implement **collaborative workflows**
- [ ] Manage **version control professionally**
- [ ] Document for **team understanding**

---

### Project Scope

**Focus**: Taking an existing project and preparing it for team collaboration

**Time Estimate**: 10-15 hours 
**Purpose**: Learn professional software development practices

---

### Collaboration Requirements

- [ ] Code review-ready documentation
- [ ] Clear commit history
- [ ] Contribution guidelines
- [ ] Issue templates and tracking
- [ ] Code style enforcement
- [ ] Peer feedback incorporation
- [ ] Team-ready architecture

---

### Key Skills

- [ ] Code review techniques
- [ ] Giving and receiving feedback
- [ ] Git workflows (branching, PRs)
- [ ] Documentation for teams
- [ ] Collaboration tools
- [ ] Conflict resolution
- [ ] Knowledge sharing

Ready to work with others professionally? 



### Your Task

1. Review the code structure
2. Implement the required functionality
3. Test your solution


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Success Checklist

- [ ] Code compiles without errors
- [ ] Output matches expected result
- [ ] All functions work correctly


### Additional Content

Understand the key concepts:

- [ ] Review each function
- [ ] Understand the flow
- [ ] Learn the patterns used


### Code Review

Key functions and their purpose:

- [ ] Main function: Entry point
- [ ] Helper functions: Support logic


<div style="page-break-after: always;"></div>

### Answer Key

### Complete Solution

```
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses std::cout to print messages to the console
3. **Standard Library**: Includes iostream for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `g++ hello.cpp -o hello`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: g++` | Compiler not installed | `sudo apt install g++` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: unknown type name 'cout'` | Missing iostream | Add `#include <iostream>` |

### Tips for Learning

- C++ is a superset of C with additional features
- `std::cout` is the C++ way to print (replaces `printf`)
- `std::endl` adds a newline and flushes the buffer
- The `std::` prefix means these are from the "standard" namespace
