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