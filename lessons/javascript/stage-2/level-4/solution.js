// Algorithm 1: Simple Input Validation
const readlineSync = require('readline-sync');

// Algorithm: Validate User Age
console.log("Please enter your age: ");
let age = parseInt(readlineSync.question());

if (age < 0 || age > 150) {
    console.log("Invalid age! Please enter an age between 0 and 150.");
} else {
    console.log("Thank you! You are " + age + " years old.");
}

console.log(); // Add some spacing

// Algorithm 2: User Information Form
// Algorithm: Collect User Information
console.log("User Information Form");
console.log("===================");

console.log("Enter your name: ");
let name = readlineSync.question();

console.log("Enter your age: ");
let age2 = readlineSync.question();  // Renamed to avoid conflict

console.log("Enter your email: ");
let email = readlineSync.question();

console.log("Enter your favorite color: ");
let color = readlineSync.question();

console.log("");
console.log("SUMMARY:");
console.log("Name: " + name);
console.log("Age: " + age2);
console.log("Email: " + email);
console.log("Favorite Color: " + color);
console.log("Form submitted successfully!");

console.log(); // Add some spacing

// Algorithm 3: Number Validation Loop
// Algorithm: Get Valid Number
let valid_input = false;

while (!valid_input) {
    console.log("Enter a positive number: ");
    let number = parseFloat(readlineSync.question());
    
    if (number > 0) {
        valid_input = true;
        console.log("Valid number entered: " + number);
    } else {
        console.log("Invalid! Please enter a positive number.");
    }
}

console.log(); // Add some spacing

// Algorithm 4: Grade Calculator with Input
// Algorithm: Calculate Letter Grade
console.log("Grade Calculator");
console.log("===============");

console.log("Enter assignment score: ");
let score = parseFloat(readlineSync.question());

console.log("Enter total possible points: ");
let total_points = parseFloat(readlineSync.question());

let percentage = (score / total_points) * 100;
let letter_grade = "F";

if (percentage >= 90) {
    letter_grade = "A";
} else if (percentage >= 80) {
    letter_grade = "B";
} else if (percentage >= 70) {
    letter_grade = "C";
} else if (percentage >= 60) {
    letter_grade = "D";
}

console.log("Score: " + score + "/" + total_points);
console.log("Percentage: " + percentage.toFixed(2) + "%");
console.log("Letter Grade: " + letter_grade);

console.log(); // Add some spacing

// Algorithm 5: Temperature Converter with Menu
// Algorithm: Temperature Converter Menu
console.log("Temperature Converter");
console.log("1. Celsius to Fahrenheit");
console.log("2. Fahrenheit to Celsius");
console.log("Choose an option (1 or 2): ");

let choice = parseInt(readlineSync.question());

if (choice === 1) {
    console.log("Enter temperature in Celsius: ");
    let celsius = parseFloat(readlineSync.question());
    let fahrenheit = celsius * 9 / 5 + 32;
    console.log(celsius + "°C = " + fahrenheit.toFixed(2) + "°F");
} else if (choice === 2) {
    console.log("Enter temperature in Fahrenheit: ");
    let fahrenheit2 = parseFloat(readlineSync.question());  // Renamed to avoid conflict
    let celsius2 = (fahrenheit2 - 32) * 5 / 9;
    console.log(fahrenheit2 + "°F = " + celsius2.toFixed(2) + "°C");
} else {
    console.log("Invalid choice! Please enter 1 or 2.");
}

console.log(); // Add some spacing

// Algorithm 6: Input Validation with Multiple Fields
// Algorithm: Validate Contact Information
let is_valid = true;

console.log("Contact Information Form");

console.log("Enter your full name: ");
let name2 = readlineSync.question();  // Renamed to avoid conflict

if (name2.length < 2) {
    console.log("Name must be at least 2 characters long.");
    is_valid = false;
}

console.log("Enter your phone number: ");
let phone = readlineSync.question();

if (phone.length < 10) {
    console.log("Phone number must be at least 10 digits.");
    is_valid = false;
}

console.log("Enter your email: ");
let email2 = readlineSync.question();  // Renamed to avoid conflict

if (!email2.includes("@")) {
    console.log("Email must contain '@' symbol.");
    is_valid = false;
}

if (is_valid) {
    console.log("Form submitted successfully!");
} else {
    console.log("Form has errors. Please fix and resubmit.");
}

console.log(); // Add some spacing

// Algorithm 7: Calculator with User Interaction
// Algorithm: Interactive Calculator
console.log("Simple Calculator");

console.log("Enter first number: ");
let num1 = parseFloat(readlineSync.question());

console.log("Enter operator (+, -, *, /): ");
let operator = readlineSync.question();

console.log("Enter second number: ");
let num2 = parseFloat(readlineSync.question());

let result = 0;
let has_error = false;

if (operator === "+") {
    result = num1 + num2;
} else if (operator === "-") {
    result = num1 - num2;
} else if (operator === "*") {
    result = num1 * num2;
} else if (operator === "/") {
    if (num2 === 0) {
        console.log("Error: Division by zero!");
        has_error = true;
    } else {
        result = num1 / num2;
    }
} else {
    console.log("Error: Invalid operator!");
    has_error = true;
}

if (!has_error) {
    console.log(num1 + " " + operator + " " + num2 + " = " + result);
}