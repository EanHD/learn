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