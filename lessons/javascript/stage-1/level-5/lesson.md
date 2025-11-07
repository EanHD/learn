# Level 5: Conditionals and Decision Making

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to make programs that can make decisions! Today you'll learn how to write code that does different things based on different conditions. This is where programs become truly intelligent!

---

### Learning Goals

- Understand if/else statements and decision making
- Learn comparison operators (==, ===, !=, !==, <, >, <=, >=)
- Practice logical operators (&&, ||, !)
- Create programs that respond differently to different inputs
- Learn to chain multiple conditions together

---

### Your Task

**Copy the following code into a new file called `conditionals.js`**

```
console.log("=== Simple Age Check ===");
// Input for age
let age = 20;

if (age >= 18) {
    console.log("You are an adult (18 or older)");
} else {
    console.log("You are a minor (under 18)");
}

console.log("");
console.log("=== Grade Classifier ===");
// Input for grade
let grade = 85;

if (grade >= 90) {
    console.log("Grade: A (90-100)");
} else if (grade >= 80) {
    console.log("Grade: B (80-89)");
} else if (grade >= 70) {
    console.log("Grade: C (70-79)");
} else if (grade >= 60) {
    console.log("Grade: D (60-69)");
} else {
    console.log("Grade: F (below 60)");
}

console.log("");
console.log("=== Temperature Adviser ===");
// Input for temperature
let temperature = 75;  // in Fahrenheit

if (temperature > 80) {
    console.log("It's hot! Stay hydrated and wear light clothes.");
} else if (temperature > 60) {
    console.log("It's a nice day! Perfect for outdoor activities.");
} else {
    console.log("It's cold! Don't forget your jacket.");
}

console.log("");
console.log("=== Username and Password Check ===");
// Input for login
let username = "admin";
let password = "secret123";

if (username === "admin" && password === "secret123") {
    console.log("Login successful! Welcome, admin.");
} else {
    console.log("Login failed! Invalid username or password.");
}

console.log("");
console.log("=== Multiple Condition Check ===");
// Check if number is positive, even, and greater than 10
let number = 12;

if (number > 0) {
    console.log("The number is positive");
    if (number % 2 === 0) {
        console.log("The number is even");
        if (number > 10) {
            console.log("The number is greater than 10");
            console.log("This number is positive, even, and greater than 10!");
        } else {
            console.log("This number is positive and even, but not greater than 10");
        }
    } else {
        console.log("This number is positive and odd");
    }
} else {
    console.log("This number is not positive");
}

console.log("");
console.log("=== Logical Operators Demo ===");
let hasID = true;
let hasMoney = true;
let ageCheck = 21;

// Using AND operator (&&) - all conditions must be true
if (hasID && hasMoney && ageCheck >= 18) {
    console.log("You can buy alcohol (if you're 18+ and have ID & money)");
} else {
    console.log("Cannot purchase: Missing ID, money, or age requirement");
}

// Using OR operator (||) - at least one condition must be true
let hasCreditCard = false;
let hasDebitCard = true;
let hasCash = false;

if (hasCreditCard || hasDebitCard || hasCash) {
    console.log("Payment method available");
} else {
    console.log("No payment method available");
}

// Using NOT operator (!) - reverses the condition
let isRaining = false;
if (!isRaining) {
    console.log("It's not raining, so no need for an umbrella!");
} else {
    console.log("It's raining, bring an umbrella!");
}

console.log("");
console.log("=== Switch Statement Demo ===");
let dayOfWeek = 3;  // 1=Monday, 2=Tuesday, etc.

switch (dayOfWeek) {
    case 1:
        console.log("Today is Monday - start of the work week");
        break;
    case 2:
        console.log("Today is Tuesday");
        break;
    case 3:
        console.log("Today is Wednesday - middle of the week");
        break;
    case 4:
        console.log("Today is Thursday");
        break;
    case 5:
        console.log("Today is Friday - weekend is almost here!");
        break;
    case 6:
        console.log("Today is Saturday - weekend fun!");
        break;
    case 7:
        console.log("Today is Sunday - rest day");
        break;
    default:
        console.log("Invalid day number! Please enter 1-7");
        break;
}

console.log("");
console.log("=== Ternary Operator Demo ===");
let score = 88;
let result = score >= 60 ? "Pass" : "Fail";
console.log("Score: " + score + ", Result: " + result);

// Ternary with multiple conditions
let timeOfDay = 14;  // 24-hour format
let greeting = timeOfDay < 12 ? "Good morning!" : 
               timeOfDay < 18 ? "Good afternoon!" : 
               "Good evening!";
console.log("Time: " + timeOfDay + ":00, Greeting: " + greeting);
```

---

### How to Execute

1. **Run your program**:
   ```
   node conditionals.js
   ```

