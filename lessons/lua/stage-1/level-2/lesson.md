# Level 2: Variables and Data Types

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the world of variables! Today you'll learn how to store and use data in your Lua programs. Variables are like labeled boxes where you can store information - numbers, text, and more!

---

### Learning Goals

- Understand what variables are and why we need them
- Learn basic data types (string, number, boolean)
- Practice declaring and initializing variables
- Learn how to display variable values
- Understand Lua's dynamic typing system

---

### Your Task

**Copy the following code into a new file called `variables.lua`**

```lua
-- String variables (text)
name = "Alex"
city = "New York"
hobby = "programming"

-- Number variables (integers and decimals)
age = 25
height = 175.5
score = 100

-- Boolean variables (true/false)
is_student = true
is_employed = false
is_happy = true

-- Print all the variables
print("=== Personal Info ===")
print("Name: " .. name)
print("City: " .. city)
print("Hobby: " .. hobby)
print()

print("=== Measurements ===")
print("Age: " .. age .. " years old")
print("Height: " .. height .. " cm")
print("Score: " .. score .. " points")
print()

print("=== Status ===")
print("Student: " .. tostring(is_student))
print("Employed: " .. tostring(is_employed))
print("Happy: " .. tostring(is_happy))

-- Lua's dynamic typing - variables can change types!
print()
print("=== Dynamic Typing Example ===")
dynamic_var = "I'm a string"
print("Dynamic variable: " .. dynamic_var)
dynamic_var = 42  -- Now it's a number!
print("Dynamic variable: " .. dynamic_var)
dynamic_var = true -- Now it's a boolean!
print("Dynamic variable: " .. tostring(dynamic_var))

-- Nil value - represents "no value"
empty_var = nil
print("Empty variable: " .. tostring(empty_var))

-- Tables (Lua's main data structure)
person = {
    name = "Sam",
    age = 30,
    hobbies = {"reading", "coding", "gaming"}
}

print()
print("=== Table Example ===")
print("Person name: " .. person.name)
print("Person age: " .. person.age)
print("First hobby: " .. person.hobbies[1])
```lua

---

### How to Execute

1. **Run your program**:
   ```bash
   lua variables.lua
   ```lua

**Expected output:**
```lua
=== Personal Info ===
Name: Alex
City: New York
Hobby: programming

=== Measurements ===
Age: 25 years old
Height: 175.5 cm
Score: 100 points

=== Status ===
Student: true
Employed: false
Happy: true

=== Dynamic Typing Example ===
Dynamic variable: I'm a string
Dynamic variable: 42
Dynamic variable: true
Empty variable: nil

=== Table Example ===
Person name: Sam
Person age: 30
First hobby: reading
```lua

---

### Success Checklist

- [ ] Created a file named `variables.lua`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw all variable values printed correctly
- [ ] Understood how Lua variables work

---

### What You Learned!

Lua has several important concepts about variables:

- No explicit declaration needed (variables are global by default)
- **Dynamic typing** = Variables can hold any type of value and change type during execution
- **String concatenation** = Using `..` to combine strings and variables
- **Tables** = Lua's primary data structure that can act as arrays, objects, or dictionaries

---

### Try This (Optional Challenges)

1. Change all the variable values to your own information
2. Add new variables for your favorite food and favorite color
3. Try creating a table that combines multiple pieces of information
4. What happens if you add a number and a string together?

---

## Quick Reference

| Data Type | What it holds | Examples | Example Declaration |
|-----------|---------------|----------|-------------------|
| `string` | Text | "Hello", "Lua", "123" | `name = "Alex"` |
| `number` | Integers and decimals | 42, -17, 3.14, 0 | `age = 25` |
| `boolean` | True/false values | true, false | `is_student = true` |
| `nil` | No value assigned | nil | `empty = nil` |
| `table` | Complex data structures | Arrays, objects | `person = {name="Sam"}` |
| `function` | Reusable code blocks | User-defined functions | `my_func = function() ... end` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```lua
-- String variables (text)
name = "Alex"
```lua
- **`--`** = Single-line comment (ignored by computer)
- **`name`** = Variable name (no declaration keyword needed in Lua)
- **`=`** = Assignment operator (stores value on right into variable on left)
- **`"Alex"`** = String value (text in quotes)
- No semicolon needed at the end of statements

```lua
age = 25
```lua
- **`age`** = Variable name (numeric variable)
- **`25`** = Number value (no quotes needed for numbers)
- Lua treats integers and decimals as the same "number" type

```lua
is_student = true
```lua
- **`is_student`** = Boolean variable name (descriptive naming)
- **`true`** = Boolean value (one of only two possible values: true or false)

