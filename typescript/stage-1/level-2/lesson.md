# Level 2: Variables

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Now that you know how to run Typescript programs, let's learn about variables! Variables are like containers that store information. Typescript makes it easy to work with different data types.

### Learning Goals

- Understand what variables are and why they're useful
- Learn about Typescript's data types
- Practice storing and displaying different types of data
- See how variables make code reusable

### Your Task

Copy the following code EXACTLY as shown into a new file called `variables.ts`:

```ts
const name: string = "Alice";
const age: number = 25;
const height: number = 5.6;
const isStudent: boolean = true;

console.log(`Hello, ${name}!`);
console.log(`You are ${age} years old.`);
console.log(`Your height is ${height} feet.`);
console.log(`Student status: ${isStudent}`);
```type

### How to Execute

```bash
ts-node variables.ts
```type

Expected output:

```typescript
Hello, Alice!
You are 25 years old.
Your height is 5.6 feet.
Student status: true
```type

### Success Checklist

- [ ] Created a file named `variables.ts`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Saw all four lines of output with the stored values

---

### What Happened?

You just used variables to store and display different types of information! Here's what each part does:

- String variables store text values
- Integer variables store whole numbers
- Float/Double variables store decimal numbers
- Boolean variables store true/false values

### Try This (Optional Challenges)

1. Change the name, age, height, and student status to your own information
2. Add a new variable for your favorite color and display it
3. Try changing a variable's value and see how the output changes

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to Typescript
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

```ts
console.log("Hello, World!");

```ts

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