**Expected output:**
```
=== Simple Age Check ===
You are an adult (18 or older)

=== Grade Classifier ===
Grade: B (80-89)

=== Temperature Adviser ===
It's a nice day! Perfect for outdoor activities.

=== Username and Password Check ===
Login successful! Welcome, admin.

=== Multiple Condition Check ===
The number is positive
The number is even
The number is greater than 10
This number is positive, even, and greater than 10!

=== Logical Operators Demo ===
You can buy alcohol (if you're 18+ and have ID & money)
Payment method available
It's not raining, so no need for an umbrella!

=== Switch Statement Demo ===
Today is Wednesday - middle of the week

=== Ternary Operator Demo ===
Score: 88, Result: Pass
Time: 14:00, Greeting: Good afternoon!
```

---

### Success Checklist

- [ ] Created a file named `conditionals.js`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw different code paths execute based on conditions
- [ ] Understood if/else statements and logical operators

---

### Understanding Comparison Operators

In JavaScript conditionals, you'll use these comparison operators:

- **`==`** = Equal value (type conversion happens)
- **`===`** = Equal value AND equal type (strict comparison, preferred)
- **`!=`** = Not equal value
- **`!==`** = Not equal value OR not equal type (strict not equal)
- **`<`** = Less than
- **`>`** = Greater than
- **`<=`** = Less than or equal to
- **`>=`** = Greater than or equal to

---

### Try This (Optional Challenges)

1. Create a BMI classifier that gives different advice based on BMI ranges
2. Build a program that determines if a year is a leap year
3. Make a simple game where the computer picks a number and the user guesses
4. Create a traffic light simulator using conditionals

---

## Quick Reference

| Operator | Name | Purpose | Example | Result |
|----------|------|---------|---------|--------|
| `==` | Equal | Value comparison (loose) | `5 == "5"` | `true` |
| `===` | Strict Equal | Value and type comparison | `5 === "5"` | `false` |
| `!=` | Not Equal | Value not equal | `5 != 3` | `true` |
| `!==` | Strict Not Equal | Value or type different | `5 !== "5"` | `true` |
| `<` | Less Than | Left less than right | `3 < 5` | `true` |
| `>` | Greater Than | Left greater than right | `5 > 3` | `true` |
| `<=` | Less or Equal | Left less than or equal | `5 <= 5` | `true` |
| `>=` | Greater or Equal | Left greater or equal | `5 >= 3` | `true` |
| `&&` | AND | Both conditions true | `true && false` | `false` |
| `||` | OR | At least one true | `true || false` | `true` |
| `!` | NOT | Reverse the condition | `!true` | `false` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```
if (age >= 18) {
    console.log("You are an adult (18 or older)");
} else {
    console.log("You are a minor (under 18)");
}
```
- **`if`** = Start of conditional statement
- **`(age >= 18)`** = Condition that evaluates to true or false
- **`{}`** = Code block executed if condition is true
- **`else`** = Code block executed if condition is false

```
if (grade >= 90) {
    console.log("Grade: A (90-100)");
} else if (grade >= 80) {
    console.log("Grade: B (80-89)");
} else if (grade >= 70) {
    console.log("Grade: C (70-79)");
} else if (grade >= 60) {
    console.log("Grade: D (60-69)");
} else {
    console.log("Grade: F (below 60)");
}
```
- **`else if`** = Additional condition to check if the first was false
- **Execution order** matters: JavaScript checks each condition in order and executes the first true one
- **Only one block** executes, not multiple blocks

```
if (username === "admin" && password === "secret123") {
    console.log("Login successful! Welcome, admin.");
} else {
    console.log("Login failed! Invalid username or password.");
}
```
- **`&&`** = Logical AND operator (both conditions must be true)
- **`===`** = Strict equality (both value AND type must match)
- **Security** considerations: Never hardcode credentials in real programs

### Comparison Operators Deep Dive

**Loose vs Strict Equality:**
```
console.log(5 == "5");   // true (values are the same after conversion)
console.log(5 === "5");  // false (different types: number vs string)
console.log(0 == false); // true (0 and false are both "falsy")
console.log(0 === false); // false (different types)
```

**Best Practice**: Use `===` (strict equality) in most cases to avoid unexpected type conversions.

### Logical Operators

| Operator | Symbol | What it does | Example | Result |
|----------|--------|--------------|---------|--------|
| AND | `&&` | Both conditions true | `true && false` | `false` |
| OR | `||` | At least one true | `true || false` | `true` |
| NOT | `!` | Reverse condition | `!true` | `false` |

**More Examples:**
```
// AND: All conditions must be true
let age = 21;
let hasID = true;
let hasMoney = true;
if (age >= 21 && hasID && hasMoney) {
    console.log("Can buy alcohol");
}

// OR: At least one condition must be true
let credit = true;
let debit = false;
let cash = false;
if (credit || debit || cash) {
    console.log("Payment available");
}

// NOT: Reverses the condition
let isLoggedIn = false;
if (!isLoggedIn) {
    console.log("Please log in first");
}
```

### Nested Conditionals

