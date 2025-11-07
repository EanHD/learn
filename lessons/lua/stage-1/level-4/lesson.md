# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Now let's make our programs interactive! Today you'll learn how to get input from users and respond to their information. This is where programs become truly useful!

---

### Learning Goals

- Learn how to get input from users
- Understand Lua's io library for input/output
- Practice creating interactive programs
- Learn to combine input with variables and math
- Handle different types of user input

---

### Your Task

**Copy the following code into a new file called `input.lua`**

```lua
print("=== Interactive Greeting Program ===")
-- Get input from user
io.write("What's your name? ")  -- io.write() doesn't add a newline
local name = io.read()  -- Read a line from standard input
print("Hello, " .. name .. "! Nice to meet you!")

print()
print("=== Simple Calculator ===")
-- Get two numbers from user
io.write("Enter first number: ")
local num1 = tonumber(io.read())  -- Convert input string to number

io.write("Enter second number: ")
local num2 = tonumber(io.read())  -- Convert input string to number

-- Perform calculations
local sum = num1 + num2
local difference = num1 - num2
local product = num1 * num2
local quotient = num1 / num2

-- Display results
print(num1 .. " + " .. num2 .. " = " .. sum)
print(num1 .. " - " .. num2 .. " = " .. difference)
print(num1 .. " * " .. num2 .. " = " .. product)
print(num1 .. " / " .. num2 .. " = " .. quotient)

print()
print("=== Age Calculator ===")
-- Ask for birth year and calculate age
io.write("What year were you born? ")
local birth_year = tonumber(io.read())
local current_year = tonumber(os.date("%Y"))  -- Get current year
local age = current_year - birth_year

print("If you were born in " .. birth_year .. ", you are about " .. age .. " years old.")

print()
print("=== Simple Quiz ===")
-- Create a simple quiz
io.write("What is the capital of France? ")
local answer = io.read()
if string.lower(answer) == "paris" then
    print("Correct! Well done!")
else
    print("Not quite! The answer is Paris.")
end

print()
print("=== Number Guessing Game ===")
-- A simple number guessing game
math.randomseed(os.time())  -- Seed the random generator
local secret_number = math.random(1, 10)
io.write("I'm thinking of a number between 1 and 10. Can you guess it? ")
local user_guess = tonumber(io.read())

if user_guess == secret_number then
    print("You got it! The number was " .. secret_number)
else
    print("Sorry, the number was " .. secret_number .. ". Better luck next time!")
end

print()
print("=== Multiple Inputs ===")
-- Collect multiple pieces of information
io.write("What's your favorite color? ")
local color = io.read()

io.write("How many pets do you have? ")
local pet_count = tonumber(io.read())

io.write("What's your favorite food? ")
local food = io.read()

print()
print("=== Your Profile ===")
print("Favorite color: " .. color)
print("Number of pets: " .. pet_count)
print("Favorite food: " .. food)
print("Thanks for sharing, " .. name .. "!")

print()
print("=== Input Validation Example ===")
-- Demonstrate input validation
io.write("Enter a positive number: ")
local user_input = io.read()
local number = tonumber(user_input)

if number ~= nil and number > 0 then
    print("Valid positive number: " .. number)
    print("Its square is: " .. number^2)
else
    print("Invalid input! That wasn't a positive number.")
end
```lua

---

### How to Execute

1. **Run your program**:
   ```bash
   lua input.lua
   ```lua

**Expected interaction:**
```lua
=== Interactive Greeting Program ===
What's your name? [User types their name and presses Enter]
Hello, [User's name]! Nice to meet you!

=== Simple Calculator ===
Enter first number: [User enters a number]
Enter second number: [User enters another number]
[Calculations are performed and results shown]

=== Age Calculator ===
What year were you born? [User enters a year]
[Age calculation is performed and shown]

[Additional prompts will ask for input and respond accordingly...]
```lua

---

### Success Checklist

- [ ] Created file named `input.lua`
- [ ] Program executed without errors
- [ ] Interacted with the program by providing input
- [ ] Saw programs respond to input appropriately
- [ ] Understood how to get input from users

---

### What You Learned!

- **`io.write()`** = Outputs text without adding a newline
- **`io.read()`** = Reads a line from standard input
- **`tonumber()`** = Converts string to number
- **`string.lower()`** = Converts string to lowercase
- **Input validation** = Checking if inputs are valid before using them

---

### Try This (Optional Challenges)

1. Create a BMI calculator that asks for height and weight
2. Make a basic chatbot that responds to different inputs
3. Create a simple math quiz with multiple questions
4. Build a program that converts temperatures based on user input

---

## Quick Reference

| Method | Purpose | Example | Notes |
|--------|---------|---------|-------|
| `io.write()` | Output without newline | `io.write("Name? ")` | Use for prompts |
| `io.read()` | Get text input | `local name = io.read()` | Returns string |
| `tonumber()` | Convert to number | `local num = tonumber("42")` | Returns number or nil |
| `string.lower()` | To lowercase | `string.lower("HELLO")` | Returns "hello" |
| `string.upper()` | To uppercase | `string.upper("hello")` | Returns "HELLO" |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```lua
local name = io.read()
```lua
- **`io.read()`** = Function from the io library that reads from standard input
- **Reads until** the user presses Enter
- **Returns a string** containing whatever the user typed

