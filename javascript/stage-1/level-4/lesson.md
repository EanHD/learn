# Level 4: User Input

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Now let's make our programs interactive! Today you'll learn how to get input from users and respond to their information. This is where programs become truly useful!

---

### Learning Goals

- Learn how to get input from users
- Understand the readline-sync module for synchronous input
- Practice creating interactive programs
- Learn to combine input with variables and math
- Handle different types of user input

---

### Your Task

**First, install the readline-sync module (if not already installed):**

```bash
npm install readline-sync
```

**Then copy the following code into a new file called `input.js`**

```javascript
// Import the readline-sync module for user input
const readlineSync = require('readline-sync');

console.log("=== Interactive Greeting Program ===");
// Get input from user
let name = readlineSync.question("What's your name? ");
console.log("Hello, " + name + "! Nice to meet you!");

console.log("");
console.log("=== Simple Calculator ===");
// Get two numbers from user
let num1 = parseFloat(readlineSync.question("Enter first number: "));
let num2 = parseFloat(readlineSync.question("Enter second number: "));

// Perform calculations
let sum = num1 + num2;
let difference = num1 - num2;
let product = num1 * num2;
let quotient = num1 / num2;

// Display results
console.log(num1 + " + " + num2 + " = " + sum);
console.log(num1 + " - " + num2 + " = " + difference);
console.log(num1 + " * " + num2 + " = " + product);
console.log(num1 + " / " + num2 + " = " + quotient);

console.log("");
console.log("=== Age Calculator ===");
// Ask for birth year and calculate age
let birthYear = parseInt(readlineSync.question("What year were you born? "));
let currentYear = new Date().getFullYear();  // Get current year automatically
let age = currentYear - birthYear;

console.log("If you were born in " + birthYear + ", you are about " + age + " years old.");

console.log("");
console.log("=== Simple Quiz ===");
// Create a simple quiz
let answer = readlineSync.question("What is the capital of France? ");
if (answer.toLowerCase() === "paris") {
    console.log("Correct! Well done!");
} else {
    console.log("Not quite! The answer is Paris.");
}

console.log("");
console.log("=== Yes/No Question ===");
// Get a yes/no response
let likePizza = readlineSync.keyInYN("Do you like pizza? ");
if (likePizza) {
    console.log("Great! Pizza lovers unite!");
} else {
    console.log("That's okay, there are other foods to enjoy!");
}

console.log("");
console.log("=== Choose an Option ===");
// Multiple choice
let choices = ['Red', 'Blue', 'Green', 'Yellow'];
let index = readlineSync.keyInSelect(choices, 'What is your favorite color?');
if (index > -1) {
    console.log("You selected: " + choices[index]);
} else {
    console.log("You didn't select anything!");
}
```

**Note:** If you don't want to install readline-sync, you can create a simpler version that demonstrates the concept without user interaction by replacing the input with preset values. Create an alternate version in `simple_input.js`:

```javascript
// This is a simplified version that doesn't require user input
// We'll simulate user answers with predefined values

console.log("=== Interactive Greeting Program ===");
// Simulated user input
let name = "Alex";
console.log("What's your name? " + name);  // Simulated input
console.log("Hello, " + name + "! Nice to meet you!");

console.log("");
console.log("=== Simple Calculator ===");
// Simulated user inputs
let num1 = 10;
let num2 = 5;
console.log("Enter first number: " + num1);  // Simulated input
console.log("Enter second number: " + num2);  // Simulated input

// Perform calculations
let sum = num1 + num2;
let difference = num1 - num2;
let product = num1 * num2;
let quotient = num1 / num2;

// Display results
console.log(num1 + " + " + num2 + " = " + sum);
console.log(num1 + " - " + num2 + " = " + difference);
console.log(num1 + " * " + num2 + " = " + product);
console.log(num1 + " / " + num2 + " = " + quotient);

console.log("");
console.log("=== Age Calculator ===");
// Simulated input
let birthYear = 1990;
console.log("What year were you born? " + birthYear);  // Simulated input
let currentYear = new Date().getFullYear();  // Get current year automatically
let age = currentYear - birthYear;

console.log("If you were born in " + birthYear + ", you are about " + age + " years old.");

console.log("");
console.log("=== Simple Quiz ===");
// Simulated answer
let answer = "Paris";
console.log("What is the capital of France? " + answer);  // Simulated input
if (answer.toLowerCase() === "paris") {
    console.log("Correct! Well done!");
} else {
    console.log("Not quite! The answer is Paris.");
}
```

