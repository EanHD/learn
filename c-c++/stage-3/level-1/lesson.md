# Level 1: Simple Problem Analysis

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

**MAJOR SHIFT!**  Welcome to Stage 3! No more copying code - now YOU are the programmer! You'll learn to analyze problems, design solutions, and create your own algorithms before writing code.

**The Process:**
1. **Read** the problem carefully
2. **Understand** what's being asked
3. **Break down** the problem into steps
4. **Write pseudocode** for your solution
5. **Test your logic** on paper
6. **Implement** in C code

---

### Learning Goals

- Analyze and understand problem requirements
- Break complex problems into manageable steps
- Design algorithms using pseudocode
- Think logically about program flow
- Create your own solutions from scratch

---

### Problem-Solving Framework

**STEP 1: Understand the Problem**
- What is the input?
- What is the expected output?
- What are the constraints?
- What are the edge cases?

**STEP 2: Plan the Solution**
- What are the main steps?
- What data do I need to track?
- What decisions need to be made?
- What calculations are required?

**STEP 3: Write Pseudocode**
- Use clear, simple language
- Break down into small steps
- Handle all cases
- Test your logic mentally

**STEP 4: Implement and Test**
- Translate pseudocode to C
- Test with different inputs
- Debug and refine

---

### Your Task

**For each problem below:**
1. **Read and understand** the problem
2. **Write pseudocode** for your solution
3. **Test your pseudocode** with sample inputs
4. **Implement** in C code
5. **Test thoroughly**

---

## Problem 1: Temperature Classifier

**Problem Description:**
Create a program that asks the user for a temperature in Fahrenheit and classifies it as:
- "Freezing" if below 32°F
- "Cold" if 32°F to 50°F
- "Comfortable" if 51°F to 78°F
- "Warm" if 79°F to 90°F
- "Hot" if above 90°F

The program should display both the temperature and its classification.

**Example:**
```
Enter temperature in Fahrenheit: 75
Temperature: 75°F - Comfortable
```

**Your Task:**
1. Write pseudocode for this problem
2. Test with temperatures: 25°F, 45°F, 65°F, 85°F, 95°F
3. Implement in C code

---

## Problem 2: Simple Vending Machine

**Problem Description:**
Create a program that simulates a vending machine selling snacks for $1.50 each. The program should:
- Ask the user how many snacks they want
- Calculate the total cost
- Ask for payment amount
- Calculate and display change (if any)
- Handle cases where payment is insufficient

**Example:**
```
How many snacks would you like? 3
Total cost: $4.50
Enter payment amount: $5.00
Change: $0.50
Thank you for your purchase!
```

**Your Task:**
1. Write pseudocode for this vending machine
2. Test with: 2 snacks ($5 payment), 1 snack ($1 payment), 4 snacks ($6 payment)
3. Implement in C code

---

## Problem 3: Age Category Sorter

**Problem Description:**
Create a program that asks for a person's age and determines their life stage category:
- "Child" if under 13
- "Teenager" if 13-19
- "Young Adult" if 20-35
- "Adult" if 36-64
- "Senior" if 65 or older

Also display how many years until the next category (or "Final stage" if Senior).

**Example:**
```
Enter age: 25
Category: Young Adult
Years until next category: 11
```

**Your Task:**
1. Write pseudocode for age categorization
2. Test with ages: 10, 15, 25, 45, 70
3. Implement in C code

---

## Problem 4: Movie Ticket Calculator

**Problem Description:**
Create a program that calculates movie ticket prices based on:
- Base price: $12.00
- Child (under 12): 50% discount
- Senior (65+): 30% discount
- Matinee (before 5 PM): additional 20% discount
- Group (3+ tickets): additional 10% discount

The program should ask for age, show time (24-hour format), and number of tickets.

**Example:**
```
Enter age: 70
Enter show time (0-23): 14
Enter number of tickets: 2

Base price per ticket: $12.00
Senior discount: 30% off
Matinee discount: 20% off
Final price per ticket: $6.72
Total for 2 tickets: $13.44
```

**Your Task:**
1. Write pseudocode for ticket price calculation
2. Test with various combinations of age, time, and group size
3. Implement in C code

