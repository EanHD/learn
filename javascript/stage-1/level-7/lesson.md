# Level 7: Functions - Code Organization

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the world of functions! Today you'll learn how to organize your code into reusable pieces called functions. This is where programming becomes truly powerful and professional.

---

### Learning Goals

- Understand what functions are and why they're important
- Learn to define and call functions
- Practice using parameters and return values
- Create reusable code blocks
- Learn about scope and variable access in functions
- Understand different ways to define functions

---

### Your Task

**Copy the following code into a new file called `functions.js`**

```javascript
console.log("=== Basic Function Definition ===");
// Define a function that greets someone
function greetUser() {
    console.log("Hello! Welcome to the wonderful world of functions!");
}

// Call the function
greetUser();
greetUser();  // Can be called multiple times

console.log("");
console.log("=== Function with Parameters ===");
// Define a function that takes parameters
function greetByName(name) {
    console.log("Hello, " + name + "! Nice to meet you!");
}

// Call the function with different arguments
greetByName("Alex");
greetByName("Taylor");
greetByName("Jordan");

console.log("");
console.log("=== Function with Multiple Parameters ===");
// Define a function with multiple parameters
function introducePerson(name, age) {
    console.log("Hi, I'm " + name + " and I'm " + age + " years old.");
}

// Call the function with multiple arguments
introducePerson("Sam", 25);
introducePerson("Morgan", 30);

console.log("");
console.log("=== Function with Return Value ===");
// Define a function that returns a value
function addNumbers(a, b) {
    let sum = a + b;
    return sum;  // Send result back to caller
}

// Use the returned value
let result1 = addNumbers(5, 3);
let result2 = addNumbers(10, 20);
console.log("5 + 3 = " + result1);
console.log("10 + 20 = " + result2);

// Functions can be used directly in expressions
console.log("The sum of 7 and 8 is: " + addNumbers(7, 8));

console.log("");
console.log("=== Function with Default Parameters ===");
// Define a function with default parameter values
function greetWithTime(name, time = "day") {
    console.log("Good " + time + ", " + name + "!");
}

// Call with both parameters
greetWithTime("Alex", "morning");
greetWithTime("Taylor", "evening");

// Call with only the required parameter (time uses default)
greetWithTime("Jordan");

console.log("");
console.log("=== Function Expression (Anonymous Function) ===");
// Define function as an expression
let multiply = function(a, b) {
    return a * b;
};

// Use the function
let product = multiply(4, 5);
console.log("4 * 5 = " + product);

console.log("");
console.log("=== Arrow Function (Modern Syntax) ===");
// Define function using arrow syntax
let square = (x) => {
    return x * x;
};

// Arrow function with single expression (implicit return)
let cube = (x) => x * x * x;

// Use the functions
console.log("Square of 4: " + square(4));
console.log("Cube of 3: " + cube(3));

console.log("");
console.log("=== Practical Function Examples ===");
// Function to calculate area of rectangle
function calculateRectangleArea(length, width) {
    return length * width;
}

// Function to calculate area of circle
function calculateCircleArea(radius) {
    return 3.14159 * radius * radius;
}

// Function to format a full name
function formatFullName(firstName, lastName) {
    return firstName + " " + lastName;
}

// Function to check if a number is even
function isEven(number) {
    return number % 2 === 0;
}

// Use the practical functions
let rectArea = calculateRectangleArea(10, 5);
let circleArea = calculateCircleArea(7);
let fullName = formatFullName("John", "Doe");
let isNumEven = isEven(12);

console.log("Rectangle area (10 x 5): " + rectArea);
console.log("Circle area (radius 7): " + circleArea.toFixed(2));
console.log("Full name: " + fullName);
console.log("Is 12 even? " + isEven(12));

console.log("");
console.log("=== Function Scope Demo ===");
let globalVariable = "I'm global!";

function scopeDemo() {
    let localVariable = "I'm local!";
    console.log("Inside function: " + globalVariable);
    console.log("Inside function: " + localVariable);
    
    // Functions can modify global variables
    globalVariable = "Modified from inside function!";
}

// Call the function
scopeDemo();

// See the change to global variable
console.log("Outside function: " + globalVariable);

// This would cause an error - localVariable is not accessible here:
// console.log("Outside function: " + localVariable);  // Commented out to prevent error

console.log("");
console.log("=== Function Inside Function ===");
function outerFunction(name) {
    function innerFunction() {
        return "Hello from inside!";
    }
    
    return name + ", " + innerFunction();
}

let message = outerFunction("Alex");
console.log(message);

console.log("");
console.log("=== Multiple Return Values (as Object) ===");
// Function that returns multiple related values
function getUserInfo(firstName, lastName, age) {
    return {
        fullName: firstName + " " + lastName,
        age: age,
        isAdult: age >= 18,
        greeting: "Hello, I'm " + firstName
    };
}

// Use the function
let userInfo = getUserInfo("Taylor", "Swift", 34);
console.log("Full Name: " + userInfo.fullName);
console.log("Age: " + userInfo.age);
console.log("Is Adult: " + userInfo.isAdult);
console.log("Greeting: " + userInfo.greeting);

console.log("");
console.log("=== Higher-Order Function Example ===");
// Function that takes another function as a parameter
function processArray(arr, callback) {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(callback(arr[i]));
    }
    return result;
}

// Example array
let numbers = [1, 2, 3, 4, 5];

// Process array by doubling each element
function double(x) {
    return x * 2;
}

let doubled = processArray(numbers, double);
console.log("Original: " + numbers);
console.log("Doubled: " + doubled);

// Process array using arrow function
let squared = processArray(numbers, (x) => x * x);
console.log("Squared: " + squared);
```

