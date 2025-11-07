# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.ts` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Make your programs interactive by reading input from users.

---

### Learning Goals

- Learn how to read user input
- Understand input/output operations
- Practice with different data types from user
- Create interactive programs that respond to users

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.ts`**

```typescript
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter your name: ', (name: string) => {
    rl.question('Enter your age: ', (ageStr: string) => {
        const age: number = parseInt(ageStr);
        
        console.log(`Hello, ${name}!`);
        console.log(`You are ${age} years old.`);
        console.log(`Next year you'll be ${age + 1}.`);
        
        rl.close();
    });
});
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

```typescript
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter your name: ', (name: string) => {
    rl.question('Enter your age: ', (ageStr: string) => {
        const age: number = parseInt(ageStr);
        
        console.log(`Hello, ${name}!`);
        console.log(`You are ${age} years old.`);
        console.log(`Next year you'll be ${age + 1}.`);
        
        rl.close();
    });
});
```type

### What This Code Does

This program demonstrates user input in TypeScript.

### Key Concepts

- **User Input**: Reading data from the user
- **Input Methods**: Language-specific ways to get user input
- **Type Conversion**: Converting string input to numbers
- **String Concatenation**: Combining text with variables

### Line-by-Line Breakdown

The code creates an interactive program:

1. **Prompt for Name**: Ask the user for their name
2. **Read Name**: Store the user's input
3. **Prompt for Age**: Ask the user for their age
4. **Read Age**: Store and convert the age to a number
5. **Greet User**: Display personalized greeting
6. **Show Age**: Display the age back to the user
7. **Calculate**: Show age + 1 (next year's age)

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Type error | Wrong data type | Ensure variables are correct type |
| Runtime error | Code runs but crashes | Check your logic and data flow |

### Bonus Knowledge

- Always validate user input in production code
- Different languages have different input methods
- Type conversion can fail if user enters invalid data
- Consider what happens if user enters unexpected input

---

**Excellent work! You've mastered user input!**

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