---

## Problem 5: Number Comparison Tool

**Problem Description:**
Create a program that asks the user for three numbers and:
- Finds and displays the largest number
- Finds and displays the smallest number
- Calculates and displays the average
- Determines if all three numbers are equal
- Determines if the numbers form an increasing sequence

**Example:**
```
Enter three numbers: 5 8 3
Largest: 8
Smallest: 3
Average: 5.33
All equal: No
Increasing sequence: No
```

**Your Task:**
1. Write pseudocode for number analysis
2. Test with: (1,2,3), (5,5,5), (10,5,15), (7,7,8)
3. Implement in C code

---

## Problem 6: Grade Calculator

**Problem Description:**
Create a program that converts a numerical grade (0-100) to a letter grade:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F

Also display a motivational message based on the grade.

**Example:**
```
Enter numerical grade (0-100): 87
Letter grade: B
Message: Good job! Keep up the excellent work!
```

**Your Task:**
1. Write pseudocode for grade conversion
2. Test with grades: 95, 87, 72, 68, 45
3. Implement in C code

---

### Pseudocode Writing Guidelines

**Good Pseudocode Structure:**
```
Algorithm: Problem Name
1. Clear step-by-step instructions
2. Handle all input/output
3. Include decision points
4. Handle edge cases
5. End with clear output
```

**Example:**
```
Algorithm: Temperature Classifier
1. Display "Enter temperature in Fahrenheit: "
2. Get temperature from user
3. If temperature < 32:
   a. Display temperature + "°F - Freezing"
4. Else if temperature <= 50:
   a. Display temperature + "°F - Cold"
5. Else if temperature <= 78:
   a. Display temperature + "°F - Comfortable"
6. Else if temperature <= 90:
   a. Display temperature + "°F - Warm"
7. Else:
   a. Display temperature + "°F - Hot"
```

---

### Success Checklist

**For Each Problem:**
- [ ] **Analysis**: Clearly understand the problem requirements
- [ ] **Planning**: Break down into logical steps
- [ ] **Pseudocode**: Write clear, step-by-step algorithm
- [ ] **Testing**: Test pseudocode with sample inputs mentally
- [ ] **Implementation**: Translate to working C code
- [ ] **Validation**: Test with multiple input scenarios

**Problem-Solving Skills:**
- [ ] Identify all inputs and outputs
- [ ] Handle edge cases and invalid inputs
- [ ] Use appropriate decision structures
- [ ] Provide clear user feedback

---

### Try This (Optional Challenges)

1. **Add Input Validation**: Check for invalid inputs in each problem
2. **Enhanced Features**: Add more categories or options
3. **Combine Problems**: Create a multi-function program
4. **Save Results**: Store calculation history

---

## Problem Analysis Framework

### Step 1: Read Carefully
- **What?** What does the program need to do?
- **Who?** Who will use it? What do they need?
- **How?** What information is needed? What output is expected?

### Step 2: Identify Components
- **Inputs**: What data does the program need?
- **Processing**: What calculations or decisions are needed?
- **Outputs**: What should be displayed to the user?

### Step 3: Break Down the Problem
- **Main Steps**: What are the high-level steps?
- **Sub-steps**: What are the detailed actions?
- **Decisions**: What choices need to be made?
- **Loops**: Are there repetitive actions?

### Step 4: Consider Edge Cases
- **Boundaries**: What happens at the limits?
- **Invalid Input**: What if user enters wrong data?
- **Special Cases**: Any unusual scenarios?

---

<div style="page-break-after: always;"></div>

---

## SOLUTION APPROACH (Read after attempting!)

### Problem 1: Temperature Classifier

**Analysis:**
- Input: Temperature in Fahrenheit (float)
- Processing: Compare against temperature ranges
- Output: Temperature + classification
- Edge cases: Negative temperatures, very high temperatures

