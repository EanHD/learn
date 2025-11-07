# Level 5: Conditional Statements

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.jl` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Add decision-making to your programs with if/else statements.

---

### Learning Goals

- Understand conditional logic and boolean expressions
- Master if, else if, and else statements
- Practice with comparison and logical operators
- Create programs that make intelligent decisions

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.jl`**

```
print("Enter your score (0-100): ")
score = parse(Int, readline())

if score >= 90
    println("Grade: A - Excellent!")
elseif score >= 80
    println("Grade: B - Good job!")
elseif score >= 70
    println("Grade: C - Passing")
elseif score >= 60
    println("Grade: D - Needs improvement")
else
    println("Grade: F - Study harder!")
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
[Output depends on conditions - varies based on input]
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

- Conditional statements let programs make decisions
- Comparison operators (==, !=, <, >, <=, >=) test relationships
- Logical operators (AND, OR, NOT) combine conditions
- Programs can respond differently based on conditions

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
print("Enter your score (0-100): ")
score = parse(Int, readline())

if score >= 90
    println("Grade: A - Excellent!")
elseif score >= 80
    println("Grade: B - Good job!")
elseif score >= 70
    println("Grade: C - Passing")
elseif score >= 60
    println("Grade: D - Needs improvement")
else
    println("Grade: F - Study harder!")
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
