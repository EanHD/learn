# Level 3: Basic Math Operations

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to do some math! Today you'll learn how to perform mathematical operations in Lua. You'll work with numbers, calculate results, and see how Lua handles different mathematical operations.

---

### Learning Goals

- Learn Lua arithmetic operators (+, -, *, /, %, ^)
- Practice mathematical calculations
- Understand operator precedence
- Learn about the modulo operator (%)
- Understand how Lua handles different number types

---

### Your Task

**Copy the following code into a new file called `math.lua`**

```
-- Basic arithmetic operations
print("=== Basic Arithmetic ===")

-- Addition
sum = 5 + 3
print("5 + 3 = " .. sum)

-- Subtraction
difference = 10 - 4
print("10 - 4 = " .. difference)

-- Multiplication
product = 6 * 7
print("6 * 7 = " .. product)

-- Division
quotient = 15 / 3
print("15 / 3 = " .. quotient)

-- Modulo (remainder)
remainder = 17 % 5
print("17 % 5 = " .. remainder .. " (remainder)")

-- Exponentiation (power)
power = 2 ^ 3
print("2 ^ 3 = " .. power .. " (2 to the power of 3)")

print()
print("=== Order of Operations ===")

-- Parentheses change the order
with_parentheses = (10 + 5) * 2
print("(10 + 5) * 2 = " .. with_parentheses)

without_parentheses = 10 + 5 * 2
print("10 + 5 * 2 = " .. without_parentheses)

print()
print("=== Real-World Calculations ===")

-- Calculate area of rectangle
length = 10
width = 5
area = length * width
print("Rectangle area (" .. length .. " x " .. width .. "): " .. area)

-- Calculate circle area (π * r²)
radius = 7
circle_area = 3.14159 * radius * radius
print("Circle area (radius " .. radius .. "): " .. circle_area)

-- Calculate average of three numbers
num1 = 10
num2 = 20
num3 = 30
average = (num1 + num2 + num3) / 3
print("Average of " .. num1 .. ", " .. num2 .. ", " .. num3 .. ": " .. average)

print()
print("=== Increment and Decrement (Manual) ===")

-- Lua doesn't have ++ or -- operators, so we do it manually
count = 5
print("Initial count: " .. count)
count = count + 1  -- Increment by 1
print("After increment: " .. count)

count2 = 5
print("Initial count2: " .. count2)
count2 = count2 + 1  -- Increment by 1
print("After increment: " .. count2)

print()
print("=== Compound Assignment Operations ===")

value = 10
print("Initial value: " .. value)

value = value + 5  -- Same as: value += 5 (if it existed)
print("After adding 5: " .. value)

value = value - 3  -- Same as: value -= 3 (if it existed)
print("After subtracting 3: " .. value)

value = value * 2  -- Same as: value *= 2 (if it existed)
print("After multiplying by 2: " .. value)

value = value / 4  -- Same as: value /= 4 (if it existed)
print("After dividing by 4: " .. value)

print()
print("=== Advanced Math Functions ===")

-- Use the math library for more advanced operations
print("Square root of 16: " .. math.sqrt(16))
print("Absolute value of -10: " .. math.abs(-10))
print("Ceiling of 4.2: " .. math.ceil(4.2))
print("Floor of 4.7: " .. math.floor(4.7))
print("Round 4.7: " .. math.floor(4.7 + 0.5))  -- Lua doesn't have round(), this is a workaround

-- Random number generation
math.randomseed(os.time())  -- Seed for random generator
print("Random number 1-10: " .. math.random(1, 10))
print("Random number 0-1: " .. math.random())

print()
print("=== Number Type Handling ===")

-- Lua has one number type that handles both integers and floats
integer_num = 42
decimal_num = 3.14159
print("Integer: " .. integer_num .. " (type: " .. type(integer_num) .. ")")
print("Decimal: " .. decimal_num .. " (type: " .. type(decimal_num) .. ")")

-- Large numbers
big_num = 123456789012345
print("Large number: " .. big_num)

-- Negative numbers
negative_num = -25
print("Negative number: " .. negative_num)

print()
print("=== Boolean Logic with Numbers ===")

-- Lua considers 0 as true in boolean context (unlike other languages)
if 0 then
    print("In Lua, 0 is considered true in boolean context")
else
    print("This won't print")
end

-- Only nil and false are considered false in boolean context
if not nil and not false then
    print("Only nil and false are considered false")
end
```

