# Level 5: Sum Problem

## Stage 3: Problem to Pseudocode

### Your Problem

Write a program that:

1. Asks user for a number n
2. Calculates the sum of all numbers from 1 to n
3. Prints the result

Example: n=5, sum = 1+2+3+4+5 = 15

---

## ANSWER KEY

### Python Solution

```python
print("Enter a number:")
n = int(input())
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum is: " + str(total))
```

---

**Accumulating values in loops is a key technique!**
