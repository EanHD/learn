# Level 5: Decision Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Level 5! Today we're focusing on decision-making operations in pseudocode. You'll learn to translate conditional statements and decision trees from pseudocode into working JavaScript code, and understand how to properly structure complex conditional logic.

---

### Learning Goals

- Understand how to represent decision-making in pseudocode
- Learn to translate nested if/else statements from pseudocode
- Practice complex conditional logic with multiple conditions
- Create programs with proper decision flow
- Develop awareness of decision tree structures

---

### Decision Operations in Pseudocode

Decision expressions in pseudocode follow these patterns:

**Simple if statements:**
```javascript
IF condition THEN
   DO something
ENDIF
```javascript

**If-else statements:**
```javascript
IF condition THEN
   DO something
ELSE
   DO something else
ENDIF
```javascript

**Multiple conditions:**
```javascript
IF condition1 THEN
   DO something
ELSE IF condition2 THEN
   DO something else
ELSE
   DO default action
ENDIF
```javascript

**Complex conditions:**
```javascript
IF (age >= 18) AND (has_license) THEN
   OUTPUT "Can drive"
ELSE
   OUTPUT "Cannot drive"
ENDIF
```javascript

**Nested conditions:**
```javascript
IF weather = "sunny" THEN
   IF temperature > 80 THEN
      OUTPUT "Hot and sunny - beach time!"
   ELSE
      OUTPUT "Sunny but cool - park time!"
   ENDIF
ELSE
   OUTPUT "Stay inside"
ENDIF
```javascript

---

### Your Task

**For each pseudocode algorithm below, translate it into working JavaScript code. Pay special attention to conditional logic and decision flow.**

---


### How to Run

1. **Run the code**:
   ```bash
   node hello.js
   ```java

**Expected output:**
```javascript
Hello, World!
```javascript

## Algorithm 1: Simple Age Check

**Pseudocode:**
```javascript
Algorithm: Determine Life Stage
1. INPUT age
2. IF age < 13 THEN
   3. OUTPUT "Child"
4. ELSE IF age < 20 THEN
   5. OUTPUT "Teenager"
6. ELSE IF age < 65 THEN
   7. OUTPUT "Adult"
8. ELSE
   9. OUTPUT "Senior"
10. ENDIF
```javascript

**Your Task:** Create a JavaScript program that categorizes by age.

---

## Algorithm 2: Grade Determination

**Pseudocode:**
```javascript
Algorithm: Assign Letter Grade
1. INPUT numeric_grade
2. IF numeric_grade >= 97 THEN
   3. SET letter_grade TO "A+"
4. ELSE IF numeric_grade >= 93 THEN
   5. SET letter_grade TO "A"
6. ELSE IF numeric_grade >= 90 THEN
   7. SET letter_grade TO "A-"
8. ELSE IF numeric_grade >= 87 THEN
   9. SET letter_grade TO "B+"
10. ELSE IF numeric_grade >= 83 THEN
   11. SET letter_grade TO "B"
12. ELSE IF numeric_grade >= 80 THEN
   13. SET letter_grade TO "B-"
14. ELSE IF numeric_grade >= 77 THEN
   15. SET letter_grade TO "C+"
16. ELSE IF numeric_grade >= 73 THEN
   17. SET letter_grade TO "C"
18. ELSE IF numeric_grade >= 70 THEN
   19. SET letter_grade TO "C-"
19. ELSE IF numeric_grade >= 67 THEN
   20. SET letter_grade TO "D+"
21. ELSE IF numeric_grade >= 65 THEN
   22. SET letter_grade TO "D"
23. ELSE
   24. SET letter_grade TO "F"
25. ENDIF
26. OUTPUT "Grade: " + letter_grade
```javascript

**Your Task:** Create a JavaScript program that determines letter grades.

---

## Algorithm 3: Shopping Discount Calculator

**Pseudocode:**
```javascript
Algorithm: Calculate Shopping Discount
1. INPUT total_amount
2. INPUT customer_type  // "regular", "premium", "vip"
3. SET discount_rate TO 0
4. IF customer_type = "vip" THEN
   5. IF total_amount >= 500 THEN
      6. SET discount_rate TO 0.20
   7. ELSE IF total_amount >= 200 THEN
      8. SET discount_rate TO 0.15
   9. ELSE
      10. SET discount_rate TO 0.10
   11. ENDIF
12. ELSE IF customer_type = "premium" THEN
   13. IF total_amount >= 300 THEN
      14. SET discount_rate TO 0.12
   15. ELSE IF total_amount >= 150 THEN
      16. SET discount_rate TO 0.08
   17. ELSE
      18. SET discount_rate TO 0.05
   19. ENDIF
20. ELSE
   21. IF total_amount >= 100 THEN
      22. SET discount_rate TO 0.03
   23. ENDIF
24. ENDIF
25. SET discount_amount TO total_amount * discount_rate
26. SET final_amount TO total_amount - discount_amount
27. OUTPUT "Original: $" + total_amount
28. OUTPUT "Discount: " + (discount_rate * 100) + "%"
29. OUTPUT "Final: $" + final_amount
```javascript

