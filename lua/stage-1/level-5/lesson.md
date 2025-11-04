# Level 5: Conditionals and Decision Making

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to make programs that can make decisions! Today you'll learn how to write code that does different things based on different conditions. This is where programs become truly intelligent!

---

### Learning Goals

- Understand if/then/else statements and decision making
- Learn comparison operators (==, ~=, <, >, <=, >=)
- Practice logical operators (and, or, not)
- Create programs that respond differently to different inputs
- Learn to chain multiple conditions together

---

### Your Task

**Copy the following code into a new file called `conditionals.lua`**

```lua
print("=== Simple Age Check ===")
-- Input for age
local age = 20

if age >= 18 then
    print("You are an adult (18 or older)")
else
    print("You are a minor (under 18)")
end

print()
print("=== Grade Classifier ===")
-- Input for grade
local grade = 85

if grade >= 90 then
    print("Grade: A (90-100)")
elseif grade >= 80 then
    print("Grade: B (80-89)")
elseif grade >= 70 then
    print("Grade: C (70-79)")
elseif grade >= 60 then
    print("Grade: D (60-69)")
else
    print("Grade: F (below 60)")
end

print()
print("=== Temperature Adviser ===")
-- Input for temperature
local temperature = 75  -- in Fahrenheit

if temperature > 80 then
    print("It's hot! Stay hydrated and wear light clothes.")
elseif temperature > 60 then
    print("It's a nice day! Perfect for outdoor activities.")
else
    print("It's cold! Don't forget your jacket.")
end

print()
print("=== Username and Password Check ===")
-- Input for login
local username = "admin"
local password = "secret123"

if username == "admin" and password == "secret123" then
    print("Login successful! Welcome, admin.")
else
    print("Login failed! Invalid username or password.")
end

print()
print("=== Multiple Condition Check ===")
-- Check if number is positive, even, and greater than 10
local number = 12

if number > 0 then
    print("The number is positive")
    if number % 2 == 0 then
        print("The number is even")
        if number > 10 then
            print("The number is greater than 10")
            print("This number is positive, even, and greater than 10!")
        else
            print("This number is positive and even, but not greater than 10")
        end
    else
        print("This number is positive and odd")
    end
else
    print("This number is not positive")
end

print()
print("=== Logical Operators Demo ===")
local has_id = true
local has_money = true
local age_check = 21

-- Using AND operator (and) - all conditions must be true
if has_id and has_money and age_check >= 18 then
    print("You can buy alcohol (if you're 18+ and have ID & money)")
else
    print("Cannot purchase: Missing ID, money, or age requirement")
end

-- Using OR operator (or) - at least one condition must be true
local has_credit_card = false
local has_debit_card = true
local has_cash = false

if has_credit_card or has_debit_card or has_cash then
    print("Payment method available")
else
    print("No payment method available")
end

-- Using NOT operator (not) - reverses the condition
local is_raining = false
if not is_raining then
    print("It's not raining, so no need for an umbrella!")
else
    print("It's raining, bring an umbrella!")
end

print()
print("=== Switch Statement Alternative (Using if-elseif) ===")
local day_of_week = 3  -- 1=Monday, 2=Tuesday, etc.

if day_of_week == 1 then
    print("Today is Monday - start of the work week")
elseif day_of_week == 2 then
    print("Today is Tuesday")
elseif day_of_week == 3 then
    print("Today is Wednesday - middle of the week")
elseif day_of_week == 4 then
    print("Today is Thursday")
elseif day_of_week == 5 then
    print("Today is Friday - weekend is almost here!")
elseif day_of_week == 6 then
    print("Today is Saturday - weekend fun!")
elseif day_of_week == 7 then
    print("Today is Sunday - rest day")
else
    print("Invalid day number! Please enter 1-7")
end

print()
print("=== Alternative: Using Table as Switch ===")
-- Lua doesn't have a switch statement, so we can use a table
local days = {
    [1] = "Monday - start of the work week",
    [2] = "Tuesday",
    [3] = "Wednesday - middle of the week", 
    [4] = "Thursday",
    [5] = "Friday - weekend is almost here!",
    [6] = "Saturday - weekend fun!",
    [7] = "Sunday - rest day"
}

local day_name = days[day_of_week]
if day_name then
    print("Using table: Today is " .. day_name)
else
    print("Using table: Invalid day number! Please enter 1-7")
end

print()
print("=== Truthy and Falsy Values ===")
-- In Lua, only nil and false are considered false
print("These values are truthy (evaluate to true in conditionals):")
print("- Number 0: " .. tostring(0 == true))  -- In conditional: true
print("- Empty string: " .. tostring("" == true))  -- In conditional: true
print("- Number -1: " .. tostring(-1 == true))  -- In conditional: true

print()
print("Only these are falsy:")
local test_nil = nil
local test_false = false
if not test_nil then print("- nil is falsy") end
if not test_false then print("- false is falsy") end
```lua

---

### How to Execute

