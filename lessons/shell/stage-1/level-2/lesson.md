# Level 2: Variables

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Now that you know how to run Shell programs, let's learn about variables! Variables are like containers that store information. Shell makes it easy to work with different data types.

### Learning Goals

- Understand what variables are and why they're useful
- Learn about Shell's data types
- Practice storing and displaying different types of data
- See how variables make code reusable

### Your Task

Copy the following code EXACTLY as shown into a new file called `variables.sh`:

```sh
#!/bin/bash
name="Alice"
age=25
height=5.6
isStudent=true

echo "Hello, $name!"
echo "You are $age years old."
echo "Your height is $height feet."
echo "Student status: $isStudent"
```

### How to Execute

```bash
bash variables.sh
```

Expected output:

```bash
Hello, Alice!
You are 25 years old.
Your height is 5.6 feet.
Student status: true
```

### Success Checklist

- [ ] Created a file named `variables.sh`
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

- Review the code structure specific to Shell
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**

