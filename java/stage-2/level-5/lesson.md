# Level 5: Decision Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Decision-making is the intelligence of programs! Today you'll master complex conditional logic, nested decisions, and rule-based systems. You'll learn to translate sophisticated decision trees from pseudocode into robust Java code.

---

### Learning Goals

- Implement complex conditional logic
- Create nested decision structures
- Handle multiple condition combinations
- Build rule-based decision systems
- Design decision trees and flowcharts
- Create intelligent program behavior

---

### Decision-Making in Programming

**Types of Decisions:**
1. **Binary Decisions**: Yes/No, True/False
2. **Multi-way Decisions**: Multiple choices (if-else-if chains)
3. **Nested Decisions**: Decisions within decisions
4. **Rule-Based Systems**: Complex business logic
5. **State Machines**: Decisions based on current state

**Decision Patterns:**
- **Eligibility Checking**: Age, income, qualifications
- **Categorization**: Grading, risk assessment, classification
- **Business Rules**: Discounts, pricing, policies
- **Validation**: Input checking, data verification

---

### Your Task

**Translate each decision-based pseudocode algorithm into working Java code.**

---


### How to Compile and Run

1. **Compile the code**:
   ```bash
   javac hello.java
   ```

2. **Run your program**:
   ```bash
   java hello
   ```

**Expected output:**
```java
Hello, World!
```java

## Algorithm 1: Loan Approval System

**Pseudocode:**
```java
Algorithm: Evaluate Loan Application
1. Display "=== Loan Approval System ==="
2. Display "Enter applicant's age: "
3. Get age from user
4. Display "Enter annual income: $"
5. Get income from user
6. Display "Enter credit score (300-850): "
7. Get creditScore from user
8. Display "Enter loan amount requested: $"
9. Get loanAmount from user
10. Initialize approvalStatus to "PENDING"
11. Initialize maxLoanAmount to 0
12. If age < 18:
   a. Set approvalStatus to "DENIED - Underage"
13. Else if age > 70:
   a. Set approvalStatus to "DENIED - Age limit exceeded"
14. Else:
   a. If creditScore < 300 or creditScore > 850:
      i. Set approvalStatus to "DENIED - Invalid credit score"
   b. Else:
      i. If creditScore >= 750:
         i. Set maxLoanAmount to income × 5
      ii. Else if creditScore >= 650:
         i. Set maxLoanAmount to income × 3
      iii. Else if creditScore >= 550:
         i. Set maxLoanAmount to income × 2
      iv. Else:
         i. Set maxLoanAmount to income × 1
      v. If loanAmount > maxLoanAmount:
         i. Set approvalStatus to "DENIED - Loan amount exceeds limit"
      vi. Else if loanAmount > income × 0.5:
         i. Set approvalStatus to "REQUIRES MANAGER APPROVAL"
      vii. Else:
         i. Set approvalStatus to "APPROVED"
15. Display "=== Loan Decision ==="
16. Display "Applicant age: " + age
17. Display "Annual income: $" + income
18. Display "Credit score: " + creditScore
19. Display "Loan requested: $" + loanAmount
20. If approvalStatus equals "APPROVED":
   a. Display " LOAN APPROVED!"
   b. Display "Maximum approved amount: $" + maxLoanAmount
21. Else if approvalStatus equals "REQUIRES MANAGER APPROVAL":
   a. Display " REQUIRES MANAGER APPROVAL"
   b. Display "Reason: High loan-to-income ratio"
22. Else:
   a. Display " LOAN DENIED"
   b. Display "Reason: " + approvalStatus
```java

**Decision Logic:**
- Age restrictions (18-70)
- Credit score validation and tiering
- Income-based loan limits
- Loan-to-income ratio checks
- Multi-level approval process

**Your Task:** Build a comprehensive loan approval system.

---

## Algorithm 2: Health Risk Assessment

**Pseudocode:**
```java
Algorithm: Assess Health Risk Factors
1. Display "=== Health Risk Assessment ==="
2. Display "Enter your age: "
3. Get age from user
4. Display "Enter your BMI: "
5. Get bmi from user
6. Display "Do you smoke? (yes/no): "
7. Get smokingStatus from user
8. Display "Do you exercise regularly? (yes/no): "
9. Get exerciseStatus from user
10. Display "Family history of heart disease? (yes/no): "
11. Get familyHistory from user
12. Initialize riskLevel to "LOW"
13. Initialize riskPoints to 0
14. If age >= 65:
   a. Add 3 to riskPoints
15. Else if age >= 45:
   a. Add 2 to riskPoints
16. Else if age >= 30:
   a. Add 1 to riskPoints
17. If bmi >= 30:
   a. Add 3 to riskPoints
18. Else if bmi >= 25:
   a. Add 2 to riskPoints
19. Else if bmi >= 23:
   a. Add 1 to riskPoints
20. If smokingStatus is "yes":
   a. Add 3 to riskPoints
21. If exerciseStatus is "no":
   a. Add 2 to riskPoints
22. If familyHistory is "yes":
   a. Add 2 to riskPoints
23. If riskPoints >= 8:
   a. Set riskLevel to "HIGH"
24. Else if riskPoints >= 5:
   a. Set riskLevel to "MODERATE"
25. Else if riskPoints >= 3:
   a. Set riskLevel to "ELEVATED"
26. Display "=== Health Risk Assessment Results ==="
27. Display "Age: " + age + " years"
28. Display "BMI: " + bmi
29. Display "Smoking: " + smokingStatus
30. Display "Exercise: " + exerciseStatus
31. Display "Family history: " + familyHistory
32. Display "Risk points: " + riskPoints + "/12"
33. Display "Risk level: " + riskLevel
34. If riskLevel equals "HIGH":
   a. Display " HIGH RISK - Consult doctor immediately"
   b. Display "Recommendations: Lifestyle changes, medical evaluation"
35. Else if riskLevel equals "MODERATE":
   a. Display " MODERATE RISK - Monitor health closely"
   b. Display "Recommendations: Improve diet, start exercising"
36. Else if riskLevel equals "ELEVATED":
   a. Display "�� ELEVATED RISK - Take preventive measures"
   b. Display "Recommendations: Regular check-ups, healthy habits"
37. Else:
   a. Display " LOW RISK - Maintain healthy lifestyle"
   b. Display "Recommendations: Continue current healthy habits"
```java