---

### How to Execute

1. **Run your program**:
   ```
   lua math.lua
   ```

**Expected output:**
```
=== Basic Arithmetic ===
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
15 / 3 = 5
17 % 5 = 2 (remainder)
2 ^ 3 = 8 (2 to the power of 3)

=== Order of Operations ===
(10 + 5) * 2 = 30
10 + 5 * 2 = 20

=== Real-World Calculations ===
Rectangle area (10 x 5): 50
Circle area (radius 7): 153.93804000000003
Average of 10, 20, 30: 20

=== Increment and Decrement (Manual) ===
Initial count: 5
After increment: 6
Initial count2: 5
After increment: 6

=== Compound Assignment Operations ===
Initial value: 10
After adding 5: 15
After subtracting 3: 12
After multiplying by 2: 24
After dividing by 4: 6

=== Advanced Math Functions ===
Square root of 16: 4
Absolute value of -10: 10
Ceiling of 4.2: 5
Floor of 4.7: 4
Round 4.7: 5
Random number 1-10: 7
Random number 0-1: 0.23456789

=== Number Type Handling ===
Integer: 42 (type: number)
Decimal: 3.14159 (type: number)
Large number: 123456789012345
Negative number: -25

=== Boolean Logic with Numbers ===
In Lua, 0 is considered true in boolean context
Only nil and false are considered false
```

*Note: Random numbers will vary each time you run the program*

---

### Success Checklist

- [ ] Created a file named `math.lua`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw all mathematical operations working correctly
- [ ] Understood operator precedence and different operations

---

### What's That Math Symbol Mean?

In Lua math, you saw some operators:

- **`+`** = Addition
- **`-`** = Subtraction
- **`*`** = Multiplication
- **`/`** = Division
- **`%`** = Modulo (remainder after division)
- **`^`** = Exponentiation (to the power of)

---

### Try This (Optional Challenges)

1. Calculate compound interest: A = P(1+r/n)^nt
2. Create a temperature converter (Celsius to Fahrenheit)
3. Calculate the hypotenuse of a right triangle using the Pythagorean theorem
4. Experiment with dividing by zero - what happens?

---

## Quick Reference

| Operator | What it does | Example | Result |
|----------|--------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 3` | `2` |
| `%` | Modulo (remainder) | `7 % 3` | `1` |
| `^` | Exponentiation | `2 ^ 3` | `8` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```
sum = 5 + 3
print("5 + 3 = " .. sum)
```
- **`=`** = Assignment operator (stores the result of 5 + 3 into variable 'sum')
- **`+`** = Addition operator (performs arithmetic addition)
- **String concatenation**: The `..` operator joins strings and numbers (number automatically converted)

```
remainder = 17 % 5
print("17 % 5 = " .. remainder .. " (remainder)")
```
- **`%`** = Modulo operator (returns the remainder after division)
- 17 ÷ 5 = 3 remainder 2, so 17 % 5 = 2
- Useful for checking if numbers are even (n % 2 == 0) or cycling through values

```
power = 2 ^ 3
print("2 ^ 3 = " .. power .. " (2 to the power of 3)")
```
- **`^`** = Exponentiation operator (raises left number to power of right number)
- 2 ^ 3 = 2 to the power of 3 = 2 × 2 × 2 = 8

### Order of Operations (PEMDAS)

Lua follows the standard mathematical order of operations:

1. **P**arentheses `()`
2. **E**xponents `^`
3. **M**ultiplication `*` and **D**ivision `/` (left to right)
4. **A**ddition `+` and **S**ubtraction `-` (left to right)
5. **M**odulo `%` (same precedence as multiplication and division)

Examples:
```
-- Without parentheses: Multiplication before addition
result = 10 + 5 * 2  -- = 10 + 10 = 20 (not 30!)

