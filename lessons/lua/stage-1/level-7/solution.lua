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