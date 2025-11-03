# Level 6: Loops and Repetition
## Stage 1: Copying Code

### Today's Mission

Time to make your programs repeat actions! Today you'll learn how to write code that runs multiple times without having to copy and paste. Loops are one of the most powerful concepts in programming.

---

### Learning Goals

- Understand for loops for counting and repetition
- Learn while loops for conditional repetition
- Practice do-while loops for guaranteed execution
- Use break and continue statements to control loops
- Iterate through arrays and collections
- Create patterns and repetitive calculations

---

### Your Task

**Copy the following code into a new file called `loops.js`**

```javascript
console.log("=== For Loop - Counting ===");
// Basic for loop: for (initialization; condition; increment)
for (let i = 1; i <= 5; i++) {
    console.log("Count: " + i);
}

console.log("");
console.log("=== For Loop - Countdown ===");
// Countdown from 10 to 1
for (let i = 10; i >= 1; i--) {
    console.log("Countdown: " + i);
}
console.log("Blast off! 🚀");

console.log("");
console.log("=== For Loop - Even Numbers ===");
// Print even numbers from 2 to 10
for (let i = 2; i <= 10; i += 2) {
    console.log("Even number: " + i);
}

console.log("");
console.log("=== For Loop - Sum of Numbers ===");
// Calculate sum of numbers 1 to 10
let sum = 0;
for (let i = 1; i <= 10; i++) {
    sum += i;  // Same as: sum = sum + i
}
console.log("Sum of 1 to 10: " + sum);

console.log("");
console.log("=== While Loop - Counting ===");
// Basic while loop: while (condition)
let count = 1;
while (count <= 5) {
    console.log("While count: " + count);
    count++;  // Important! Without this, infinite loop!
}

console.log("");
console.log("=== While Loop - Random Number Game ===");
// Generate random numbers until we get 6
let roll;
let rolls = 0;
while (roll !== 6) {
    roll = Math.floor(Math.random() * 6) + 1;  // Random 1-6
    rolls++;
    console.log("Roll #" + rolls + ": " + roll);
}
console.log("Got a 6 after " + rolls + " rolls!");

console.log("");
console.log("=== Do-While Loop - Menu ===");
// Do-while executes at least once, then checks condition
let menuChoice;
let tries = 0;
do {
    tries++;
    menuChoice = Math.floor(Math.random() * 4) + 1;  // Random 1-4
    console.log("Menu attempt #" + tries + ": Option " + menuChoice);
    
    if (menuChoice === 3) {
        console.log("Option 3 selected! Exiting menu.");
    }
} while (menuChoice !== 3 && tries < 10);  // Stop if option 3 or after 10 tries

console.log("");
console.log("=== For Loop with Break ===");
// Using break to exit a loop early
for (let i = 1; i <= 10; i++) {
    if (i === 7) {
        console.log("Found 7, stopping the loop!");
        break;  // Exit the loop completely
    }
    console.log("Number: " + i);
}

console.log("");
console.log("=== For Loop with Continue ===");
// Using continue to skip an iteration
for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) {  // If even number
        console.log(i + " is even - skipping");
        continue;  // Skip the rest of this iteration
    }
    console.log("Odd number: " + i);
}

console.log("");
console.log("=== Looping Through an Array ===");
// Array of items to iterate through
let fruits = ["apple", "banana", "orange", "grape", "mango"];

// Traditional for loop with array
for (let i = 0; i < fruits.length; i++) {
    console.log("Fruit at index " + i + ": " + fruits[i]);
}

console.log("");
console.log("=== For-Of Loop ===");
// Modern for-of loop for arrays
for (let fruit of fruits) {
    console.log("Fruit: " + fruit);
}

console.log("");
console.log("=== Nested Loops - Multiplication Table ===");
// Create a multiplication table (3x3)
for (let i = 1; i <= 3; i++) {
    let row = "";
    for (let j = 1; j <= 3; j++) {
        row += (i * j) + "\t";  // \t is a tab character
    }
    console.log(row);
}

console.log("");
console.log("=== Pattern - Stars ===");
// Create a right triangle pattern
for (let i = 1; i <= 5; i++) {
    let pattern = "";
    for (let j = 1; j <= i; j++) {
        pattern += "* ";
    }
    console.log(pattern);
}

console.log("");
console.log("=== Looping with User Input Simulation ===");
// Simulate processing multiple items
let items = ["item1", "item2", "item3", "item4", "item5"];
for (let i = 0; i < items.length; i++) {
    console.log("Processing " + items[i] + "...");
    // In a real program, we might do some work here
    console.log("✓ " + items[i] + " processed");
}
```

