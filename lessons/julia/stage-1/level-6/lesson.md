# Level 6: Loops

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.jl` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Learn to repeat actions efficiently using loops.

---

### Learning Goals

- Understand loop concepts and iteration
- Master for loops and while loops
- Practice with loop control (break, continue)
- Create programs that handle repetitive tasks

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.jl`**

```
# For loop
println("Counting 1 to 10:")
for i in 1:10
    print("$i ")
end
println()

# While loop
println("\nCountdown:")
count = 5
while count > 0
    println(count)
    count -= 1
end
println("Blastoff!")

# Multiplication table
num = 7
println("\n$num times table:")
for i in 1:10
    println("$num × $i = $(num * i)")
end
```

---

### How to Run

**Method 1 (Vim - Recommended):**
```
<Space>r
```

**Method 2 (Terminal):**
```
julia main.jl
```

**Expected output:**
```
1 2 3 4 5 6 7 8 9 10
```


---

### Success Checklist

- [ ] Created a file named `main.jl`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

### What Just Happened?

You just created a real Julia program! Here's what makes it work:

- Loops repeat code efficiently
- For loops work well when you know the count
- While loops continue until a condition is false
- Break and continue control loop execution

---

### Try This (Optional Challenges)

1. Modify the values and see what changes
2. Add your own variations to the code
3. Combine concepts from previous lessons
4. Break something on purpose, then fix it!

---

### Pro Tips

- Julia is fast like C, easy like Python
- Type annotations are optional
- Great for scientific computing

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
# For loop
println("Counting 1 to 10:")
for i in 1:10
    print("$i ")
end
println()

# While loop
println("\nCountdown:")
count = 5
while count > 0
    println(count)
    count -= 1
end
println("Blastoff!")

# Multiplication table
num = 7
println("\n$num times table:")
for i in 1:10
    println("$num × $i = $(num * i)")
end
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
