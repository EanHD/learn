# Level 5: Decision Pseudocode

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Decision-making is the intelligence of programs! Today you'll master complex conditional logic, nested decisions, and rule-based systems. You'll learn to translate sophisticated decision trees from pseudocode into robust C code.

---

### Learning Goals

- [ ] Implement complex conditional logic
- [ ] Create nested decision structures
- [ ] Handle multiple condition combinations
- [ ] Build rule-based decision systems
- [ ] Design decision trees and flowcharts
- [ ] Create intelligent program behavior

---

### Decision-Making in Programming

**Types of Decisions:**
1. **Binary Decisions**: Yes/No, True/False
2. **Multi-way Decisions**: Multiple choices (if-else-if chains)
3. **Nested Decisions**: Decisions within decisions
4. **Rule-Based Systems**: Complex business logic
5. **State Machines**: Decisions based on current state

**Decision Patterns:**
- [ ] **Eligibility Checking**: Age, income, qualifications
- [ ] **Categorization**: Grading, risk assessment, classification
- [ ] **Business Rules**: Discounts, pricing, policies
- [ ] **Validation**: Input checking, data verification

---

### Your Task

**Translate each decision-based pseudocode algorithm into working C code.**

---

## Algorithm 1: Loan Approval System

**Pseudocode:**
```
Algorithm: Evaluate Loan Application
1. Display "=== Loan Approval System ==="
2. Display "Enter applicant's age: "
3. Get age from user
4. Display "Enter annual income: $"
5. Get income from user
6. Display "Enter credit score (300-850): "
7. Get credit_score from user
8. Display "Enter loan amount requested: $"
9. Get loan_amount from user
10. Initialize approval_status to "PENDING"
11. Initialize max_loan_amount to 0
12. If age < 18:
   a. Set approval_status to "DENIED - Underage"
13. Else if age > 70:
   a. Set approval_status to "DENIED - Age limit exceeded"
14. Else:
   a. If credit_score < 300 or credit_score > 850:
      i. Set approval_status to "DENIED - Invalid credit score"
   b. Else:
      i. If credit_score >= 750:
         i. Set max_loan_amount to income × 5
      ii. Else if credit_score >= 650:
         i. Set max_loan_amount to income × 3
      iii. Else if credit_score >= 550:
         i. Set max_loan_amount to income × 2
      iv. Else:
         i. Set max_loan_amount to income × 1
      v. If loan_amount > max_loan_amount:
         i. Set approval_status to "DENIED - Loan amount exceeds limit"
      vi. Else if loan_amount > income × 0.5:
         i. Set approval_status to "REQUIRES MANAGER APPROVAL"
      vii. Else:
         i. Set approval_status to "APPROVED"
15. Display "=== Loan Decision ==="
16. Display "Applicant age: " + age
17. Display "Annual income: $" + income
18. Display "Credit score: " + credit_score
19. Display "Loan requested: $" + loan_amount
20. If approval_status equals "APPROVED":
   a. Display " LOAN APPROVED!"
   b. Display "Maximum approved amount: $" + max_loan_amount
21. Else if approval_status equals "REQUIRES MANAGER APPROVAL":
   a. Display " REQUIRES MANAGER APPROVAL"
   b. Display "Reason: High loan-to-income ratio"
22. Else:
   a. Display " LOAN DENIED"
   b. Display "Reason: " + approval_status
```

**Decision Logic:**
- [ ] Age restrictions (18-70)
- [ ] Credit score validation and tiering
- [ ] Income-based loan limits
- [ ] Loan-to-income ratio checks
- [ ] Multi-level approval process

**Your Task:** Build a comprehensive loan approval system.

---

## Algorithm 2: Health Risk Assessment

