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