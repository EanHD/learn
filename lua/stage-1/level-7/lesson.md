# Level 7: Functions - Code Organization

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the world of functions! Today you'll learn how to organize your code into reusable pieces called functions. This is where programming becomes truly powerful and professional.

---

### Learning Goals

- Understand what functions are and why they're important
- Learn to define and call functions
- Practice using parameters and return values
- Create reusable code blocks
- Learn about scope and variable access in functions
- Understand different ways to define functions

---

### Your Task

**Copy the following code into a new file called `functions.lua`**

```lua
print("=== Basic Function Definition ===")
-- Define a function that greets someone
function greet_user()
    print("Hello! Welcome to the wonderful world of functions!")
end

-- Call the function
greet_user()
greet_user()  -- Can be called multiple times

print()
print("=== Function with Parameters ===")
-- Define a function that takes parameters
function greet_by_name(name)
    print("Hello, " .. name .. "! Nice to meet you!")
end

-- Call the function with different arguments
greet_by_name("Alex")
greet_by_name("Taylor")
greet_by_name("Jordan")

print()
print("=== Function with Multiple Parameters ===")
-- Define a function with multiple parameters
function introduce_person(name, age)
    print("Hi, I'm " .. name .. " and I'm " .. age .. " years old.")
end

-- Call the function with multiple arguments
introduce_person("Sam", 25)
introduce_person("Morgan", 30)

print()
print("=== Function with Return Value ===")
-- Define a function that returns a value
function add_numbers(a, b)
    local sum = a + b
    return sum  -- Send result back to caller
end

-- Use the returned value
local result1 = add_numbers(5, 3)
local result2 = add_numbers(10, 20)
print("5 + 3 = " .. result1)
print("10 + 20 = " .. result2)

-- Functions can be used directly in expressions
print("The sum of 7 and 8 is: " .. add_numbers(7, 8))

print()
print("=== Function with Multiple Return Values ===")
-- Lua can return multiple values from a function
function get_name_and_age()
    return "Alex", 25
end

-- Receive multiple return values
local name, age = get_name_and_age()
print("Name: " .. name .. ", Age: " .. age)

-- Function that returns multiple calculated values
function rectangle_properties(length, width)
    local area = length * width
    local perimeter = 2 * (length + width)
    return area, perimeter
end

local area, perimeter = rectangle_properties(10, 5)
print("Rectangle area: " .. area .. ", perimeter: " .. perimeter)

print()
print("=== Function Expression (Anonymous Function) ===")
-- Define function as a variable
local multiply = function(a, b)
    return a * b
end

-- Use the function
local product = multiply(4, 5)
print("4 * 5 = " .. product)

print()
print("=== Local Functions ===")
-- Define a local function (only accessible in current scope)
local function calculate_square(x)
    return x * x
end

print("Square of 4: " .. calculate_square(4))

print()
print("=== Practical Function Examples ===")
-- Function to calculate area of rectangle
function calculate_rectangle_area(length, width)
    return length * width
end

-- Function to calculate area of circle
function calculate_circle_area(radius)
    return 3.14159 * radius * radius
end

-- Function to format a full name
function format_full_name(first_name, last_name)
    return first_name .. " " .. last_name
end

-- Function to check if a number is even
function is_even(number)
    return number % 2 == 0
end

-- Use the practical functions
local rect_area = calculate_rectangle_area(10, 5)
local circle_area = calculate_circle_area(7)
local full_name = format_full_name("John", "Doe")
local is_num_even = is_even(12)

print("Rectangle area (10 x 5): " .. rect_area)
print("Circle area (radius 7): " .. string.format("%.2f", circle_area))
print("Full name: " .. full_name)
print("Is 12 even? " .. tostring(is_num_even))

print()
print("=== Function Scope Demo ===")
local global_variable = "I'm global!"

function scope_demo()
    local local_variable = "I'm local!"
    print("Inside function: " .. global_variable)
    print("Inside function: " .. local_variable)
    
    -- Functions can modify global variables (though not recommended)
    global_variable = "Modified from inside function!"
end

-- Call the function
scope_demo()

-- See the change to global variable
print("Outside function: " .. global_variable)

-- Local variable is not accessible here:
-- print("Outside function: " .. local_variable)  -- This would cause an error

print()
print("=== Function Inside Function ===")
function outer_function(name)
    local function inner_function()
        return "Hello from inside!"
    end
    
    return name .. ", " .. inner_function()
end

local message = outer_function("Alex")
print(message)

print()
print("=== Variadic Functions (Functions with Variable Arguments) ===")
-- Function that accepts variable number of arguments
function sum_all(...)
    local args = {...}  -- Collect all arguments into a table
    local total = 0
    for i, value in ipairs(args) do
        total = total + value
    end
    return total
end

print("Sum of 1, 2, 3: " .. sum_all(1, 2, 3))
print("Sum of 1, 2, 3, 4, 5: " .. sum_all(1, 2, 3, 4, 5))

print()
print("=== Higher-Order Function Example ===")
-- Function that takes another function as a parameter
function process_array(arr, callback)
    local result = {}
    for i, value in ipairs(arr) do
        table.insert(result, callback(value))
    end
    return result
end

-- Example array
local numbers = {1, 2, 3, 4, 5}

-- Process array by doubling each element
function double(x)
    return x * 2
end

local doubled = process_array(numbers, double)
print("Original: " .. table.concat(numbers, ", "))
print("Doubled: " .. table.concat(doubled, ", "))

-- Process array using anonymous function
local squared = process_array(numbers, function(x) return x * x end)
print("Squared: " .. table.concat(squared, ", "))

print()
print("=== Closure Example ===")
-- A closure is a function that captures variables from its outer scope
function create_counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end

-- Create two independent counters
local counter1 = create_counter()
local counter2 = create_counter()

print("Counter 1: " .. counter1())  -- 1
print("Counter 1: " .. counter1())  -- 2
print("Counter 2: " .. counter2())  -- 1 (independent counter)
print("Counter 1: " .. counter1())  -- 3
print("Counter 2: " .. counter2())  -- 2
```