```lua
local num1 = tonumber(io.read())
```lua
- **`tonumber()`** = Converts string to number
- **Necessary** because `io.read()` returns a string, but we want to do math
- **Returns nil** if conversion fails (input wasn't a valid number)

```lua
io.write("What's your name? ")
```lua
- **`io.write()`** = Outputs text to the console
- **Doesn't add** a newline character (unlike print)
- **Useful for** prompts where user types on same line

### Alternative Input Methods

**Reading multiple values:**
```lua
-- Read multiple values on one line (space separated)
local first, second = io.read("*number", "*number")
print("First: " .. first .. ", Second: " .. second)
```lua

**Reading with different modes:**
```lua
-- Read one character
local char = io.read(1)

-- Read entire file
local content = io.read("*all")

-- Read current line
local line = io.read("*line")
```lua

### Important Input Considerations

**Always validate user input:**
```lua
local user_input = io.read()
local number = tonumber(user_input)

if number == nil then
    print("That's not a valid number!")
else
    print("You entered: " .. number)
end
```lua

**Case sensitivity:**
```lua
-- Without string.lower(), "Paris" and "paris" would be different
if answer == "Paris" then  -- "paris" would not match
    -- This would fail if user types "paris"
end

-- With string.lower(), both "Paris" and "paris" match
if string.lower(answer) == "paris" then  -- Works for any case
    -- This works regardless of case
end
```lua

### String Manipulation

**Common string functions:**
```lua
-- Length of string
local text = "Hello"
print(string.len(text))  -- Output: 5

-- Extract substring
print(string.sub(text, 1, 3))  -- Output: "Hel"

-- Find substring
print(string.find(text, "ll"))  -- Output: 3 (position where "ll" starts)

-- Replace text (pattern matching)
local new_text = string.gsub(text, "H", "h")  -- "hello"
```lua

### Error Prevention with Input

**Safe number conversion:**
```lua
local get_number = function(prompt)
    io.write(prompt)
    local input = io.read()
    local num = tonumber(input)
    
    if num == nil then
        print("Invalid number! Please try again.")
        return get_number(prompt)  -- Recursive call to try again
    end
    
    return num
end

-- Usage
local age = get_number("Enter your age: ")
```lua

### Date and Time in Lua

```lua
-- Get current date components
local year = tonumber(os.date("%Y"))   -- Full year (e.g., 2025)
local month = tonumber(os.date("%m"))  -- Month (01-12)
local day = tonumber(os.date("%d"))    -- Day (01-31)

-- Get full date string
local full_date = os.date("%Y-%m-%d")  -- e.g., "2025-10-30"
```lua

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `attempt to perform arithmetic on a string` | Forgetting to use `tonumber()` | Always convert with `tonumber()` before math |
| `nil` results | Invalid number conversion | Check if result of `tonumber()` is nil |
| Input not captured | Using `print` instead of `io.write` for prompts | Use `io.write` for prompts, `print` for output |
| Case sensitivity issues | Not handling different cases | Use `string.lower()` or `string.upper()` |

### Best Practices for Input

**Always validate user input:**
```lua
local age = tonumber(io.read())
if age == nil or age < 0 or age > 150 then
    print("Please enter a valid age between 0 and 150")
else
    print("You are " .. age .. " years old")
end
```lua

**Handle potential nil returns from tonumber:**
```lua
local input = io.read()
local number = tonumber(input)
if number ~= nil then
    -- Process the number
    print("Processing number: " .. number)
else
    print("Invalid input - not a number")
end
```lua

### Security Considerations

When accepting user input:
- **Validation**: Always validate and sanitize input
- **Type conversion**: Be careful with `tonumber()` and other conversion functions
- **Length limits**: Set reasonable limits on input length

### Advanced Challenge (For the Brave!)

Try this full interactive program:

```lua
print("=== Personal Finance Calculator ===")

-- Get user's income
io.write("Enter your monthly income: $")
local monthly_income = tonumber(io.read())

-- Get expenses
io.write("Enter monthly rent: $")
local rent = tonumber(io.read())

io.write("Enter monthly grocery cost: $")
local groceries = tonumber(io.read())

io.write("Enter monthly utilities: $")
local utilities = tonumber(io.read())

io.write("Enter monthly transportation: $")
local transportation = tonumber(io.read())

-- Calculate totals
local total_expenses = rent + groceries + utilities + transportation
local remaining = monthly_income - total_expenses
local savings_percentage = (remaining / monthly_income) * 100

-- Display results
print()
print("=== FINANCIAL SUMMARY ===")
print("Monthly Income: $" .. string.format("%.2f", monthly_income))
print("Total Expenses: $" .. string.format("%.2f", total_expenses))
print("Remaining: $" .. string.format("%.2f", remaining))
print("Savings Rate: " .. string.format("%.1f", savings_percentage) .. "%")

if remaining > 0 then
    print("Great! You're saving money each month.")
else
    print("You're spending more than you earn. Consider reducing expenses.")
end
```lua

---

 **Excellent work! You now know how to make interactive programs that respond to user input!** 

*Ready for the next challenge? Let's make programs that make decisions!*


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
