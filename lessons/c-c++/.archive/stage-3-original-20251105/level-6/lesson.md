# Level 6: Repetitive Problems

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

**LOOP MASTER!**  You're now creating algorithms that process data repeatedly, generate patterns, and perform iterative calculations. This level focuses on mastering loop structures and repetitive logic patterns.

**The Process:**
1. **Identify** the repetitive pattern or process
2. **Determine** the loop structure needed
3. **Plan** loop initialization and termination
4. **Design** the iteration logic
5. **Handle** loop control and edge cases
6. **Write pseudocode** for repetitive algorithms
7. **Test iterations** with different inputs
8. **Implement** in C code

---

### Learning Goals

- [ ] Master different loop structures (for, while, do-while)
- [ ] Design pattern generation algorithms
- [ ] Create data processing loops
- [ ] Implement iterative calculations
- [ ] Handle loop control and termination
- [ ] Optimize repetitive processes

---

### Repetitive Algorithm Framework

**STEP 1: Pattern Analysis**
- [ ] What needs to be repeated?
- [ ] How many iterations are needed?
- [ ] What changes each iteration?
- [ ] What is the termination condition?

**STEP 2: Loop Structure Selection**
- [ ] For loop: Known number of iterations
- [ ] While loop: Condition-based continuation
- [ ] Do-while loop: Execute at least once
- [ ] Nested loops: Multi-dimensional patterns

**STEP 3: Iteration Design**
- [ ] Initialize loop variables
- [ ] Define iteration logic
- [ ] Update control variables
- [ ] Handle boundary conditions

**STEP 4: Loop Optimization**
- [ ] Minimize unnecessary operations
- [ ] Use efficient increment patterns
- [ ] Consider loop unrolling for performance
- [ ] Handle large iteration counts

---

### Your Task

**For each repetitive problem:**
1. **Analyze** the pattern or repetitive process
2. **Choose** appropriate loop structure
3. **Design** the iteration algorithm
4. **Write pseudocode** for the repetitive logic
5. **Test iterations** mentally
6. **Implement** in C code
7. **Validate** with different input sizes

---

## Problem 1: Star Pattern Generator

**Problem Description:**
Create a program that generates different star patterns based on user input:
1. Right triangle
2. Inverted right triangle
3. Pyramid
4. Diamond

Ask for pattern type and size, then display the pattern.

**Example:**
```
Enter pattern type (1-4): 1
Enter size: 5

*
**
***
****
*****
```

**Your Task:**
1. Write pseudocode for pattern generation algorithms
2. Test different patterns and sizes
3. Implement in C code

---

## Problem 2: Number Pattern Generator

**Problem Description:**
Create a program that generates number patterns:
1. Counting pattern (1 2 3 4 5...)
2. Multiplication table
3. Fibonacci sequence display
4. Prime number list

Display the pattern up to a user-specified limit.

**Example:**
```
Enter pattern type (1-4): 2
Enter size: 5

1 x 1 = 1
1 x 2 = 2
...
5 x 5 = 25
```

**Your Task:**
1. Write pseudocode for number pattern algorithms
2. Test different patterns and limits
3. Implement in C code

---

## Problem 3: Data Statistics Calculator

**Problem Description:**
Create a program that calculates statistics for a series of numbers:
- [ ] Read numbers until user enters -1
- [ ] Calculate: count, sum, average, minimum, maximum
- [ ] Display running statistics after each input
- [ ] Show final summary

**Example:**
```
Enter numbers (enter -1 to stop):
Number 1: 10
Count: 1, Sum: 10, Avg: 10.0, Min: 10, Max: 10

Number 2: 20
Count: 2, Sum: 30, Avg: 15.0, Min: 10, Max: 20

Number 3: -1

Final Statistics:
Count: 2
Sum: 30
Average: 15.0
Minimum: 10
Maximum: 20
```

**Your Task:**
1. Write pseudocode for statistics calculation loop
2. Test with different number sequences
3. Implement in C code

---

## Problem 4: Population Growth Simulator

**Problem Description:**
Create a population growth simulator using the formula:
New Population = Current Population × (1 + Growth Rate)

Simulate growth over multiple years, showing:
- [ ] Population each year
- [ ] Growth amount
- [ ] Total growth over time

