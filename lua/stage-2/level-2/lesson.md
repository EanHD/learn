# Level 2: Variables in Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Level 2! Today we're focusing on how to handle variables in your pseudocode. You'll learn to translate pseudocode that uses variables into working Lua code, and understand how to track variable changes as your algorithms run.

---

### Learning Goals

- Understand how to represent variables in pseudocode
- Learn to translate variable declarations and assignments from pseudocode
- Practice tracking variable changes through algorithms
- Create programs that properly manage data flow
- Develop awareness of variable scope and state

---

### Variable Concepts in Pseudocode

Variables in pseudocode follow simple patterns:

**Declaration and assignment:**
```lua
SET name TO "John"
SET age TO 25
SET is_student TO TRUE
```

**Reassignment:**
```lua
SET age TO age + 1
SET total TO total + new_value
SET is_student TO FALSE
```

**Calculations with variables:**
```lua
SET area TO length * width
SET average TO (num1 + num2 + num3) / 3
SET is_adult TO age >= 18
```

---

### Your Task

**For each pseudocode algorithm below, translate it into working Lua code. Pay special attention to how variables are declared, assigned, and modified.**

---


### How to Run

1. **Run the code**:
   ```bash
   lua hello.lua
   ```

**Expected output:**
```
Hello, World!
```

## Algorithm 1: Simple Variable Swapping

**Pseudocode:**
```lua
Algorithm: Swap Two Variables
1. SET first_number TO 10
2. SET second_number TO 20
3. DISPLAY "Before swap: first=" + first_number + ", second=" + second_number
4. SET temp TO first_number
5. SET first_number TO second_number
6. SET second_number TO temp
7. DISPLAY "After swap: first=" + first_number + ", second=" + second_number
```

**Your Task:** Create a Lua program that demonstrates variable swapping.

---

## Algorithm 2: Running Total Calculator

**Pseudocode:**
```lua
Algorithm: Calculate Running Total
1. SET total TO 0
2. SET count TO 0
3. SET number TO 5
4. SET total TO total + number
5. SET count TO count + 1
6. SET number TO 10
7. SET total TO total + number
8. SET count TO count + 1
9. SET number TO 15
10. SET total TO total + number
11. SET count TO count + 1
12. SET average TO total / count
13. DISPLAY "Total: " + total
14. DISPLAY "Count: " + count
15. DISPLAY "Average: " + average
```

**Your Task:** Create a Lua program that calculates a running total and average.

---

## Algorithm 3: Temperature Tracker

**Pseudocode:**
```lua
Algorithm: Track Temperature Readings
1. SET min_temp TO 100
2. SET max_temp TO -100
3. SET current_temp TO 72
4. IF current_temp < min_temp THEN
   SET min_temp TO current_temp
5. IF current_temp > max_temp THEN
   SET max_temp TO current_temp
6. DISPLAY "Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp
7. SET current_temp TO 65
8. IF current_temp < min_temp THEN
   SET min_temp TO current_temp
9. IF current_temp > max_temp THEN
   SET max_temp TO current_temp
10. DISPLAY "Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp
11. SET current_temp TO 80
12. IF current_temp < min_temp THEN
   SET min_temp TO current_temp
13. IF current_temp > max_temp THEN
   SET max_temp TO current_temp
14. DISPLAY "Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp
```

**Your Task:** Create a Lua program that tracks min/max temperatures.

---

## Algorithm 4: Account Balance Tracker

**Pseudocode:**
```lua
Algorithm: Track Bank Account Balance
1. SET account_balance TO 1000
2. SET transaction_amount TO -50
3. SET account_balance TO account_balance + transaction_amount
4. DISPLAY "Balance after withdrawal: $" + account_balance
5. SET transaction_amount TO 200
6. SET account_balance TO account_balance + transaction_amount
7. DISPLAY "Balance after deposit: $" + account_balance
8. SET transaction_amount TO -75.50
9. SET account_balance TO account_balance + transaction_amount
10. DISPLAY "Balance after withdrawal: $" + account_balance
11. SET transaction_amount TO 150.25
12. SET account_balance TO account_balance + transaction_amount
13. DISPLAY "Balance after deposit: $" + account_balance
```

**Your Task:** Create a Lua program that tracks account balance changes.

---

## Algorithm 5: Student Grade Calculator

