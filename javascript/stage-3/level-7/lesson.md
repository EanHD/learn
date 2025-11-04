# Level 7: Even/Odd Counter Problem

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 3: Problem to Pseudocode

### Your Problem

Count even and odd numbers from 1 to 20.

Example output:

```
Even numbers: 10
Odd numbers: 10
```

---

## ANSWER KEY

```javascript
let evenCount = 0;
let oddCount = 0;

for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) {
        evenCount = evenCount + 1;
    } else {
        oddCount = oddCount + 1;
    }
}

console.log("Even numbers: " + evenCount);
console.log("Odd numbers: " + oddCount);
```

---

**Modulo operator and conditional counting!**
