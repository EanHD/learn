# Level 3: Basic Math Operations

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.ts` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Master arithmetic operations and use the language as your calculator.

---

### Learning Goals

- Learn all basic arithmetic operators (+, -, *, /, %)
- Understand operator precedence (order of operations)
- Practice mathematical expressions
- Work with both integers and floating-point numbers

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.ts`**

```
const a: number = 15;
const b: number = 4;

console.log(`Addition: ${a} + ${b} = ${a + b}`);
console.log(`Subtraction: ${a} - ${b} = ${a - b}`);
console.log(`Multiplication: ${a} × ${b} = ${a * b}`);
console.log(`Division: ${a} / ${b} = ${a / b}`);
console.log(`Remainder: ${a} % ${b} = ${a % b}`);

const x: number = 15.0;
const y: number = 4.0;
console.log(`Precise Division: ${x} / ${y} = ${x / y}`);
```type

---

### Success Checklist

- [ ] Created a file named `main.ts`
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
const a: number = 15;
const b: number = 4;

console.log(`Addition: ${a} + ${b} = ${a + b}`);
console.log(`Subtraction: ${a} - ${b} = ${a - b}`);
console.log(`Multiplication: ${a} × ${b} = ${a * b}`);
console.log(`Division: ${a} / ${b} = ${a / b}`);
console.log(`Remainder: ${a} % ${b} = ${a % b}`);

const x: number = 15.0;
const y: number = 4.0;
console.log(`Precise Division: ${x} / ${y} = ${x / y}`);
```type

### What This Code Does

This program demonstrates basic math operations in TypeScript.

### Key Concepts

- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`
- **Integer Division**: Division with whole numbers
- **Floating-Point Division**: Division with decimals for precise results
- **Operator Precedence**: Order of operations (PEMDAS)

### Line-by-Line Breakdown

The code performs basic mathematical operations:

1. **Variable Declaration**: Store two numbers to work with
2. **Addition**: Adding two numbers together
3. **Subtraction**: Finding the difference between numbers
4. **Multiplication**: Multiplying numbers
5. **Division**: Dividing numbers (integer division)
6. **Remainder/Modulus**: Finding the remainder after division
7. **Precise Division**: Using decimals for accurate results

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Type error | Wrong data type | Ensure variables are correct type |
| Runtime error | Code runs but crashes | Check your logic and data flow |

### Bonus Knowledge

- The modulus operator (%) is useful for checking if numbers are even or odd
- Integer division truncates (removes) decimal places
- Always use floating-point numbers when precision matters
- Order of operations: Parentheses → Multiply/Divide → Add/Subtract

---

**Excellent work! You've mastered basic math operations!**

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
console.log("Hello, World!");

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard typescript conventions with proper imports and main function
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
