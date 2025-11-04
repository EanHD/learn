# Level 3: Mathematical Problems

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

**ADVANCED MATH CHALLENGES!**  You're now tackling complex mathematical algorithms! This level focuses on formulas, sequences, and mathematical calculations that require careful algorithm design.

**The Process:**
1. **Read** the mathematical problem carefully
2. **Identify** the formula or sequence needed
3. **Design** step-by-step calculation algorithm
4. **Handle** mathematical edge cases
5. **Write pseudocode** for your solution
6. **Test your logic** with mathematical examples
7. **Implement** in C code

---

### Learning Goals

- Apply mathematical formulas in programming
- Work with sequences and series
- Handle mathematical edge cases
- Design efficient calculation algorithms
- Validate mathematical inputs and outputs

---

### Mathematical Problem Framework

**STEP 1: Understand the Mathematics**
- What mathematical concept is involved?
- What is the formula or sequence?
- What are the input constraints?
- What are the mathematical limitations?

**STEP 2: Plan the Algorithm**
- How to implement the formula step-by-step?
- What variables track intermediate results?
- How to handle special cases (zero, negative numbers, etc.)?
- What precision is needed for calculations?

**STEP 3: Write Mathematical Pseudocode**
- Break down complex formulas into steps
- Handle mathematical operations carefully
- Consider overflow and precision issues
- Validate inputs mathematically

**STEP 4: Test and Validate**
- Test with known mathematical results
- Verify edge cases mathematically
- Check for calculation accuracy

---

### Your Task

**For each mathematical problem:**
1. **Understand** the mathematical concept
2. **Design** the calculation algorithm
3. **Write pseudocode** for your solution
4. **Test your pseudocode** with mathematical examples
5. **Implement** in C code
6. **Validate** calculations

---

## Problem 1: Fibonacci Sequence Calculator

**Problem Description:**
Create a program that calculates the nth Fibonacci number. The Fibonacci sequence is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

The program should ask for n and display the nth Fibonacci number.

**Example:**
```
Enter n: 8
Fibonacci number 8 is: 21
```

**Your Task:**
1. Write pseudocode for Fibonacci calculation
2. Test with n = 0, 1, 5, 10, 15
3. Implement in C code

---

## Problem 2: Prime Number Checker

**Problem Description:**
Create a program that determines if a given number is prime. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

**Example:**
```
Enter a number: 17
17 is a prime number.
```

```
Enter a number: 15
15 is not a prime number.
```

**Your Task:**
1. Write pseudocode for primality testing
2. Test with numbers: 2, 7, 15, 23, 1, 0
3. Implement in C code

---

## Problem 3: Factorial Calculator

**Problem Description:**
Create a program that calculates the factorial of a given number. Factorial of n (n!) is the product of all positive integers less than or equal to n:
- 0! = 1
- 1! = 1
- n! = n × (n-1) × (n-2) × ... × 1

**Example:**
```
Enter n: 5
5! = 120
```

**Your Task:**
1. Write pseudocode for factorial calculation
2. Test with n = 0, 1, 5, 10
3. Implement in C code

---

## Problem 4: Compound Interest Calculator

**Problem Description:**
Create a program that calculates compound interest. The formula is:
A = P(1 + r/n)^(nt)

Where:
- A = final amount
- P = principal amount
- r = annual interest rate (decimal)
- n = number of times interest is compounded per year
- t = time in years

**Example:**
```
Enter principal amount: 1000
Enter annual interest rate (decimal): 0.05
Enter compounding frequency per year: 12
Enter time in years: 2

Final amount: $1104.54
Interest earned: $104.54
```

**Your Task:**
1. Write pseudocode for compound interest calculation
2. Test with different rates and compounding frequencies
3. Implement in C code

---

## Problem 5: Arithmetic Series Sum

**Problem Description:**
Create a program that calculates the sum of an arithmetic series. An arithmetic series has a constant difference between consecutive terms.

The sum formula is: S = n/2 × (2a + (n-1)d)
Where:
- S = sum of series
- a = first term
- d = common difference
- n = number of terms

**Example:**
```
Enter first term: 3
Enter common difference: 2
Enter number of terms: 5

Series: 3, 5, 7, 9, 11
Sum: 35
```

**Your Task:**
1. Write pseudocode for arithmetic series sum
2. Test with different series
3. Implement in C code

---

## Problem 6: Perfect Number Checker

**Problem Description:**
Create a program that determines if a number is perfect. A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).

Example: 6 is perfect because 1 + 2 + 3 = 6

**Example:**
```
Enter a number: 28
28 is a perfect number.
Divisors: 1, 2, 4, 7, 14 (sum = 28)
```

**Your Task:**
1. Write pseudocode for perfect number checking
2. Test with numbers: 6, 28, 12, 24, 496
3. Implement in C code

---

### Mathematical Pseudocode Guidelines

**Formula Implementation:**
```
Algorithm: Formula Calculator
1. Identify all variables in the formula
2. Determine the order of operations
3. Handle special cases (division by zero, etc.)
4. Calculate step by step
5. Display results with appropriate precision
```

**Sequence Generation:**
```
Algorithm: Sequence Generator
1. Initialize first terms
2. Use loop to generate subsequent terms
3. Apply the sequence rule
4. Store or display terms as needed
5. Handle termination conditions
```