**Decision Logic:**
- Multi-factor risk assessment
- Point-based scoring system
- Categorical risk levels
- Personalized recommendations

**Your Task:** Create a health risk assessment tool.

---

## Algorithm 3: Academic Standing Calculator

**Pseudocode:**
```java
Algorithm: Determine Academic Standing
1. Display "=== Academic Standing Calculator ==="
2. Display "Enter GPA (0.0-4.0): "
3. Get gpa from user
4. Display "Enter total credit hours completed: "
5. Get creditHours from user
6. Display "Enter number of semesters completed: "
7. Get semesters from user
8. Display "Any academic probation? (yes/no): "
9. Get probationStatus from user
10. Initialize standing to "UNDETERMINED"
11. Initialize eligibilityStatus to "ELIGIBLE"
12. If probationStatus is "yes":
   a. Set standing to "ACADEMIC PROBATION"
   b. Set eligibilityStatus to "RESTRICTED"
13. Else:
   a. If gpa >= 3.75 and creditHours >= 60:
      i. Set standing to "SUMMA CUM LAUDE CANDIDATE"
   b. Else if gpa >= 3.5 and creditHours >= 45:
      i. Set standing to "MAGNA CUM LAUDE CANDIDATE"
   c. Else if gpa >= 3.25 and creditHours >= 30:
      i. Set standing to "CUM LAUDE CANDIDATE"
   d. Else if gpa >= 3.0:
      i. If creditHours >= 90:
         i. Set standing to "GOOD STANDING - NEAR GRADUATION"
      ii. Else if creditHours >= 60:
         i. Set standing to "GOOD STANDING - JUNIOR"
      iii. Else if creditHours >= 30:
         i. Set standing to "GOOD STANDING - SOPHOMORE"
      iv. Else:
         i. Set standing to "GOOD STANDING - FRESHMAN"
   e. Else if gpa >= 2.0:
      i. Set standing to "SATISFACTORY STANDING"
   f. Else:
      i. Set standing to "ACADEMIC WARNING"
      ii. Set eligibilityStatus to "COUNSELING REQUIRED"
14. Display "=== Academic Assessment ==="
15. Display "GPA: " + gpa
16. Display "Credit Hours: " + creditHours
17. Display "Semesters: " + semesters
18. Display "Probation Status: " + probationStatus
19. Display "Academic Standing: " + standing
20. Display "Eligibility Status: " + eligibilityStatus
21. If eligibilityStatus equals "ELIGIBLE":
   a. Display " Eligible for all academic activities"
22. Else if eligibilityStatus equals "RESTRICTED":
   a. Display " Limited eligibility - Academic plan required"
23. Else:
   a. Display " Counseling required - Contact academic advisor"
```java

**Decision Logic:**
- Multi-criteria academic evaluation
- Honors program eligibility
- Class standing determination
- Academic intervention triggers

**Your Task:** Build an academic standing assessment system.

---

## Algorithm 4: Insurance Premium Calculator

