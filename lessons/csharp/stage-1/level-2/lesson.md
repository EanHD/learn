# Level 2: Variables

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.

## Stage 1: Copying Code

### Today's Mission

Now that you know how to run Csharp programs, let's learn about variables! Variables are like containers that store information. Csharp makes it easy to work with different data types.

### Learning Goals

- Understand what variables are and why they're useful
- Learn about Csharp's data types
- Practice storing and displaying different types of data
- See how variables make code reusable

### Your Task

Copy the following code EXACTLY as shown into a new file called `variables.cs`:

```
using System;

class Program {
 static void Main() {
 string name = "Alice";
 int age = 25;
 double height = 5.6;
 bool isStudent = true;

 Console.WriteLine($"Hello, {name}!");
 Console.WriteLine($"You are {age} years old.");
 Console.WriteLine($"Your height is {height} feet.");
 Console.WriteLine($"Student status: {isStudent}");
 }
}
```

### How to Execute

```
csc variables.cs
```

Expected output:

```
Hello, Alice!
You are 25 years old.
Your height is 5.6 feet.
Student status: true
```

### Success Checklist

- [ ] Created a file named `variables.cs`
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
