# Level 6: Loops and Repetition
## Stage 1: Copying Code

### Today's Mission

Time to make your programs repeat actions! Today you'll learn how to write code that runs multiple times without having to copy and paste. Loops are one of the most powerful concepts in programming.

---

### Learning Goals

- Understand for loops for counting and repetition
- Learn while loops for conditional repetition
- Practice repeat-until loops for guaranteed execution
- Use break and continue statements to control loops
- Iterate through tables and collections
- Create patterns and repetitive calculations

---

### Your Task

**Copy the following code into a new file called `loops.lua`**

```lua
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
```

---

### How to Execute

1. **Run your program**:
   ```bash
   lua loops.lua
   ```

**Expected output:**
```
=== Numeric For Loop - Counting ===
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

=== Numeric For Loop - Countdown ===
Countdown: 10
Countdown: 9
Countdown: 8
Countdown: 7
Countdown: 6
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Blast off! 🚀

=== Numeric For Loop - Even Numbers ===
Even number: 2
Even number: 4
Even number: 6
Even number: 8
Even number: 10

=== Numeric For Loop - Sum of Numbers ===
Sum of 1 to 10: 55

=== Generic For Loop - ipairs (indexed table) ===
Fruit at index 1: apple
Fruit at index 2: banana
Fruit at index 3: orange
Fruit at index 4: grape
Fruit at index 5: mango

=== Generic For Loop - pairs (key-value table) ===
name: Alex
city: New York
age: 25

=== While Loop - Counting ===
While count: 1
While count: 2
While count: 3
While count: 4
While count: 5

=== While Loop - Random Number Game ===
Roll #1: 3
Roll #2: 1
Roll #3: 6
Got a 6 after 3 rolls!

=== Repeat-Until Loop - Menu ===
Menu attempt #1: Option 2
Menu attempt #2: Option 4
Menu attempt #3: Option 3
Option 3 selected! Exiting menu.

=== For Loop with Break ===
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Number: 6
Found 7, stopping the loop!

=== For Loop with Continue Alternative ===
2 is even - skipping
Odd number: 1
4 is even - skipping
Odd number: 3
6 is even - skipping
Odd number: 5
8 is even - skipping
Odd number: 7
10 is even - skipping
Odd number: 9

=== Nested Loops - Multiplication Table ===
1	2	3	
2	4	6	
3	6	9	

=== Pattern - Stars ===
* 
* * 
* * * 
* * * * 
* * * * * 

=== Looping with Table Length ===
Color 1: red
Color 2: green
Color 3: blue
Color 4: yellow
Color 5: purple

=== Processing Table Values ===
Processing numbers:
Processing number 1: 10
Processing number 2: 20
Processing number 3: 30
Processing number 4: 40
Processing number 5: 50
Total sum: 150
```
*Note: Random numbers will vary each time you run the program*

---

### Success Checklist

- [ ] Created a file named `loops.lua`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw different types of loops working correctly
- [ ] Understood how break and loop control works

---

### Loop Types Summary

- **Numeric For Loop**: Use when you know how many times to repeat, with a counter variable
- **Generic For Loop**: Use for iterating through tables (ipairs for arrays, pairs for key-value)
- **While Loop**: Use when you want to repeat while a condition is true
- **Repeat-Until Loop**: Use when you want to repeat at least once then check condition

---

### Try This (Optional Challenges)

1. Create a Fibonacci sequence generator using loops
2. Build a password validation program that checks multiple requirements
3. Make a prime number checker
4. Create a simple text-based game using loops for turns

---

## Quick Reference

| Loop Type | Syntax | When to Use |
|-----------|--------|-------------|
| Numeric For | `for i=start,stop,step do` | When you know the number of iterations |
| Generic For | `for k,v in ipairs/pairs(t) do` | When iterating through tables |
| While | `while condition do` | When you repeat while condition is true |
| Repeat-Until | `repeat until condition` | When you must run at least once |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```lua
for i = 1, 5 do
    print("Count: " .. i)
end
```
- **`for`** = Loop keyword
- **`i = 1, 5`** = Loop variable starts at 1, ends at 5 (inclusive)
- **`, 1`** = Step is optional, defaults to 1
- **`do`** = Keyword to begin loop body
- **`end`** = Required keyword to end the loop block
- **Loop execution**: 1, 2, 3, 4, 5 (stops after 5)

```lua
for i = 10, 1, -1 do
    print("Countdown: " .. i)
end
```
- **`10, 1, -1`** = Start at 10, stop at 1, step by -1 (counting backwards)

```lua
while count <= 5 do
    print("While count: " .. count)
    count = count + 1  -- Critical: must update the counter!
end
```
- **`while`** = Loop that continues while condition is true
- **Condition checked first** before each iteration
- **`count = count + 1`** = Must update counter inside the loop or it runs forever!

