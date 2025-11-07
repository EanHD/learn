// String variables (text)
let name = "Alex";
let city = "New York";
let hobby = "programming";

// Number variables (integers and decimals)
let age = 25;
let height = 175.5;
let score = 100;

// Boolean variables (true/false)
let isStudent = true;
let isEmployed = false;
let isHappy = true;

// Print all the variables
console.log("=== Personal Info ===");
console.log("Name: " + name);
console.log("City: " + city);
console.log("Hobby: " + hobby);
console.log("");

console.log("=== Measurements ===");
console.log("Age: " + age + " years old");
console.log("Height: " + height + " cm");
console.log("Score: " + score + " points");
console.log("");

console.log("=== Status ===");
console.log("Student: " + isStudent);
console.log("Employed: " + isEmployed);
console.log("Happy: " + isHappy);

// JavaScript's dynamic typing - variables can change types!
console.log("");
console.log("=== Dynamic Typing Example ===");
let dynamicVar = "I'm a string";
console.log("Dynamic variable: " + dynamicVar);
dynamicVar = 42;  // Now it's a number!
console.log("Dynamic variable: " + dynamicVar);
dynamicVar = true; // Now it's a boolean!
console.log("Dynamic variable: " + dynamicVar);