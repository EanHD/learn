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
console.log("Is 12 even? " + isNumEven);

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