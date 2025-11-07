print("=== Numeric For Loop - Counting ===")
-- Basic numeric for loop: for variable = start, stop, step
for i = 1, 5 do
    print("Count: " .. i)
end

print()
print("=== Numeric For Loop - Countdown ===")
-- Countdown from 10 to 1 (step of -1)
for i = 10, 1, -1 do
    print("Countdown: " .. i)
end
print("Blast off! 🚀")

print()
print("=== Numeric For Loop - Even Numbers ===")
-- Print even numbers from 2 to 10 (step of 2)
for i = 2, 10, 2 do
    print("Even number: " .. i)
end

print()
print("=== Numeric For Loop - Sum of Numbers ===")
-- Calculate sum of numbers 1 to 10
local sum = 0
for i = 1, 10 do
    sum = sum + i  -- Same as: sum = sum + i
end
print("Sum of 1 to 10: " .. sum)

print()
print("=== Generic For Loop - ipairs (indexed table) ===")
-- Loop through an indexed table (array-like)
local fruits = {"apple", "banana", "orange", "grape", "mango"}

for index, fruit in ipairs(fruits) do
    print("Fruit at index " .. index .. ": " .. fruit)
end

print()
print("=== Generic For Loop - pairs (key-value table) ===")
-- Loop through a key-value table
local person = {
    name = "Alex",
    age = 25,
    city = "New York"
}

for key, value in pairs(person) do
    print(key .. ": " .. tostring(value))
end

print()
print("=== While Loop - Counting ===")
-- Basic while loop: while condition
local count = 1
while count <= 5 do
    print("While count: " .. count)
    count = count + 1  -- Important! Without this, infinite loop!
end

print()
print("=== While Loop - Random Number Game ===")
-- Generate random numbers until we get 6
math.randomseed(os.time()) -- Seed for random generator
local roll = 0
local rolls = 0
while roll ~= 6 do
    roll = math.random(1, 6)  -- Random 1-6
    rolls = rolls + 1
    print("Roll #" .. rolls .. ": " .. roll)
end
print("Got a 6 after " .. rolls .. " rolls!")

print()
print("=== Repeat-Until Loop - Menu ===")
-- Repeat-until executes at least once, then checks condition
local menu_choice = 0
local tries = 0
repeat
    tries = tries + 1
    menu_choice = math.random(1, 4)  -- Random 1-4
    print("Menu attempt #" .. tries .. ": Option " .. menu_choice)
    
    if menu_choice == 3 then
        print("Option 3 selected! Exiting menu.")
    end
until menu_choice == 3 or tries >= 10  -- Stop if option 3 or after 10 tries

print()
print("=== For Loop with Break ===")
-- Using break to exit a loop early
for i = 1, 10 do
    if i == 7 then
        print("Found 7, stopping the loop!")
        break  -- Exit the loop completely
    end
    print("Number: " .. i)
end

print()
print("=== For Loop with Continue Alternative ===")
-- Lua doesn't have continue keyword, but we can achieve same effect
for i = 1, 10 do
    if i % 2 == 0 then  -- If even number
        print(i .. " is even - skipping")
    else
        print("Odd number: " .. i)
    end
end

print()
print("=== Nested Loops - Multiplication Table ===")
-- Create a multiplication table (3x3)
for i = 1, 3 do
    local row = ""
    for j = 1, 3 do
        row = row .. (i * j) .. "\t"  -- \t is a tab character
    end
    print(row)
end

print()
print("=== Pattern - Stars ===")
-- Create a right triangle pattern
for i = 1, 5 do
    local pattern = ""
    for j = 1, i do
        pattern = pattern .. "* "
    end
    print(pattern)
end

print()
print("=== Looping with Table Length ===")
-- Loop using the length operator (#)
local colors = {"red", "green", "blue", "yellow", "purple"}

for i = 1, #colors do
    print("Color " .. i .. ": " .. colors[i])
end

print()
print("=== Processing Table Values ===")
-- Process each value in a table
local numbers = {10, 20, 30, 40, 50}
local total = 0

print("Processing numbers:")
for i, num in ipairs(numbers) do
    print("Processing number " .. i .. ": " .. num)
    total = total + num
end

print("Total sum: " .. total)