**Pseudocode:**
```java
Algorithm: Calculate Insurance Premium
1. Display "=== Auto Insurance Premium Calculator ==="
2. Display "Enter driver's age: "
3. Get age from user
4. Display "Enter years of driving experience: "
5. Get experience from user
6. Display "Enter vehicle type (sedan/suv/truck/sports): "
7. Get vehicleType from user
8. Display "Any accidents in last 3 years? (yes/no): "
9. Get accidentHistory from user
10. Display "Annual mileage: "
11. Get mileage from user
12. Initialize basePremium to 500
13. Initialize riskMultiplier to 1.0
14. If age < 25:
   a. Set riskMultiplier to riskMultiplier × 1.5
15. Else if age > 65:
   a. Set riskMultiplier to riskMultiplier × 1.2
16. If experience < 3:
   a. Set riskMultiplier to riskMultiplier × 1.4
17. Else if experience > 10:
   a. Set riskMultiplier to riskMultiplier × 0.9
18. If vehicleType is "sports":
   a. Set riskMultiplier to riskMultiplier × 1.8
19. Else if vehicleType is "suv":
   a. Set riskMultiplier to riskMultiplier × 1.3
20. Else if vehicleType is "truck":
   a. Set riskMultiplier to riskMultiplier × 1.1
21. If accidentHistory is "yes":
   a. Set riskMultiplier to riskMultiplier × 1.6
22. If mileage > 15000:
   a. Set riskMultiplier to riskMultiplier × 1.2
23. Else if mileage < 5000:
   a. Set riskMultiplier to riskMultiplier × 0.95
24. Calculate finalPremium = basePremium × riskMultiplier
25. Display "=== Premium Calculation ==="
26. Display "Driver Age: " + age
27. Display "Driving Experience: " + experience + " years"
28. Display "Vehicle Type: " + vehicleType
29. Display "Accident History: " + accidentHistory
30. Display "Annual Mileage: " + mileage
31. Display "Base Premium: $" + basePremium
32. Display "Risk Multiplier: " + riskMultiplier
33. Display "Final Premium: $" + finalPremium
34. If riskMultiplier > 2.0:
   a. Display " HIGH RISK PROFILE"
   b. Display "Consider defensive driving courses"
35. Else if riskMultiplier > 1.5:
   a. Display " MODERATE RISK PROFILE"
   b. Display "Safe driving discount may apply"
36. Else:
   a. Display " LOW RISK PROFILE"
   b. Display "Eligible for premium discounts"
```java

**Decision Logic:**
- Multi-factor risk assessment
- Cumulative risk multipliers
- Vehicle type categorization
- Experience-based adjustments

**Your Task:** Create an insurance premium calculator.

---

## Algorithm 5: Travel Itinerary Planner

**Pseudocode:**
```java
Algorithm: Plan Travel Itinerary
1. Display "=== Travel Itinerary Planner ==="
2. Display "Enter destination city: "
3. Get destination from user
4. Display "Enter trip duration in days: "
5. Get tripDays from user
6. Display "Enter budget per day: $"
7. Get dailyBudget from user
8. Display "Travel season (spring/summer/fall/winter): "
9. Get season from user
10. Display "Group size: "
11. Get groupSize from user
12. Initialize totalCost to 0
13. Initialize activityCount to 0
14. If season is "summer":
   a. If destination contains "beach":
      i. Display " Beach activities recommended"
      ii. Add 50 to totalCost per day
      iii. Set activityCount to 5
   b. Else:
      i. Display " Mountain activities recommended"
      ii. Add 40 to totalCost per day
      iii. Set activityCount to 4
15. Else if season is "winter":
   a. If destination contains "mountain":
      i. Display " Skiing activities recommended"
      ii. Add 80 to totalCost per day
      iii. Set activityCount to 3
   b. Else:
      i. Display "�� Cultural activities recommended"
      ii. Add 30 to totalCost per day
      iii. Set activityCount to 4
16. Else:
   a. Display " Outdoor activities recommended"
   b. Add 35 to totalCost per day
   c. Set activityCount to 4
17. Calculate accommodationCost = dailyBudget × 0.4 × tripDays
18. Calculate foodCost = dailyBudget × 0.3 × tripDays
19. Calculate activityCost = totalCost × tripDays
20. Calculate transportationCost = dailyBudget × 0.2 × tripDays
21. Calculate miscellaneousCost = dailyBudget × 0.1 × tripDays
22. Calculate totalBudget = accommodationCost + foodCost + activityCost + transportationCost + miscellaneousCost
23. If groupSize > 4:
   a. Calculate groupDiscount = totalBudget × 0.1
   b. Subtract groupDiscount from totalBudget
   c. Display " Group discount applied: $" + groupDiscount
24. Display "=== Travel Itinerary ==="
25. Display "Destination: " + destination
26. Display "Duration: " + tripDays + " days"
27. Display "Season: " + season
28. Display "Group Size: " + groupSize
29. Display "Daily Budget: $" + dailyBudget
30. Display "=== Cost Breakdown ==="
31. Display "Accommodation: $" + accommodationCost
32. Display "Food: $" + foodCost
33. Display "Activities: $" + activityCost + " (" + activityCount + " per day)"
34. Display "Transportation: $" + transportationCost
35. Display "Miscellaneous: $" + miscellaneousCost
36. Display "Total Estimated Cost: $" + totalBudget
37. If totalBudget > dailyBudget × tripDays:
   a. Display " Budget exceeded by $" + (totalBudget - dailyBudget × tripDays)
38. Else:
   a. Display " Within budget - $" + (dailyBudget × tripDays - totalBudget) + " remaining"
```java

**Decision Logic:**
- Seasonal activity recommendations
- Destination-based planning
- Budget allocation percentages
- Group discount calculations

**Your Task:** Build a travel itinerary planning system.

---

## Algorithm 6: Employee Performance Review