**Example:**
```
Enter initial population: 1000
Enter annual growth rate (%): 5
Enter years to simulate: 10

Year 1: 1000 → 1050 (+50)
Year 2: 1050 → 1102 (+52)
...
Year 10: 1628 → 1709 (+81)

Total growth: 709 people
```

**Your Task:**
1. Write pseudocode for growth simulation loop
2. Test different growth rates and time periods
3. Implement in C code

---

## Problem 5: Linear Search Algorithm

**Problem Description:**
Create a program that searches for a target value in an array:
- [ ] Generate or input an array of numbers
- [ ] Ask for target value to search
- [ ] Display position if found, or "not found"
- [ ] Count comparisons made
- [ ] Show search efficiency

**Example:**
```
Enter array size: 5
Enter 5 numbers: 10 20 30 40 50
Enter target to search: 30

Target 30 found at position 3
Comparisons made: 3
```

**Your Task:**
1. Write pseudocode for linear search algorithm
2. Test with different array sizes and targets
3. Implement in C code

---

## Problem 6: Savings Account Simulator

**Problem Description:**
Create a savings account simulator with monthly compounding:
- [ ] Initial deposit
- [ ] Monthly deposit amount
- [ ] Annual interest rate
- [ ] Number of years

Show balance each month and final totals.

**Example:**
```
Enter initial deposit: 1000
Enter monthly deposit: 100
Enter annual interest rate (%): 6
Enter years: 2

Month 1: Balance $1,100.00 (Interest: $5.00)
Month 2: Balance $1,205.30 (Interest: $5.53)
...
Month 24: Balance $3,422.19

Total deposited: $3,400.00
Total interest earned: $422.19
```

**Your Task:**
1. Write pseudocode for savings simulation
2. Test different deposit and interest scenarios
3. Implement in C code

---

### Loop Algorithm Guidelines

**For Loop Structure:**
```
Algorithm: Pattern Generator
1. Get size/input parameters
2. For i from 1 to size:
   a. For j from 1 to i:
      i. Print pattern element
   b. Move to next line
3. End pattern
```

**While Loop Structure:**
```
Algorithm: Data Processor
1. Initialize variables
2. While condition is true:
   a. Process current data
   b. Update variables
   c. Check termination condition
3. Display final results
```

---

### Success Checklist

**For Each Problem:**
- [ ] **Pattern Recognition**: Identify the repetitive structure
- [ ] **Loop Selection**: Choose appropriate loop type
- [ ] **Initialization**: Set up loop variables correctly
- [ ] **Iteration Logic**: Define what happens each loop
- [ ] **Termination**: Handle loop ending conditions
- [ ] **Pseudocode**: Write clear iterative algorithms
- [ ] **Testing**: Test with different iteration counts
- [ ] **Implementation**: Translate to working C code
- [ ] **Validation**: Verify correct repetitive behavior

**Repetitive Skills:**
- [ ] Master for/while/do-while loops
- [ ] Design nested loop patterns
- [ ] Handle loop control variables
- [ ] Optimize iterative processes
- [ ] Process data sequences efficiently

---

### Try This (Optional Challenges)

1. **Performance Optimization**: Optimize loops for large datasets
2. **Pattern Variations**: Add more complex pattern types
3. **Loop Unrolling**: Implement manual loop unrolling
4. **Parallel Processing**: Design for multi-threaded execution

---

## Repetitive Algorithm Framework

### Step 1: Repetition Analysis
- [ ] **What**: What action needs to be repeated?
- [ ] **How Many**: How many times to repeat?
- [ ] **How**: How does each iteration differ?
- [ ] **When**: When to stop repeating?

### Step 2: Loop Design
- [ ] **Control Variable**: What controls the loop?
- [ ] **Initialization**: Starting values
- [ ] **Update**: How control variable changes
- [ ] **Condition**: When to continue/stop

### Step 3: Iteration Logic
- [ ] **Processing**: What to do each iteration?
- [ ] **State Changes**: What variables update?
- [ ] **Output**: What to display each time?
- [ ] **Accumulation**: What totals to maintain?

---

<div style="page-break-after: always;"></div>

---

## SOLUTION APPROACH (Read after attempting!)

### Problem 1: Star Pattern Generator