```
if (number > 0) {
    console.log("The number is positive");
    if (number % 2 === 0) {        // Nested if
        console.log("The number is even");
        if (number > 10) {         // Double nested if
            console.log("The number is greater than 10");
        }
    }
}
```
- **Inner condition** only evaluated if outer condition is true
- **Be careful** with nesting - too deep can be hard to read

### Switch Statement

```
switch (dayOfWeek) {
    case 1:
        console.log("Today is Monday");
        break;  // Important! Without break, it continues to next case
    case 2:
        console.log("Today is Tuesday");
        break;
    default:  // Executes if no case matches
        console.log("Invalid day number");
        break;
}
```
- **Alternative to long if/else if** chains
- **`break`** = Stops execution and exits switch
- **Without break** = Falls through to next case ("fallthrough")
- **`default`** = Catch-all case when no others match

### Ternary Operator

```
let result = score >= 60 ? "Pass" : "Fail";
```
- **Syntax**: `condition ? valueIfTrue : valueIfFalse`
- **Same as**:
```
let result;
if (score >= 60) {
    result = "Pass";
} else {
    result = "Fail";
}
```

**Chained Ternary (advanced):**
```
let timeOfDay = 14;
let greeting = timeOfDay < 12 ? "Good morning!" : 
               timeOfDay < 18 ? "Good afternoon!" : 
               "Good evening!";
```

### Truthy and Falsy Values

In JavaScript, these values are "falsy":
- `false`
- `0`
- `-0`
- `0n` (BigInt)
- `""` (empty string)
- `null`
- `undefined`
- `NaN`

All other values are "truthy", even `"false"` (string) and `[]` (empty array)!

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Using `=` instead of `==` | Assigning instead of comparing | Use `==` for comparison, `=` for assignment |
| Using `==` instead of `===` | Unexpected type conversion | Use `===` for strict equality |
| Missing `break` in switch | Fallthrough behavior | Always include `break;` after each case |
| Confusing `&&` and `||` | Wrong logic | Remember: AND needs ALL true, OR needs ANY true |
| Forgetting parentheses in if | Syntax error | Always use `if (condition)` with parentheses |

### Best Practices for Conditionals

**Use descriptive variable names:**
```
// Good
if (isAdult) { ... }
if (isValidEmail) { ... }

// Avoid
if (x) { ... }
if (flag) { ... }
```

**Keep conditions simple:**
```
// Good - store complex condition in variable
let canVote = age >= 18 && isCitizen && !isInPrison;
if (canVote) { ... }

// Avoid - hard to read
if (age >= 18 && isCitizen && !isInPrison) { ... }
```

**Consider switch vs if/else if:**
- Use `switch` for exact value matching
- Use `if/else if` for ranges and complex conditions

### Advanced Challenge (For the Brave!)

Try this complex conditional program:

```
// A simple grading system with lots of conditions
let studentName = "Alex";
let examScore = 88;
let homeworkScore = 92;
let participation = true;

console.log("=== Student Report for " + studentName + " ===");

// Calculate overall grade
let overallScore = (examScore * 0.7) + (homeworkScore * 0.3);
console.log("Overall Score: " + overallScore.toFixed(2));

// Determine letter grade
let letterGrade;
if (overallScore >= 97) {
    letterGrade = "A+";
} else if (overallScore >= 93) {
    letterGrade = "A";
} else if (overallScore >= 90) {
    letterGrade = "A-";
} else if (overallScore >= 87) {
    letterGrade = "B+";
} else if (overallScore >= 83) {
    letterGrade = "B";
} else if (overallScore >= 80) {
    letterGrade = "B-";
} else if (overallScore >= 77) {
    letterGrade = "C+";
} else if (overallScore >= 73) {
    letterGrade = "C";
} else if (overallScore >= 70) {
    letterGrade = "C-";
} else if (overallScore >= 67) {
    letterGrade = "D+";
} else if (overallScore >= 63) {
    letterGrade = "D";
} else if (overallScore >= 60) {
    letterGrade = "D-";
} else {
    letterGrade = "F";
}

console.log("Letter Grade: " + letterGrade);

// Special recognition
if (letterGrade === "A+" && participation) {
    console.log("Outstanding performance! Keep up the excellent work!");
} else if (letterGrade === "A" || letterGrade === "A+") {
    console.log("Excellent work! Very impressive!");
} else if (letterGrade === "B" || letterGrade === "B+") {
    console.log("Good job! You're doing well!");
} else if (overallScore >= 70) {
    console.log("Satisfactory performance. Keep trying!");
} else {
    console.log("Please see your instructor for additional help.");
}

// Graduation eligibility
if (overallScore >= 75 && participation) {
    console.log("Eligible for graduation with honors consideration");
} else if (overallScore >= 60) {
    console.log("Eligible for graduation");
} else {
    console.log("Not eligible for graduation, must repeat course");
}
```

---

 **Excellent work! You now understand how to make your programs make intelligent decisions!** 

*Ready for the next challenge? Let's learn about loops and repetition!*


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

```js
console.log("Hello, World!");

```js

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard javascript conventions with proper imports and main function
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
