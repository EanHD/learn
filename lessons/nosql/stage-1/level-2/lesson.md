# Level 2: Variables and Data Types

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.js` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Learn how to store and work with different types of data in MongoDB (NoSQL).

---

### Learning Goals

- Understand variables and data types
- Learn to declare and initialize variables
- Practice with numbers, strings, and other types
- Display variable values to the screen

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.js`**

```
// MongoDB document with variables
db.test.insertOne({
    name: "Alex",
    age: 25,
    score: 100,
    price: 29.99
});

// Display
var doc = db.test.findOne();
print("Name: " + doc.name);
print("Age: " + doc.age);
print("Price: $" + doc.price.toFixed(2));
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
Name: Alex
Age: 25
Price: $29.99
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

- MongoDB stores data as documents
- JavaScript shell for queries
- NoSQL = flexible schema

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
// MongoDB document with variables
db.test.insertOne({
    name: "Alex",
    age: 25,
    score: 100,
    price: 29.99
});

// Display
var doc = db.test.findOne();
print("Name: " + doc.name);
print("Age: " + doc.age);
print("Price: $" + doc.price.toFixed(2));
```

### Explanation

This solution demonstrates the key concepts from this lesson. Copy this code exactly as shown, and make sure you understand each part before moving on.

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