---

### How to Execute

1. **Run your program**:
   ```bash
   lua functions.lua
   ```

**Expected output:**
```
=== Basic Function Definition ===
Hello! Welcome to the wonderful world of functions!
Hello! Welcome to the wonderful world of functions!

=== Function with Parameters ===
Hello, Alex! Nice to meet you!
Hello, Taylor! Nice to meet you!
Hello, Jordan! Nice to meet you!

=== Function with Multiple Parameters ===
Hi, I'm Sam and I'm 25 years old.
Hi, I'm Morgan and I'm 30 years old.

=== Function with Return Value ===
5 + 3 = 8
10 + 20 = 20
The sum of 7 and 8 is: 15

=== Function with Multiple Return Values ===
Name: Alex, Age: 25
Rectangle area: 50, perimeter: 30

=== Function Expression (Anonymous Function) ===
4 * 5 = 20

=== Local Functions ===
Square of 4: 16

=== Practical Function Examples ===
Rectangle area (10 x 5): 50
Circle area (radius 7): 153.94
Full name: John Doe
Is 12 even? true

=== Function Scope Demo ===
Inside function: I'm global!
Inside function: I'm local!
Outside function: Modified from inside function!

=== Function Inside Function ===
Alex, Hello from inside!

=== Variadic Functions (Functions with Variable Arguments) ===
Sum of 1, 2, 3: 6
Sum of 1, 2, 3, 4, 5: 15

=== Higher-Order Function Example ===
Original: 1, 2, 3, 4, 5
Doubled: 2, 4, 6, 8, 10
Squared: 1, 4, 9, 16, 25

=== Closure Example ===
Counter 1: 1
Counter 1: 2
Counter 2: 1
Counter 1: 3
Counter 2: 2
```

---

### Success Checklist

- [ ] Created a file named `functions.lua`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw functions being defined and called correctly
- [ ] Understood parameters, return values, and scope

---

### Function Types Summary

- **`function name()`** = Function declaration
- **`local function name()`** = Local function declaration
- **`local name = function()`** = Function expression
- **Parameters** = Variables in function definition
- **Arguments** = Values passed when calling function
- **Return** = Sends value(s) back to caller (Lua can return multiple values!)

---

### Try This (Optional Challenges)