**Pseudocode:**
```java
Algorithm: Evaluate Employee Performance
1. Display "=== Employee Performance Review ==="
2. Display "Enter employee name: "
3. Get employeeName from user
4. Display "Enter years of service: "
5. Get yearsService from user
6. Display "Enter productivity score (1-10): "
7. Get productivity from user
8. Display "Enter quality score (1-10): "
9. Get quality from user
10. Display "Enter teamwork score (1-10): "
11. Get teamwork from user
12. Display "Any disciplinary actions? (yes/no): "
13. Get disciplinaryStatus from user
14. Calculate averageScore = (productivity + quality + teamwork) ÷ 3
15. Initialize performanceRating to "UNDETERMINED"
16. Initialize salaryAdjustment to 0
17. If disciplinaryStatus is "yes":
   a. Set performanceRating to "UNSATISFACTORY"
   b. Set salaryAdjustment to -5
18. Else:
   a. If averageScore >= 9.0:
      i. If yearsService >= 5:
         i. Set performanceRating to "OUTSTANDING"
         ii. Set salaryAdjustment to 15
      ii. Else:
         i. Set performanceRating to "EXCELLENT"
         ii. Set salaryAdjustment to 12
   b. Else if averageScore >= 8.0:
      i. Set performanceRating to "VERY GOOD"
      ii. Set salaryAdjustment to 8
   c. Else if averageScore >= 7.0:
      i. Set performanceRating to "GOOD"
      ii. Set salaryAdjustment to 5
   d. Else if averageScore >= 6.0:
      i. Set performanceRating to "SATISFACTORY"
      ii. Set salaryAdjustment to 2
   e. Else:
      i. Set performanceRating to "NEEDS IMPROVEMENT"
      ii. Set salaryAdjustment to 0
19. Display "=== Performance Review Results ==="
20. Display "Employee: " + employeeName
21. Display "Years of Service: " + yearsService
22. Display "Productivity Score: " + productivity + "/10"
23. Display "Quality Score: " + quality + "/10"
24. Display "Teamwork Score: " + teamwork + "/10"
25. Display "Average Score: " + averageScore + "/10"
26. Display "Disciplinary Actions: " + disciplinaryStatus
27. Display "Performance Rating: " + performanceRating
28. Display "Salary Adjustment: " + salaryAdjustment + "%"
29. If performanceRating equals "OUTSTANDING":
   a. Display " EMPLOYEE OF THE YEAR CANDIDATE"
   b. Display "Eligible for bonus and promotion consideration"
30. Else if performanceRating equals "UNSATISFACTORY":
   a. Display " PERFORMANCE IMPROVEMENT PLAN REQUIRED"
   b. Display "Mandatory counseling and training"
31. Else:
   a. Display " Performance review complete"
   b. Display "Continue professional development"
```java

**Decision Logic:**
- Multi-criteria performance evaluation
- Disciplinary action overrides
- Experience-based rating adjustments
- Salary adjustment calculations

**Your Task:** Create an employee performance evaluation system.

---

### Decision Tree Patterns

**Eligibility Checking:**
```java
If primaryCondition && secondaryCondition:
    If qualifyingFactor:
        APPROVE
    Else:
        DENY
Else:
    DENY
```java

**Risk Assessment:**
```java
Initialize riskScore = 0
For each riskFactor:
    If factorPresent:
        Add points to riskScore
Categorize based on totalScore
```java

**Multi-tier Classification:**
```java
If score >= thresholdA:
    If subCondition:
        CATEGORY_A_PLUS
    Else:
        CATEGORY_A
Else if score >= thresholdB:
    CATEGORY_B
Else:
    CATEGORY_C
```java

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
3. **Add Validation**: Ensure all inputs are within valid ranges with try-catch
4. **Export Results**: Save decision outcomes to files using PrintWriter

---

## Advanced Decision Patterns

### State Machine Concept
```java
enum ApplicationState {
    INITIAL,
    PROCESSING,
    APPROVED,
    DENIED,
    PENDING
}

ApplicationState evaluateApplication(ApplicationData data) {
    if (data.age < 18) return ApplicationState.DENIED;
    if (data.score < 500) return ApplicationState.PENDING;
    if (data.income > 50000 && data.score > 700) return ApplicationState.APPROVED;
    return ApplicationState.PROCESSING;
}
```java

### Rule Engine Pattern
```java
int evaluateRules(DataItem item, Rule[] rules) {
    int score = 0;
    for (Rule rule : rules) {
        if (matchesRule(item, rule)) {
            score += rule.weight;
        }
    }
    return score;
}
```java

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Loan Approval System

