# Level 7: Functions

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.js` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

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

**Copy the following code EXACTLY as shown below into `main.js`**

```javascript
// Functions in MongoDB JavaScript
function greet(name) {
    print("Hello, " + name + "!");
}

function add(a, b) {
    return a + b;
}

function factorial(n) {
    var result = 1;
    for (var i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

greet("Alice");
greet("Bob");

var sum = add(5, 3);
print("5 + 3 = " + sum);

print("5! = " + factorial(5));
```

---

### How to Run

**Method 1 (Vim - Recommended):**
```javascript
<Space>r
```

**Method 2 (Terminal):**
```bash
mongo < script.js
```

**Expected output:**
```
Result: 15
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

- MongoDB stores data as documents
- JavaScript shell for queries
- NoSQL = flexible schema

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

The code you copied demonstrates fundamental MongoDB (NoSQL) concepts:

**Key Components:**
- Syntax rules specific to MongoDB (NoSQL)
- How data is stored and manipulated
- Input/output operations
- Program flow and structure

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Runtime error | Code runs but crashes | Check your logic and data types |
| Unexpected output | Logic error | Review your algorithm step-by-step |

### Bonus Knowledge

- MongoDB (NoSQL) has a rich ecosystem of libraries and tools
- Understanding these basics prepares you for advanced topics
- Practice is key - try writing similar programs from scratch
- Every expert programmer started exactly where you are now!

### Real-World Applications

This concept is used in:
1. Professional software development
2. Web applications and mobile apps
3. Data analysis and scientific computing
4. Automation and scripting
5. Game development

---

**Excellent work! You've mastered a fundamental concept!**

*Ready for the next challenge? Keep going!*