**Pseudocode:**
```
Algorithm: Assess Health Risk Factors
1. Display "=== Health Risk Assessment ==="
2. Display "Enter your age: "
3. Get age from user
4. Display "Enter your BMI: "
5. Get bmi from user
6. Display "Do you smoke? (yes/no): "
7. Get smoking_status from user
8. Display "Do you exercise regularly? (yes/no): "
9. Get exercise_status from user
10. Display "Family history of heart disease? (yes/no): "
11. Get family_history from user
12. Initialize risk_level to "LOW"
13. Initialize risk_points to 0
14. If age >= 65:
   a. Add 3 to risk_points
15. Else if age >= 45:
   a. Add 2 to risk_points
16. Else if age >= 30:
   a. Add 1 to risk_points
17. If bmi >= 30:
   a. Add 3 to risk_points
18. Else if bmi >= 25:
   a. Add 2 to risk_points
19. Else if bmi >= 23:
   a. Add 1 to risk_points
20. If smoking_status is "yes":
   a. Add 3 to risk_points
21. If exercise_status is "no":
   a. Add 2 to risk_points
22. If family_history is "yes":
   a. Add 2 to risk_points
23. If risk_points >= 8:
   a. Set risk_level to "HIGH"
24. Else if risk_points >= 5:
   a. Set risk_level to "MODERATE"
25. Else if risk_points >= 3:
   a. Set risk_level to "ELEVATED"
26. Display "=== Health Risk Assessment Results ==="
27. Display "Age: " + age + " years"
28. Display "BMI: " + bmi
29. Display "Smoking: " + smoking_status
30. Display "Exercise: " + exercise_status
31. Display "Family history: " + family_history
32. Display "Risk points: " + risk_points + "/12"
33. Display "Risk level: " + risk_level
34. If risk_level equals "HIGH":
   a. Display " HIGH RISK - Consult doctor immediately"
   b. Display "Recommendations: Lifestyle changes, medical evaluation"
35. Else if risk_level equals "MODERATE":
   a. Display " MODERATE RISK - Monitor health closely"
   b. Display "Recommendations: Improve diet, start exercising"
36. Else if risk_level equals "ELEVATED":
   a. Display " ELEVATED RISK - Take preventive measures"
   b. Display "Recommendations: Regular check-ups, healthy habits"
37. Else:
   a. Display " LOW RISK - Maintain healthy lifestyle"
   b. Display "Recommendations: Continue current healthy habits"
```

**Decision Logic:**
- [ ] Multi-factor risk assessment
- [ ] Point-based scoring system
- [ ] Categorical risk levels
- [ ] Personalized recommendations

**Your Task:** Create a health risk assessment tool.

---

## Algorithm 3: Academic Standing Calculator

**Pseudocode:**
```
Algorithm: Determine Academic Standing
1. Display "=== Academic Standing Calculator ==="
2. Display "Enter GPA (0.0-4.0): "
3. Get gpa from user
4. Display "Enter total credit hours completed: "
5. Get credit_hours from user
6. Display "Enter number of semesters completed: "
7. Get semesters from user
8. Display "Any academic probation? (yes/no): "
9. Get probation_status from user
10. Initialize standing to "UNDETERMINED"
11. Initialize eligibility_status to "ELIGIBLE"
12. If probation_status is "yes":
   a. Set standing to "ACADEMIC PROBATION"
   b. Set eligibility_status to "RESTRICTED"
13. Else:
   a. If gpa >= 3.75 and credit_hours >= 60:
      i. Set standing to "SUMMA CUM LAUDE CANDIDATE"
   b. Else if gpa >= 3.5 and credit_hours >= 45:
      i. Set standing to "MAGNA CUM LAUDE CANDIDATE"
   c. Else if gpa >= 3.25 and credit_hours >= 30:
      i. Set standing to "CUM LAUDE CANDIDATE"
   d. Else if gpa >= 3.0:
      i. If credit_hours >= 90:
         i. Set standing to "GOOD STANDING - NEAR GRADUATION"
      ii. Else if credit_hours >= 60:
         i. Set standing to "GOOD STANDING - JUNIOR"
      iii. Else if credit_hours >= 30:
         i. Set standing to "GOOD STANDING - SOPHOMORE"
      iv. Else:
         i. Set standing to "GOOD STANDING - FRESHMAN"
   e. Else if gpa >= 2.0:
      i. Set standing to "SATISFACTORY STANDING"
   f. Else:
      i. Set standing to "ACADEMIC WARNING"
      ii. Set eligibility_status to "COUNSELING REQUIRED"
14. Display "=== Academic Assessment ==="
15. Display "GPA: " + gpa
16. Display "Credit Hours: " + credit_hours
17. Display "Semesters: " + semesters
18. Display "Probation Status: " + probation_status
19. Display "Academic Standing: " + standing
20. Display "Eligibility Status: " + eligibility_status
21. If eligibility_status equals "ELIGIBLE":
   a. Display " Eligible for all academic activities"
22. Else if eligibility_status equals "RESTRICTED":
   a. Display " Limited eligibility - Academic plan required"
23. Else:
   a. Display " Counseling required - Contact academic advisor"
```

**Decision Logic:**
- [ ] Multi-criteria academic evaluation
- [ ] Honors program eligibility
- [ ] Class standing determination
- [ ] Academic intervention triggers

**Your Task:** Build an academic standing assessment system.

---

## Algorithm 4: Insurance Premium Calculator