```lua
repeat
    print("Menu attempt #" .. tries .. ": Option " .. menu_choice)
until menu_choice == 3
```
- **`repeat`** = Code block executes first
- **`until`** = Then condition is checked
- **Result**: Block runs at least once regardless of condition

### For Loop Variations

**Numeric for loop variations:**
```lua
-- Basic: for variable = start, stop, step
for i = 1, 5 do          -- i: 1, 2, 3, 4, 5
    print(i)
end

for i = 2, 10, 2 do      -- i: 2, 4, 6, 8, 10
    print(i)
end

for i = 10, 1, -1 do     -- i: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    print(i)
end
```

### Table Iteration Methods

**ipairs() vs pairs():**
```lua
-- ipairs() - iterates in numerical order with integer indices
local arr = {"a", "b", "c"}
for i, v in ipairs(arr) do
    print(i, v)  -- 1 a, 2 b, 3 c
end

-- pairs() - iterates in random order, all key-value pairs
local t = {name = "Alex", age = 25, [1] = "first"}
for k, v in pairs(t) do
    print(k, v)  -- Could print in any order
end
```

### Loop Control

**break** = Exits the loop completely:
```lua
for i = 1, 10 do
    if i == 5 then
        break  -- Loop stops here
    end
    print(i)  -- Prints: 1, 2, 3, 4
end
```

Lua doesn't have a continue keyword, but you can achieve similar effects with if-then-else:
```lua
for i = 1, 5 do
    if i ~= 3 then  -- Skip when i equals 3
        print(i)  -- Prints: 1, 2, 4, 5 (skips 3)
    else
        print("Skipped " .. i)
    end
end
```

### Nested Loops

```lua
for i = 1, 3 do          -- Outer loop
    for j = 1, 3 do      -- Inner loop
        print("i=" .. i .. ", j=" .. j)
    end
end
```
**Output:**
```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3
```
- **Inner loop** completes all iterations for each outer loop iteration
- **Total iterations**: 3 × 3 = 9

### Table Length with #

```lua
local arr = {"apple", "banana", "orange"}
for i = 1, #arr do        -- #arr returns 3
    print(arr[i])
end
```
**Note**: The `#` operator only works predictably on sequences (arrays with consecutive integer keys starting from 1).

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Infinite loop | Not updating loop variable | Always update the variable that controls the loop |
| Never executes | Wrong condition | Double-check your condition logic |
| Index out of bounds | `i <= #array` vs `i < #array` | Use `<=` for array access with # operator |
| Forgetting loop keywords | Missing do, until, or end | Always use proper loop syntax |
| ipairs vs pairs confusion | Using wrong iterator | Use ipairs for arrays, pairs for general tables |

### When to Use Each Loop Type

**Use numeric for loop when:**
- You know the number of iterations in advance
- You need a counter variable
- You're iterating through arrays with indices

**Use generic for loop (ipairs/pairs) when:**
- You're iterating through tables
- You want to access both keys and values
- You don't need a numeric counter

**Use while loop when:**
- You don't know how many iterations you need
- You're waiting for a condition to be met
- You're processing input until a sentinel value

**Use repeat-until loop when:**
- You need the code to run at least once
- You're creating interactive menus
- You need to validate input

### Advanced Challenge (For the Brave!)

Try this complex loop program:

```lua
print("=== Advanced Loop Examples ===")

-- Prime number finder
print("Prime numbers from 2 to 30:")
for num = 2, 30 do
    local is_prime = true
    
    -- Check if num is divisible by any number from 2 to sqrt(num)
    for divisor = 2, math.sqrt(num) do
        if num % divisor == 0 then
            is_prime = false
            break  -- Found a divisor, not prime
        end
    end
    
    if is_prime then
        print(num .. " is prime")
    end
end

print()
-- Factorial calculator
print("Factorials from 1 to 7:")
for n = 1, 7 do
    local factorial = 1
    for i = 1, n do
        factorial = factorial * i
    end
    print(n .. "! = " .. factorial)
end

print()
-- Fibonacci sequence
print("First 10 numbers in Fibonacci sequence:")
local a, b = 0, 1
print("0: " .. a)
print("1: " .. b)

for i = 2, 9 do
    local next = a + b
    print(i .. ": " .. next)
    a, b = b, next  -- Lua's multiple assignment
end

print()
-- Multiplication table (1-5)
print("Multiplication table (1-5):")
for i = 1, 5 do
    local row = i .. " | "
    for j = 1, 5 do
        row = row .. string.format("%3d", i * j) .. " "
    end
    print(row)
end
```

---

 **Excellent work! You now understand how to repeat actions efficiently with loops!** 

*Ready for the next challenge? Let's learn about functions - the building blocks of reusable code!*