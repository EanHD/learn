-- Algorithm 1: Simple Variable Swapping
local first_number = 10
local second_number = 20

print("Before swap: first=" .. first_number .. ", second=" .. second_number)

local temp = first_number
first_number = second_number
second_number = temp

print("After swap: first=" .. first_number .. ", second=" .. second_number)

print() -- Add some spacing

-- Algorithm 2: Running Total Calculator
local total = 0
local count = 0

local number = 5
total = total + number
count = count + 1

number = 10
total = total + number
count = count + 1

number = 15
total = total + number
count = count + 1

local average = total / count

print("Total: " .. total)
print("Count: " .. count)
print("Average: " .. average)

print() -- Add some spacing

-- Algorithm 3: Temperature Tracker
local min_temp = 100
local max_temp = -100

local current_temp = 72
if current_temp < min_temp then
    min_temp = current_temp
end
if current_temp > max_temp then
    max_temp = current_temp
end
print("Current: " .. current_temp .. ", Min: " .. min_temp .. ", Max: " .. max_temp)

current_temp = 65
if current_temp < min_temp then
    min_temp = current_temp
end
if current_temp > max_temp then
    max_temp = current_temp
end
print("Current: " .. current_temp .. ", Min: " .. min_temp .. ", Max: " .. max_temp)

current_temp = 80
if current_temp < min_temp then
    min_temp = current_temp
end
if current_temp > max_temp then
    max_temp = current_temp
end
print("Current: " .. current_temp .. ", Min: " .. min_temp .. ", Max: " .. max_temp)

print() -- Add some spacing

-- Algorithm 4: Account Balance Tracker
local account_balance = 1000

local transaction_amount = -50
account_balance = account_balance + transaction_amount
print("Balance after withdrawal: $" .. account_balance)

transaction_amount = 200
account_balance = account_balance + transaction_amount
print("Balance after deposit: $" .. account_balance)

transaction_amount = -75.50
account_balance = account_balance + transaction_amount
print("Balance after withdrawal: $" .. account_balance)

transaction_amount = 150.25
account_balance = account_balance + transaction_amount
print("Balance after deposit: $" .. account_balance)

print() -- Add some spacing

-- Algorithm 5: Student Grade Calculator
local total_points = 0
local possible_points = 0

local assignment_points = 85
local assignment_possible = 100
total_points = total_points + assignment_points
possible_points = possible_points + assignment_possible

assignment_points = 92
assignment_possible = 100
total_points = total_points + assignment_points
possible_points = possible_points + assignment_possible

assignment_points = 78
assignment_possible = 100
total_points = total_points + assignment_points
possible_points = possible_points + assignment_possible

local percentage = (total_points / possible_points) * 100
local letter_grade = "F"

if percentage >= 90 then
    letter_grade = "A"
elseif percentage >= 80 then
    letter_grade = "B"
elseif percentage >= 70 then
    letter_grade = "C"
elseif percentage >= 60 then
    letter_grade = "D"
end

print("Total Points: " .. total_points)
print("Possible Points: " .. possible_points)
print("Percentage: " .. percentage)
print("Letter Grade: " .. letter_grade)

print() -- Add some spacing

-- Algorithm 6: Counter Patterns
local counter = 1
while counter <= 5 do
    print("Count: " .. counter)
    counter = counter + 1
end

local even_counter = 2
while even_counter <= 10 do
    print("Even: " .. even_counter)
    even_counter = even_counter + 2
end

local odd_counter = 1
while odd_counter <= 10 do
    print("Odd: " .. odd_counter)
    odd_counter = odd_counter + 2
end

print() -- Add some spacing

-- Algorithm 7: Accumulator Pattern
local sum = 0
local count = 0
local product = 1

local current_value = 3
sum = sum + current_value
count = count + 1
product = product * current_value

current_value = 4
sum = sum + current_value
count = count + 1
product = product * current_value

current_value = 5
sum = sum + current_value
count = count + 1
product = product * current_value

local average = sum / count

print("Sum: " .. sum)
print("Count: " .. count)
print("Product: " .. product)
print("Average: " .. average)