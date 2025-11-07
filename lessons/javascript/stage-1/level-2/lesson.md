# Level 2: Variables and Data Types

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the world of variables! Today you'll learn how to store and use data in your JavaScript programs. Variables are like labeled boxes where you can store information - numbers, text, and more!

---

### Learning Goals

- Understand what variables are and why we need them
- Learn basic data types (string, number, boolean)
- Practice declaring and initializing variables
- Learn how to display variable values
- Understand JavaScript's dynamic typing system

---

### Your Task

**Copy the following code into a new file called `variables.js`**

```
// String variables (text)
let name = "Alex";
let city = "New York";
let hobby = "programming";

// Number variables (integers and decimals)
let age = 25;
let height = 175.5;
let score = 100;

// Boolean variables (true/false)
let isStudent = true;
let isEmployed = false;
let isHappy = true;

// Print all the variables
console.log("=== Personal Info ===");
console.log("Name: " + name);
console.log("City: " + city);
console.log("Hobby: " + hobby);
console.log("");

console.log("=== Measurements ===");
console.log("Age: " + age + " years old");
console.log("Height: " + height + " cm");
console.log("Score: " + score + " points");
console.log("");

console.log("=== Status ===");
console.log("Student: " + isStudent);
console.log("Employed: " + isEmployed);
console.log("Happy: " + isHappy);

// JavaScript's dynamic typing - variables can change types!
console.log("");
console.log("=== Dynamic Typing Example ===");
let dynamicVar = "I'm a string";
console.log("Dynamic variable: " + dynamicVar);
dynamicVar = 42;  // Now it's a number!
console.log("Dynamic variable: " + dynamicVar);
dynamicVar = true; // Now it's a boolean!
console.log("Dynamic variable: " + dynamicVar);
```

---

### How to Execute

1. **Run your program**:
   ```
   node variables.js
   ```

**Expected output:**
```
=== Personal Info ===
Name: Alex
City: New York
Hobby: programming

=== Measurements ===
Age: 25 years old
Height: 175.5 cm
Score: 100 points

=== Status ===
Student: true
Employed: false
Happy: true

=== Dynamic Typing Example ===
Dynamic variable: I'm a string
Dynamic variable: 42
Dynamic variable: true
```

---

### Success Checklist

- [ ] Created a file named `variables.js`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw all variable values printed correctly
- [ ] Understood how JavaScript variables work

---

### What You Learned!

JavaScript has several important concepts about variables:

