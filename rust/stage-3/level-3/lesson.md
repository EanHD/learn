# Level 3: Mathematical Problems
## Stage 3: Problem to Pseudocode

### Today's Mission

Mathematical problems often require careful analysis of formulas and algorithms. You'll design a solution for a problem involving mathematical computation.

---

### Learning Goals

- Analyze mathematical problem requirements
- Design step-by-step calculation algorithms
- Handle complex mathematical operations
- Create accurate computational logic

---

### Your Task

**Read the problem below, then write pseudocode to solve it. Create a file called `mathematical_problems.md` with your pseudocode solution.**

### Problem: Compound Interest Calculator

**Description:**
Create a program that calculates compound interest for savings accounts. The program should:

1. Ask for the principal amount (initial investment)
2. Ask for the annual interest rate (as a percentage)
3. Ask for the number of years to invest
4. Ask for compounding frequency (yearly, monthly, quarterly)
5. Calculate the final amount and total interest earned
6. Display a detailed breakdown

**Compound Interest Formula:**
```
A = P(1 + r/n)^(nt)
```
Where:
- A = Final amount
- P = Principal amount
- r = Annual interest rate (decimal)
- n = Number of times interest is compounded per year
- t = Number of years

**Compounding Options:**
- Yearly: n = 1
- Quarterly: n = 4
- Monthly: n = 12

**Example Interaction:**
```
Compound Interest Calculator
Enter principal amount: $1000
Enter annual interest rate (%): 5
Enter number of years: 3
Compounding frequency:
1. Yearly
2. Quarterly
3. Monthly
Enter choice (1-3): 2

Investment Summary
------------------
Principal: $1000.00
Interest Rate: 5.00%
Years: 3
Compounding: Quarterly
Final Amount: $1161.54
Total Interest: $161.54
```

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your pseudocode file**:
   ```bash
   touch mathematical_problems.md
   ```
3. **Break down the formula** - Understand each component
4. **Plan input validation** - Ensure reasonable values
5. **Design calculations** - Step-by-step mathematical operations

---

### Success Checklist

- [ ] Created `mathematical_problems.md` file
- [ ] Understood compound interest formula components
- [ ] Planned input collection for all variables
- [ ] Designed calculation logic with proper operator precedence
- [ ] Considered different compounding frequencies
- [ ] Planned clear financial report output

---

### What Did You Learn?

Mathematical problem analysis involves:
- **Formula understanding** - Breaking down complex equations
- **Variable identification** - What data is needed?
- **Calculation sequencing** - Order of mathematical operations
- **Precision handling** - Dealing with decimal numbers

---

### Try This (Optional Challenges)

1. Add daily compounding option
2. Calculate monthly payment amounts
3. Show year-by-year growth breakdown

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Problem Analysis

**Mathematical Components:**
- Principal (P): Initial investment amount
- Rate (r): Annual percentage converted to decimal
- Time (t): Number of years
- Frequency (n): Compounding periods per year
- Final Amount (A): Result of compound interest formula

**Formula Breakdown:**
```
A = P(1 + r/n)^(nt)
Total Interest = A - P
```

### Sample Pseudocode Solution

```
START PROGRAM
    DISPLAY "Compound Interest Calculator"
    
    DISPLAY "Enter principal amount:"
    READ principal AS NUMBER
    
    DISPLAY "Enter annual interest rate (%):"
    READ rate_percent AS NUMBER
    SET rate TO rate_percent / 100  // Convert to decimal
    
    DISPLAY "Enter number of years:"
    READ years AS NUMBER
    
    DISPLAY "Compounding frequency:"
    DISPLAY "1. Yearly"
    DISPLAY "2. Quarterly"
    DISPLAY "3. Monthly"
    DISPLAY "Enter choice (1-3):"
    READ frequency_choice AS NUMBER
    
    // Set compounding frequency
    IF frequency_choice == 1 THEN
        SET n TO 1
        SET frequency_name TO "Yearly"
    ELSE IF frequency_choice == 2 THEN
        SET n TO 4
        SET frequency_name TO "Quarterly"
    ELSE IF frequency_choice == 3 THEN
        SET n TO 12
        SET frequency_name TO "Monthly"
    ELSE
        DISPLAY "Invalid choice. Using yearly compounding."
        SET n TO 1
        SET frequency_name TO "Yearly"
    END IF
    
    // Calculate compound interest
    SET base TO 1 + (rate / n)
    SET exponent TO n * years
    SET final_amount TO principal * (base ^ exponent)
    SET total_interest TO final_amount - principal
    
    // Display results
    DISPLAY "Investment Summary"
    DISPLAY "------------------"
    DISPLAY "Principal: $" + principal
    DISPLAY "Interest Rate: " + rate_percent + "%"
    DISPLAY "Years: " + years
    DISPLAY "Compounding: " + frequency_name
    DISPLAY "Final Amount: $" + final_amount
    DISPLAY "Total Interest: $" + total_interest
END PROGRAM
```

### Analysis Breakdown

**Mathematical Logic:**
- **Rate conversion**: Percentage to decimal (5% → 0.05)
- **Formula application**: A = P(1 + r/n)^(nt)
- **Exponentiation**: Using power function for compound calculation
- **Interest calculation**: Simple subtraction (A - P)

**Why this approach?**
- **Modular frequency selection**: Clear menu for compounding options
- **Step-by-step calculation**: Break complex formula into parts
- **Error handling**: Default to yearly if invalid choice
- **Clear reporting**: Financial summary with all details

**Potential improvements:**
- Input validation for positive amounts and reasonable rates
- Currency formatting (2 decimal places)
- Year-by-year breakdown of growth

### Common Analysis Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Wrong rate conversion | Forgetting percentage to decimal | Divide by 100 |
| Incorrect formula order | Wrong operator precedence | Use parentheses for clarity |
| No frequency validation | Invalid compounding choice | Provide default and warn user |
| Poor variable names | Unclear mathematical meaning | Use descriptive names (principal, rate) |

### Bonus Knowledge

- **Financial Mathematics**: Real-world application of exponents
- **Algorithm Design**: Breaking complex calculations into steps
- **Precision Issues**: Floating-point arithmetic considerations
- **Business Logic**: Financial calculation requirements

---

 **Great! You analyzed a complex mathematical problem!** 

*Next: Interactive Problems!*