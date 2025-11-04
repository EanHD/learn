# Level 7: Pseudocode for Array Operations

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Your Task

Translate this pseudocode into JavaScript:

```
PROGRAM: Array Sum
1. Create an array with numbers [10, 20, 30, 40]
2. Declare a sum variable starting at 0
3. Loop through each number
4. Add each number to the sum
5. Print the sum
```

---

### How to Execute

```bash
node solution.js
```

---

## ANSWER KEY

```javascript
let numbers = [10, 20, 30, 40];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
    sum = sum + numbers[i];
}

console.log(sum);
```

Expected output: `100`

---

**Master arrays and accumulator patterns!**
