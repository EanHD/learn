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