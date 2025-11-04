# Level 2: Simple Calculator Problem

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 3: Problem to Pseudocode

### Your Problem

Write a program that:

1. Asks user for two numbers
2. Calculates their sum, difference, product, and quotient
3. Displays all four results

Example:

```
Enter first number: 10
Enter second number: 3
Sum: 13
Difference: 7
Product: 30
Quotient: 3.33333...
```

---

### Your Task

1. Write pseudocode for this problem
2. Translate to Python
3. Test with multiple number pairs

---

## ANSWER KEY

### Pseudocode

```text
START
    print "Enter first number:"
    num1 = get input
    print "Enter second number:"
    num2 = get input
    sum = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    print "Sum: " + sum
    print "Difference: " + difference
    print "Product: " + product
    print "Quotient: " + quotient
END
```

### Python Solution

```python
print("Enter first number:")
num1 = int(input())
print("Enter second number:")
num2 = int(input())
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
print("Sum: " + str(sum))
print("Difference: " + str(difference))
print("Product: " + str(product))
print("Quotient: " + str(quotient))
```

### Key Insight

Notice `str()` converts numbers to strings for printing! Otherwise Python can't concatenate numbers with strings.

---

**Handling multiple calculations - excellent practice!**