---

### How to Execute

**For the full interactive version:**
1. **Install readline-sync** (if not already installed):
   ```bash
   npm install readline-sync
   ```
2. **Run your program**:
   ```bash
   node input.js
   ```

**For the simplified version (no installation needed):**
1. **Run your program**:
   ```bash
   node simple_input.js
   ```

---

### Success Checklist

- [ ] Created file(s) named `input.js` (and optionally `simple_input.js`)
- [ ] For interactive version: installed readline-sync module
- [ ] For interactive version: program executed without errors
- [ ] For simplified version: ran successfully without modules
- [ ] Saw programs respond to input appropriately
- [ ] Understood how to get input from users

---

### What You Learned!

- **`readlineSync.question()`** = Gets text input from user
- **`readlineSync.keyInYN()`** = Gets yes/no answer from user
- **`readlineSync.keyInSelect()`** = Gets choice from a list
- **`parseInt()`** = Converts string to integer
- **`parseFloat()`** = Converts string to floating-point number
- **Input validation** = Converting strings to the right data type

---

### Try This (Optional Challenges)

1. Create a BMI calculator that asks for height and weight
2. Make a basic chatbot that responds to different inputs
3. Create a simple math quiz with multiple questions
4. Build a program that converts temperatures based on user input

---

## Quick Reference