---

### How to Execute

1. **Run your program**:
   ```bash
   node loops.js
   ```

**Expected output:**
```
=== For Loop - Counting ===
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

=== For Loop - Countdown ===
Countdown: 10
Countdown: 9
Countdown: 8
Countdown: 7
Countdown: 6
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Blast off! 🚀

=== For Loop - Even Numbers ===
Even number: 2
Even number: 4
Even number: 6
Even number: 8
Even number: 10

=== For Loop - Sum of Numbers ===
Sum of 1 to 10: 55

=== While Loop - Counting ===
While count: 1
While count: 2
While count: 3
While count: 4
While count: 5

=== While Loop - Random Number Game ===
Roll #1: 3
Roll #2: 1
Roll #3: 6
Got a 6 after 3 rolls!

=== Do-While Loop - Menu ===
Menu attempt #1: Option 2
Menu attempt #2: Option 4
Menu attempt #3: Option 3
Option 3 selected! Exiting menu.

=== For Loop with Break ===
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Number: 6
Found 7, stopping the loop!

=== For Loop with Continue ===
1 is odd - skipping
2 is even - skipping
Odd number: 3
4 is even - skipping
Odd number: 5
6 is even - skipping
Odd number: 7
8 is even - skipping
Odd number: 9
10 is even - skipping

=== Looping Through an Array ===
Fruit at index 0: apple
Fruit at index 1: banana
Fruit at index 2: orange
Fruit at index 3: grape
Fruit at index 4: mango

=== For-Of Loop ===
Fruit: apple
Fruit: banana
Fruit: orange
Fruit: grape
Fruit: mango

=== Nested Loops - Multiplication Table ===
1	2	3	
2	4	6	
3	6	9	

=== Pattern - Stars ===
* 
* * 
* * * 
* * * * 
* * * * * 

=== Looping with User Input Simulation ===
Processing item1...
✓ item1 processed
Processing item2...
✓ item2 processed
Processing item3...
✓ item3 processed
Processing item4...
✓ item4 processed
Processing item5...
✓ item5 processed
```

---

### Success Checklist

- [ ] Created a file named `loops.js`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw different types of loops working correctly
- [ ] Understood how break and continue work

---

### Loop Types Summary

- **`for` loop**: Use when you know how many times to repeat
- **`while` loop**: Use when you want to repeat while a condition is true
- **`do-while` loop**: Use when you want to repeat at least once then check condition
- **`for-of` loop**: Use for iterating through arrays and collections

---

### Try This (Optional Challenges)

1. Create a Fibonacci sequence generator using loops
2. Build a password validation program that checks multiple requirements
3. Make a prime number checker
4. Create a simple text-based game using loops for turns

---

## Quick Reference

| Loop Type | Syntax | When to Use |
|-----------|--------|-------------|
| `for` | `for (init; condition; increment)` | When you know the number of iterations |
| `while` | `while (condition)` | When you repeat while condition is true |
| `do-while` | `do { } while (condition)` | When you must run at least once |
| `for-of` | `for (element of array)` | When iterating through arrays/objects |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```javascript
for (let i = 1; i <= 5; i++) {
    console.log("Count: " + i);
}
```
- **`for`** = Loop keyword
- **`let i = 1`** = Initialization: set up the counter variable
- **`i <= 5`** = Condition: keep looping while this is true
- **`i++`** = Increment: update the counter after each iteration
- **`{}`** = Code block that runs each iteration
- **Loop execution**: 1, 2, 3, 4, 5 (stops when i becomes 6)

```javascript
while (count <= 5) {
    console.log("While count: " + count);
    count++;  // Critical: must update the counter!
}
```
- **`while`** = Loop that continues while condition is true
- **Condition checked first** before each iteration
- **`count++`** = Must update counter inside the loop or it runs forever!

```javascript
do {
    console.log("Menu attempt #" + tries + ": Option " + menuChoice);
} while (menuChoice !== 3 && tries < 10);
```
- **`do`** = Code block executes first
- **`while`** = Then condition is checked
- **Result**: Block runs at least once regardless of condition

### For Loop Variations

**Different increment patterns:**
```javascript
// Count by 5s
for (let i = 0; i <= 25; i += 5) {
    console.log(i); // 0, 5, 10, 15, 20, 25
}

// Count backwards
for (let i = 10; i > 0; i--) {
    console.log(i); // 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
}

// Count with decimals
for (let i = 0; i <= 1; i += 0.2) {
    console.log(i); // 0, 0.2, 0.4, 0.6, 0.8, 1
}
```

