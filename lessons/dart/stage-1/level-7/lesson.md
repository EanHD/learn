# Level 7: Functions

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.dart` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.dart`**

```
void greet(String name) {
  print('Hello, $name!');
}

int add(int a, int b) {
  return a + b;
}

int factorial(int n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

void main() {
  greet('Alice');
  greet('Bob');

  int sum = add(15, 7);
  print('15 + 7 = $sum');

  int fact = factorial(5);
  print('5! = $fact');
}
```

---

### Success Checklist

- [ ] Created a file named `main.dart`
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
void greet(String name) {
  print('Hello, $name!');
}

int add(int a, int b) {
  return a + b;
}

int factorial(int n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}

void main() {
  greet('Alice');
  greet('Bob');

  int sum = add(15, 7);
  print('15 + 7 = $sum');

  int fact = factorial(5);
  print('5! = $fact');
}
```

### What This Code Does

This program demonstrates functions in Dart.

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
