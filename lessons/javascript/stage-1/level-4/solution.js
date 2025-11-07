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