1. **Run your program**:
   ```bash
   lua conditionals.lua
   ```lua

**Expected output:**
```lua
=== Simple Age Check ===
You are an adult (18 or older)

=== Grade Classifier ===
Grade: B (80-89)

=== Temperature Adviser ===
It's a nice day! Perfect for outdoor activities.

=== Username and Password Check ===
Login successful! Welcome, admin.

=== Multiple Condition Check ===
The number is positive
The number is even
The number is greater than 10
This number is positive, even, and greater than 10!

=== Logical Operators Demo ===
You can buy alcohol (if you're 18+ and have ID & money)
Payment method available
It's not raining, so no need for an umbrella!

=== Switch Statement Alternative (Using if-elseif) ===
Today is Wednesday - middle of the week

=== Alternative: Using Table as Switch ===
Using table: Today is Wednesday - middle of the week

=== Truthy and Falsy Values ===
These values are truthy (evaluate to true in conditionals):
- Number 0: true
- Empty string: true
- Number -1: true

Only these are falsy:
- nil is falsy
- false is falsy
```lua

---

### Success Checklist

- [ ] Created a file named `conditionals.lua`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw different code paths execute based on conditions
- [ ] Understood if/then/else statements and logical operators

---

### Understanding Comparison Operators

In Lua conditionals, you'll use these comparison operators:

- **`==`** = Equal to
- **`~=`** = Not equal to
- **`<`** = Less than
- **`>`** = Greater than
- **`<=`** = Less than or equal to
- **`>=`** = Greater than or equal to

---

### Try This (Optional Challenges)

1. Create a BMI classifier that gives different advice based on BMI ranges
2. Build a program that determines if a year is a leap year
3. Make a simple game where the computer picks a number and the user guesses
4. Create a traffic light simulator using conditionals

---

## Quick Reference

| Operator | Name | Purpose | Example | Result |
|----------|------|---------|---------|--------|
| `==` | Equal | Value comparison | `5 == 5` | `true` |
| `~=` | Not Equal | Value not equal | `5 ~= 3` | `true` |
| `<` | Less Than | Left less than right | `3 < 5` | `true` |
| `>` | Greater Than | Left greater than right | `5 < 3` | `true` |
| `<=` | Less or Equal | Left less than or equal | `5 <= 5` | `true` |
| `>=` | Greater or Equal | Left greater or equal | `5 >= 3` | `true` |
| `and` | AND | Both conditions true | `true and false` | `false` |
| `or` | OR | At least one true | `true or false` | `true` |
| `not` | NOT | Reverse the condition | `not true` | `false` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```lua
if age >= 18 then
    print("You are an adult (18 or older)")
else
    print("You are a minor (under 18)")
end
```lua
- **`if`** = Start of conditional statement
- **`age >= 18`** = Condition that evaluates to true or false
- **`then`** = Keyword required after condition
- **`end`** = Required to close the if block
- **`else`** = Code block executed if condition is false

```lua
if grade >= 90 then
    print("Grade: A (90-100)")
elseif grade >= 80 then
    print("Grade: B (80-89)")
elseif grade >= 70 then
    print("Grade: B (70-79)")
else
    print("Grade: F (below 60)")
end
```lua
- **`elseif`** = Additional condition to check if the first was false
- **Execution order** matters: Lua checks each condition in order and executes the first true one
- **Only one block** executes, not multiple blocks

```lua
if username == "admin" and password == "secret123" then
    print("Login successful! Welcome, admin.")
else
    print("Login failed! Invalid username or password.")
end
```lua
- **`and`** = Logical AND operator (both conditions must be true)
- **`==`** = Equality comparison operator
- **Security** considerations: Never hardcode credentials in real programs

### Comparison Operators Deep Dive

**Equality vs Assignment:**
```lua
-- Wrong! This assigns a value (would cause an error in conditional)
if username = "admin" then  -- ERROR: Should be ==

-- Correct! This compares values
if username == "admin" then  -- OK: Comparison
```lua

### Logical Operators

| Operator | Symbol | What it does | Example | Result |
|----------|--------|--------------|---------|--------|
| AND | `and` | Both conditions true | `true and false` | `false` |
| OR | `or` | At least one true | `true or false` | `true` |
| NOT | `not` | Reverse condition | `not true` | `false` |

**More Examples:**
```lua
-- AND: All conditions must be true
local age = 21
local has_id = true
local has_money = true
if age >= 21 and has_id and has_money then
    print("Can buy alcohol")
end

-- OR: At least one condition must be true
local credit = true
local debit = false
local cash = false
if credit or debit or cash then
    print("Payment available")
end

-- NOT: Reverses the condition
local is_logged_in = false
if not is_logged_in then
    print("Please log in first")
end
```lua

### Nested Conditionals

```lua
if number > 0 then
    print("The number is positive")
    if number % 2 == 0 then        -- Nested if
        print("The number is even")
        if number > 10 then         -- Double nested if
            print("The number is greater than 10")
        end
    end
end
```lua
- **Inner condition** only evaluated if outer condition is true
- **Be careful** with nesting - too deep can be hard to read

