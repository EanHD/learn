// Basic arithmetic operations
console.log("=== Basic Arithmetic ===");

// Addition
let sum = 5 + 3;
console.log("5 + 3 = " + sum);

// Subtraction
let difference = 10 - 4;
console.log("10 - 4 = " + difference);

// Multiplication
let product = 6 * 7;
console.log("6 * 7 = " + product);

// Division
let quotient = 15 / 3;
console.log("15 / 3 = " + quotient);

// Modulo (remainder)
let remainder = 17 % 5;
console.log("17 % 5 = " + remainder + " (remainder)");

// Exponentiation (new in ES2016)
let power = 2 ** 3;
console.log("2 ** 3 = " + power + " (2 to the power of 3)");

console.log("");
console.log("=== Order of Operations ===");

// Parentheses change the order
let withParentheses = (10 + 5) * 2;
console.log("(10 + 5) * 2 = " + withParentheses);

let withoutParentheses = 10 + 5 * 2;
console.log("10 + 5 * 2 = " + withoutParentheses);

console.log("");
console.log("=== Real-World Calculations ===");

// Calculate area of rectangle
let length = 10;
let width = 5;
let area = length * width;
console.log("Rectangle area (" + length + " x " + width + "): " + area);

// Calculate circle area (π * r²)
let radius = 7;
let circleArea = 3.14159 * radius * radius;
console.log("Circle area (radius " + radius + "): " + circleArea);

// Calculate average of three numbers
let num1 = 10;
let num2 = 20;
let num3 = 30;
let average = (num1 + num2 + num3) / 3;
console.log("Average of " + num1 + ", " + num2 + ", " + num3 + ": " + average);

console.log("");
console.log("=== Increment and Decrement ===");

// Pre-increment (++variable)
let count = 5;
console.log("Initial count: " + count);
console.log("Pre-increment (++count): " + (++count));
console.log("After pre-increment: " + count);

// Post-increment (variable++)
let count2 = 5;
console.log("Initial count2: " + count2);
console.log("Post-increment (count2++): " + (count2++));
console.log("After post-increment: " + count2);

console.log("");
console.log("=== Compound Assignment Operators ===");

let value = 10;
console.log("Initial value: " + value);

value += 5;  // Same as: value = value + 5
console.log("After += 5: " + value);

value -= 3;  // Same as: value = value - 3
console.log("After -= 3: " + value);

value *= 2;  // Same as: value = value * 2
console.log("After *= 2: " + value);

value /= 4;  // Same as: value = value / 4
console.log("After /= 4: " + value);