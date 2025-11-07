// Algorithm 1: Simple Variable Swapping
let first_number = 10;
let second_number = 20;

console.log("Before swap: first=" + first_number + ", second=" + second_number);

let temp = first_number;
first_number = second_number;
second_number = temp;

console.log("After swap: first=" + first_number + ", second=" + second_number);

console.log(); // Add some spacing

// Algorithm 2: Running Total Calculator
let total = 0;
let count = 0;

let number = 5;
total = total + number;
count = count + 1;

number = 10;
total = total + number;
count = count + 1;

number = 15;
total = total + number;
count = count + 1;

let average = total / count;

console.log("Total: " + total);
console.log("Count: " + count);
console.log("Average: " + average);

console.log(); // Add some spacing

// Algorithm 3: Temperature Tracker
let min_temp = 100;
let max_temp = -100;

let current_temp = 72;
if (current_temp < min_temp) {
    min_temp = current_temp;
}
if (current_temp > max_temp) {
    max_temp = current_temp;
}
console.log("Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp);

current_temp = 65;
if (current_temp < min_temp) {
    min_temp = current_temp;
}
if (current_temp > max_temp) {
    max_temp = current_temp;
}
console.log("Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp);

current_temp = 80;
if (current_temp < min_temp) {
    min_temp = current_temp;
}
if (current_temp > max_temp) {
    max_temp = current_temp;
}
console.log("Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp);

console.log(); // Add some spacing

// Algorithm 4: Account Balance Tracker
let account_balance = 1000;

let transaction_amount = -50;
account_balance = account_balance + transaction_amount;
console.log("Balance after withdrawal: $" + account_balance);

transaction_amount = 200;
account_balance = account_balance + transaction_amount;
console.log("Balance after deposit: $" + account_balance);

transaction_amount = -75.50;
account_balance = account_balance + transaction_amount;
console.log("Balance after withdrawal: $" + account_balance);

transaction_amount = 150.25;
account_balance = account_balance + transaction_amount;
console.log("Balance after deposit: $" + account_balance);

console.log(); // Add some spacing

// Algorithm 5: Student Grade Calculator
let total_points = 0;
let possible_points = 0;

let assignment_points = 85;
let assignment_possible = 100;
total_points = total_points + assignment_points;
possible_points = possible_points + assignment_possible;

assignment_points = 92;
assignment_possible = 100;
total_points = total_points + assignment_points;
possible_points = possible_points + assignment_possible;

assignment_points = 78;
assignment_possible = 100;
total_points = total_points + assignment_points;
possible_points = possible_points + assignment_possible;

let percentage = (total_points / possible_points) * 100;
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

console.log("Total Points: " + total_points);
console.log("Possible Points: " + possible_points);
console.log("Percentage: " + percentage);
console.log("Letter Grade: " + letter_grade);

console.log(); // Add some spacing

// Algorithm 6: Counter Patterns
let counter = 1;
while (counter <= 5) {
    console.log("Count: " + counter);
    counter = counter + 1;
}

let even_counter = 2;
while (even_counter <= 10) {
    console.log("Even: " + even_counter);
    even_counter = even_counter + 2;
}

let odd_counter = 1;
while (odd_counter <= 10) {
    console.log("Odd: " + odd_counter);
    odd_counter = odd_counter + 2;
}

console.log(); // Add some spacing

// Algorithm 7: Accumulator Pattern
let sum = 0;
let count = 0;
let product = 1;

let current_value = 3;
sum = sum + current_value;
count = count + 1;
product = product * current_value;

current_value = 4;
sum = sum + current_value;
count = count + 1;
product = product * current_value;

current_value = 5;
sum = sum + current_value;
count = count + 1;
product = product * current_value;

let average = sum / count;

console.log("Sum: " + sum);
console.log("Count: " + count);
console.log("Product: " + product);
console.log("Average: " + average);