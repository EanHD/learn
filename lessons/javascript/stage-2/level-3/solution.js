// Algorithm 1: Complex Arithmetic Expression
let a = 10;
let b = 5;
let c = 2;

let result = (a + b) * c - a / c;
console.log("Result: " + result);

let result2 = a + b * c - a / c;
console.log("Result without parentheses: " + result2);

let result3 = ((a + b) * c - a) / c;
console.log("Result with different grouping: " + result3);

console.log(); // Add some spacing

// Algorithm 2: Quadratic Formula Calculator
let a2 = 1;  // Renamed to avoid conflict
let b2 = -5;
let c2 = 6;

let discriminant = b2 * b2 - 4 * a2 * c2;
let sqrt_discriminant = Math.sqrt(discriminant);
let root1 = (-b2 + sqrt_discriminant) / (2 * a2);
let root2 = (-b2 - sqrt_discriminant) / (2 * a2);

console.log("Root 1: " + root1);
console.log("Root 2: " + root2);

console.log(); // Add some spacing

// Algorithm 3: Compound Interest Calculator
let principal = 1000;
let rate = 0.05;
let time = 10;
let compounds_per_year = 12;

let amount = principal * Math.pow(1 + rate / compounds_per_year, compounds_per_year * time);
let interest = amount - principal;

console.log("Principal: $" + principal);
console.log("Final Amount: $" + amount.toFixed(2));
console.log("Interest Earned: $" + interest.toFixed(2));

console.log(); // Add some spacing

// Algorithm 4: Geometric Calculations
let radius = 5;
let side = 4;
let base = 6;
let height = 8;

let circle_area = Math.PI * radius * radius;
let circle_circumference = 2 * Math.PI * radius;
let square_area = side * side;
let square_perimeter = 4 * side;
let triangle_area = 0.5 * base * height;

console.log("Circle - Area: " + circle_area.toFixed(2) + ", Circumference: " + circle_circumference.toFixed(2));
console.log("Square - Area: " + square_area + ", Perimeter: " + square_perimeter);
console.log("Triangle - Area: " + triangle_area);

console.log(); // Add some spacing

// Algorithm 5: Physics Formula Calculator
let mass = 5.5;
let velocity = 10;
let acceleration = 9.8;
let time2 = 3;  // Renamed to avoid conflict

let kinetic_energy = 0.5 * mass * velocity * velocity;
let force = mass * acceleration;
let distance = velocity * time2 + 0.5 * acceleration * time2 * time2;
let momentum = mass * velocity;

console.log("Kinetic Energy: " + kinetic_energy);
console.log("Force: " + force);
console.log("Distance: " + distance);
console.log("Momentum: " + momentum);

console.log(); // Add some spacing

// Algorithm 6: Temperature Conversion with Multiple Formulas
let celsius = 25;
let fahrenheit = celsius * 9 / 5 + 32;
let kelvin = celsius + 273.15;
let celsius_from_f = (fahrenheit - 32) * 5 / 9;
let celsius_from_k = kelvin - 273.15;

console.log("Celsius: " + celsius);
console.log("Fahrenheit: " + fahrenheit);
console.log("Kelvin: " + kelvin);
console.log("F to C: " + celsius_from_f);
console.log("K to C: " + celsius_from_k);

console.log(); // Add some spacing

// Algorithm 7: Statistical Calculations
let num1 = 10;
let num2 = 20;
let num3 = 30;

let sum = num1 + num2 + num3;
let average = sum / 3;
let range = num3 - num1; // assuming num3 is largest, num1 is smallest
let sum_of_squares = num1 * num1 + num2 * num2 + num3 * num3;
let mean_of_squares = sum_of_squares / 3;
let variance = mean_of_squares - average * average;
let std_deviation = Math.sqrt(variance);

console.log("Sum: " + sum);
console.log("Average: " + average);
console.log("Range: " + range);
console.log("Variance: " + variance);
console.log("Standard Deviation: " + std_deviation.toFixed(2));