**Pseudocode:**
```
Algorithm: Calculate Insurance Premium
1. Display "=== Auto Insurance Premium Calculator ==="
2. Display "Enter driver's age: "
3. Get age from user
4. Display "Enter years of driving experience: "
5. Get experience from user
6. Display "Enter vehicle type (sedan/suv/truck/sports): "
7. Get vehicle_type from user
8. Display "Any accidents in last 3 years? (yes/no): "
9. Get accident_history from user
10. Display "Annual mileage: "
11. Get mileage from user
12. Initialize base_premium to 500
13. Initialize risk_multiplier to 1.0
14. If age < 25:
   a. Set risk_multiplier to risk_multiplier × 1.5
15. Else if age > 65:
   a. Set risk_multiplier to risk_multiplier × 1.2
16. If experience < 3:
   a. Set risk_multiplier to risk_multiplier × 1.4
17. Else if experience > 10:
   a. Set risk_multiplier to risk_multiplier × 0.9
18. If vehicle_type is "sports":
   a. Set risk_multiplier to risk_multiplier × 1.8
19. Else if vehicle_type is "suv":
   a. Set risk_multiplier to risk_multiplier × 1.3
20. Else if vehicle_type is "truck":
   a. Set risk_multiplier to risk_multiplier × 1.1
21. If accident_history is "yes":
   a. Set risk_multiplier to risk_multiplier × 1.6
22. If mileage > 15000:
   a. Set risk_multiplier to risk_multiplier × 1.2
23. Else if mileage < 5000:
   a. Set risk_multiplier to risk_multiplier × 0.95
24. Calculate final_premium = base_premium × risk_multiplier
25. Display "=== Premium Calculation ==="
26. Display "Driver Age: " + age
27. Display "Driving Experience: " + experience + " years"
28. Display "Vehicle Type: " + vehicle_type
29. Display "Accident History: " + accident_history
30. Display "Annual Mileage: " + mileage
31. Display "Base Premium: $" + base_premium
32. Display "Risk Multiplier: " + risk_multiplier
33. Display "Final Premium: $" + final_premium
34. If risk_multiplier > 2.0:
   a. Display " HIGH RISK PROFILE"
   b. Display "Consider defensive driving courses"
35. Else if risk_multiplier > 1.5:
   a. Display " MODERATE RISK PROFILE"
   b. Display "Safe driving discount may apply"
36. Else:
   a. Display " LOW RISK PROFILE"
   b. Display "Eligible for premium discounts"
```

**Decision Logic:**
- [ ] Multi-factor risk assessment
- [ ] Cumulative risk multipliers
- [ ] Vehicle type categorization
- [ ] Experience-based adjustments

**Your Task:** Create an insurance premium calculator.

---

## Algorithm 5: Travel Itinerary Planner

**Pseudocode:**
```
Algorithm: Plan Travel Itinerary
1. Display "=== Travel Itinerary Planner ==="
2. Display "Enter destination city: "
3. Get destination from user
4. Display "Enter trip duration in days: "
5. Get trip_days from user
6. Display "Enter budget per day: $"
7. Get daily_budget from user
8. Display "Travel season (spring/summer/fall/winter): "
9. Get season from user
10. Display "Group size: "
11. Get group_size from user
12. Initialize total_cost to 0
13. Initialize activity_count to 0
14. If season is "summer":
   a. If destination is "beach":
      i. Display " Beach activities recommended"
      ii. Add 50 to total_cost per day
      iii. Set activity_count to 5
   b. Else:
      i. Display " Mountain activities recommended"
      ii. Add 40 to total_cost per day
      iii. Set activity_count to 4
15. Else if season is "winter":
   a. If destination is "mountain":
      i. Display " Skiing activities recommended"
      ii. Add 80 to total_cost per day
      iii. Set activity_count to 3
   b. Else:
      i. Display " Cultural activities recommended"
      ii. Add 30 to total_cost per day
      iii. Set activity_count to 4
16. Else:
   a. Display " Outdoor activities recommended"
   b. Add 35 to total_cost per day
   c. Set activity_count to 4
17. Calculate accommodation_cost = daily_budget × 0.4 × trip_days
18. Calculate food_cost = daily_budget × 0.3 × trip_days
19. Calculate activity_cost = total_cost × trip_days
20. Calculate transportation_cost = daily_budget × 0.2 × trip_days
21. Calculate miscellaneous_cost = daily_budget × 0.1 × trip_days
22. Calculate total_budget = accommodation_cost + food_cost + activity_cost + transportation_cost + miscellaneous_cost
23. If group_size > 4:
   a. Calculate group_discount = total_budget × 0.1
   b. Subtract group_discount from total_budget
   c. Display " Group discount applied: $" + group_discount
24. Display "=== Travel Itinerary ==="
25. Display "Destination: " + destination
26. Display "Duration: " + trip_days + " days"
27. Display "Season: " + season
28. Display "Group Size: " + group_size
29. Display "Daily Budget: $" + daily_budget
30. Display "=== Cost Breakdown ==="
31. Display "Accommodation: $" + accommodation_cost
32. Display "Food: $" + food_cost
33. Display "Activities: $" + activity_cost + " (" + activity_count + " per day)"
34. Display "Transportation: $" + transportation_cost
35. Display "Miscellaneous: $" + miscellaneous_cost
36. Display "Total Estimated Cost: $" + total_budget
37. If total_budget > daily_budget × trip_days:
   a. Display " Budget exceeded by $" + (total_budget - daily_budget × trip_days)
38. Else:
   a. Display " Within budget - $" + (daily_budget × trip_days - total_budget) + " remaining"
```