### Truthy and Falsy Values

This is a major difference from other languages!

**In Lua:**
- **Falsy values**: Only `nil` and `false`
- **Truthy values**: Everything else, including:
  - `0` (zero)
  - `""` (empty string)
  - Any other number
  - Any table, function, thread, userdata

```lua
-- Examples
if 0 then print("0 is truthy in Lua!") end           -- This prints!
if "" then print("Empty string is truthy in Lua!") end -- This prints!
if -1 then print("-1 is truthy in Lua!") end         -- This prints!

-- Only nil and false are falsy
if not nil then print("nil is falsy in Lua") end      -- This prints!
if not false then print("false is falsy in Lua") end  -- This prints!
```lua

**This is different from JavaScript, Python, C++, etc. where 0 and empty strings are falsy!**

### Control Flow with Logical Operators

```lua
-- Short-circuit evaluation
local result = true and print("This will print")
-- print() returns nil, which is assigned to result

-- Useful patterns
local name = user_input or "Anonymous"  -- Use default if user_input is nil
local value = some_condition and "yes" or "no"  -- Ternary-like operation
```lua

### Switch Alternative with Tables

```lua
-- Instead of long if-elseif chains, you can use a table:
local actions = {
    fire = function() print("Fire attack!") end,
    water = function() print("Water attack!") end,
    earth = function() print("Earth attack!") end
}

local element = "fire"
local action = actions[element]
if action then
    action()  -- Execute the fire attack function
end
```lua

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `expected 'then'` | Missing `then` after condition | Always use `if condition then` |
| `expected 'end'` | Missing `end` to close block | Always close if/then with `end` |
| Using `=` instead of `==` | Assigning instead of comparing | Use `==` for comparison, `=` for assignment |
| Unexpected truthy/falsy behavior | Forgetting Lua's truthy rules | Remember: only nil and false are falsy |
| Forgetting `elseif` instead of `else if` | Wrong syntax | Use `elseif`, not `else if` |

### Best Practices for Conditionals

**Use descriptive variable names:**
```lua
-- Good
if is_adult then ... end
if is_valid_email then ... end

-- Avoid
if x then ... end
if flag then ... end
```lua

**Keep conditions simple:**
```lua
-- Good - store complex condition in variable
local can_vote = age >= 18 and is_citizen and not is_in_prison
if can_vote then ... end

-- Avoid - hard to read
if age >= 18 and is_citizen and not is_in_prison then ... end
```lua

**Consider table lookup vs if/elseif:**
- Use `if/elseif` for complex conditions and ranges
- Use tables for simple value mapping

### Advanced Challenge (For the Brave!)

Try this complex conditional program:

```lua
print("=== Advanced Conditional Example ===")

-- A simple grading system with lots of conditions
local student_name = "Alex"
local exam_score = 88
local homework_score = 92
local participation = true

print("=== Student Report for " .. student_name .. " ===")

-- Calculate overall grade
local overall_score = (exam_score * 0.7) + (homework_score * 0.3)
print("Overall Score: " .. string.format("%.2f", overall_score))

-- Determine letter grade
local letter_grade
if overall_score >= 97 then
    letter_grade = "A+"
elseif overall_score >= 93 then
    letter_grade = "A"
elseif overall_score >= 90 then
    letter_grade = "A-"
elseif overall_score >= 87 then
    letter_grade = "B+"
elseif overall_score >= 83 then
    letter_grade = "B"
elseif overall_score >= 80 then
    letter_grade = "B-"
elseif overall_score >= 77 then
    letter_grade = "C+"
elseif overall_score >= 73 then
    letter_grade = "C"
elseif overall_score >= 70 then
    letter_grade = "C-"
elseif overall_score >= 67 then
    letter_grade = "D+"
elseif overall_score >= 63 then
    letter_grade = "D"
elseif overall_score >= 60 then
    letter_grade = "D-"
else
    letter_grade = "F"
end

print("Letter Grade: " .. letter_grade)

-- Special recognition
if letter_grade == "A+" and participation then
    print("Outstanding performance! Keep up the excellent work!")
elseif letter_grade == "A" or letter_grade == "A+" then
    print("Excellent work! Very impressive!")
elseif letter_grade == "B" or letter_grade == "B+" then
    print("Good job! You're doing well!")
elseif overall_score >= 70 then
    print("Satisfactory performance. Keep trying!")
else
    print("Please see your instructor for additional help.")
end

-- Graduation eligibility
if overall_score >= 75 and participation then
    print("Eligible for graduation with honors consideration")
elseif overall_score >= 60 then
    print("Eligible for graduation")
else
    print("Not eligible for graduation, must repeat course")
end
```lua

---

 **Excellent work! You now understand how to make your programs make intelligent decisions!** 

*Ready for the next challenge? Let's learn about loops and repetition!*


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


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

```lua
print("Hello, World!")

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard lua conventions with proper imports and main function
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