```java
import java.util.Scanner;

public class LoanApproval {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int age, creditScore;
        double income, loanAmount;
        String approvalStatus = "PENDING";
        double maxLoanAmount = 0.0;
        
        System.out.println("=== Loan Approval System ===");
        System.out.print("Enter applicant's age: ");
        age = scanner.nextInt();
        System.out.print("Enter annual income: $");
        income = scanner.nextDouble();
        System.out.print("Enter credit score (300-850): ");
        creditScore = scanner.nextInt();
        System.out.print("Enter loan amount requested: $");
        loanAmount = scanner.nextDouble();
        
        if (age < 18) {
            approvalStatus = "DENIED - Underage";
        } else if (age > 70) {
            approvalStatus = "DENIED - Age limit exceeded";
        } else {
            if (creditScore < 300 || creditScore > 850) {
                approvalStatus = "DENIED - Invalid credit score";
            } else {
                if (creditScore >= 750) {
                    maxLoanAmount = income * 5;
                } else if (creditScore >= 650) {
                    maxLoanAmount = income * 3;
                } else if (creditScore >= 550) {
                    maxLoanAmount = income * 2;
                } else {
                    maxLoanAmount = income * 1;
                }
                
                if (loanAmount > maxLoanAmount) {
                    approvalStatus = "DENIED - Loan amount exceeds limit";
                } else if (loanAmount > income * 0.5) {
                    approvalStatus = "REQUIRES MANAGER APPROVAL";
                } else {
                    approvalStatus = "APPROVED";
                }
            }
        }
        
        System.out.println("\n=== Loan Decision ===");
        System.out.println("Applicant age: " + age);
        System.out.printf("Annual income: $%.2f\n", income);
        System.out.println("Credit score: " + creditScore);
        System.out.printf("Loan requested: $%.2f\n", loanAmount);
        
        if (approvalStatus.equals("APPROVED")) {
            System.out.println(" LOAN APPROVED!");
            System.out.printf("Maximum approved amount: $%.2f\n", maxLoanAmount);
        } else if (approvalStatus.equals("REQUIRES MANAGER APPROVAL")) {
            System.out.println(" REQUIRES MANAGER APPROVAL");
            System.out.println("Reason: High loan-to-income ratio");
        } else {
            System.out.println(" LOAN DENIED");
            System.out.println("Reason: " + approvalStatus);
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Complex nested conditional logic
- String variables for status messages (not arrays in Java)
- Multi-tier approval criteria
- Financial ratio calculations with double

**Variable Analysis:**
- `age`, `creditScore` (int): Applicant data
- `income`, `loanAmount`, `maxLoanAmount` (double): Financial data
- `approvalStatus` (String): Approval outcome message

**Java-Specific Notes:**
- Use `String.equals()` for String comparison, not `==`
- Nested if-else can be 3+ levels deep for complex decisions
- double for currency (precision matters)

---

### Algorithm 2: Health Risk Assessment

```java
import java.util.Scanner;

public class HealthRiskAssessment {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int age, riskPoints = 0;
        double bmi;
        String smokingStatus, exerciseStatus, familyHistory;
        String riskLevel = "LOW";
        
        System.out.println("=== Health Risk Assessment ===");
        System.out.print("Enter your age: ");
        age = scanner.nextInt();
        System.out.print("Enter your BMI: ");
        bmi = scanner.nextDouble();
        scanner.nextLine(); // Consume newline
        System.out.print("Do you smoke? (yes/no): ");
        smokingStatus = scanner.nextLine();
        System.out.print("Do you exercise regularly? (yes/no): ");
        exerciseStatus = scanner.nextLine();
        System.out.print("Family history of heart disease? (yes/no): ");
        familyHistory = scanner.nextLine();
        
        // Age risk
        if (age >= 65) riskPoints += 3;
        else if (age >= 45) riskPoints += 2;
        else if (age >= 30) riskPoints += 1;
        
        // BMI risk
        if (bmi >= 30) riskPoints += 3;
        else if (bmi >= 25) riskPoints += 2;
        else if (bmi >= 23) riskPoints += 1;
        
        // Lifestyle risk
        if (smokingStatus.equalsIgnoreCase("yes")) riskPoints += 3;
        if (exerciseStatus.equalsIgnoreCase("no")) riskPoints += 2;
        if (familyHistory.equalsIgnoreCase("yes")) riskPoints += 2;
        
        // Determine risk level
        if (riskPoints >= 8) riskLevel = "HIGH";
        else if (riskPoints >= 5) riskLevel = "MODERATE";
        else if (riskPoints >= 3) riskLevel = "ELEVATED";
        
        System.out.println("\n=== Health Risk Assessment Results ===");
        System.out.println("Age: " + age + " years");
        System.out.printf("BMI: %.1f\n", bmi);
        System.out.println("Smoking: " + smokingStatus);
        System.out.println("Exercise: " + exerciseStatus);
        System.out.println("Family history: " + familyHistory);
        System.out.println("Risk points: " + riskPoints + "/12");
        System.out.println("Risk level: " + riskLevel);
        
