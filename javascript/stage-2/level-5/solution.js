// Algorithm 1: Simple Age Check
const readlineSync = require('readline-sync');

// Algorithm: Determine Life Stage
let age = parseInt(readlineSync.question("Enter age: "));

if (age < 13) {
    console.log("Child");
} else if (age < 20) {
    console.log("Teenager");
} else if (age < 65) {
    console.log("Adult");
} else {
    console.log("Senior");
}

console.log(); // Add spacing

// Algorithm 2: Grade Determination
// Algorithm: Assign Letter Grade
let numeric_grade = parseFloat(readlineSync.question("Enter numeric grade: "));
let letter_grade;

if (numeric_grade >= 97) {
    letter_grade = "A+";
} else if (numeric_grade >= 93) {
    letter_grade = "A";
} else if (numeric_grade >= 90) {
    letter_grade = "A-";
} else if (numeric_grade >= 87) {
    letter_grade = "B+";
} else if (numeric_grade >= 83) {
    letter_grade = "B";
} else if (numeric_grade >= 80) {
    letter_grade = "B-";
} else if (numeric_grade >= 77) {
    letter_grade = "C+";
} else if (numeric_grade >= 73) {
    letter_grade = "C";
} else if (numeric_grade >= 70) {
    letter_grade = "C-";
} else if (numeric_grade >= 67) {
    letter_grade = "D+";
} else if (numeric_grade >= 65) {
    letter_grade = "D";
} else {
    letter_grade = "F";
}

console.log("Grade: " + letter_grade);

console.log(); // Add spacing

// Algorithm 3: Shopping Discount Calculator
// Algorithm: Calculate Shopping Discount
let total_amount = parseFloat(readlineSync.question("Enter total amount: "));
let customer_type = readlineSync.question("Enter customer type (regular/premium/vip): ");

let discount_rate = 0;

if (customer_type === "vip") {
    if (total_amount >= 500) {
        discount_rate = 0.20;
    } else if (total_amount >= 200) {
        discount_rate = 0.15;
    } else {
        discount_rate = 0.10;
    }
} else if (customer_type === "premium") {
    if (total_amount >= 300) {
        discount_rate = 0.12;
    } else if (total_amount >= 150) {
        discount_rate = 0.08;
    } else {
        discount_rate = 0.05;
    }
} else {
    if (total_amount >= 100) {
        discount_rate = 0.03;
    }
}

let discount_amount = total_amount * discount_rate;
let final_amount = total_amount - discount_amount;

console.log("Original: $" + total_amount.toFixed(2));
console.log("Discount: " + (discount_rate * 100) + "%");
console.log("Final: $" + final_amount.toFixed(2));

console.log(); // Add spacing

// Algorithm 4: Weather Advisory
// Algorithm: Weather Advisory System
let temperature = parseFloat(readlineSync.question("Enter temperature: "));
let is_raining = readlineSync.question("Is it raining? (y/n): ").toLowerCase() === 'y';
let is_snowing = readlineSync.question("Is it snowing? (y/n): ").toLowerCase() === 'y';
let wind_speed = parseFloat(readlineSync.question("Enter wind speed: "));

console.log("Weather Conditions:");

if (temperature > 90) {
    console.log("Hot - Stay hydrated");
    if (is_raining) {
        console.log("Be careful of heat and rain combination");
    }
} else if (temperature > 70) {
    console.log("Warm - Comfortable");
    if (is_raining) {
        console.log("Umbrella recommended");
    }
} else if (temperature > 32) {
    console.log("Cool - Light jacket suggested");
    if (is_snowing) {
        console.log("Snow gear recommended");
    }
} else {
    console.log("Cold - Heavy coat needed");
    if (is_snowing || is_raining) {
        console.log("Ice formation possible - be cautious");
    }
}

if (wind_speed > 25) {
    console.log("High winds - Secure loose objects");
}

console.log(); // Add spacing

// Algorithm 5: Password Validator
// Algorithm: Validate Password Strength
let password = readlineSync.question("Enter password: ");

let has_uppercase = false;
let has_lowercase = false;
let has_digit = false;
let has_special = false;
let length_ok = false;

if (password.length >= 8) {
    length_ok = true;
}

for (let i = 0; i < password.length; i++) {
    let char = password[i];
    if (char >= 'A' && char <= 'Z') {
        has_uppercase = true;
    } else if (char >= 'a' && char <= 'z') {
        has_lowercase = true;
    } else if (char >= '0' && char <= '9') {
        has_digit = true;
    } else {
        has_special = true;
    }
}

if (length_ok && has_uppercase && has_lowercase && has_digit && has_special) {
    console.log("Password is strong");
} else {
    console.log("Password is weak:");
    if (!length_ok) console.log("- Must be at least 8 characters long");
    if (!has_uppercase) console.log("- Must contain uppercase letter");
    if (!has_lowercase) console.log("- Must contain lowercase letter");
    if (!has_digit) console.log("- Must contain digit");
    if (!has_special) console.log("- Must contain special character");
}

console.log(); // Add spacing

// Algorithm 6: Transportation Advisor
// Algorithm: Recommend Transportation
let distance = parseFloat(readlineSync.question("Enter distance in miles: "));
let weather_condition = readlineSync.question("Enter weather (good/bad/severe): ");
let purpose = readlineSync.question("Enter purpose (commute/shopping/emergency): ");

console.log("Transportation Recommendation:");

if (purpose === "emergency") {
    console.log("Emergency services or taxi");
} else if (distance <= 1 && weather_condition !== "severe") {
    console.log("Walking");
} else if (distance <= 3 && weather_condition !== "severe") {
    console.log("Bicycle");
} else if (distance <= 15 && weather_condition !== "severe") {
    console.log("Public transit");
} else if (weather_condition === "severe") {
    console.log("Stay home or use professional service");
} else if (distance > 15) {
    console.log("Personal vehicle");
} else {
    console.log("Consider public transit or taxi");
}

console.log(); // Add spacing

// Algorithm 7: Complex Business Logic
// Algorithm: Process Order
let order_amount = parseFloat(readlineSync.question("Enter order amount: "));
let customer_type = readlineSync.question("Enter customer type (new/returning/loyal): ");
let is_member = readlineSync.question("Is member? (y/n): ").toLowerCase() === 'y';
let days_since_last_order = parseInt(readlineSync.question("Days since last order: "));

let discount = 0;
let shipping_cost = 5.99;
let is_priority_processing = false;

if (order_amount >= 100) {
    discount = 0.10;
    shipping_cost = 0;  // Free shipping
} else if (is_member) {
    discount = 0.05;
}

if (customer_type === "loyal" || (customer_type === "returning" && days_since_last_order < 30)) {
    is_priority_processing = true;
    discount += 0.05;
}

if (customer_type === "new" && order_amount > 50) {
    discount += 0.15;  // Welcome discount
}

let total_discount = order_amount * discount;
let final_amount = order_amount - total_discount + shipping_cost;

console.log("Order Summary:");
console.log("Original Amount: $" + order_amount.toFixed(2));
console.log("Discount (" + (discount*100).toFixed(2) + "%): -$" + total_discount.toFixed(2));
console.log("Shipping: $" + shipping_cost.toFixed(2));
console.log("Final Amount: $" + final_amount.toFixed(2));

if (is_priority_processing) {
    console.log("Priority Processing: Yes");
} else {
    console.log("Priority Processing: No");
}