---

### How to Execute

1. **Run your program**:
   ```bash
   node functions.js
   ```

**Expected output:**
```
=== Basic Function Definition ===
Hello! Welcome to the wonderful world of functions!
Hello! Welcome to the wonderful world of functions!

=== Function with Parameters ===
Hello, Alex! Nice to meet you!
Hello, Taylor! Nice to meet you!
Hello, Jordan! Nice to meet you!

=== Function with Multiple Parameters ===
Hi, I'm Sam and I'm 25 years old.
Hi, I'm Morgan and I'm 30 years old.

=== Function with Return Value ===
5 + 3 = 8
10 + 20 = 20
The sum of 7 and 8 is: 15

=== Function with Default Parameters ===
Good morning, Alex!
Good evening, Taylor!
Good day, Jordan!

=== Function Expression (Anonymous Function) ===
4 * 5 = 20

=== Arrow Function (Modern Syntax) ===
Square of 4: 16
Cube of 3: 27

=== Practical Function Examples ===
Rectangle area (10 x 5): 50
Circle area (radius 7): 153.94
Full name: John Doe
Is 12 even? true

=== Function Scope Demo ===
Inside function: I'm global!
Inside function: I'm local!
Outside function: Modified from inside function!

=== Function Inside Function ===
Alex, Hello from inside!

=== Multiple Return Values (as Object) ===
Full Name: Taylor Swift
Age: 34
Is Adult: true
Greeting: Hello, I'm Taylor

=== Higher-Order Function Example ===
Original: 1,2,3,4,5
Doubled: 2,4,6,8,10
Squared: 1,4,9,16,25
```

---

### Success Checklist

- [ ] Created a file named `functions.js`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw functions being defined and called correctly
- [ ] Understood parameters, return values, and scope

---

### Function Types Summary

- **`function name()`** = Function declaration
- **`let name = function()`** = Function expression
- **`let name = () =>`** = Arrow function
- **Parameters** = Variables in function definition
- **Arguments** = Values passed when calling function
- **Return** = Sends value back to caller

---

### Try This (Optional Challenges)

1. Create a calculator with functions for add, subtract, multiply, divide
2. Build a function that validates email addresses
3. Make a function that generates random passwords
4. Create a function that sorts an array of numbers

---

## Quick Reference

