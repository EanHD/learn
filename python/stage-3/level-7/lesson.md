# Level 7: Even/Odd Counter Problem

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 3: Problem to Pseudocode

### Your Problem

Write a program that:

1. Asks user for a number n
2. Counts how many even and odd numbers from 1 to n
3. Prints both counts

Example: n=10

- Even: 2,4,6,8,10 = 5 numbers
- Odd: 1,3,5,7,9 = 5 numbers

---

## ANSWER KEY

### Python Solution

```python
print("Enter a number:")
n = int(input())
even_count = 0
odd_count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("Even numbers: " + str(even_count))
print("Odd numbers: " + str(odd_count))
```

---

**Combining loops, conditionals, and counting!**
