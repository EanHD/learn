# Level 5: Sum Problem

## Stage 3: Problem to Pseudocode

### Your Problem

Calculate 1 + 2 + 3 + 4 + 5 and display the result.

Example output:

```
Sum of 1 to 5 = 15
```

---

## ANSWER KEY

```javascript
let sum = 0;
for (let i = 1; i <= 5; i++) {
    sum = sum + i;
}
console.log("Sum of 1 to 5 = " + sum);
```

---

**Accumulator pattern!**
