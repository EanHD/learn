# Level 2: Variables and Data Types

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.R` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Learn how to store and work with different types of data in R.

---

### Learning Goals

- Understand variables and data types
- Learn to declare and initialize variables
- Practice with numbers, strings, and other types
- Display variable values to the screen

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.R`**

```
# Numeric variables
age <- 25
score <- 100
price <- 29.99

# Character variable
name <- "Alex"

# Display
cat("Name:", name, "\n")
cat("Age:", age, "\n")
cat(sprintf("Price: $%.2f\n", price))
```

---

### How to Run

**Method 1 (Vim - Recommended):**
```
<Space>r
```

**Method 2 (Terminal):**
```
Rscript main.R
```

**Expected output:**
```
Name: Alex
Age: 25
Price: $29.99
```


---

### Success Checklist

- [ ] Created a file named `main.R`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

### What Just Happened?

You just created a real R program! Here's what makes it work:

- Variables store data for later use
- Different data types (integers, floats, strings) serve different purposes
- You can perform operations on variables
- Displaying variables shows their current values

---

### Try This (Optional Challenges)

1. Modify the values and see what changes
2. Add your own variations to the code
3. Combine concepts from previous lessons
4. Break something on purpose, then fix it!

---

### Pro Tips

- Use <- for assignment
- Vectors are fundamental to R
- R is great for data analysis

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
# Numeric variables
age <- 25
score <- 100
price <- 29.99

# Character variable
name <- "Alex"

# Display
cat("Name:", name, "\n")
cat("Age:", age, "\n")
cat(sprintf("Price: $%.2f\n", price))
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