| Function Type | Syntax | When to Use |
|---------------|--------|-------------|
| Declaration | `function name(params) { }` | Most common, hoisted |
| Expression | `let name = function(params) { }` | Assign to variable |
| Arrow | `let name = (params) => { }` | Concise, modern syntax |
| Arrow (short) | `let name = params => expression` | Single expression |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```javascript
function greetUser() {
    console.log("Hello! Welcome to the wonderful world of functions!");
}
```
- **`function`** = Keyword to declare a function
- **`greetUser`** = Function name (follows variable naming rules)
- **`()`** = Parameters (empty because no parameters needed)
- **`{}`** = Function body (code that runs when function is called)
- **No return** = Function runs code but doesn't return a value

```javascript
function greetByName(name) {
    console.log("Hello, " + name + "! Nice to meet you!");
}
```
- **`name`** = Parameter (variable that receives the argument value)
- **Parameters** = Variables defined in function declaration
- **Arguments** = Actual values passed when calling the function

```javascript
let result1 = addNumbers(5, 3);
```
- **`addNumbers(5, 3)`** = Function call with arguments
- **`5` and `3`** = Arguments passed to the function
- **Return value** = Value that function sends back
- **`result1`** = Variable that stores the returned value

### Function Declaration vs Expression

**Function Declaration (Traditional):**
```javascript
function add(a, b) {
    return a + b;
}
// Can be called before or after the declaration due to hoisting
```

**Function Expression:**
```javascript
let add = function(a, b) {
    return a + b;
};
// Must be defined before calling (no hoisting)
```

### Arrow Functions

**Full syntax:**
```javascript
let add = (a, b) => {
    return a + b;
};
```

**Shortened syntax (implicit return):**
```javascript
let add = (a, b) => a + b;  // Returns a + b automatically
let square = x => x * x;    // Single parameter doesn't need parentheses
let greet = () => "Hello!"; // No parameters need empty parentheses
```

### Function Parameters

**Default parameters:**
```javascript
function greet(name, greeting = "Hello") {
    console.log(greeting + ", " + name + "!");
}

greet("Alex");           // "Hello, Alex!" (greeting uses default)
greet("Taylor", "Hi");   // "Hi, Taylor!" (greeting overridden)
```

**Rest parameters (for multiple values):**
```javascript
function sum(...numbers) {
    let total = 0;
    for (let num of numbers) {
        total += num;
    }
    return total;
}

console.log(sum(1, 2, 3));      // 6
console.log(sum(1, 2, 3, 4, 5)); // 15
```

### Function Scope

**Global scope:**
```javascript
let globalVar = "I'm accessible everywhere";
```

**Local scope:**
```javascript
function myFunction() {
    let localVar = "I'm only accessible inside this function";
    // Can access both globalVar and localVar
}
// Can access globalVar but NOT localVar
```

**Scope rules:**
- Functions can access variables in their own scope
- Functions can access variables in outer (enclosing) scopes
- Outer scopes cannot access variables inside functions
- Inner functions can access variables from outer functions

### Return Values

**Functions without return:**
```javascript
function sayHello() {
    console.log("Hello!");
}
// Returns 'undefined' implicitly
```

**Functions with return:**
```javascript
function getHello() {
    return "Hello!";
}
// Returns "Hello!" which can be stored in a variable
```

**Early return:**
```javascript
function divide(a, b) {
    if (b === 0) {
        console.log("Cannot divide by zero!");
        return null;  // Exit function early
    }
    return a / b;
}
```

### Higher-Order Functions

Functions that take other functions as parameters or return functions:

```javascript
// Function that takes another function as a parameter
function executeTwice(func) {
    func();
    func();
}

function sayHello() {
    console.log("Hello!");
}

executeTwice(sayHello);  // Will output "Hello!" twice
```

### Pure vs Impure Functions