**Your Task:** Create a JavaScript program with nested decision logic for discounts.

---

## Algorithm 4: Weather Advisory

**Pseudocode:**
```javascript
Algorithm: Weather Advisory System
1. INPUT temperature
2. INPUT is_raining
3. INPUT is_snowing
4. INPUT wind_speed
5. OUTPUT "Weather Conditions:"
6. IF temperature > 90 THEN
   7. OUTPUT "Hot - Stay hydrated"
   8. IF is_raining THEN
      9. OUTPUT "Be careful of heat and rain combination"
   10. ENDIF
11. ELSE IF temperature > 70 THEN
   12. OUTPUT "Warm - Comfortable"
   13. IF is_raining THEN
      14. OUTPUT "Umbrella recommended"
   15. ENDIF
16. ELSE IF temperature > 32 THEN
   17. OUTPUT "Cool - Light jacket suggested"
   18. IF is_snowing THEN
      19. OUTPUT "Snow gear recommended"
   20. ENDIF
21. ELSE
   22. OUTPUT "Cold - Heavy coat needed"
   23. IF is_snowing OR is_raining THEN
      24. OUTPUT "Ice formation possible - be cautious"
   25. ENDIF
26. ENDIF
27. IF wind_speed > 25 THEN
   28. OUTPUT "High winds - Secure loose objects"
29. ENDIF
```javascript

**Your Task:** Create a JavaScript program that gives weather advisory.

---

## Algorithm 5: Password Validator

**Pseudocode:**
```javascript
Algorithm: Validate Password Strength
1. INPUT password
2. SET has_uppercase TO FALSE
3. SET has_lowercase TO FALSE
4. SET has_digit TO FALSE
5. SET has_special TO FALSE
6. SET length_ok TO FALSE
7. SET is_valid TO FALSE
8. IF LENGTH(password) >= 8 THEN
   9. SET length_ok TO TRUE
10. ENDIF
11. FOR each character IN password DO
   12. IF character IS uppercase THEN
      13. SET has_uppercase TO TRUE
   14. ELSE IF character IS lowercase THEN
      15. SET has_lowercase TO TRUE
   16. ELSE IF character IS digit THEN
      17. SET has_digit TO TRUE
   18. ELSE
      19. SET has_special TO TRUE
   20. ENDIF
21. ENDFOR
22. IF length_ok AND has_uppercase AND has_lowercase AND has_digit AND has_special THEN
   23. SET is_valid TO TRUE
   24. OUTPUT "Password is strong"
25. ELSE
   26. OUTPUT "Password is weak:"
   27. IF NOT length_ok THEN
      28. OUTPUT "- Must be at least 8 characters long"
   29. ENDIF
   30. IF NOT has_uppercase THEN
      31. OUTPUT "- Must contain uppercase letter"
   32. ENDIF
   33. IF NOT has_lowercase THEN
      34. OUTPUT "- Must contain lowercase letter"
   35. ENDIF
   36. IF NOT has_digit THEN
      37. OUTPUT "- Must contain digit"
   38. ENDIF
   39. IF NOT has_special THEN
      40. OUTPUT "- Must contain special character"
   41. ENDIF
42. ENDIF
```javascript

**Your Task:** Create a JavaScript program that validates password strength.

---

## Algorithm 6: Transportation Advisor

**Pseudocode:**
```javascript
Algorithm: Recommend Transportation
1. INPUT distance  // in miles
2. INPUT weather_condition  // "good", "bad", "severe"
3. INPUT purpose  // "commute", "shopping", "emergency"
4. OUTPUT "Transportation Recommendation:"
5. IF purpose = "emergency" THEN
   6. OUTPUT "Emergency services or taxi"
7. ELSE IF distance <= 1 AND weather_condition != "severe" THEN
   8. OUTPUT "Walking"
9. ELSE IF distance <= 3 AND weather_condition != "severe" THEN
   10. OUTPUT "Bicycle"
11. ELSE IF distance <= 15 AND weather_condition != "severe" THEN
   12. OUTPUT "Public transit"
13. ELSE IF weather_condition = "severe" THEN
   14. OUTPUT "Stay home or use professional service"
15. ELSE IF distance > 15 THEN
   16. OUTPUT "Personal vehicle"
17. ELSE
   18. OUTPUT "Consider public transit or taxi"
19. ENDIF
```javascript