| Method | Purpose | Example | Notes |
|--------|---------|---------|-------|
| `readlineSync.question()` | Get text input | `let name = readlineSync.question("Name? ")` | Returns string |
| `readlineSync.keyInYN()` | Get yes/no answer | `let answer = readlineSync.keyInYN("Continue? ")` | Returns boolean |
| `readlineSync.keyInSelect()` | Choose from list | `let choice = readlineSync.keyInSelect(['A','B'], 'Choose: ')` | Returns index |
| `parseInt()` | Convert to integer | `let num = parseInt("42")` | Use for whole numbers |
| `parseFloat()` | Convert to decimal | `let num = parseFloat("42.5")` | Use for decimal numbers |
| `String()` | Convert to string | `let text = String(42)` | Convert number to string |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```javascript
const readlineSync = require('readline-sync');
```
- **`const`** = Declares a constant (value that won't change)
- **`require()`** = Imports external module functionality
- **`'readline-sync'`** = The module name we want to import
- This module allows us to get user input synchronously (waits for input before continuing)

```javascript
let name = readlineSync.question("What's your name? ");
```
- **`readlineSync.question()`** = Method to get text input from user
- **`"What's your name? "`** = Prompt message shown to user
- **Returns a string** containing whatever the user typed

```javascript
let num1 = parseFloat(readlineSync.question("Enter first number: "));
```
- **`parseFloat()`** = Converts string to floating-point number
- **Necessary** because `readlineSync.question()` returns a string, but we want to do math
- **`parseInt()`** = For integers (whole numbers only)
- **`parseFloat()`** = For numbers with decimal points

### Alternative Input Methods

**In Browser Environment (HTML):**
```html
<!DOCTYPE html>
<html>
<body>
  <script>
    let name = prompt("What's your name? ");
    alert("Hello, " + name + "!");
  </script>
</body>
</html>
```

**Command Line Arguments:**
```javascript
// Access arguments passed to node: `node program.js arg1 arg2`
let name = process.argv[2];  // First argument after filename
console.log("Hello, " + name + "!");
```

### Data Type Conversion

JavaScript is dynamically typed, but we still need to convert strings to numbers for math:

```javascript
// Without conversion - concatenation instead of addition!
let str1 = "5";
let str2 = "3";
console.log(str1 + str2);  // Output: "53" (not 8!)

// With conversion - proper mathematical addition
let num1 = parseFloat("5");
let num2 = parseFloat("3");
console.log(num1 + num2);  // Output: 8
```

### Error Handling for Input

Real programs need to handle invalid input:

```javascript
let userInput = readlineSync.question("Enter a number: ");
let number = parseFloat(userInput);

if (isNaN(number)) {  // Check if it's Not-a-Number
    console.log("That's not a valid number!");
} else {
    console.log("You entered: " + number);
}
```

### readline-sync Methods

**Text Input:**
```javascript
// Get any text
let name = readlineSync.question("Name: ");

// Get text with masking (good for passwords)
let password = readlineSync.question("Password: ", {hideEchoBack: true});
```

**Yes/No Questions:**
```javascript
// Returns true for yes/y/Y, false for no/n/N
let continue = readlineSync.keyInYN("Continue? ");
if (continue) {
    console.log("Continuing...");
} else {
    console.log("Exiting...");
}
```

**Multiple Choice:**
```javascript
let colors = ['Red', 'Blue', 'Green'];
let index = readlineSync.keyInSelect(colors, 'Choose a color: ');

if (index > -1) {  // -1 means no selection
    console.log("You chose: " + colors[index]);
}
```

### Date and Time in JavaScript

```javascript
// Get current date and time
let now = new Date();
console.log(now);  // Full date/time

// Get specific parts
let currentYear = now.getFullYear();  // 2025 (or current year)
let currentMonth = now.getMonth() + 1;  // 0-11, so add 1 for 1-12
let currentDay = now.getDate();  // 1-31
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ReferenceError: require is not defined` | Using require in browser | Use Node.js instead of browser |
| `Error: Cannot find module 'readline-sync'` | Module not installed | Run `npm install readline-sync` |
| `undefined` results | Forgetting to assign input | Make sure to use `let variable = ...` |
| Math errors with string input | Not converting strings to numbers | Use `parseInt()` or `parseFloat()` |
| `NaN` results | Invalid number conversion | Check input before converting |

### Best Practices for Input

**Always validate user input:**
```javascript
let userInput = readlineSync.question("Enter age: ");
let age = parseInt(userInput);

// Validate the input
if (isNaN(age) || age < 0 || age > 150) {
    console.log("Please enter a valid age between 0 and 150");
} else {
    console.log("You are " + age + " years old");
}
```

**Handle different string cases:**
```javascript
let answer = readlineSync.question("Yes or No? ");
if (answer.toLowerCase() === "yes" || answer.toLowerCase() === "y") {
    console.log("You said yes!");
}
```

### Security Considerations

When accepting user input, be aware of potential security issues:
- **Injection attacks**: Don't execute user input as code
- **Validation**: Always validate and sanitize input
- **Length limits**: Set reasonable limits on input length

### Advanced Challenge (For the Brave!)

Try this full interactive program:

```javascript
const readlineSync = require('readline-sync');

console.log("=== Personal Finance Calculator ===");

// Get user's income
let monthlyIncome = parseFloat(readlineSync.question("Enter your monthly income: $"));

// Get expenses
let rent = parseFloat(readlineSync.question("Enter monthly rent: $"));
let groceries = parseFloat(readlineSync.question("Enter monthly grocery cost: $"));
let utilities = parseFloat(readlineSync.question("Enter monthly utilities: $"));
let transportation = parseFloat(readlineSync.question("Enter monthly transportation: $"));

// Calculate totals
let totalExpenses = rent + groceries + utilities + transportation;
let remaining = monthlyIncome - totalExpenses;
let savingsPercentage = (remaining / monthlyIncome) * 100;

// Display results
console.log("");
console.log("=== FINANCIAL SUMMARY ===");
console.log("Monthly Income: $" + monthlyIncome.toFixed(2));
console.log("Total Expenses: $" + totalExpenses.toFixed(2));
console.log("Remaining: $" + remaining.toFixed(2));
console.log("Savings Rate: " + savingsPercentage.toFixed(1) + "%");

if (remaining > 0) {
    console.log("Great! You're saving money each month.");
} else {
    console.log("You're spending more than you earn. Consider reducing expenses.");
}
```

---

 **Excellent work! You now know how to make interactive programs that respond to user input!** 

*Ready for the next challenge? Let's make programs that make decisions!*