**Pure function:**
- Same input always gives same output
- No side effects (doesn't modify external state)
```javascript
function add(a, b) {
    return a + b;  // Pure function
}
```

**Impure function:**
- May have side effects or depend on external state
```javascript
let count = 0;
function increment() {
    count++;  // Modifies external variable
    return count;
}  // Impure function
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ReferenceError: function is not defined` | Function not declared or typo in name | Check function name and spelling |
| Function doesn't return expected value | Forgot `return` statement | Add `return` for values you need |
| `undefined` when expecting result | Function doesn't return anything | Add return statement |
| `SyntaxError` in function | Missing brackets, commas, etc. | Check function syntax carefully |
| Parameters not working | Confusion between parameters and arguments | Parameters are in definition, arguments in call |

### Best Practices for Functions

**Function naming:**
```javascript
// Good - descriptive names
function calculateArea(length, width) { ... }
function isValidEmail(email) { ... }
function sendNotification(message) { ... }

// Avoid - vague names
function doStuff() { ... }
function process() { ... }
```

**Function size:**
- Keep functions focused on a single task
- Aim for functions that are 5-10 lines when possible
- If a function gets too long, consider breaking it into smaller ones

**Single Responsibility Principle:**
```javascript
// Good - one purpose
function calculateTax(amount, rate) {
    return amount * rate;
}

// Better than trying to do everything in one function
function processOrder(order) {
    let tax = calculateTax(order.amount, order.taxRate);
    let total = order.amount + tax;
    // ... other processing
    return total;
}
```

### Advanced Challenge (For the Brave!)

Try this comprehensive function example:

```javascript
// A comprehensive banking application using functions
console.log("=== Banking Application with Functions ===");

// Function to create a bank account object
function createAccount(name, initialBalance = 0) {
    return {
        name: name,
        balance: initialBalance,
        transactions: []  // Track all transactions
    };
}

// Function to deposit money
function deposit(account, amount) {
    if (amount <= 0) {
        console.log("Deposit amount must be positive!");
        return false;
    }
    
    account.balance += amount;
    account.transactions.push({
        type: "deposit",
        amount: amount,
        date: new Date().toLocaleDateString(),
        balanceAfter: account.balance
    });
    
    console.log("$" + amount + " deposited. New balance: $" + account.balance);
    return true;
}

// Function to withdraw money
function withdraw(account, amount) {
    if (amount <= 0) {
        console.log("Withdrawal amount must be positive!");
        return false;
    }
    
    if (amount > account.balance) {
        console.log("Insufficient funds! Current balance: $" + account.balance);
        return false;
    }
    
    account.balance -= amount;
    account.transactions.push({
        type: "withdrawal",
        amount: amount,
        date: new Date().toLocaleDateString(),
        balanceAfter: account.balance
    });
    
    console.log("$" + amount + " withdrawn. New balance: $" + account.balance);
    return true;
}

// Function to check balance
function checkBalance(account) {
    console.log(account.name + "'s balance: $" + account.balance);
    return account.balance;
}

// Function to get transaction history
function getTransactionHistory(account) {
    console.log(account.name + "'s Transaction History:");
    for (let i = 0; i < account.transactions.length; i++) {
        let transaction = account.transactions[i];
        console.log(transaction.date + " - " + transaction.type + ": $" + 
                   transaction.amount + " - Balance: $" + transaction.balanceAfter);
    }
}

// Function to transfer money between accounts
function transfer(fromAccount, toAccount, amount) {
    if (withdraw(fromAccount, amount)) {
        deposit(toAccount, amount);
        console.log("Transfer of $" + amount + " from " + fromAccount.name + 
                   " to " + toAccount.name + " completed!");
        return true;
    }
    return false;
}

// Create accounts
let alexAccount = createAccount("Alex", 1000);
let taylorAccount = createAccount("Taylor", 500);

// Perform transactions
deposit(alexAccount, 200);
withdraw(alexAccount, 150);
transfer(alexAccount, taylorAccount, 300);
checkBalance(alexAccount);
checkBalance(taylorAccount);

console.log("");
getTransactionHistory(alexAccount);
```

---

 **Excellent work! You now understand how to organize code using functions - a fundamental skill for all programmers!** 

*This completes Stage 1 of JavaScript learning! You've mastered the fundamentals of JavaScript programming. Great job!*