1. Create a calculator with functions for add, subtract, multiply, divide
2. Build a function that validates email addresses
3. Make a function that generates random passwords
4. Create a function that sorts an array of numbers

---

## Quick Reference

| Function Type | Syntax | When to Use |
|---------------|--------|-------------|
| Global | `function name(params)` | When function needs global access |
| Local | `local function name(params)` | Most functions, limits scope |
| Expression | `local name = function(params)` | Assign to variable |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```lua
function greet_user()
    print("Hello! Welcome to the wonderful world of functions!")
end
```
- **`function`** = Keyword to declare a function
- **`greet_user`** = Function name (follows variable naming rules)
- **`()`** = Parameters (empty because no parameters needed)
- **`end`** = Required to close the function definition
- **No return** = Function runs code but doesn't return a value

```lua
function greet_by_name(name)
    print("Hello, " .. name .. "! Nice to meet you!")
end
```
- **`name`** = Parameter (variable that receives the argument value)
- **Parameters** = Variables defined in function declaration
- **Arguments** = Actual values passed when calling the function

```lua
local result1 = add_numbers(5, 3)
```
- **`add_numbers(5, 3)`** = Function call with arguments
- **`5` and `3`** = Arguments passed to the function
- **Return value** = Value that function sends back
- **`result1`** = Variable that stores the returned value

### Function Declaration vs Expression

**Function Declaration (Traditional):**
```lua
function add(a, b)
    return a + b
end
-- Can be called before or after the declaration
```

**Function Expression:**
```lua
local add = function(a, b)
    return a + b
end
-- Must be defined before calling
```

### Multiple Return Values

One unique feature of Lua is that functions can return multiple values:

```lua
function get_coordinates()
    return 10, 20, 30  -- x, y, z coordinates
end

local x, y, z = get_coordinates()
print(x, y, z)  -- Output: 10 20 30
```

### Function Parameters

**Default parameters** (Lua 5.4+):
```lua
function greet(name, greeting) 
    greeting = greeting or "Hello"  -- Use "Hello" if greeting is nil
    print(greeting .. ", " .. name .. "!")
end
```

**Variadic parameters** (...):
```lua
function sum_all(...)
    local args = {...}  -- Create table from all arguments
    local total = 0
    for _, value in ipairs(args) do
        total = total + value
    end
    return total
end
```

### Function Scope

**Global scope:**
```lua
local global_var = "I'm accessible in functions"
```

**Local scope:**
```lua
function my_function()
    local local_var = "I'm only accessible inside this function"
    -- Can access both global_var and local_var
end
-- Can access global_var but NOT local_var
```

**Important:** In Lua, variables are global by default unless declared `local`:

```lua
-- This creates a global variable
function set_global()
    accidentally_global = "This is global!"
end

-- This creates a local variable
function set_local()
    local intentionally_local = "This is local!"
end
```

### Return Values

**Functions without return:**
```lua
function say_hello()
    print("Hello!")
end
-- Returns 'nil' implicitly
```

**Functions with return:**
```lua
function get_hello()
    return "Hello!"
end
-- Returns "Hello!" which can be stored in a variable
```

**Multiple returns:**
```lua
function divide_with_remainder(a, b)
    return math.floor(a / b), a % b  -- quotient, remainder
end

local quotient, remainder = divide_with_remainder(17, 5)  -- 3, 2
```

### Closures

A closure is a function that captures variables from its outer scope:

```lua
function create_multiplier(factor)
    return function(number)
        return number * factor  -- 'factor' captured from outer scope
    end
end

local double = create_multiplier(2)
local triple = create_multiplier(3)

print(double(5))  -- Output: 10
print(triple(5))  -- Output: 15
```

### Higher-Order Functions

Functions that take other functions as parameters or return functions:

```lua
-- Function that takes another function as a parameter
function execute_twice(func)
    func()
    func()
end

function say_hello()
    print("Hello!")
end

execute_twice(say_hello)  -- Will output "Hello!" twice
```

### Pure vs Impure Functions

