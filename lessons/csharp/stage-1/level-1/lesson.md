# Level 1: Hello World

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.

## Stage 1: Copying Code

### Today's Mission

Welcome to C#! Today, you'll create your first C# program. C# is a modern, object-oriented language from Microsoft used for .NET development, game development with Unity, and web applications.

### Learning Goals

- Understand C# program structure
- Learn how to compile and run C#
- Create your first output
- Get comfortable with C# syntax

### Your Task

Copy the following code EXACTLY as shown into a new file called `hello.cs`:

```csharp
using System;

class Program {
 static void Main() {
 Console.WriteLine("Hello, World!");
 }
}
```csharp

### How to Execute

```bash
csc hello.cs
./hello.exe
```csharp

Expected output:

```csharp
Hello, World!
```csharp

### Success Checklist

- [ ] Created a file named `hello.cs`
- [ ] Copied the code exactly as shown
- [ ] Program compiled without errors
- [ ] Saw "Hello, World!" printed

---

**C# is elegant, powerful, and runs on the .NET platform!**

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

### Key Concepts

- Review the code structure specific to Csharp
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**

### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim

### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used

### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```cs
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard csharp conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