**Decision Logic:**
- [ ] Seasonal activity recommendations
- [ ] Destination-based planning
- [ ] Budget allocation percentages
- [ ] Group discount calculations

**Your Task:** Build a travel itinerary planning system.

---

## Algorithm 6: Employee Performance Review

**Pseudocode:**
```
Algorithm: Evaluate Employee Performance
1. Display "=== Employee Performance Review ==="
2. Display "Enter employee name: "
3. Get employee_name from user
4. Display "Enter years of service: "
5. Get years_service from user
6. Display "Enter productivity score (1-10): "
7. Get productivity from user
8. Display "Enter quality score (1-10): "
9. Get quality from user
10. Display "Enter teamwork score (1-10): "
11. Get teamwork from user
12. Display "Any disciplinary actions? (yes/no): "
13. Get disciplinary_status from user
14. Calculate average_score = (productivity + quality + teamwork) ÷ 3
15. Initialize performance_rating to "UNDETERMINED"
16. Initialize salary_adjustment to 0
17. If disciplinary_status is "yes":
   a. Set performance_rating to "UNSATISFACTORY"
   b. Set salary_adjustment to -5
18. Else:
   a. If average_score >= 9.0:
      i. If years_service >= 5:
         i. Set performance_rating to "OUTSTANDING"
         ii. Set salary_adjustment to 15
      ii. Else:
         i. Set performance_rating to "EXCELLENT"
         ii. Set salary_adjustment to 12
   b. Else if average_score >= 8.0:
      i. Set performance_rating to "VERY GOOD"
      ii. Set salary_adjustment to 8
   c. Else if average_score >= 7.0:
      i. Set performance_rating to "GOOD"
      ii. Set salary_adjustment to 5
   d. Else if average_score >= 6.0:
      i. Set performance_rating to "SATISFACTORY"
      ii. Set salary_adjustment to 2
   e. Else:
      i. Set performance_rating to "NEEDS IMPROVEMENT"
      ii. Set salary_adjustment to 0
19. Display "=== Performance Review Results ==="
20. Display "Employee: " + employee_name
21. Display "Years of Service: " + years_service
22. Display "Productivity Score: " + productivity + "/10"
23. Display "Quality Score: " + quality + "/10"
24. Display "Teamwork Score: " + teamwork + "/10"
25. Display "Average Score: " + average_score + "/10"
26. Display "Disciplinary Actions: " + disciplinary_status
27. Display "Performance Rating: " + performance_rating
28. Display "Salary Adjustment: " + salary_adjustment + "%"
29. If performance_rating equals "OUTSTANDING":
   a. Display " EMPLOYEE OF THE YEAR CANDIDATE"
   b. Display "Eligible for bonus and promotion consideration"
30. Else if performance_rating equals "UNSATISFACTORY":
   a. Display " PERFORMANCE IMPROVEMENT PLAN REQUIRED"
   b. Display "Mandatory counseling and training"
31. Else:
   a. Display " Performance review complete"
   b. Display "Continue professional development"
```

**Decision Logic:**
- [ ] Multi-criteria performance evaluation
- [ ] Disciplinary action overrides
- [ ] Experience-based rating adjustments
- [ ] Salary adjustment calculations

**Your Task:** Create an employee performance evaluation system.

---

### Decision Tree Patterns

**Eligibility Checking:**
```
If primary_condition AND secondary_condition:
    If qualifying_factor:
        APPROVE
    Else:
        DENY
Else:
    DENY
```

**Risk Assessment:**
```
Initialize risk_score = 0
For each risk_factor:
    If factor_present:
        Add points to risk_score
Categorize based on total_score
```

**Multi-tier Classification:**
```
If score >= threshold_A:
    If sub_condition:
        CATEGORY_A_PLUS
    Else:
        CATEGORY_A
Else if score >= threshold_B:
    CATEGORY_B
Else:
    CATEGORY_C
```

---

### Success Checklist

**For Each Algorithm:**
- [ ] Implemented complex nested conditional logic
- [ ] Handled multiple decision criteria
- [ ] Used appropriate data types and calculations
- [ ] Provided clear decision outcomes
- [ ] Included comprehensive result displays

**Decision Logic:**
- [ ] Created multi-level decision trees
- [ ] Handled edge cases and special conditions
- [ ] Used logical operators effectively (&&, ||)
- [ ] Implemented rule-based systems

---

### Try This (Optional Challenges)

1. **Add More Criteria**: Include additional factors in decision making
2. **Create Decision Tables**: Document the logic in table format
3. **Add Validation**: Ensure all inputs are within valid ranges
4. **Export Results**: Save decision outcomes to files

---

## Advanced Decision Patterns