**Pure function:**
- Same input always gives same output
- No side effects (doesn't modify external state)
```lua
function add(a, b)
    return a + b  -- Pure function
end
```

**Impure function:**
- May have side effects or depend on external state
```lua
local count = 0
function increment()
    count = count + 1  -- Modifies external variable
    return count
end  -- Impure function
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `attempt to call a nil value` | Function not declared or typo in name | Check function name and spelling |
| Function doesn't return expected value | Forgot `return` statement | Add `return` for values you need |
| `nil` when expecting result | Function doesn't return anything | Add return statement |
| `syntax error` in function | Missing function/end keywords | Check function syntax carefully |
| Global variable pollution | Forgetting to declare variables as `local` | Always use `local` for function variables |

### Best Practices for Functions

**Function naming:**
```lua
-- Good - descriptive names
function calculate_area(length, width) ... end
function is_valid_email(email) ... end
function send_notification(message) ... end

-- Avoid - vague names
function do_stuff() ... end
function process() ... end
```

**Use local variables:**
```lua
-- Good - limits scope of variables
function calculate_total(items)
    local total = 0
    for i, price in ipairs(items) do
        local tax = price * 0.08
        total = total + price + tax
    end
    return total
end
```

**Function size:**
- Keep functions focused on a single task
- Aim for functions that are 5-10 lines when possible
- If a function gets too long, consider breaking it into smaller ones

**Single Responsibility Principle:**
```lua
-- Good - one purpose
function calculate_tax(amount, rate)
    return amount * rate
end

-- Better than trying to do everything in one function
function process_order(order)
    local tax = calculate_tax(order.amount, order.tax_rate)
    local total = order.amount + tax
    -- ... other processing
    return total
end
```

### Advanced Challenge (For the Brave!)

Try this comprehensive function example:

```lua
print("=== Banking Application with Functions ===")

-- Function to create a bank account object
function create_account(name, initial_balance)
    initial_balance = initial_balance or 0  -- Default to 0 if not provided
    return {
        name = name,
        balance = initial_balance,
        transactions = {}  -- Track all transactions
    }
end

-- Function to deposit money
function deposit(account, amount)
    if amount <= 0 then
        print("Deposit amount must be positive!")
        return false
    end
    
    account.balance = account.balance + amount
    table.insert(account.transactions, {
        type = "deposit",
        amount = amount,
        date = os.date("%Y-%m-%d"),
        balance_after = account.balance
    })
    
    print("$" .. amount .. " deposited. New balance: $" .. account.balance)
    return true
end

-- Function to withdraw money
function withdraw(account, amount)
    if amount <= 0 then
        print("Withdrawal amount must be positive!")
        return false
    end
    
    if amount > account.balance then
        print("Insufficient funds! Current balance: $" .. account.balance)
        return false
    end
    
    account.balance = account.balance - amount
    table.insert(account.transactions, {
        type = "withdrawal", 
        amount = amount,
        date = os.date("%Y-%m-%d"),
        balance_after = account.balance
    })
    
    print("$" .. amount .. " withdrawn. New balance: $" .. account.balance)
    return true
end

-- Function to check balance
function check_balance(account)
    print(account.name .. "'s balance: $" .. account.balance)
    return account.balance
end

-- Function to get transaction history
function get_transaction_history(account)
    print(account.name .. "'s Transaction History:")
    for i, transaction in ipairs(account.transactions) do
        print(transaction.date .. " - " .. transaction.type .. ": $" .. 
              transaction.amount .. " - Balance: $" .. transaction.balance_after)
    end
end

-- Function to transfer money between accounts
function transfer(from_account, to_account, amount)
    if withdraw(from_account, amount) then
        deposit(to_account, amount)
        print("Transfer of $" .. amount .. " from " .. from_account.name .. 
              " to " .. to_account.name .. " completed!")
        return true
    end
    return false
end

-- Create accounts
local alex_account = create_account("Alex", 1000)
local taylor_account = create_account("Taylor", 500)

-- Perform transactions
deposit(alex_account, 200)
withdraw(alex_account, 150)
transfer(alex_account, taylor_account, 300)
check_balance(alex_account)
check_balance(taylor_account)

print()
get_transaction_history(alex_account)
```

---

 **Excellent work! You now understand how to organize code using functions - a fundamental skill for all programmers!** 

*This completes Stage 1 of Lua learning! You've mastered the fundamentals of Lua programming. Great job!*
