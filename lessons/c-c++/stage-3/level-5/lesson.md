# Level 5: Decision-Based Problems

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

**RULE ENGINE MASTER!**  You're now building decision-making systems with complex rules, eligibility criteria, and multi-factor evaluations. This level focuses on creating algorithms that make intelligent decisions based on multiple criteria.

**The Process:**
1. **Analyze** the decision criteria and rules
2. **Design** the decision tree or rule engine
3. **Plan** how to evaluate multiple conditions
4. **Handle** complex logical combinations
5. **Write pseudocode** for decision logic
6. **Test edge cases** and rule interactions
7. **Implement** in C code

---

### Learning Goals

- [ ] Design complex decision trees
- [ ] Implement rule-based systems
- [ ] Handle multiple eligibility criteria
- [ ] Create evaluation algorithms
- [ ] Manage decision logic complexity
- [ ] Provide clear decision explanations

---

### Decision System Framework

**STEP 1: Rule Analysis**
- [ ] What are the decision criteria?
- [ ] What are the possible outcomes?
- [ ] What rules determine each outcome?
- [ ] How do rules interact or conflict?

**STEP 2: Logic Design**
- [ ] How to structure the decision tree?
- [ ] What order to evaluate conditions?
- [ ] How to handle rule priorities?
- [ ] What to do with conflicting rules?

**STEP 3: Decision Algorithm**
- [ ] Break down complex decisions into steps
- [ ] Handle AND/OR logic combinations
- [ ] Consider rule precedence
- [ ] Plan for tie-breaking scenarios

**STEP 4: Validation and Testing**
- [ ] Test all rule combinations
- [ ] Verify edge cases
- [ ] Ensure logical consistency
- [ ] Validate decision outcomes

---

### Your Task

**For each decision problem:**
1. **Analyze** the rules and criteria
2. **Design** the decision logic
3. **Write pseudocode** for the rule engine
4. **Test decision scenarios** thoroughly
5. **Implement** in C code
6. **Validate** all decision paths

---

## Problem 1: Loan Eligibility Checker

**Problem Description:**
Create a loan eligibility system that evaluates applicants based on:
- [ ] Credit score (300-850)
- [ ] Annual income ($20,000+)
- [ ] Debt-to-income ratio (<40%)
- [ ] Employment status (employed/unemployed)
- [ ] Loan amount requested

Eligibility rules:
- [ ] Credit score >= 650 AND income >= $30,000 AND DTI < 40%
- [ ] OR credit score >= 700 AND income >= $25,000
- [ ] Maximum loan: 3x annual income
- [ ] Employed applicants get preferred rates

**Example:**
```cpp
=== Loan Application ===
Enter credit score (300-850): 720
Enter annual income: 45000
Enter debt-to-income ratio (%): 25
Are you employed? (y/n): y
Enter loan amount requested: 100000

ELIGIBLE!
Loan amount: $100,000
Interest rate: 6.5%
Monthly payment: $632.07
```cpp

**Your Task:**
1. Write pseudocode for loan eligibility rules
2. Test various applicant profiles
3. Implement in C code

---

## Problem 2: Insurance Premium Calculator

**Problem Description:**
Create an insurance premium calculator with rules:
- [ ] Base premium: $500/year
- [ ] Age factors: Under 25 (+50%), 25-40 (+0%), 41-60 (+25%), 60+ (+75%)
- [ ] Driving record: Clean (-10%), 1 accident (+20%), 2+ accidents (+50%)
- [ ] Vehicle type: Sedan (+0%), SUV (+15%), Sports car (+30%)
- [ ] Coverage level: Basic (+0%), Standard (+25%), Premium (+50%)

**Example:**
```cpp
=== Insurance Quote ===
Enter age: 28
Enter accidents in last 3 years: 0
Enter vehicle type (sedan/suv/sports): sedan
Enter coverage level (basic/standard/premium): standard

Annual Premium: $687.50
(Base: $500 + Age: $0 + Record: -$50 + Vehicle: $0 + Coverage: $125)
```cpp