---

### Success Checklist

**For Each Problem:**
- [ ] **Mathematical Understanding**: Correctly identify the formula/sequence
- [ ] **Algorithm Design**: Break down calculation into clear steps
- [ ] **Edge Case Handling**: Handle mathematical boundaries
- [ ] **Pseudocode**: Write clear, mathematical algorithm
- [ ] **Testing**: Verify with known mathematical results
- [ ] **Implementation**: Translate to working C code
- [ ] **Validation**: Test with multiple mathematical scenarios

**Mathematical Skills:**
- [ ] Apply formulas correctly
- [ ] Handle precision and overflow
- [ ] Validate mathematical inputs
- [ ] Provide clear mathematical output

---

### Try This (Optional Challenges)

1. **Performance Optimization**: Optimize Fibonacci calculation for large n
2. **Multiple Formulas**: Add support for different interest types
3. **Series Visualization**: Display series terms along with sum
4. **Mathematical Validation**: Add input validation for mathematical constraints

---

## Mathematical Analysis Framework

### Step 1: Mathematical Understanding
- **Formula**: What is the exact mathematical formula?
- **Variables**: What do each variable represent?
- **Domain**: What are the valid input ranges?
- **Range**: What are the expected output values?

### Step 2: Algorithm Design
- **Steps**: How to break down the calculation?
- **Order**: What order to perform operations?
- **Precision**: How to handle floating-point calculations?
- **Efficiency**: How to optimize for performance?

### Step 3: Implementation Considerations
- **Data Types**: int vs float vs double?
- **Libraries**: Need math.h for advanced functions?
- **Error Handling**: How to handle invalid mathematical inputs?
- **Output Format**: How to display results clearly?

---

<div style="page-break-after: always;"></div>

---

## SOLUTION APPROACH (Read after attempting!)

### Problem 1: Fibonacci Sequence Calculator

**Analysis:**
- Input: n (non-negative integer)
- Processing: Iterative or recursive calculation
- Edge cases: n = 0, n = 1
- Efficiency: Iterative approach for large n

**Sample Pseudocode:**
```
Algorithm: Fibonacci Calculator
1. Display "Enter n: "
2. Get n from user
3. If n == 0:
   a. Display "Fibonacci number 0 is: 0"
4. Else if n == 1:
   a. Display "Fibonacci number 1 is: 1"
5. Else:
   a. Set a = 0, b = 1
   b. For i from 2 to n:
      i. Set temp = a + b
      ii. Set a = b
      iii. Set b = temp
   c. Display "Fibonacci number " + n + " is: " + b
```

---

### Problem 2: Prime Number Checker

**Analysis:**
- Input: positive integer > 1
- Processing: Check divisibility from 2 to sqrt(n)
- Edge cases: 1, 2, even numbers > 2
- Optimization: Check 2 separately, then odd numbers only

**Key Algorithm:**
- If n <= 1: not prime
- If n == 2: prime
- If n is even: not prime
- Check odd divisors from 3 to sqrt(n)

---

### Problem 3: Factorial Calculator

**Analysis:**
- Input: non-negative integer
- Processing: Iterative multiplication
- Edge cases: 0! = 1, 1! = 1
- Limitation: Factorial grows very quickly

**Implementation Notes:**
- Use long long for larger factorials
- Handle overflow gracefully
- Consider recursive vs iterative approach

---

### Problem 4: Compound Interest Calculator

**Analysis:**
- Formula: A = P(1 + r/n)^(nt)
- Inputs: P, r, n, t
- Processing: Power calculation, careful with floating-point
- Edge cases: r = 0, n = 0, t = 0

**Calculation Steps:**
1. Get all inputs
2. Calculate (1 + r/n)
3. Raise to power (n*t)
4. Multiply by P
5. Calculate interest = A - P

---

### Problem 5: Arithmetic Series Sum

**Analysis:**
- Formula: S = n/2 × (2a + (n-1)d)
- Alternative: S = n/2 × (first + last)
- Inputs: a, d, n
- Processing: Use formula or loop summation

**Two Approaches:**
- Direct formula application
- Loop: sum = sum + (a + (i-1)*d) for i=1 to n

---

### Problem 6: Perfect Number Checker

**Analysis:**
- Definition: Sum of proper divisors equals the number
- Processing: Find all divisors from 1 to n/2
- Edge cases: Perfect numbers are rare
- Known perfect numbers: 6, 28, 496, 8128

**Algorithm:**
1. Initialize sum = 0
2. For i from 1 to n/2:
   a. If n % i == 0:
      i. Add i to sum
3. If sum == n: perfect number

---

### Mathematical Best Practices

**Precision Handling:**
- Use double for floating-point calculations
- Be aware of floating-point precision limits
- Consider integer arithmetic when possible

**Performance Considerations:**
- Avoid unnecessary calculations
- Use efficient algorithms for large inputs
- Consider memory usage for large sequences

**Error Prevention:**
- Check for division by zero
- Validate input ranges
- Handle overflow conditions

---

 **Congratulations! You've mastered mathematical algorithms!** 

*Next: Interactive problems with user interfaces and menus! *