- **`let`** = Declares a variable that can be reassigned
- **`const`** = Declares a constant that cannot be changed (we'll see this later)
- **Dynamic typing** = Variables can hold any type of value and change type during execution
- **String concatenation** = Using `+` to combine strings and variables

---

### Try This (Optional Challenges)

1. Change all the variable values to your own information
2. Add new variables for your favorite food and favorite color
3. Try creating a variable that combines multiple pieces of information
4. What happens if you add a number and a string together?

---

## Quick Reference

| Data Type | What it holds | Examples | Example Declaration |
|-----------|---------------|----------|-------------------|
| `string` | Text | "Hello", "JavaScript", "123" | `let name = "Alex";` |
| `number` | Integers and decimals | 42, -17, 3.14, 0 | `let age = 25;` |
| `boolean` | True/false values | true, false | `let isStudent = true;` |
| `undefined` | No value assigned | undefined | `let emptyVar;` |
| `null` | Intentionally empty value | null | `let empty = null;` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```
// String variables (text)
let name = "Alex";
```
- **`//`** = Single-line comment (ignored by computer)
- **`let`** = Keyword to declare a variable that can be reassigned
- **`name`** = Variable name (follows naming rules)
- **`=`** = Assignment operator (stores value on right into variable on left)
- **`"Alex"`** = String value (text in quotes)
- **`;`** = End of statement

```
let age = 25;
```
- **`age`** = Variable name (numeric variable)
- **`25`** = Number value (no quotes needed for numbers)
- JavaScript treats integers and decimals the same way

```
let isStudent = true;
```
- **`isStudent`** = Boolean variable name (descriptive naming)
- **`true`** = Boolean value (one of only two possible values: true or false)

```
console.log("Name: " + name);
```
- **`+`** = String concatenation operator (joins strings together)
- The variable `name` gets its value inserted into the output string

### Variable Declaration Methods in JavaScript

JavaScript has three main ways to declare variables:

1. **`var`** - The old way (avoid in modern code)
2. **`let`** - Modern way for variables that change
3. **`const`** - For variables that won't change

```
// var (old style - avoid)
var oldStyle = "Don't use this much anymore";

// let (modern - for variables that might change)
let canChange = "This value can be updated later";

// const (modern - for constants that won't change)
const neverChanges = "This value cannot be changed";
```

### Variable Naming Rules

**Valid names**: `name`, `myAge`, `age1`, `student_score`, `studentScore`
**Invalid names**: `123age`, `my-age`, `let`, `age score`

**Rules to remember:**
1. Start with letter, underscore (_), or dollar sign ($)
2. Use only letters, numbers, and underscores after the first character
3. Can't use reserved keywords (`let`, `const`, `var`, `true`, `false`, etc.)
4. Case sensitive (`age` ≠ `Age` ≠ `AGE`)

### Data Types Deep Dive

| Type | Description | Examples |
|------|-------------|----------|
| `string` | Text data | `"Hello"`, `'JavaScript'`, `"123"` |
| `number` | Numeric data | `42`, `-17`, `3.14159`, `0` |
| `boolean` | Logical values | `true`, `false` |
| `undefined` | Declared but no value assigned | `let x; console.log(x);` → `undefined` |
| `null` | Intentionally empty value | `let y = null;` |
| `object` | Complex data structures | Arrays, objects, dates |
| `symbol` | Unique identifiers | Advanced feature |
| `bigint` | Very large integers | Advanced feature |

### Dynamic Typing Explained

JavaScript is dynamically typed, meaning:

```
let dynamic = "I start as a string";
console.log(typeof dynamic);  // Output: "string"

dynamic = 42;  // Now it's a number
console.log(typeof dynamic);  // Output: "number"

dynamic = true;  // Now it's a boolean
console.log(typeof dynamic);  // Output: "boolean"
```

This is different from statically typed languages like C/C++ where you must declare the type in advance.

### String Concatenation Methods

There are multiple ways to combine strings:

```
let firstName = "John";
let lastName = "Doe";

// Method 1: Plus operator (what we used)
console.log("Full name: " + firstName + " " + lastName);

// Method 2: Template literals (modern approach)
console.log(`Full name: ${firstName} ${lastName}`);

// Method 3: concat() method
console.log("Full name: ".concat(firstName, " ", lastName));
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ReferenceError: name is not defined` | Variable doesn't exist | Check spelling, make sure it's declared |
| `SyntaxError` | Missing semicolon, bracket, or quote | Check syntax carefully |
| `TypeError` | Using wrong type of value | Verify data types match usage |
| `undefined` output | Variable declared but not assigned | Assign a value before using |

### Bonus Knowledge

- **JavaScript vs ECMAScript**: JavaScript is the language; ECMAScript is the standard that defines it
- **Hoisting**: `var` declarations are "hoisted" to the top of their scope (but not `let`/`const`)
- **typeof operator**: Use `typeof variable` to check what type of value a variable holds
- **camelCase**: JavaScript convention for variable names (firstName, not first_name or FirstName)

### Advanced Challenge (For the Brave!)

Try this modified version:

```
// Let's do some calculations with variables!
const currentYear = 2025;
let birthYear = 2000;
let calculatedAge = currentYear - birthYear;

console.log("Born in " + birthYear + ", now it's " + currentYear);
console.log("Calculated age: " + calculatedAge + " years old");

// Working with strings
let firstName = "Jane";
let lastName = "Smith";
let fullName = firstName + " " + lastName;

console.log("Full name: " + fullName);

// JavaScript's type conversion
console.log("Number and string: " + (5 + "3"));  // Output: "53"
console.log("Number math: " + (5 + 3));          // Output: "8"
```

---

 **Excellent work! You now understand variables - the foundation of all programming!**

*Ready for the next challenge? Let's do some math with our variables!*


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