**Analysis:**
- [ ] Different patterns require different loop structures
- [ ] Nested loops for 2D patterns
- [ ] Careful spacing and alignment

**Right Triangle Pattern:**
```
For i from 1 to size:
    For j from 1 to i:
        Print "*"
    Print newline
```

**Pyramid Pattern:**
```
For i from 1 to size:
    For spaces from 1 to (size-i):
        Print " "
    For stars from 1 to (2*i-1):
        Print "*"
    Print newline
```

---

### Problem 2: Number Pattern Generator

**Analysis:**
- [ ] Different number sequences
- [ ] Formatting for readability
- [ ] Variable increment patterns

**Multiplication Table:**
```
For i from 1 to size:
    For j from 1 to size:
        Print i + " x " + j + " = " + (i*j)
    Print newline
```

---

### Problem 3: Data Statistics Calculator

**Analysis:**
- [ ] Continuous input until sentinel value
- [ ] Running calculations during input
- [ ] Multiple statistics to track

**Loop Structure:**
```
Initialize: count=0, sum=0, min=MAX, max=MIN
While true:
    Get number
    If number == -1: break
    count++
    sum += number
    if number < min: min = number
    if number > max: max = number
    Display current stats
Display final summary
```

---

### Problem 4: Population Growth Simulator

**Analysis:**
- [ ] Year-by-year calculation
- [ ] Display format for each year
- [ ] Cumulative tracking

**Growth Loop:**
```
current_pop = initial
For year from 1 to years:
    growth = current_pop * (rate/100)
    new_pop = current_pop + growth
    Display year, current_pop, new_pop, growth
    current_pop = new_pop
```

---

### Problem 5: Linear Search Algorithm

**Analysis:**
- [ ] Sequential search through array
- [ ] Position tracking (1-based vs 0-based)
- [ ] Early termination on find

**Search Algorithm:**
```
found = false
position = -1
comparisons = 0
For i from 0 to size-1:
    comparisons++
    If array[i] == target:
        found = true
        position = i+1  // 1-based
        Break
If found:
    Display position and comparisons
Else:
    Display not found
```

---

### Problem 6: Savings Account Simulator

**Analysis:**
- [ ] Monthly compounding calculation
- [ ] Monthly deposits
- [ ] Interest calculation per month

**Monthly Simulation:**
```
balance = initial_deposit
total_deposited = initial_deposit
monthly_rate = annual_rate / 100 / 12

For month from 1 to (years * 12):
    // Add monthly deposit
    balance += monthly_deposit
    total_deposited += monthly_deposit

    // Calculate interest
    interest = balance * monthly_rate
    balance += interest

    Display month details
```

---

### Loop Optimization Techniques

**Efficient Loops:**
- [ ] Minimize operations inside loops
- [ ] Use pre-calculated values
- [ ] Avoid function calls in tight loops
- [ ] Consider loop fusion for related operations

**Memory Considerations:**
- [ ] Avoid large arrays in loops
- [ ] Reuse variables when possible
- [ ] Clear memory when done
- [ ] Consider streaming for large datasets

**Performance Patterns:**
- [ ] Cache-friendly access patterns
- [ ] Minimize branch predictions
- [ ] Use appropriate data types
- [ ] Profile and optimize bottlenecks

---

 **Congratulations! You've mastered repetitive algorithms!** 

*Next: Complex system problems with multi-component integration! *

### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Additional Content

Understand the key concepts:

- [ ] Review each function
- [ ] Understand the flow
- [ ] Learn the patterns used


### Code Review

Key functions and their purpose:

- [ ] Main function: Entry point
- [ ] Helper functions: Support logic


### <div style="page-break-after: always;"></div>

Answer Key

Expected implementation provided.

<div style="page-break-after: always;"></div>

---

## Answer Key

### Complete Solution

```
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses std::cout to print messages to the console
3. **Standard Library**: Includes iostream for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `g++ hello.cpp -o hello`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: g++` | Compiler not installed | `sudo apt install g++` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: unknown type name 'cout'` | Missing iostream | Add `#include <iostream>` |

### Tips for Learning

- C++ is a superset of C with additional features
- `std::cout` is the C++ way to print (replaces `printf`)
- `std::endl` adds a newline and flushes the buffer
- The `std::` prefix means these are from the "standard" namespace