### State Machine Implementation
```c
typedef enum {
    STATE_INITIAL,
    STATE_PROCESSING,
    STATE_APPROVED,
    STATE_DENIED,
    STATE_PENDING
} ApplicationState;

ApplicationState evaluate_application(ApplicationData data) {
    if (data.age < 18) return STATE_DENIED;
    if (data.score < 500) return STATE_PENDING;
    if (data.income > 50000 && data.score > 700) return STATE_APPROVED;
    return STATE_PROCESSING;
}
```

### Rule Engine Pattern
```c
int evaluate_rules(DataItem item, Rule* rules, int rule_count) {
    int score = 0;
    for (int i = 0; i < rule_count; i++) {
        if (matches_rule(item, rules[i])) {
            score += rules[i].weight;
        }
    }
    return score;
}
```

### Decision Table Pattern
```c
// Decision table for loan approval
// Age | Income | Credit | Decision
// <25 | Any    | Any    | Deny
// >=25| <30k   | <600   | Deny
// >=25| >=30k  | >=600  | Approve
// >=25| <30k   | >=600  | Review
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Loan Approval System

```c
#include <stdio.h>

int main() {
    int age, credit_score;
    float income, loan_amount;
    char approval_status[50] = "PENDING";
    float max_loan_amount = 0.0;
    
    printf("=== Loan Approval System ===\n");
    printf("Enter applicant's age: ");
    scanf("%d", &age);
    printf("Enter annual income: $");
    scanf("%f", &income);
    printf("Enter credit score (300-850): ");
    scanf("%d", &credit_score);
    printf("Enter loan amount requested: $");
    scanf("%f", &loan_amount);
    
    if (age < 18) {
        strcpy(approval_status, "DENIED - Underage");
    } else if (age > 70) {
        strcpy(approval_status, "DENIED - Age limit exceeded");
    } else {
        if (credit_score < 300 || credit_score > 850) {
            strcpy(approval_status, "DENIED - Invalid credit score");
        } else {
            if (credit_score >= 750) {
                max_loan_amount = income * 5;
            } else if (credit_score >= 650) {
                max_loan_amount = income * 3;
            } else if (credit_score >= 550) {
                max_loan_amount = income * 2;
            } else {
                max_loan_amount = income * 1;
            }
            
            if (loan_amount > max_loan_amount) {
                strcpy(approval_status, "DENIED - Loan amount exceeds limit");
            } else if (loan_amount > income * 0.5) {
                strcpy(approval_status, "REQUIRES MANAGER APPROVAL");
            } else {
                strcpy(approval_status, "APPROVED");
            }
        }
    }
    
    printf("\n=== Loan Decision ===\n");
    printf("Applicant age: %d\n", age);
    printf("Annual income: $%.2f\n", income);
    printf("Credit score: %d\n", credit_score);
    printf("Loan requested: $%.2f\n", loan_amount);
    
    if (strcmp(approval_status, "APPROVED") == 0) {
        printf(" LOAN APPROVED!\n");
        printf("Maximum approved amount: $%.2f\n", max_loan_amount);
    } else if (strcmp(approval_status, "REQUIRES MANAGER APPROVAL") == 0) {
        printf(" REQUIRES MANAGER APPROVAL\n");
        printf("Reason: High loan-to-income ratio\n");
    } else {
        printf(" LOAN DENIED\n");
        printf("Reason: %s\n", approval_status);
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] Complex nested conditional logic
- [ ] String manipulation for status messages
- [ ] Multi-tier approval criteria
- [ ] Financial ratio calculations

---

### Algorithm 2: Health Risk Assessment

```c
#include <stdio.h>
# include <string.h>

int main() {
    int age, risk_points = 0;
    float bmi;
    char smoking_status[10], exercise_status[10], family_history[10];
    char risk_level[20] = "LOW";
    
    printf("=== Health Risk Assessment ===\n");
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Enter your BMI: ");
    scanf("%f", &bmi);
    printf("Do you smoke? (yes/no): ");
    scanf("%s", smoking_status);
    printf("Do you exercise regularly? (yes/no): ");
    scanf("%s", exercise_status);
    printf("Family history of heart disease? (yes/no): ");
    scanf("%s", family_history);
    
    // Age risk
    if (age >= 65) risk_points += 3;
    else if (age >= 45) risk_points += 2;
    else if (age >= 30) risk_points += 1;
    
    // BMI risk
    if (bmi >= 30) risk_points += 3;
    else if (bmi >= 25) risk_points += 2;
    else if (bmi >= 23) risk_points += 1;
    
    // Lifestyle risk
    if (strcmp(smoking_status, "yes") == 0) risk_points += 3;
    if (strcmp(exercise_status, "no") == 0) risk_points += 2;
    if (strcmp(family_history, "yes") == 0) risk_points += 2;
    
    // Determine risk level
    if (risk_points >= 8) strcpy(risk_level, "HIGH");
    else if (risk_points >= 5) strcpy(risk_level, "MODERATE");
    else if (risk_points >= 3) strcpy(risk_level, "ELEVATED");
    
    printf("\n=== Health Risk Assessment Results ===\n");
    printf("Age: %d years\n", age);
    printf("BMI: %.1f\n", bmi);
    printf("Smoking: %s\n", smoking_status);
    printf("Exercise: %s\n", exercise_status);
    printf("Family history: %s\n", family_history);
    printf("Risk points: %d/12\n", risk_points);
    printf("Risk level: %s\n", risk_level);
    
    if (strcmp(risk_level, "HIGH") == 0) {
        printf(" HIGH RISK - Consult doctor immediately\n");
        printf("Recommendations: Lifestyle changes, medical evaluation\n");
    } else if (strcmp(risk_level, "MODERATE") == 0) {
        printf(" MODERATE RISK - Monitor health closely\n");
        printf("Recommendations: Improve diet, start exercising\n");
    } else if (strcmp(risk_level, "ELEVATED") == 0) {
        printf(" ELEVATED RISK - Take preventive measures\n");
        printf("Recommendations: Regular check-ups, healthy habits\n");
    } else {
        printf(" LOW RISK - Maintain healthy lifestyle\n");
        printf("Recommendations: Continue current healthy habits\n");
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] Point-based risk assessment system
- [ ] Multiple risk factor evaluation
- [ ] Categorical risk level determination
- [ ] Personalized health recommendations

---

### Algorithm 3: Academic Standing Calculator

```c
#include <stdio.h>
# include <string.h>

int main() {
    float gpa;
    int credit_hours, semesters;
    char probation_status[10];
    char standing[50] = "UNDETERMINED";
    char eligibility_status[30] = "ELIGIBLE";
    
    printf("=== Academic Standing Calculator ===\n");
    printf("Enter GPA (0.0-4.0): ");
    scanf("%f", &gpa);
    printf("Enter total credit hours completed: ");
    scanf("%d", &credit_hours);
    printf("Enter number of semesters completed: ");
    scanf("%d", &semesters);
    printf("Any academic probation? (yes/no): ");
    scanf("%s", probation_status);
    
    if (strcmp(probation_status, "yes") == 0) {
        strcpy(standing, "ACADEMIC PROBATION");
        strcpy(eligibility_status, "RESTRICTED");
    } else {
        if (gpa >= 3.75 && credit_hours >= 60) {
            strcpy(standing, "SUMMA CUM LAUDE CANDIDATE");
        } else if (gpa >= 3.5 && credit_hours >= 45) {
            strcpy(standing, "MAGNA CUM LAUDE CANDIDATE");
        } else if (gpa >= 3.25 && credit_hours >= 30) {
            strcpy(standing, "CUM LAUDE CANDIDATE");
        } else if (gpa >= 3.0) {
            if (credit_hours >= 90) {
                strcpy(standing, "GOOD STANDING - NEAR GRADUATION");
            } else if (credit_hours >= 60) {
                strcpy(standing, "GOOD STANDING - JUNIOR");
            } else if (credit_hours >= 30) {
                strcpy(standing, "GOOD STANDING - SOPHOMORE");
            } else {
                strcpy(standing, "GOOD STANDING - FRESHMAN");
            }
        } else if (gpa >= 2.0) {
            strcpy(standing, "SATISFACTORY STANDING");
        } else {
            strcpy(standing, "ACADEMIC WARNING");
            strcpy(eligibility_status, "COUNSELING REQUIRED");
        }
    }
    
    printf("\n=== Academic Assessment ===\n");
    printf("GPA: %.2f\n", gpa);
    printf("Credit Hours: %d\n", credit_hours);
    printf("Semesters: %d\n", semesters);
    printf("Probation Status: %s\n", probation_status);
    printf("Academic Standing: %s\n", standing);
    printf("Eligibility Status: %s\n", eligibility_status);
    
    if (strcmp(eligibility_status, "ELIGIBLE") == 0) {
        printf(" Eligible for all academic activities\n");
    } else if (strcmp(eligibility_status, "RESTRICTED") == 0) {
        printf(" Limited eligibility - Academic plan required\n");
    } else {
        printf(" Counseling required - Contact academic advisor\n");
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] Multi-criteria academic evaluation
- [ ] Honors program eligibility logic
- [ ] Academic intervention triggers
- [ ] Status-based eligibility determination

---

### Algorithm 4: Insurance Premium Calculator

```c
#include <stdio.h>
# include <string.h>

int main() {
    int age, experience, mileage;
    char vehicle_type[20], accident_history[10];
    float base_premium = 500.0, risk_multiplier = 1.0, final_premium;
    
    printf("=== Auto Insurance Premium Calculator ===\n");
    printf("Enter driver's age: ");
    scanf("%d", &age);
    printf("Enter years of driving experience: ");
    scanf("%d", &experience);
    printf("Enter vehicle type (sedan/suv/truck/sports): ");
    scanf("%s", vehicle_type);
    printf("Any accidents in last 3 years? (yes/no): ");
    scanf("%s", accident_history);
    printf("Annual mileage: ");
    scanf("%d", &mileage);
    
    // Age risk
    if (age < 25) risk_multiplier *= 1.5;
    else if (age > 65) risk_multiplier *= 1.2;
    
    // Experience risk
    if (experience < 3) risk_multiplier *= 1.4;
    else if (experience > 10) risk_multiplier *= 0.9;
    
    // Vehicle type risk
    if (strcmp(vehicle_type, "sports") == 0) risk_multiplier *= 1.8;
    else if (strcmp(vehicle_type, "suv") == 0) risk_multiplier *= 1.3;
    else if (strcmp(vehicle_type, "truck") == 0) risk_multiplier *= 1.1;
    
    // Accident history
    if (strcmp(accident_history, "yes") == 0) risk_multiplier *= 1.6;
    
    // Mileage risk
    if (mileage > 15000) risk_multiplier *= 1.2;
    else if (mileage < 5000) risk_multiplier *= 0.95;
    
    final_premium = base_premium * risk_multiplier;
    
    printf("\n=== Premium Calculation ===\n");
    printf("Driver Age: %d\n", age);
    printf("Driving Experience: %d years\n", experience);
    printf("Vehicle Type: %s\n", vehicle_type);
    printf("Accident History: %s\n", accident_history);
    printf("Annual Mileage: %d\n", mileage);
    printf("Base Premium: $%.2f\n", base_premium);
    printf("Risk Multiplier: %.2f\n", risk_multiplier);
    printf("Final Premium: $%.2f\n", final_premium);
    
    if (risk_multiplier > 2.0) {
        printf(" HIGH RISK PROFILE\n");
        printf("Consider defensive driving courses\n");
    } else if (risk_multiplier > 1.5) {
        printf(" MODERATE RISK PROFILE\n");
        printf("Safe driving discount may apply\n");
    } else {
        printf(" LOW RISK PROFILE\n");
        printf("Eligible for premium discounts\n");
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] Cumulative risk multiplier system
- [ ] Multi-factor insurance rating
- [ ] Vehicle type categorization
- [ ] Risk profile assessment

---

### Algorithm 5: Travel Itinerary Planner

```c
#include <stdio.h>
# include <string.h>

int main() {
    char destination[50], season[20];
    int trip_days, group_size, activity_count = 0;
    float daily_budget, total_cost = 0.0;
    float accommodation_cost, food_cost, activity_cost, transportation_cost, miscellaneous_cost, total_budget;
    
    printf("=== Travel Itinerary Planner ===\n");
    printf("Enter destination city: ");
    scanf("%s", destination);
    printf("Enter trip duration in days: ");
    scanf("%d", &trip_days);
    printf("Enter budget per day: $");
    scanf("%f", &daily_budget);
    printf("Travel season (spring/summer/fall/winter): ");
    scanf("%s", season);
    printf("Group size: ");
    scanf("%d", &group_size);
    
    // Seasonal activity planning
    if (strcmp(season, "summer") == 0) {
        if (strstr(destination, "beach") != NULL || strstr(destination, "Beach") != NULL) {
            printf(" Beach activities recommended\n");
            total_cost += 50;
            activity_count = 5;
        } else {
            printf(" Mountain activities recommended\n");
            total_cost += 40;
            activity_count = 4;
        }
    } else if (strcmp(season, "winter") == 0) {
        if (strstr(destination, "mountain") != NULL || strstr(destination, "Mountain") != NULL) {
            printf(" Skiing activities recommended\n");
            total_cost += 80;
            activity_count = 3;
        } else {
            printf(" Cultural activities recommended\n");
            total_cost += 30;
            activity_count = 4;
        }
    } else {
        printf(" Outdoor activities recommended\n");
        total_cost += 35;
        activity_count = 4;
    }
    
    // Cost calculations
    accommodation_cost = daily_budget * 0.4 * trip_days;
    food_cost = daily_budget * 0.3 * trip_days;
    activity_cost = total_cost * trip_days;
    transportation_cost = daily_budget * 0.2 * trip_days;
    miscellaneous_cost = daily_budget * 0.1 * trip_days;
    total_budget = accommodation_cost + food_cost + activity_cost + transportation_cost + miscellaneous_cost;
    
    // Group discount
    if (group_size > 4) {
        float group_discount = total_budget * 0.1;
        total_budget -= group_discount;
        printf(" Group discount applied: $%.2f\n", group_discount);
    }
    
    printf("\n=== Travel Itinerary ===\n");
    printf("Destination: %s\n", destination);
    printf("Duration: %d days\n", trip_days);
    printf("Season: %s\n", season);
    printf("Group Size: %d\n", group_size);
    printf("Daily Budget: $%.2f\n", daily_budget);
    printf("\n=== Cost Breakdown ===\n");
    printf("Accommodation: $%.2f\n", accommodation_cost);
    printf("Food: $%.2f\n", food_cost);
    printf("Activities: $%.2f (%.0f per day)\n", activity_cost, total_cost);
    printf("Transportation: $%.2f\n", transportation_cost);
    printf("Miscellaneous: $%.2f\n", miscellaneous_cost);
    printf("Total Estimated Cost: $%.2f\n", total_budget);
    
    float budget_limit = daily_budget * trip_days;
    if (total_budget > budget_limit) {
        printf(" Budget exceeded by $%.2f\n", total_budget - budget_limit);
    } else {
        printf(" Within budget - $%.2f remaining\n", budget_limit - total_budget);
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] Seasonal activity recommendations
- [ ] Budget allocation by percentages
- [ ] Destination-based planning logic
- [ ] Group discount calculations

---

### Algorithm 6: Employee Performance Review

```c
#include <stdio.h>
# include <string.h>

int main() {
    char employee_name[50], disciplinary_status[10];
    int years_service, productivity, quality, teamwork;
    float average_score, salary_adjustment = 0.0;
    char performance_rating[30] = "UNDETERMINED";
    
    printf("=== Employee Performance Review ===\n");
    printf("Enter employee name: ");
    scanf("%s", employee_name);
    printf("Enter years of service: ");
    scanf("%d", &years_service);
    printf("Enter productivity score (1-10): ");
    scanf("%d", &productivity);
    printf("Enter quality score (1-10): ");
    scanf("%d", &quality);
    printf("Enter teamwork score (1-10): ");
    scanf("%d", &teamwork);
    printf("Any disciplinary actions? (yes/no): ");
    scanf("%s", disciplinary_status);
    
    average_score = (productivity + quality + teamwork) / 3.0;
    
    if (strcmp(disciplinary_status, "yes") == 0) {
        strcpy(performance_rating, "UNSATISFACTORY");
        salary_adjustment = -5.0;
    } else {
        if (average_score >= 9.0) {
            if (years_service >= 5) {
                strcpy(performance_rating, "OUTSTANDING");
                salary_adjustment = 15.0;
            } else {
                strcpy(performance_rating, "EXCELLENT");
                salary_adjustment = 12.0;
            }
        } else if (average_score >= 8.0) {
            strcpy(performance_rating, "VERY GOOD");
            salary_adjustment = 8.0;
        } else if (average_score >= 7.0) {
            strcpy(performance_rating, "GOOD");
            salary_adjustment = 5.0;
        } else if (average_score >= 6.0) {
            strcpy(performance_rating, "SATISFACTORY");
            salary_adjustment = 2.0;
        } else {
            strcpy(performance_rating, "NEEDS IMPROVEMENT");
            salary_adjustment = 0.0;
        }
    }
    
    printf("\n=== Performance Review Results ===\n");
    printf("Employee: %s\n", employee_name);
    printf("Years of Service: %d\n", years_service);
    printf("Productivity Score: %d/10\n", productivity);
    printf("Quality Score: %d/10\n", quality);
    printf("Teamwork Score: %d/10\n", teamwork);
    printf("Average Score: %.1f/10\n", average_score);
    printf("Disciplinary Actions: %s\n", disciplinary_status);
    printf("Performance Rating: %s\n", performance_rating);
    printf("Salary Adjustment: %.1f%%\n", salary_adjustment);
    
    if (strcmp(performance_rating, "OUTSTANDING") == 0) {
        printf(" EMPLOYEE OF THE YEAR CANDIDATE\n");
        printf("Eligible for bonus and promotion consideration\n");
    } else if (strcmp(performance_rating, "UNSATISFACTORY") == 0) {
        printf(" PERFORMANCE IMPROVEMENT PLAN REQUIRED\n");
        printf("Mandatory counseling and training\n");
    } else {
        printf(" Performance review complete\n");
        printf("Continue professional development\n");
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] Multi-criteria performance evaluation
- [ ] Disciplinary action override logic
- [ ] Experience-based rating adjustments
- [ ] Salary adjustment calculations

---

### Decision Logic Best Practices

**Readable Conditions:**
```c
// Good - clear and readable
if (age >= 18 && age <= 65 && income > 30000) {
    // approve
}

// Bad - confusing
if (age >= 18) {
    if (age <= 65) {
        if (income > 30000) {
            // approve
        }
    }
}
```

**Consistent Structure:**
```c
// Use consistent patterns
if (condition1) {
    // handle case 1
} else if (condition2) {
    // handle case 2
} else {
    // handle default case
}
```

**Early Returns:**
```c
// Good - fail fast
if (invalid_input) {
    printf("Error: Invalid input\n");
    return;
}
// continue with valid input
```

---

 **Brilliant! You've mastered complex decision-making in code!** 

*Programs can now make intelligent decisions like real applications. Next: Loop algorithms in pseudocode! *

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


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```
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
