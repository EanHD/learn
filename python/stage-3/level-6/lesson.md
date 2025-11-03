# Level 6: Multiplication Table Problem

## Stage 3: Problem to Pseudocode

### Your Problem

Write a program that:

1. Asks for a number
2. Prints its multiplication table from 1 to 10

Example: n=3

```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30
```

---

## ANSWER KEY

### Python Solution

```python
print("Enter a number:")
n = int(input())
for i in range(1, 11):
    result = n * i
    print(str(n) + " x " + str(i) + " = " + str(result))
```

---

**Combining loops, multiplication, and string formatting!**