```lua
print("Name: " .. name)
```lua
- **`..`** = String concatenation operator (joins strings together)
- The variable `name` gets its value inserted into the output string

### Variable Declaration in Lua

In Lua, variables are global by default unless declared local:

```lua
-- Global variables (accessible anywhere)
name = "Global"
age = 25

-- Local variables (only accessible in current scope)
local local_name = "Local"
local local_age = 30
```lua

### Variable Naming Rules

**Valid names**: `name`, `myAge`, `age1`, `student_score`, `studentScore`
**Invalid names**: `123age`, `my-age`, `function`, `age score`

**Rules to remember:**
1. Start with letter or underscore (_)
2. Use only letters, numbers, and underscores after the first character
3. Can't use reserved keywords (`and`, `break`, `do`, `else`, `elseif`, `end`, `false`, `for`, `function`, `if`, `in`, `local`, `nil`, `not`, `or`, `repeat`, `return`, `then`, `true`, `until`, `while`)
4. Case sensitive (`age` ≠ `Age` ≠ `AGE`)

### Data Types Deep Dive

| Type | Description | Examples |
|------|-------------|----------|
| `string` | Text data | `"Hello"`, `'Lua'`, `"123"` |
| `number` | Numeric data | `42`, `-17`, `3.14159`, `0` |
| `boolean` | Logical values | `true`, `false` |
| `nil` | No value / undefined | `local x = nil` |
| `table` | Complex data structures | Arrays, objects, dictionaries |
| `function` | Reusable code blocks | User-defined functions |
| `thread` | Coroutines | Advanced feature |
| `userdata` | C data structures | For C extensions |

### Dynamic Typing Explained

Lua is dynamically typed, meaning:

```lua
dynamic = "I start as a string"
print(type(dynamic))  -- Output: "string"

dynamic = 42  -- Now it's a number
print(type(dynamic))  -- Output: "number"

dynamic = true  -- Now it's a boolean
print(type(dynamic))  -- Output: "boolean"
```lua

### String Concatenation

In Lua, use `..` for string concatenation:

```lua
first_name = "John"
last_name = "Doe"

-- Using concatenation operator
full_name = first_name .. " " .. last_name
print("Full name: " .. full_name)

-- Note: You can't directly concatenate numbers and strings without conversion
-- This will cause an error: print("Age: " .. 25)
-- Instead, convert the number to string: print("Age: " .. tostring(25))
```lua

### Tables - Lua's Powerhouse

Tables are Lua's most important data structure:

```lua
-- Array-like table (numeric indices)
fruits = {"apple", "banana", "orange"}
print(fruits[1])  -- Output: "apple" (1-indexed!)

-- Dictionary-like table (key-value pairs)
person = {name = "Alex", age = 25}
print(person.name)  -- Output: "Alex"

-- Mixed table
mixed = {name = "Bob", years = {2020, 2021, 2022}}
print(mixed.years[2])  -- Output: 2021
```lua

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `attempt to concatenate a number` | Mixing strings and numbers | Use `tostring()` to convert numbers |
| `attempt to call a nil value` | Calling undefined function | Check function names |
| `unexpected symbol near '='` | Assignment in wrong place | Check syntax |
| `variable not found` | Variable name typo | Check spelling (case-sensitive) |

### Bonus Knowledge

- **Everything is a table**: In Lua, even global variables are stored in a global table
- **1-based indexing**: Unlike many languages, Lua tables start at index 1, not 0
- **No block scope**: Variables declared with `local` in a block remain visible after the block
- **Multiple assignment**: `a, b = 1, 2` assigns 1 to `a` and 2 to `b`

### Advanced Challenge (For the Brave!)

Try this modified version:

```lua
-- Let's explore Lua's dynamic nature!
print("=== Lua Advanced Variables ===")

-- Multiple assignment
name, age, city = "Jane", 35, "Seattle"
print("Name: " .. name .. ", Age: " .. age .. ", City: " .. city)

-- Tables with functions
calculator = {
    add = function(a, b) return a + b end,
    multiply = function(a, b) return a * b end
}

result1 = calculator.add(5, 3)
result2 = calculator.multiply(4, 7)
print("5 + 3 = " .. result1)
print("4 * 7 = " .. result2)

-- Dynamic table modification
person = {name = "Alice", age = 28}
person.job = "Engineer"  -- Add new field
person.age = person.age + 1  -- Update field
print(person.name .. " is " .. person.age .. " years old and works as " .. person.job)
```lua

---

 **Excellent work! You now understand variables - the foundation of all programming!** 

*Ready for the next challenge? Let's do some math with our variables!*


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