### Array Iteration Methods

```javascript
let fruits = ["apple", "banana", "orange"];

// Traditional for loop
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// For-of loop (modern)
for (let fruit of fruits) {
    console.log(fruit);
}

// For-each method (alternative)
fruits.forEach(function(fruit) {
    console.log(fruit);
});
```

**`array.length`** = Property that returns the number of elements in the array.

### Break and Continue

**`break`** = Exits the loop completely:
```javascript
for (let i = 1; i <= 10; i++) {
    if (i === 5) {
        break;  // Loop stops here
    }
    console.log(i);  // Prints: 1, 2, 3, 4
}
```

**`continue`** = Skips the rest of current iteration:
```javascript
for (let i = 1; i <= 5; i++) {
    if (i === 3) {
        continue;  // Skip to next iteration
    }
    console.log(i);  // Prints: 1, 2, 4, 5 (skips 3)
}
```

### Nested Loops

```javascript
for (let i = 1; i <= 3; i++) {          // Outer loop
    for (let j = 1; j <= 3; j++) {      // Inner loop
        console.log("i=" + i + ", j=" + j);
    }
}
```
**Output:**
```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3
```
- **Inner loop** completes all iterations for each outer loop iteration
- **Total iterations**: 3 × 3 = 9

### Random Numbers in JavaScript

```javascript
// Random integer between min and max (inclusive)
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Examples:
console.log(randomInt(1, 6));    // Random die roll
console.log(randomInt(1, 100));  // Random number 1-100
console.log(randomInt(10, 20));  // Random number 10-20
```

### Loop Performance Considerations

**Cache array length** (minor optimization):
```javascript
// Instead of this (length checked each iteration):
for (let i = 0; i < myArray.length; i++) { ... }

// Do this (length calculated once):
let len = myArray.length;
for (let i = 0; i < len; i++) { ... }
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Infinite loop | Not updating loop variable | Always update the variable that controls the loop |
| Never executes | Wrong condition | Double-check your condition logic |
| Off-by-one error | `<=` vs `<` confusion | Test with small examples to verify |
| Forgetting to initialize | Loop variable not set | Always initialize before loop |
| Array out of bounds | `i < array.length` vs `i <= array.length` | Use `<` not `<=` for array access |

### When to Use Each Loop Type

**Use `for` loop when:**
- You know the number of iterations in advance
- You need a counter variable
- You're iterating through arrays with indices

**Use `while` loop when:**
- You don't know how many iterations you need
- You're waiting for a condition to be met
- You're processing input until a sentinel value

**Use `do-while` loop when:**
- You need the code to run at least once
- You're creating interactive menus
- You need to validate input

**Use `for-of` loop when:**
- You just want to iterate through all values in an array
- You don't need the index
- You want clean, readable code

### Advanced Challenge (For the Brave!)

Try this complex loop program:

```javascript
console.log("=== Advanced Loop Examples ===");

// Prime number finder
console.log("Prime numbers from 2 to 30:");
for (let num = 2; num <= 30; num++) {
    let isPrime = true;
    
    // Check if num is divisible by any number from 2 to sqrt(num)
    for (let divisor = 2; divisor <= Math.sqrt(num); divisor++) {
        if (num % divisor === 0) {
            isPrime = false;
            break;  // Found a divisor, not prime
        }
    }
    
    if (isPrime) {
        console.log(num + " is prime");
    }
}

console.log("");
// Factorial calculator
console.log("Factorials from 1 to 7:");
for (let n = 1; n <= 7; n++) {
    let factorial = 1;
    for (let i = 1; i <= n; i++) {
        factorial *= i;
    }
    console.log(n + "! = " + factorial);
}

console.log("");
// Fibonacci sequence
console.log("First 10 numbers in Fibonacci sequence:");
let a = 0, b = 1;
console.log("0: " + a);
console.log("1: " + b);

for (let i = 2; i < 10; i++) {
    let next = a + b;
    console.log(i + ": " + next);
    a = b;
    b = next;
}

console.log("");
// Multiplication table (1-10)
console.log("Multiplication table (1-5):");
for (let i = 1; i <= 5; i++) {
    let row = i + " | ";
    for (let j = 1; j <= 5; j++) {
        row += (i * j).toString().padStart(3, " ") + " ";
    }
    console.log(row);
}
```

---

 **Excellent work! You now understand how to repeat actions efficiently with loops!** 

*Ready for the next challenge? Let's learn about functions - the building blocks of reusable code!*