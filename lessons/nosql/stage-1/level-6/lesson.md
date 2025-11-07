# Level 6: Loops

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.js` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.js`**

```
// Loop operations in MongoDB
print("Creating documents 1-10:");
for (var i = 1; i <= 10; i++) {
    db.numbers.insertOne({ value: i });
}

// Read and display
var docs = db.numbers.find().sort({ value: 1 });
print("\nStored numbers:");
docs.forEach(function(doc) {
    print(doc.value);
});

// Multiplication table
var num = 7;
print("\n" + num + " times table:");
for (var i = 1; i <= 10; i++) {
    print(num + " × " + i + " = " + (num * i));
}
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
1 2 3 4 5 6 7 8 9 10
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

- MongoDB stores data as documents
- JavaScript shell for queries
- NoSQL = flexible schema

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
// Loop operations in MongoDB
print("Creating documents 1-10:");
for (var i = 1; i <= 10; i++) {
    db.numbers.insertOne({ value: i });
}

// Read and display
var docs = db.numbers.find().sort({ value: 1 });
print("\nStored numbers:");
docs.forEach(function(doc) {
    print(doc.value);
});

// Multiplication table
var num = 7;
print("\n" + num + " times table:");
for (var i = 1; i <= 10; i++) {
    print(num + " × " + i + " = " + (num * i));
}
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
