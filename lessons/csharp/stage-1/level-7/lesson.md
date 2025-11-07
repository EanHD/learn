# Level 7: Functions

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.cs` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.cs`**

```
using System;

class Program {
 static void Greet(string name) {
 Console.WriteLine($"Hello, {name}!");
 }
 
 static int Add(int a, int b) {
 return a + b;
 }
 
 static int Factorial(int n) {
 if (n <= 1) return 1;
 return n * Factorial(n - 1);
 }
 
 static void Main() {
 Greet("Alice");
 Greet("Bob");
 
 int sum = Add(15, 7);
 Console.WriteLine($"15 + 7 = {sum}");
 
 int fact = Factorial(5);
 Console.WriteLine($"5! = {fact}");
 }
}
```

---

### Success Checklist

- [ ] Created a file named `main.cs`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study after attempting!)

### The Complete Code

```
using System;

class Program {
 static void Greet(string name) {
 Console.WriteLine($"Hello, {name}!");
 }
 
 static int Add(int a, int b) {
 return a + b;
 }
 
 static int Factorial(int n) {
 if (n <= 1) return 1;
 return n * Factorial(n - 1);
 }
 
 static void Main() {
 Greet("Alice");
 Greet("Bob");
 
 int sum = Add(15, 7);
 Console.WriteLine($"15 + 7 = {sum}");
 
 int fact = Factorial(5);
 Console.WriteLine($"5! = {fact}");
 }
}
```

### What This Code Does

This program demonstrates functions in C#.

### Key Concepts

- **Functions**: Reusable blocks of code
- **Function Definition**: Creating a function with parameters
- **Function Calls**: Using a function by calling its name
- **Return Values**: Functions that give back a result
- **Recursion**: Functions that call themselves

### Line-by-Line Breakdown

The code organizes logic into functions:

1. **Greet Function**: Takes a name, displays greeting
2. **Add Function**: Takes two numbers, returns their sum
3. **Factorial Function**: Recursive function for factorial calculation
4. **Call Functions**: Use the functions in the main program
5. **Display Results**: Show the outputs of function calls

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Type error | Wrong data type | Ensure variables are correct type |
| Runtime error | Code runs but crashes | Check your logic and data flow |
| Compilation error | Code won't compile | Fix syntax before running |

### Bonus Knowledge

- Functions make code more organized and reusable
- Parameters pass data into functions
- Return values send data back from functions
- Recursive functions must have a base case to stop
- Good function names describe what they do

---

**Excellent work! You've mastered functions!**

*Continue to the next level to keep building your skills!*

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

```
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