**Sample Pseudocode:**
```
Algorithm: Temperature Classifier
1. Display "Enter temperature in Fahrenheit: "
2. Get temperature from user
3. If temperature < 32:
   a. Display temperature + "°F - Freezing"
4. Else if temperature <= 50:
   a. Display temperature + "°F - Cold"
5. Else if temperature <= 78:
   a. Display temperature + "°F - Comfortable"
6. Else if temperature <= 90:
   a. Display temperature + "°F - Warm"
7. Else:
   a. Display temperature + "°F - Hot"
```

**Test Cases:**
- 25°F → Freezing
- 45°F → Cold
- 65°F → Comfortable
- 85°F → Warm
- 95°F → Hot

---

### Problem 2: Simple Vending Machine

**Analysis:**
- Inputs: Number of snacks, payment amount
- Processing: Cost calculation, change calculation
- Validation: Sufficient payment check
- Constants: Snack price = $1.50

**Sample Pseudocode:**
```
Algorithm: Vending Machine
1. Set snack_price to 1.50
2. Display "How many snacks would you like? "
3. Get num_snacks from user
4. Calculate total_cost = num_snacks × snack_price
5. Display "Total cost: $" + total_cost
6. Display "Enter payment amount: $"
7. Get payment from user
8. If payment >= total_cost:
   a. Calculate change = payment - total_cost
   b. Display "Change: $" + change
   c. Display "Thank you for your purchase!"
9. Else:
   a. Calculate needed = total_cost - payment
   b. Display "Insufficient payment. You need $" + needed + " more."
```

---

### Problem 3: Age Category Sorter

**Analysis:**
- Input: Age (integer)
- Processing: Category determination + years to next category
- Categories: Child (<13), Teen (13-19), Young Adult (20-35), Adult (36-64), Senior (65+)
- Calculation: Years until next category boundary

**Key Calculations:**
- Child (under 13) → 13 - age years until Teen
- Teen (13-19) → 20 - age years until Young Adult
- Young Adult (20-35) → 36 - age years until Adult
- Adult (36-64) → 65 - age years until Senior
- Senior (65+) → "Final stage"

---

### Problem 4: Movie Ticket Calculator

**Analysis:**
- Inputs: Age, show time (0-23), number of tickets
- Base price: $12.00
- Discounts: Age-based, time-based, group-based
- Order matters: Apply discounts sequentially

**Discount Order:**
1. Age discount (child/senior)
2. Matinee discount (if before 17:00)
3. Group discount (if 3+ tickets)

---

### Problem 5: Number Comparison Tool

**Analysis:**
- Inputs: Three numbers (can be float for average)
- Processing: Find min/max, calculate average, check equality, check sequence
- Sequence check: num1 < num2 < num3

**Multiple Approaches:**
- Use if-else chains for min/max
- Use variables to track current min/max
- Use boolean flags for equality and sequence checks

---

### Problem 6: Grade Calculator

**Analysis:**
- Input: Numerical grade (0-100)
- Processing: Convert to letter grade using ranges
- Output: Letter grade + motivational message
- Validation: Ensure grade is within 0-100 range

**Grade Ranges:**
- A: 90-100 (Excellent work!)
- B: 80-89 (Good job!)
- C: 70-79 (Satisfactory)
- D: 60-69 (Needs improvement)
- F: 0-59 (Keep trying!)

---

### Common Problem-Solving Patterns

**Range Checking:**
```
If value >= min AND value <= max:
    Process valid value
Else:
    Handle invalid value
```

**Sequential Processing:**
```
Step 1: Get input
Step 2: Validate input
Step 3: Process data
Step 4: Display results
```

**Decision Trees:**
```
If condition A:
    If sub-condition A1:
        Action A1
    Else:
        Action A2
Else if condition B:
    Action B
Else:
    Default action
```

---

### Implementation Tips

**Start Simple:**
- Implement basic functionality first
- Add validation and error handling later
- Test with normal cases before edge cases

**Debugging:**
- Add printf statements to trace program flow
- Test with known inputs and verify expected outputs
- Check variable values at key points

**Code Organization:**
- Use meaningful variable names
- Add comments explaining complex logic
- Break long functions into smaller ones
- Test incrementally as you build

---

 **Congratulations! You've created your first independent algorithms!** 

*Problem analysis is the foundation of programming. Next: Data management problems! *