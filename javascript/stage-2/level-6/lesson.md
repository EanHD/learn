# Level 6: Pseudocode for String Operations

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Your Task

Translate this pseudocode into JavaScript:

```
PROGRAM: String Reverser
1. Declare a string variable with text "Hello"
2. Declare an empty string called reversed
3. Loop from the end of the string to the beginning
4. Add each character to reversed
5. Print the result
```

---

### How to Execute

```bash
node solution.js
```

---

## ANSWER KEY

```javascript
let text = "Hello";
let reversed = "";

for (let i = text.length - 1; i >= 0; i--) {
    reversed = reversed + text[i];
}

console.log(reversed);
```

Expected output: `olleH`

---

**Learn how strings work and loop backwards through them!**
