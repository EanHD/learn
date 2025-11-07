# Level 7: Functions

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.php` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Organize your code into reusable functions/methods.

---

### Learning Goals

- Understand function concepts and modularity
- Learn to define and call functions
- Practice with parameters and return values
- Create organized, maintainable code

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.php`**

```
<?php
// Function to greet someone
function greet($name) {
    echo "Hello, $name!\n";
}

// Function that returns a value
function add($a, $b) {
    return $a + $b;
}

// Function to calculate factorial
function factorial($n) {
    $result = 1;
    for ($i = 1; $i <= $n; $i++) {
        $result *= $i;
    }
    return $result;
}

greet("Alice");
greet("Bob");

$sum = add(5, 3);
echo "5 + 3 = $sum\n";

echo "5! = " . factorial(5) . "\n";
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
Result: 15
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

- Functions organize code into reusable blocks
- Parameters pass data into functions
- Return values send data back from functions
- Functions make code more maintainable and testable

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
// Function to greet someone
function greet($name) {
    echo "Hello, $name!\n";
}

// Function that returns a value
function add($a, $b) {
    return $a + $b;
}

// Function to calculate factorial
function factorial($n) {
    $result = 1;
    for ($i = 1; $i <= $n; $i++) {
        $result *= $i;
    }
    return $result;
}

greet("Alice");
greet("Bob");

$sum = add(5, 3);
echo "5 + 3 = $sum\n";

echo "5! = " . factorial(5) . "\n";
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