**Your Task:** Create a JavaScript program that recommends transportation.

---

## Algorithm 7: Complex Business Logic

**Pseudocode:**
```javascript
Algorithm: Process Order
1. INPUT order_amount
2. INPUT customer_type  // "new", "returning", "loyal"
3. INPUT is_member  // TRUE/FALSE
4. INPUT days_since_last_order
5. SET discount TO 0
6. SET shipping_cost TO 5.99
7. SET is_priority_processing TO FALSE
8. IF order_amount >= 100 THEN
   9. SET discount TO 0.10
   10. SET shipping_cost TO 0  // Free shipping
11. ELSE IF is_member THEN
   12. SET discount TO 0.05
13. ENDIF
14. IF customer_type = "loyal" OR (customer_type = "returning" AND days_since_last_order < 30) THEN
   15. SET is_priority_processing TO TRUE
   16. SET discount TO discount + 0.05
17. ENDIF
18. IF customer_type = "new" AND order_amount > 50 THEN
   19. SET discount TO discount + 0.15  // Welcome discount
20. ENDIF
21. SET total_discount = order_amount * discount
22. SET final_amount = order_amount - total_discount + shipping_cost
23. OUTPUT "Order Summary:"
24. OUTPUT "Original Amount: $" + order_amount
25. OUTPUT "Discount (" + (discount*100) + "%): -$" + total_discount
26. OUTPUT "Shipping: $" + shipping_cost
27. OUTPUT "Final Amount: $" + final_amount
28. IF is_priority_processing THEN
   29. OUTPUT "Priority Processing: Yes"
30. ELSE
   30. OUTPUT "Priority Processing: No"
31. ENDIF
```javascript

**Your Task:** Create a JavaScript program with complex business logic.

---

### Key Concepts for Decision Operations

**If-Else Structure:**
- Properly nest if statements for complex logic
- Use else-if chains for mutually exclusive conditions
- Always consider the default case with else

**Boolean Logic:**
- Use `&&` (AND) when all conditions must be true
- Use `||` (OR) when any condition can be true
- Use `!` (NOT) to negate conditions

**Decision Flow:**
- Evaluate conditions in logical order
- Design decision trees to be clear and maintainable
- Test all possible decision paths

---

### Success Checklist

**For Each Algorithm:**
- [ ] Conditional logic correctly translated from pseudocode
- [ ] Nested conditions properly structured
- [ ] Program runs without errors
- [ ] All decision paths properly handled
- [ ] Output matches expected results

**Overall Progress:**
- [ ] Completed all 7 algorithms
- [ ] All programs work correctly
- [ ] Decision logic is properly implemented

---

### Try This (Optional Challenges)

1. **Enhance Algorithm 2**: Add grade pluses and minuses based on specific thresholds
2. **Enhance Algorithm 4**: Add more weather conditions and combinations
3. **Enhance Algorithm 6**: Consider real-time traffic data in recommendations
4. **Create Your Own**: Design a decision algorithm for recommending movies based on user preferences

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Simple Age Check

```javascript
// For Node.js environment with readline-sync
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
```javascript

### Algorithm 2: Grade Determination

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

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
```javascript

### Algorithm 3: Shopping Discount Calculator

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

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
```javascript

### Algorithm 4: Weather Advisory

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

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
```javascript

### Algorithm 5: Password Validator

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

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
```javascript

### Algorithm 6: Transportation Advisor

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

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
```javascript

### Algorithm 7: Complex Business Logic

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

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
```javascript

### Decision Operation Translation Patterns

| Pseudocode | JavaScript |
|------------|------------|
| `IF condition THEN` | `if (condition) {` |
| `ELSE IF condition THEN` | `} else if (condition) {` |
| `ELSE` | `} else {` |
| `ENDIF` | `}` |
| `AND` | `&&` |
| `OR` | `||` |
| `NOT` | `!` |
| `LENGTH(string)` | `string.length` |
| `FOR each item IN collection` | `for (let item of collection)` or traditional for loops |

### Important Notes

**Logical Operators**: Use `&&` for AND, `||` for OR, and `!` for NOT in JavaScript.

**String Comparison**: Use `===` for exact string comparison in JavaScript.

**Nested Conditions**: Properly indent nested if statements to maintain readability.

**Boolean Values**: JavaScript treats strings like "y" and "n" as strings; convert them to booleans when needed.

---

 **Excellent work! You've mastered translating decision operations from pseudocode to JavaScript!** 

*Next up: Loop pseudocode!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```js
console.log("Hello, World!");

```js

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard javascript conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
