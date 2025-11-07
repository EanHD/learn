# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.php` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Make your programs interactive by reading input from users.

---

### Learning Goals

- Learn how to read user input in PHP
- Understand input/output operations
- Practice with different data types from user
- Create interactive programs that respond to users

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.php`**

```
<?php
echo "Enter your name: ";
$name = trim(fgets(STDIN));

echo "Enter your age: ";
$age = intval(trim(fgets(STDIN)));

echo "Hello, $name!\n";
echo "You are $age years old.\n";
?>
```

---

### How to Run

**Method 1 (Vim - Recommended):**
```
<Space>r
```

**Method 2 (Terminal):**
```
php main.php
```

**Expected output:**
```
[Interactive - output varies based on user input]
```


---

### Success Checklist

- [ ] Created a file named `main.php`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

### What Just Happened?

You just created a real PHP program! Here's what makes it work:

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

- Variables start with $
- Use <?php to start PHP code
- Use . for string concatenation

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
<?php
echo "Enter your name: ";
$name = trim(fgets(STDIN));

echo "Enter your age: ";
$age = intval(trim(fgets(STDIN)));

echo "Hello, $name!\n";
echo "You are $age years old.\n";
?>
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