-- With parentheses: Addition before multiplication
result = (10 + 5) * 2  -- = 15 * 2 = 30
```

### Lua's Math Library

Lua comes with a built-in math library for advanced operations:

```
-- Basic operations
math.sqrt(16)     -- Square root: 4
math.abs(-5)      -- Absolute value: 5
math.min(1, 5, 3) -- Minimum: 1
math.max(1, 5, 3) -- Maximum: 5

-- Rounding functions
math.floor(4.7)   -- Floor (round down): 4
math.ceil(4.2)    -- Ceiling (round up): 5
-- Note: Lua doesn't have math.round(), use math.floor(x + 0.5)

-- Trigonometry (in radians)
math.sin(math.pi/2)  -- Sine of π/2: 1
math.cos(0)          -- Cosine of 0: 1

-- Constants
math.pi     -- π: 3.141592653589793
math.huge   -- Infinity
```

### Random Number Generation

```
-- Seed the random generator (typically done once at program start)
math.randomseed(os.time())

-- Random integer between min and max (inclusive)
random_int = math.random(1, 100)  -- Random 1-100

-- Random float between 0 and 1
random_float = math.random()  -- 0.0 to 1.0

-- Random integer between 1 and N
random_single = math.random(10)  -- Random 1-10
```

### Important Lua Math Notes

**Number Type**: Lua has a single number type that handles both integers and floats:

```
integer_val = 42      -- Stored as number
float_val = 3.14      -- Also stored as number
print(type(integer_val))  -- Output: "number"
print(type(float_val))    -- Output: "number"
```

**Division Results**: Division always returns a float:

```
print(6 / 3)     -- Output: 2.0 (not 2)
print(5 / 2)     -- Output: 2.5
```

**Division by Zero**: In Lua, dividing by zero results in inf (infinity):

```
print(5 / 0)     -- Output: inf
print(-5 / 0)    -- Output: -inf
```

### Comparison with Other Languages

**No compound assignment operators**: Lua doesn't have `+=`, `-=`, `*=`, `/=` like other languages:

```
-- Instead of: value += 5
value = value + 5

-- Instead of: count++
count = count + 1
```

**No integer division**: Lua doesn't have a special integer division operator like Python's `//`. Use math.floor for integer division:

```
result = math.floor(7 / 2)  -- Result: 3 (integer division)
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `attempt to perform arithmetic on a string` | Mixing numbers and strings | Convert string to number with `tonumber()` |
| `unexpected symbol near '^'` | Syntax error | Check your expression syntax |
| `1 / 0` gives `inf` | Division by zero | Check for zero denominators |
| Operator precedence issues | Wrong order of operations | Use parentheses to clarify order |

### Math in Real Life

Lua math is used in various applications:
- **Game Development**: Physics calculations, score tracking, positioning
- **Scripting**: Configuration calculations, automation math
- **Embedded Systems**: Resource calculations, timing
- **Web Applications**: Financial calculations, form validation

### Advanced Challenge (For the Brave!)

Try this complex calculation:

```
print("=== Complex Math Example ===")

-- Compound interest calculation
principal = 1000        -- Initial amount
rate = 0.05             -- 5% annual interest rate
times_compounded = 12   -- Compounded monthly
years = 10              -- 10 years

-- Formula: A = P(1 + r/n)^(nt)
amount = principal * (1 + rate/times_compounded)^(times_compounded * years)

print("Initial investment: $" .. principal)
print("After " .. years .. " years at " .. (rate*100) .. "% interest: $" .. string.format("%.2f", amount))

-- Calculate percentage change
original = 100
new_amount = 125
percentage_change = ((new_amount - original) / original) * 100
print("Percentage change from " .. original .. " to " .. new_amount .. ": " .. percentage_change .. "%")

-- Pythagorean theorem (a² + b² = c²)
side_a = 3
side_b = 4
hypotenuse = math.sqrt(side_a^2 + side_b^2)
print("Right triangle with sides " .. side_a .. " and " .. side_b .. " has hypotenuse: " .. hypotenuse)
```

---

 **Excellent work! You're becoming a mathematical wizard in Lua!** 

*Ready for the next challenge? Let's learn how to get input from users!*


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

```
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
