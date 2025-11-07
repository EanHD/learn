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