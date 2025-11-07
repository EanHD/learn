# Level 6: Loops

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.php` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.php`**

```
<?php
// For loop
echo "Counting 1 to 10:\n";
for ($i = 1; $i <= 10; $i++) {
    echo "$i ";
}
echo "\n";

// While loop
echo "\nCountdown:\n";
$count = 5;
while ($count > 0) {
    echo "$count\n";
    $count--;
}
echo "Blastoff!\n";

// Multiplication table
$num = 7;
echo "\n$num times table:\n";
for ($i = 1; $i <= 10; $i++) {
    echo "$num × $i = " . ($num * $i) . "\n";
}
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
1 2 3 4 5 6 7 8 9 10
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
// For loop
echo "Counting 1 to 10:\n";
for ($i = 1; $i <= 10; $i++) {
    echo "$i ";
}
echo "\n";

// While loop
echo "\nCountdown:\n";
$count = 5;
while ($count > 0) {
    echo "$count\n";
    $count--;
}
echo "Blastoff!\n";

// Multiplication table
$num = 7;
echo "\n$num times table:\n";
for ($i = 1; $i <= 10; $i++) {
    echo "$num × $i = " . ($num * $i) . "\n";
}
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
