-- Algorithm 1: Complex Arithmetic Expression
local a = 10
local b = 5
local c = 2

local result = (a + b) * c - a / c
print("Result: " .. result)

local result2 = a + b * c - a / c
print("Result without parentheses: " .. result2)

local result3 = ((a + b) * c - a) / c
print("Result with different grouping: " .. result3)

print() -- Add some spacing

-- Algorithm 2: Quadratic Formula Calculator
local a2 = 1  -- Renamed to avoid conflict
local b2 = -5
local c2 = 6

local discriminant = b2 * b2 - 4 * a2 * c2
local sqrt_discriminant = math.sqrt(discriminant)
local root1 = (-b2 + sqrt_discriminant) / (2 * a2)
local root2 = (-b2 - sqrt_discriminant) / (2 * a2)

print("Root 1: " .. root1)
print("Root 2: " .. root2)

print() -- Add some spacing

-- Algorithm 3: Compound Interest Calculator
local principal = 1000
local rate = 0.05
local time = 10
local compounds_per_year = 12

local amount = principal * math.pow(1 + rate / compounds_per_year, compounds_per_year * time)
local interest = amount - principal

print("Principal: $" .. principal)
print("Final Amount: $" .. string.format("%.2f", amount))
print("Interest Earned: $" .. string.format("%.2f", interest))

print() -- Add some spacing

-- Algorithm 4: Geometric Calculations
local radius = 5
local side = 4
local base = 6
local height = 8

local circle_area = math.pi * radius * radius
local circle_circumference = 2 * math.pi * radius
local square_area = side * side
local square_perimeter = 4 * side
local triangle_area = 0.5 * base * height

print("Circle - Area: " .. string.format("%.2f", circle_area) .. ", Circumference: " .. string.format("%.2f", circle_circumference))
print("Square - Area: " .. square_area .. ", Perimeter: " .. square_perimeter)
print("Triangle - Area: " .. triangle_area)

print() -- Add some spacing

-- Algorithm 5: Physics Formula Calculator
local mass = 5.5
local velocity = 10
local acceleration = 9.8
local time2 = 3  -- Renamed to avoid conflict

local kinetic_energy = 0.5 * mass * velocity * velocity
local force = mass * acceleration
local distance = velocity * time2 + 0.5 * acceleration * time2 * time2
local momentum = mass * velocity

print("Kinetic Energy: " .. kinetic_energy)
print("Force: " .. force)
print("Distance: " .. distance)
print("Momentum: " .. momentum)

print() -- Add some spacing

-- Algorithm 6: Temperature Conversion with Multiple Formulas
local celsius = 25
local fahrenheit = celsius * 9 / 5 + 32
local kelvin = celsius + 273.15
local celsius_from_f = (fahrenheit - 32) * 5 / 9
local celsius_from_k = kelvin - 273.15

print("Celsius: " .. celsius)
print("Fahrenheit: " .. fahrenheit)
print("Kelvin: " .. kelvin)
print("F to C: " .. celsius_from_f)
print("K to C: " .. celsius_from_k)

print() -- Add some spacing

-- Algorithm 7: Statistical Calculations
local num1 = 10
local num2 = 20
local num3 = 30

local sum = num1 + num2 + num3
local average = sum / 3
local range = num3 - num1 -- assuming num3 is largest, num1 is smallest
local sum_of_squares = num1 * num1 + num2 * num2 + num3 * num3
local mean_of_squares = sum_of_squares / 3
local variance = mean_of_squares - average * average
local std_deviation = math.sqrt(variance)

print("Sum: " .. sum)
print("Average: " .. average)
print("Range: " .. range)
print("Variance: " .. variance)
print("Standard Deviation: " .. string.format("%.2f", std_deviation))