**Your Task:**
1. Write pseudocode for premium calculation rules
2. Test different customer profiles
3. Implement in C code

---

## Problem 3: Scholarship Eligibility System

**Problem Description:**
Create a scholarship eligibility system with criteria:
- [ ] GPA (4.0 scale): 3.5+ required, 4.0 = bonus
- [ ] Family income: <$50,000 = priority
- [ ] Community service hours: 50+ hours = bonus
- [ ] Leadership roles: President/VP = bonus
- [ ] Essay score (1-10): 7+ required
- [ ] Recommendation strength (1-10): 8+ = bonus

Award levels:
- [ ] Full scholarship: GPA 4.0 AND income <$30,000 AND essay >=9
- [ ] Partial scholarship: GPA >=3.7 AND (income <$50,000 OR service >=100)
- [ ] Honorable mention: GPA >=3.5 AND essay >=7

**Example:**
```cpp
=== Scholarship Application ===
Enter GPA (0.0-4.0): 3.8
Enter family income: 35000
Enter service hours: 75
Leadership role? (y/n): y
Enter essay score (1-10): 8
Enter recommendation score (1-10): 9

AWARD: Partial Scholarship
Reason: Strong GPA and leadership experience
```cpp

**Your Task:**
1. Write pseudocode for scholarship rules
2. Test different applicant scenarios
3. Implement in C code

---

## Problem 4: Tax Bracket Calculator

**Problem Description:**
Create a tax calculator for 2024 tax brackets:
- [ ] 10% on income up to $11,000
- [ ] 12% on $11,001-$44,725
- [ ] 22% on $44,726-$95,375
- [ ] 24% on $95,376-$182,100
- [ ] Plus standard deduction: $13,850

Also calculate effective tax rate and after-tax income.

**Example:**
```cpp
=== Tax Calculator ===
Enter annual income: 75000

Taxable income: $61,150
Tax owed: $8,847.50
Effective rate: 11.8%
After-tax income: $66,152.50

Tax breakdown:
10% bracket: $1,100.00
12% bracket: $4,032.00
22% bracket: $3,715.50
```cpp

**Your Task:**
1. Write pseudocode for tax bracket calculations
2. Test different income levels
3. Implement in C code

---

## Problem 5: Medical Diagnosis Assistant

**Problem Description:**
Create a simple medical diagnosis assistant with symptoms:
- [ ] Fever, cough, fatigue, headache, nausea
- [ ] Rules for common conditions:
  - Flu: Fever + (cough OR fatigue) + headache
  - Cold: Cough + headache + (fatigue OR nausea)
  - Migraine: Headache + nausea + fatigue
  - Stomach bug: Nausea + fatigue (no fever)

Provide diagnosis and recommend seeing a doctor if multiple symptoms match.

**Example:**
```cpp
=== Symptom Checker ===
Do you have a fever? (y/n): y
Do you have a cough? (y/n): y
Are you fatigued? (y/n): y
Do you have a headache? (y/n): n
Do you feel nauseous? (y/n): n

Possible diagnosis: Flu
Recommendation: Rest, drink fluids, see doctor if symptoms worsen
```cpp

**Your Task:**
1. Write pseudocode for diagnosis rules
2. Test different symptom combinations
3. Implement in C code

---

## Problem 6: Job Application Screener

**Problem Description:**
Create a job application screening system with criteria:
- [ ] Years of experience: 0-2 (junior), 3-5 (mid), 6+ (senior)
- [ ] Education: High school, Associate, Bachelor's, Master's
- [ ] Required skills: Must have 2+ of 5 listed skills
- [ ] Location preference: Local (+), Willing to relocate (+)
- [ ] Salary expectation: Within 20% of offered range

