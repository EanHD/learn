# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.jl` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Make your programs interactive by reading input from users.

---

### Learning Goals

- Learn how to read user input in Julia
- Understand input/output operations
- Practice with different data types from user
- Create interactive programs that respond to users

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.jl`**

```
print("Enter your name: ")
name = readline()

print("Enter your age: ")
age = parse(Int, readline())

println("Hello, $name!")
println("You are $age years old.")
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
[Interactive - output varies based on user input]
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

- Programs can read input from users
- Input makes programs interactive and dynamic
- Different methods exist for different data types
- Always validate user input in real programs

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
print("Enter your name: ")
name = readline()

print("Enter your age: ")
age = parse(Int, readline())

println("Hello, $name!")
println("You are $age years old.")
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