        if (riskLevel.equals("HIGH")) {
            System.out.println(" HIGH RISK - Consult doctor immediately");
            System.out.println("Recommendations: Lifestyle changes, medical evaluation");
        } else if (riskLevel.equals("MODERATE")) {
            System.out.println(" MODERATE RISK - Monitor health closely");
            System.out.println("Recommendations: Improve diet, start exercising");
        } else if (riskLevel.equals("ELEVATED")) {
            System.out.println(" ELEVATED RISK - Take preventive measures");
            System.out.println("Recommendations: Regular check-ups, healthy habits");
        } else {
            System.out.println(" LOW RISK - Maintain healthy lifestyle");
            System.out.println("Recommendations: Continue current healthy habits");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Point-based risk assessment system
- Multiple risk factor evaluation with accumulation
- Categorical risk level determination
- Personalized health recommendations

**Variable Analysis:**
- `riskPoints` (int): Cumulative score from 0-12
- `riskLevel` (String): Final categorization (LOW/ELEVATED/MODERATE/HIGH)
- `smokingStatus`, `exerciseStatus`, `familyHistory` (String): User responses

**Java-Specific Notes:**
- `equalsIgnoreCase()` for case-insensitive String comparison
- += operator for accumulating points
- Remember scanner.nextLine() after nextInt/nextDouble

---

### Algorithm 3: Academic Standing Calculator

```java
import java.util.Scanner;

public class AcademicStanding {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double gpa;
        int creditHours, semesters;
        String probationStatus;
        String standing = "UNDETERMINED";
        String eligibilityStatus = "ELIGIBLE";
        
        System.out.println("=== Academic Standing Calculator ===");
        System.out.print("Enter GPA (0.0-4.0): ");
        gpa = scanner.nextDouble();
        System.out.print("Enter total credit hours completed: ");
        creditHours = scanner.nextInt();
        System.out.print("Enter number of semesters completed: ");
        semesters = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Any academic probation? (yes/no): ");
        probationStatus = scanner.nextLine();
        
        if (probationStatus.equalsIgnoreCase("yes")) {
            standing = "ACADEMIC PROBATION";
            eligibilityStatus = "RESTRICTED";
        } else {
            if (gpa >= 3.75 && creditHours >= 60) {
                standing = "SUMMA CUM LAUDE CANDIDATE";
            } else if (gpa >= 3.5 && creditHours >= 45) {
                standing = "MAGNA CUM LAUDE CANDIDATE";
            } else if (gpa >= 3.25 && creditHours >= 30) {
                standing = "CUM LAUDE CANDIDATE";
            } else if (gpa >= 3.0) {
                if (creditHours >= 90) {
                    standing = "GOOD STANDING - NEAR GRADUATION";
                } else if (creditHours >= 60) {
                    standing = "GOOD STANDING - JUNIOR";
                } else if (creditHours >= 30) {
                    standing = "GOOD STANDING - SOPHOMORE";
                } else {
                    standing = "GOOD STANDING - FRESHMAN";
                }
            } else if (gpa >= 2.0) {
                standing = "SATISFACTORY STANDING";
            } else {
                standing = "ACADEMIC WARNING";
                eligibilityStatus = "COUNSELING REQUIRED";
            }
        }
        
        System.out.println("\n=== Academic Assessment ===");
        System.out.printf("GPA: %.2f\n", gpa);
        System.out.println("Credit Hours: " + creditHours);
        System.out.println("Semesters: " + semesters);
        System.out.println("Probation Status: " + probationStatus);
        System.out.println("Academic Standing: " + standing);
        System.out.println("Eligibility Status: " + eligibilityStatus);
        
        if (eligibilityStatus.equals("ELIGIBLE")) {
            System.out.println(" Eligible for all academic activities");
        } else if (eligibilityStatus.equals("RESTRICTED")) {
            System.out.println(" Limited eligibility - Academic plan required");
        } else {
            System.out.println(" Counseling required - Contact academic advisor");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Multi-criteria academic evaluation
- Honors program eligibility logic (GPA AND credit hours)
- Academic intervention triggers
- Status-based eligibility determination
- Nested decisions (GPA 3.0+ then check credit hours)

**Variable Analysis:**
- `gpa` (double): Grade point average 0.0-4.0
- `creditHours` (int): Total completed credits
- `standing` (String): Academic classification
- `eligibilityStatus` (String): Program eligibility

---

### Algorithm 4: Insurance Premium Calculator

```java
import java.util.Scanner;

public class InsurancePremium {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int age, experience, mileage;
        String vehicleType, accidentHistory;
        double basePremium = 500.0, riskMultiplier = 1.0, finalPremium;
        
        System.out.println("=== Auto Insurance Premium Calculator ===");
        System.out.print("Enter driver's age: ");
        age = scanner.nextInt();
        System.out.print("Enter years of driving experience: ");
        experience = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter vehicle type (sedan/suv/truck/sports): ");
        vehicleType = scanner.nextLine();
        System.out.print("Any accidents in last 3 years? (yes/no): ");
        accidentHistory = scanner.nextLine();
        System.out.print("Annual mileage: ");
        mileage = scanner.nextInt();
        
        // Age risk
        if (age < 25) riskMultiplier *= 1.5;
        else if (age > 65) riskMultiplier *= 1.2;
        
        // Experience risk
        if (experience < 3) riskMultiplier *= 1.4;
        else if (experience > 10) riskMultiplier *= 0.9;
        
        // Vehicle type risk
        if (vehicleType.equalsIgnoreCase("sports")) riskMultiplier *= 1.8;
        else if (vehicleType.equalsIgnoreCase("suv")) riskMultiplier *= 1.3;
        else if (vehicleType.equalsIgnoreCase("truck")) riskMultiplier *= 1.1;
        
        // Accident history
        if (accidentHistory.equalsIgnoreCase("yes")) riskMultiplier *= 1.6;
        
        // Mileage risk
        if (mileage > 15000) riskMultiplier *= 1.2;
        else if (mileage < 5000) riskMultiplier *= 0.95;
        
        finalPremium = basePremium * riskMultiplier;
        
        System.out.println("\n=== Premium Calculation ===");
        System.out.println("Driver Age: " + age);
        System.out.println("Driving Experience: " + experience + " years");
        System.out.println("Vehicle Type: " + vehicleType);
        System.out.println("Accident History: " + accidentHistory);
        System.out.println("Annual Mileage: " + mileage);
        System.out.printf("Base Premium: $%.2f\n", basePremium);
        System.out.printf("Risk Multiplier: %.2f\n", riskMultiplier);
        System.out.printf("Final Premium: $%.2f\n", finalPremium);
        
        if (riskMultiplier > 2.0) {
            System.out.println(" HIGH RISK PROFILE");
            System.out.println("Consider defensive driving courses");
        } else if (riskMultiplier > 1.5) {
            System.out.println(" MODERATE RISK PROFILE");
            System.out.println("Safe driving discount may apply");
        } else {
            System.out.println(" LOW RISK PROFILE");
            System.out.println("Eligible for premium discounts");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Cumulative risk multiplier system (*= operator)
- Multi-factor insurance rating
- Vehicle type categorization with String comparison
- Risk profile assessment based on final multiplier

**Variable Analysis:**
- `riskMultiplier` (double): Starts at 1.0, modified by each risk factor
- `basePremium` (double): Fixed starting rate ($500)
- `finalPremium` (double): Calculated result

**Java-Specific Notes:**
- *= operator for cumulative multiplication (riskMultiplier *= 1.5 means multiply by 1.5)
- Each risk factor independently modifies the multiplier
- equalsIgnoreCase() handles "Sports", "SPORTS", "sports" equally

---

### Algorithm 5: Travel Itinerary Planner

```java
import java.util.Scanner;

public class TravelPlanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String destination, season;
        int tripDays, groupSize, activityCount = 0;
        double dailyBudget, totalCost = 0.0;
        double accommodationCost, foodCost, activityCost, transportationCost, miscellaneousCost, totalBudget;
        
        System.out.println("=== Travel Itinerary Planner ===");
        System.out.print("Enter destination city: ");
        destination = scanner.nextLine();
        System.out.print("Enter trip duration in days: ");
        tripDays = scanner.nextInt();
        System.out.print("Enter budget per day: $");
        dailyBudget = scanner.nextDouble();
        scanner.nextLine(); // Consume newline
        System.out.print("Travel season (spring/summer/fall/winter): ");
        season = scanner.nextLine();
        System.out.print("Group size: ");
        groupSize = scanner.nextInt();
        
        // Seasonal activity planning
        if (season.equalsIgnoreCase("summer")) {
            if (destination.toLowerCase().contains("beach")) {
                System.out.println(" Beach activities recommended");
                totalCost += 50;
                activityCount = 5;
            } else {
                System.out.println(" Mountain activities recommended");
                totalCost += 40;
                activityCount = 4;
            }
        } else if (season.equalsIgnoreCase("winter")) {
            if (destination.toLowerCase().contains("mountain")) {
                System.out.println(" Skiing activities recommended");
                totalCost += 80;
                activityCount = 3;
            } else {
                System.out.println(" Cultural activities recommended");
                totalCost += 30;
                activityCount = 4;
            }
        } else {
            System.out.println(" Outdoor activities recommended");
            totalCost += 35;
            activityCount = 4;
        }
        
        // Cost calculations
        accommodationCost = dailyBudget * 0.4 * tripDays;
        foodCost = dailyBudget * 0.3 * tripDays;
        activityCost = totalCost * tripDays;
        transportationCost = dailyBudget * 0.2 * tripDays;
        miscellaneousCost = dailyBudget * 0.1 * tripDays;
        totalBudget = accommodationCost + foodCost + activityCost + transportationCost + miscellaneousCost;
        
        // Group discount
        if (groupSize > 4) {
            double groupDiscount = totalBudget * 0.1;
            totalBudget -= groupDiscount;
            System.out.printf(" Group discount applied: $%.2f\n", groupDiscount);
        }
        
        System.out.println("\n=== Travel Itinerary ===");
        System.out.println("Destination: " + destination);
        System.out.println("Duration: " + tripDays + " days");
        System.out.println("Season: " + season);
        System.out.println("Group Size: " + groupSize);
        System.out.printf("Daily Budget: $%.2f\n", dailyBudget);
        System.out.println("\n=== Cost Breakdown ===");
        System.out.printf("Accommodation: $%.2f\n", accommodationCost);
        System.out.printf("Food: $%.2f\n", foodCost);
        System.out.printf("Activities: $%.2f (%d per day)\n", activityCost, activityCount);
        System.out.printf("Transportation: $%.2f\n", transportationCost);
        System.out.printf("Miscellaneous: $%.2f\n", miscellaneousCost);
        System.out.printf("Total Estimated Cost: $%.2f\n", totalBudget);
        
        double budgetLimit = dailyBudget * tripDays;
        if (totalBudget > budgetLimit) {
            System.out.printf(" Budget exceeded by $%.2f\n", totalBudget - budgetLimit);
        } else {
            System.out.printf(" Within budget - $%.2f remaining\n", budgetLimit - totalBudget);
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Seasonal activity recommendations (nested if for season + destination)
- Budget allocation by percentages (40% accommodation, 30% food, etc.)
- Destination-based planning logic with String.contains()
- Group discount calculations (conditional discount)

**Variable Analysis:**
- `totalCost` (double): Activity cost per day
- `activityCount` (int): Number of activities per day
- Five cost categories calculated as percentages of daily budget
- `budgetLimit` (double): Total budget available (dailyBudget × tripDays)

**Java-Specific Notes:**
- `String.contains()` for substring search (destination.contains("beach"))
- `toLowerCase()` for case-insensitive search
- Percentage calculations with 0.4, 0.3, 0.2, 0.1 (total 100% + activities)

---

### Algorithm 6: Employee Performance Review

```java
import java.util.Scanner;

public class PerformanceReview {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String employeeName, disciplinaryStatus;
        int yearsService, productivity, quality, teamwork;
        double averageScore, salaryAdjustment = 0.0;
        String performanceRating = "UNDETERMINED";
        
        System.out.println("=== Employee Performance Review ===");
        System.out.print("Enter employee name: ");
        employeeName = scanner.nextLine();
        System.out.print("Enter years of service: ");
        yearsService = scanner.nextInt();
        System.out.print("Enter productivity score (1-10): ");
        productivity = scanner.nextInt();
        System.out.print("Enter quality score (1-10): ");
        quality = scanner.nextInt();
        System.out.print("Enter teamwork score (1-10): ");
        teamwork = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Any disciplinary actions? (yes/no): ");
        disciplinaryStatus = scanner.nextLine();
        
        averageScore = (productivity + quality + teamwork) / 3.0;
        
        if (disciplinaryStatus.equalsIgnoreCase("yes")) {
            performanceRating = "UNSATISFACTORY";
            salaryAdjustment = -5.0;
        } else {
            if (averageScore >= 9.0) {
                if (yearsService >= 5) {
                    performanceRating = "OUTSTANDING";
                    salaryAdjustment = 15.0;
                } else {
                    performanceRating = "EXCELLENT";
                    salaryAdjustment = 12.0;
                }
            } else if (averageScore >= 8.0) {
                performanceRating = "VERY GOOD";
                salaryAdjustment = 8.0;
            } else if (averageScore >= 7.0) {
                performanceRating = "GOOD";
                salaryAdjustment = 5.0;
            } else if (averageScore >= 6.0) {
                performanceRating = "SATISFACTORY";
                salaryAdjustment = 2.0;
            } else {
                performanceRating = "NEEDS IMPROVEMENT";
                salaryAdjustment = 0.0;
            }
        }
        
        System.out.println("\n=== Performance Review Results ===");
        System.out.println("Employee: " + employeeName);
        System.out.println("Years of Service: " + yearsService);
        System.out.println("Productivity Score: " + productivity + "/10");
        System.out.println("Quality Score: " + quality + "/10");
        System.out.println("Teamwork Score: " + teamwork + "/10");
        System.out.printf("Average Score: %.1f/10\n", averageScore);
        System.out.println("Disciplinary Actions: " + disciplinaryStatus);
        System.out.println("Performance Rating: " + performanceRating);
        System.out.printf("Salary Adjustment: %.1f%%\n", salaryAdjustment);
        
        if (performanceRating.equals("OUTSTANDING")) {
            System.out.println(" EMPLOYEE OF THE YEAR CANDIDATE");
            System.out.println("Eligible for bonus and promotion consideration");
        } else if (performanceRating.equals("UNSATISFACTORY")) {
            System.out.println(" PERFORMANCE IMPROVEMENT PLAN REQUIRED");
            System.out.println("Mandatory counseling and training");
        } else {
            System.out.println(" Performance review complete");
            System.out.println("Continue professional development");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Multi-criteria performance evaluation (three scores averaged)
- Disciplinary action override logic (immediate UNSATISFACTORY)
- Experience-based rating adjustments (5+ years for OUTSTANDING)
- Salary adjustment calculations based on rating

**Variable Analysis:**
- `averageScore` (double): Mean of three scores
- `performanceRating` (String): Final evaluation category
- `salaryAdjustment` (double): Percentage change (-5% to +15%)

**Java-Specific Notes:**
- Division by 3.0 (not 3) to get double result
- Negative salary adjustment possible (-5.0%)
- Disciplinary status overrides all other criteria (early exit from logic)

**Common Mistakes:**
- Integer division: `(productivity + quality + teamwork) / 3` would truncate to int
- Forgetting String.equals() and using == (won't work for Strings)
- Not handling disciplinary action as priority condition

---

### Decision Logic Best Practices in Java

**Readable Conditions:**
```java
// Good - clear and readable
if (age >= 18 && age <= 65 && income > 30000) {
    // approve
}

// Bad - too nested
if (age >= 18) {
    if (age <= 65) {
        if (income > 30000) {
            // approve
        }
    }
}
```java

**Consistent Structure:**
```java
// Use consistent patterns
if (condition1) {
    // handle case 1
} else if (condition2) {
    // handle case 2
} else {
    // handle default case
}
```java

**Early Returns (in methods):**
```java
// Good - fail fast
public void processApplication(int age, double income) {
    if (age < 18) {
        System.out.println("Error: Too young");
        return;
    }
    // continue with valid input
}
```java

**Enum for States:**
```java
enum RiskLevel {
    LOW, ELEVATED, MODERATE, HIGH
}

RiskLevel level = RiskLevel.LOW;
if (riskPoints >= 8) level = RiskLevel.HIGH;
else if (riskPoints >= 5) level = RiskLevel.MODERATE;
else if (riskPoints >= 3) level = RiskLevel.ELEVATED;
```java

---

 **Brilliant! You've mastered complex decision-making in code!** 

*Programs can now make intelligent decisions like real applications. Next: Loop algorithms in pseudocode! *
