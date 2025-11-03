// Algorithm 1: Greeting Program
const readlineSync = require('readline-sync');

console.log("Algorithm 1: Greeting Program");

// Display "Hello! What's your name?" to the user
let name = readlineSync.question("Hello! What's your name? ");

// Display "Nice to meet you, " followed by the user's name
console.log("Nice to meet you, " + name);

// Display "Welcome to programming!"
console.log("Welcome to programming!");

console.log("\n"); // Add some spacing

// Algorithm 2: Simple Calculator
console.log("Algorithm 2: Simple Calculator");

// Ask user for first number
let firstNum = parseFloat(readlineSync.question("Enter first number: "));

// Ask user for second number
let secondNum = parseFloat(readlineSync.question("Enter second number: "));

// Calculate sum of the two numbers
let sum = firstNum + secondNum;

// Display "The sum is: " followed by the sum
console.log("The sum is: " + sum);

console.log("\n"); // Add some spacing

// Algorithm 3: Age Calculator
console.log("Algorithm 3: Age Calculator");

// Display "Enter your age in years: "
let age = parseInt(readlineSync.question("Enter your age in years: "));

// Calculate days = age × 365
let days = age * 365;

// Display messages
console.log("You are approximately " + days + " days old");
console.log("That's a lot of days!");

console.log("\n"); // Add some spacing

// Algorithm 4: Temperature Converter
console.log("Algorithm 4: Temperature Converter");

// Display "Enter temperature in Celsius: "
let celsius = parseFloat(readlineSync.question("Enter temperature in Celsius: "));

// Calculate Fahrenheit = (Celsius × 9/5) + 32
let fahrenheit = (celsius * 9/5) + 32;

// Display the results
console.log(celsius + "°C = " + fahrenheit + "°F");

console.log("\n"); // Add some spacing

// Algorithm 5: Rectangle Area Calculator
console.log("Rectangle Area Calculator");

// Get length from user
let length = parseFloat(readlineSync.question("Enter length: "));

// Get width from user
let width = parseFloat(readlineSync.question("Enter width: "));

// Calculate area = length × width
let area = length * width;

// Calculate perimeter = 2 × (length + width)
let perimeter = 2 * (length + width);

// Display results
console.log("Area: " + area);
console.log("Perimeter: " + perimeter);

console.log("\n"); // Add some spacing

// Algorithm 6: Simple Interest Calculator
console.log("Simple Interest Calculator");

// Get principal from user
let principal = parseFloat(readlineSync.question("Enter principal amount: $"));

// Get rate from user
let rate = parseFloat(readlineSync.question("Enter interest rate (%): "));

// Get time from user
let time = parseFloat(readlineSync.question("Enter time in years: "));

// Calculate interest = (principal × rate × time) ÷ 100
let interest = (principal * rate * time) / 100;

// Calculate total = principal + interest
let total = principal + interest;

// Display results
console.log("Principal: $" + principal.toFixed(2));
console.log("Interest: $" + interest.toFixed(2));
console.log("Total: $" + total.toFixed(2));

console.log("\n"); // Add some spacing

// Algorithm 7: BMI Calculator
console.log("BMI Calculator");

// Get weight from user
let weight = parseFloat(readlineSync.question("Enter weight in kg: "));

// Get height from user
let height = parseFloat(readlineSync.question("Enter height in meters: "));

// Calculate bmi = weight ÷ (height × height)
let bmi = weight / (height * height);

// Display the BMI
console.log("Your BMI is: " + bmi.toFixed(2));

// Category determination
if (bmi < 18.5) {
    console.log("Category: Underweight");
} else if (bmi < 25) {
    console.log("Category: Normal weight");
} else if (bmi < 30) {
    console.log("Category: Overweight");
} else {
    console.log("Category: Obesity");
}