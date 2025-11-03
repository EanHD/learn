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