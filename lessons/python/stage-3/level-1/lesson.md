# Level 1: Greeting Problem

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 3: Problem to Pseudocode

### Today's Mission

Now you'll design solutions before coding! You'll read a problem description, design the solution in pseudocode, then implement it. This is how professional programmers work!

---

### Your Problem

Write a program that:

1. Asks the user for their name
2. Asks for their favorite color
3. Prints a message like: "Hi {name}, I like {color} too!"

Example: User enters "Alice" and "blue"

```
Hi Alice, I like blue too!
```

---

### Your Task

1. First, write pseudocode that solves this problem
2. Then, translate it to Python code
3. Test it with different inputs

**Hints for Pseudocode:**

- Use print for output
- Use input for getting data
- Use + for joining strings

---

### How to Run

Navigate to your workspace and run your solution.

---

### Success Checklist

- [ ] Program asks for name
- [ ] Program asks for color
- [ ] Output follows the format exactly
- [ ] Works with any name/color input
- [ ] Program runs without errors

---

## ANSWER KEY

### Pseudocode

```text
START
    print "What is your name?"
    name = get input from user
    print "What is your favorite color?"
    color = get input from user
    print "Hi " + name + ", I like " + color + " too!"
END
```

### Python Solution

```
print("What is your name?")
name = input()
print("What is your favorite color?")
color = input()
print("Hi " + name + ", I like " + color + " too!")
```

### Explanation

This problem requires:

- Two `input()` calls to get user data
- Variable storage of both inputs
- String concatenation to build output message
- Clear prompts for user

---

**You're designing solutions now - that's real programming!**

*Next up: Number problems!*


### Learning Goals

- Understand core concepts
- Practice implementation


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

```py
print("Hello, World!")

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard python conventions with proper imports and main function
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