Screening rules:
- [ ] Auto-reject: <2 years exp AND no Bachelor's AND <2 skills
- [ ] Phone screen: 2-5 years exp OR Bachelor's degree
- [ ] Interview: 3+ skills AND (senior OR Master's)
- [ ] Offer: Interview qualified AND salary match AND local

**Example:**
```cpp
=== Application Screening ===
Enter years of experience: 4
Enter education level (HS/Associate/BS/MS): BS
Enter number of required skills (0-5): 3
Location preference (local/relocate): local
Salary expectation: 85000
Offered salary range: 80000-90000

SCREENING RESULT: Interview
Reason: Good experience, education, and skills match
```cpp

**Your Task:**
1. Write pseudocode for screening rules
2. Test various candidate profiles
3. Implement in C code

---

### Decision Logic Guidelines

**Rule Engine Structure:**
```cpp
Algorithm: Decision Engine
1. Gather all input criteria
2. Evaluate primary rules first
3. Check secondary conditions
4. Apply rule combinations (AND/OR)
5. Determine final decision
6. Provide reasoning for decision
```cpp

**Complex Condition Handling:**
```cpp
If (condition_A AND condition_B) OR (condition_C AND condition_D):
    Outcome 1
Else if condition_E OR (condition_F AND condition_G):
    Outcome 2
Else:
    Default outcome
```cpp

---

### Success Checklist

**For Each Problem:**
- [ ] **Rule Analysis**: Clearly identify all decision criteria
- [ ] **Logic Design**: Structure complex conditions properly
- [ ] **Edge Cases**: Handle boundary conditions
- [ ] **Rule Conflicts**: Resolve conflicting criteria
- [ ] **Pseudocode**: Write clear decision algorithms
- [ ] **Testing**: Test all rule combinations
- [ ] **Implementation**: Translate to working C code
- [ ] **Validation**: Verify decision accuracy

**Decision Skills:**
- [ ] Design multi-criteria evaluation systems
- [ ] Handle complex logical combinations
- [ ] Provide clear decision explanations
- [ ] Test decision logic thoroughly
- [ ] Handle rule precedence and conflicts

---

### Try This (Optional Challenges)

1. **Advanced Rules**: Add rule weighting and scoring systems
2. **Dynamic Rules**: Allow users to modify decision criteria
3. **Audit Trail**: Log decision-making process for transparency
4. **Rule Validation**: Check for logical inconsistencies in rules

---

## Decision Framework

### Step 1: Criteria Analysis
- [ ] **Inputs**: What information is needed for decisions?
- [ ] **Rules**: What conditions determine outcomes?
- [ ] **Outcomes**: What are the possible results?
- [ ] **Priorities**: Which rules take precedence?

### Step 2: Logic Structure
- [ ] **Primary Rules**: Must-meet conditions
- [ ] **Secondary Rules**: Bonus or tie-breaker conditions
- [ ] **Combinations**: How rules interact (AND/OR/NOT)
- [ ] **Precedence**: Order of rule evaluation

### Step 3: Implementation Planning
- [ ] **Data Structures**: How to store criteria and rules?
- [ ] **Evaluation Order**: Which conditions to check first?
- [ ] **Error Handling**: What if criteria are missing?
- [ ] **Output Format**: How to present decisions clearly?

---

<div style="page-break-after: always;"></div>

---

## SOLUTION APPROACH (Read after attempting!)

### Problem 1: Loan Eligibility Checker

**Analysis:**
- [ ] Multiple eligibility paths (AND/OR combinations)
- [ ] Numerical comparisons and boolean logic
- [ ] Calculation of loan terms if eligible

**Decision Tree:**
```cpp
If (credit >= 650 AND income >= 30000 AND dti < 40) OR (credit >= 700 AND income >= 25000):
    If loan_amount <= income * 3:
        ELIGIBLE
        Calculate rates and payments
    Else:
        INELIGIBLE - Loan too large
Else:
    INELIGIBLE - Doesn't meet criteria
```cpp

---

### Problem 2: Insurance Premium Calculator

**Analysis:**
- [ ] Additive premium calculation
- [ ] Multiple factor adjustments
- [ ] Percentage-based modifications

**Calculation Structure:**
```cpp
base_premium = 500
age_adjustment = calculate_age_factor(age)
record_adjustment = calculate_record_factor(accidents)
vehicle_adjustment = calculate_vehicle_factor(type)
coverage_adjustment = calculate_coverage_factor(level)
total = base + age + record + vehicle + coverage
```cpp

---

### Problem 3: Scholarship Eligibility System

**Analysis:**
- [ ] Multi-level award system
- [ ] Combination of quantitative and qualitative factors
- [ ] Priority ranking for awards

**Evaluation Logic:**
```cpp
score = 0
If GPA >= 3.5: score += 1
If income < 50000: score += 1
If service >= 50: score += 1
If leadership: score += 1
If essay >= 7: score += 1
If recommendation >= 8: score += 1

If score >= 5 AND GPA == 4.0: Full Scholarship
Else if score >= 4: Partial Scholarship
Else if score >= 3: Honorable Mention
```cpp

---

### Problem 4: Tax Bracket Calculator

**Analysis:**
- [ ] Progressive tax system
- [ ] Bracket calculations
- [ ] Marginal vs effective rates

**Tax Calculation:**
```cpp
taxable = income - deduction
tax = 0

If taxable > 0:
    // 10% bracket
    bracket1 = min(taxable, 11000)
    tax += bracket1 * 0.10
    taxable -= bracket1

    // 12% bracket
    bracket2 = min(taxable, 33725)
    tax += bracket2 * 0.12
    // Continue for other brackets
```cpp

---

### Problem 5: Medical Diagnosis Assistant

**Analysis:**
- [ ] Symptom pattern matching
- [ ] Boolean logic for conditions
- [ ] Multiple possible diagnoses

**Diagnosis Logic:**
```cpp
flu_score = 0
if fever: flu_score += 1
if cough or fatigue: flu_score += 1
if headache: flu_score += 1

cold_score = 0
if cough: cold_score += 1
if headache: cold_score += 1
if fatigue or nausea: cold_score += 1

// Compare scores and determine diagnosis
```cpp

---

### Problem 6: Job Application Screener

**Analysis:**
- [ ] Multi-stage screening process
- [ ] Progressive qualification
- [ ] Multiple criteria evaluation

**Screening Flow:**
```cpp
If experience < 2 AND education < BS AND skills < 2:
    REJECT
Else if experience >= 3 OR education >= BS:
    If skills >= 3 AND (experience >= 6 OR education == MS):
        If salary_match AND location_ok:
            OFFER
        Else:
            INTERVIEW
    Else:
        PHONE_SCREEN
Else:
    HOLD
```cpp

---

### Decision System Best Practices

**Rule Clarity:**
- [ ] Use clear, unambiguous conditions
- [ ] Document rule rationale
- [ ] Test all rule combinations
- [ ] Provide decision explanations

**Maintainability:**
- [ ] Separate rules from logic
- [ ] Use constants for thresholds
- [ ] Comment complex conditions
- [ ] Modular decision functions

**Robustness:**
- [ ] Handle missing data gracefully
- [ ] Validate input ranges
- [ ] Provide default behaviors
- [ ] Log decision processes

---

 **Congratulations! You've built intelligent decision systems!** 

*Next: Repetitive problems with loop-based algorithms and patterns! *

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

```cpp
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses printf to print messages to the console
3. **Standard Library**: Includes stdio.h for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `gcc main.c -o main`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: gcc` | Compiler not installed | `sudo apt install gcc` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: implicit declaration of function 'printf'` | Missing stdio.h | Add `#include <stdio.h>` |

### Tips for Learning

- C uses stdio.h for input/output with additional features
- `printf` is the C standard for formatted output
- `\n` adds a newline character in format strings
- Format specifiers control how data is displayed (%d, %f, %s, etc.)