**Pseudocode:**
```lua
Algorithm: Calculate Student Grade
1. SET total_points TO 0
2. SET possible_points TO 0
3. SET assignment_points TO 85
4. SET assignment_possible TO 100
5. SET total_points TO total_points + assignment_points
6. SET possible_points TO possible_points + assignment_possible
7. SET assignment_points TO 92
8. SET assignment_possible TO 100
9. SET total_points TO total_points + assignment_points
10. SET possible_points TO possible_points + assignment_possible
11. SET assignment_points TO 78
12. SET assignment_possible TO 100
13. SET total_points TO total_points + assignment_points
14. SET possible_points TO possible_points + assignment_possible
15. SET percentage TO (total_points / possible_points) * 100
16. SET letter_grade TO "F"
17. IF percentage >= 90 THEN SET letter_grade TO "A"
18. ELSE IF percentage >= 80 THEN SET letter_grade TO "B"
19. ELSE IF percentage >= 70 THEN SET letter_grade TO "C"
20. ELSE IF percentage >= 60 THEN SET letter_grade TO "D"
21. DISPLAY "Total Points: " + total_points
22. DISPLAY "Possible Points: " + possible_points
23. DISPLAY "Percentage: " + percentage
24. DISPLAY "Letter Grade: " + letter_grade
```

**Your Task:** Create a Lua program that calculates student grades.

---

## Algorithm 6: Counter Patterns

**Pseudocode:**
```lua
Algorithm: Different Counter Patterns
1. SET counter TO 1
2. SET even_counter TO 2
3. SET odd_counter TO 1
4. WHILE counter <= 5 DO
   5. DISPLAY "Count: " + counter
   6. SET counter TO counter + 1
7. END WHILE
8. WHILE even_counter <= 10 DO
   9. DISPLAY "Even: " + even_counter
   10. SET even_counter TO even_counter + 2
11. END WHILE
12. WHILE odd_counter <= 10 DO
   13. DISPLAY "Odd: " + odd_counter
   14. SET odd_counter TO odd_counter + 2
15. END WHILE
```

**Your Task:** Create a Lua program that demonstrates different counting patterns.

---

## Algorithm 7: Accumulator Pattern

**Pseudocode:**
```lua
Algorithm: Calculate Statistics
1. SET sum TO 0
2. SET count TO 0
3. SET product TO 1
4. SET current_value TO 3
5. SET sum TO sum + current_value
6. SET count TO count + 1
7. SET product TO product * current_value
8. SET current_value TO 4
9. SET sum TO sum + current_value
10. SET count TO count + 1
11. SET product TO product * current_value
12. SET current_value TO 5
13. SET sum TO sum + current_value
14. SET count TO count + 1
15. SET product TO product * current_value
16. SET average TO sum / count
17. DISPLAY "Sum: " + sum
18. DISPLAY "Count: " + count
19. DISPLAY "Product: " + product
20. DISPLAY "Average: " + average
```

**Your Task:** Create a Lua program that demonstrates accumulator patterns.

---

### Key Concepts for Variable Handling

**Variable Declaration:**
- In Lua, variables are global by default unless declared with `local`
- Use `local` for variables that should only be accessible in the current scope

**Assignment vs Comparison:**
- Pseudocode `SET x TO value` becomes Lua `x = value`
- Pseudocode comparisons like `x > 5` become `x > 5` in Lua

**Tracking Variable Changes:**
- Each assignment statement updates the variable's value
- The order of operations matters in algorithms
- Variables can be used in calculations and then updated

---

### Success Checklist

**For Each Algorithm:**
- [ ] All variables properly declared using local for local scope
- [ ] Variable assignments correctly translated from pseudocode
- [ ] Program runs without errors
- [ ] Output matches expected results
- [ ] Variable state changes tracked correctly

**Overall Progress:**
- [ ] Completed all 7 algorithms
- [ ] All programs work correctly
- [ ] Code clearly shows variable tracking

---

### Try This (Optional Challenges)

1. **Enhance Algorithm 1**: Add multiple swaps in sequence to see how temporary variables work
2. **Enhance Algorithm 3**: Add more temperature readings and track how min/max change
3. **Enhance Algorithm 4**: Add a transaction history table to track all changes
4. **Create Your Own**: Write pseudocode for calculating compound interest with variables

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Simple Variable Swapping

```lua
-- Algorithm: Swap Two Variables
local first_number = 10
local second_number = 20

print("Before swap: first=" .. first_number .. ", second=" .. second_number)

local temp = first_number
first_number = second_number
second_number = temp

print("After swap: first=" .. first_number .. ", second=" .. second_number)
```

### Algorithm 2: Running Total Calculator

```lua
-- Algorithm: Calculate Running Total
local total = 0
local count = 0

local number = 5
total = total + number
count = count + 1

number = 10
total = total + number
count = count + 1

number = 15
total = total + number
count = count + 1

local average = total / count

print("Total: " .. total)
print("Count: " .. count)
print("Average: " .. average)
```

