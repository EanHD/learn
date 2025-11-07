# Level 5: Conditional Statements

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.js` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.js`**

```
// Conditional queries in MongoDB
db.students.insertMany([
    { name: "Alice", score: 95 },
    { name: "Bob", score: 75 },
    { name: "Carol", score: 55 }
]);

// Find students by grade
var excellent = db.students.find({ score: { $gte: 90 } });
print("Excellent students (A):");
excellent.forEach(function(s) {
    print("  " + s.name + ": " + s.score);
});

var passing = db.students.find({ score: { $gte: 70, $lt: 90 } });
print("\nPassing students (B/C):");
passing.forEach(function(s) {
    print("  " + s.name + ": " + s.score);
});
```

---

### How to Run

**Method 1 (Vim - Recommended):**
```
<Space>r
```

**Method 2 (Terminal):**
```
mongo < script.js
```

**Expected output:**
```
[Output depends on conditions - varies based on input]
```


---

### Success Checklist

- [ ] Created a file named `main.js`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

### What Just Happened?

You just created a real MongoDB (NoSQL) program! Here's what makes it work:

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

- MongoDB stores data as documents
- JavaScript shell for queries
- NoSQL = flexible schema

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
// Conditional queries in MongoDB
db.students.insertMany([
    { name: "Alice", score: 95 },
    { name: "Bob", score: 75 },
    { name: "Carol", score: 55 }
]);

// Find students by grade
var excellent = db.students.find({ score: { $gte: 90 } });
print("Excellent students (A):");
excellent.forEach(function(s) {
    print("  " + s.name + ": " + s.score);
});

var passing = db.students.find({ score: { $gte: 70, $lt: 90 } });
print("\nPassing students (B/C):");
passing.forEach(function(s) {
    print("  " + s.name + ": " + s.score);
});
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