### Algorithm 3: Temperature Tracker

```lua
-- Algorithm: Track Temperature Readings
local min_temp = 100
local max_temp = -100

local current_temp = 72
if current_temp < min_temp then
    min_temp = current_temp
end
if current_temp > max_temp then
    max_temp = current_temp
end
print("Current: " .. current_temp .. ", Min: " .. min_temp .. ", Max: " .. max_temp)

current_temp = 65
if current_temp < min_temp then
    min_temp = current_temp
end
if current_temp > max_temp then
    max_temp = current_temp
end
print("Current: " .. current_temp .. ", Min: " .. min_temp .. ", Max: " .. max_temp)

current_temp = 80
if current_temp < min_temp then
    min_temp = current_temp
end
if current_temp > max_temp then
    max_temp = current_temp
end
print("Current: " .. current_temp .. ", Min: " .. min_temp .. ", Max: " .. max_temp)
```

### Algorithm 4: Account Balance Tracker

```lua
-- Algorithm: Track Bank Account Balance
local account_balance = 1000

local transaction_amount = -50
account_balance = account_balance + transaction_amount
print("Balance after withdrawal: $" .. account_balance)

transaction_amount = 200
account_balance = account_balance + transaction_amount
print("Balance after deposit: $" .. account_balance)

transaction_amount = -75.50
account_balance = account_balance + transaction_amount
print("Balance after withdrawal: $" .. account_balance)

transaction_amount = 150.25
account_balance = account_balance + transaction_amount
print("Balance after deposit: $" .. account_balance)
```

### Algorithm 5: Student Grade Calculator

```lua
-- Algorithm: Calculate Student Grade
local total_points = 0
local possible_points = 0

local assignment_points = 85
local assignment_possible = 100
total_points = total_points + assignment_points
possible_points = possible_points + assignment_possible

assignment_points = 92
assignment_possible = 100
total_points = total_points + assignment_points
possible_points = possible_points + assignment_possible

assignment_points = 78
assignment_possible = 100
total_points = total_points + assignment_points
possible_points = possible_points + assignment_possible

local percentage = (total_points / possible_points) * 100
local letter_grade = "F"

if percentage >= 90 then
    letter_grade = "A"
elseif percentage >= 80 then
    letter_grade = "B"
elseif percentage >= 70 then
    letter_grade = "C"
elseif percentage >= 60 then
    letter_grade = "D"
end

print("Total Points: " .. total_points)
print("Possible Points: " .. possible_points)
print("Percentage: " .. percentage)
print("Letter Grade: " .. letter_grade)
```

### Algorithm 6: Counter Patterns

```lua
-- Algorithm: Different Counter Patterns
local counter = 1
while counter <= 5 do
    print("Count: " .. counter)
    counter = counter + 1
end

local even_counter = 2
while even_counter <= 10 do
    print("Even: " .. even_counter)
    even_counter = even_counter + 2
end

local odd_counter = 1
while odd_counter <= 10 do
    print("Odd: " .. odd_counter)
    odd_counter = odd_counter + 2
end
```

### Algorithm 7: Accumulator Pattern

```lua
-- Algorithm: Calculate Statistics
local sum = 0
local count = 0
local product = 1

local current_value = 3
sum = sum + current_value
count = count + 1
product = product * current_value

current_value = 4
sum = sum + current_value
count = count + 1
product = product * current_value

current_value = 5
sum = sum + current_value
count = count + 1
product = product * current_value

local average = sum / count

print("Sum: " .. sum)
print("Count: " .. count)
print("Product: " .. product)
print("Average: " .. average)
```

### Variable Translation Patterns

| Pseudocode | Lua |
|------------|-----|
| `SET variable TO value` | `local variable = value` |
| `SET variable TO variable + 1` | `variable = variable + 1` |
| `SET variable TO variable * value` | `variable = variable * value` |
| `SET variable TO calculation` | `local variable = calculation` |

### Important Notes

**Scope**: In Lua, variables are global by default unless declared with `local`. Always use `local` for variables that don't need global access.

**Dynamic Typing**: Like JavaScript, Lua variables can change type, but for algorithm translation, the type usually stays consistent.

**String Concatenation**: Use `..` to concatenate strings and variables in Lua.

**Accumulator Pattern**: This is a common pattern where a variable accumulates values: `total = total + newValue`.

**Swapping Pattern**: To swap two variables, you need a temporary variable to hold one value during the swap.

---

 **Excellent work! You've mastered handling variables in pseudocode-to-code translation!** 

*Next up: Mathematical operations in pseudocode!*
