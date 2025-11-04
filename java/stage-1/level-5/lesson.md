# Level 5: Conditional Statements

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Time to add intelligence to your programs! Today you'll learn how to make decisions with conditional statements. Your programs will finally be able to think and respond differently based on different situations.

---

### Learning Goals

- Master if, else if, and else statements
- Understand comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Learn logical operators (`&&`, `||`, `!`)
- Practice nested conditionals
- Create programs that make intelligent decisions

---

### Your Task

**Copy the following code EXACTLY as shown below into `Main.java`**

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("=== DECISION MAKER 3000 ===\n");

        // Example 1: Simple if-else
        System.out.print("Enter your age: ");
        int age = input.nextInt();

        if (age >= 18) {
            System.out.println("You are an adult!");
        } else {
            System.out.println("You are a minor.");
        }

        // Example 2: Multiple conditions with else if
        System.out.println("\n=== GRADE ANALYZER ===");
        System.out.print("Enter your test score (0-100): ");
        int score = input.nextInt();

        if (score >= 90) {
            System.out.println("Grade: A - Excellent!");
        } else if (score >= 80) {
            System.out.println("Grade: B - Good job!");
        } else if (score >= 70) {
            System.out.println("Grade: C - Passing");
        } else if (score >= 60) {
            System.out.println("Grade: D - Needs improvement");
        } else {
            System.out.println("Grade: F - Study harder!");
        }

        // Example 3: Logical operators (AND, OR)
        System.out.println("\n=== MOVIE TICKET ELIGIBILITY ===");
        System.out.print("Enter your age: ");
        int movieAge = input.nextInt();
        System.out.print("Do you have parental consent? (true/false): ");
        boolean hasConsent = input.nextBoolean();

        if (movieAge >= 17 || (movieAge >= 13 && hasConsent)) {
            System.out.println("You can watch R-rated movies!");
        } else if (movieAge >= 13) {
            System.out.println("You can watch PG-13 movies.");
        } else {
            System.out.println("You can watch G and PG movies.");
        }

        // Example 4: Nested conditionals
        System.out.println("\n=== DRIVING LICENSE CHECKER ===");
        System.out.print("Enter your age: ");
        int drivingAge = input.nextInt();
        System.out.print("Do you have a learner's permit? (true/false): ");
        boolean hasPermit = input.nextBoolean();

        if (drivingAge >= 16) {
            if (hasPermit) {
                System.out.println("You can drive with supervision!");
            } else {
                System.out.println("You need to get a learner's permit first.");
            }
        } else {
            System.out.println("You're too young to drive. Wait until you're 16.");
        }

        // Example 5: Comparison operators
        System.out.println("\n=== NUMBER COMPARISON ===");
        System.out.print("Enter first number: ");
        int num1 = input.nextInt();
        System.out.print("Enter second number: ");
        int num2 = input.nextInt();

        if (num1 == num2) {
            System.out.println(num1 + " is EQUAL to " + num2);
        } else if (num1 > num2) {
            System.out.println(num1 + " is GREATER than " + num2);
        } else {
            System.out.println(num1 + " is LESS than " + num2);
        }

        if (num1 != num2) {
            System.out.println("The numbers are different!");
        }

        // Example 6: Complex decision making
        System.out.println("\n=== WEATHER ADVISOR ===");
        System.out.print("What's the temperature in Fahrenheit? ");
        int temp = input.nextInt();
        System.out.print("Is it raining? (true/false): ");
        boolean isRaining = input.nextBoolean();
        System.out.print("Is it windy? (true/false): ");
        boolean isWindy = input.nextBoolean();

        System.out.println("\nWeather Advice:");
        if (temp > 80 && !isRaining) {
            System.out.println("- Perfect day for swimming!");
        } else if (temp > 60 && temp <= 80 && !isRaining) {
            System.out.println("- Great day for outdoor activities!");
        } else if (isRaining && temp > 50) {
            System.out.println("- Bring an umbrella!");
        } else if (isRaining && temp <= 50) {
            System.out.println("- Bring an umbrella and wear a jacket!");
        } else if (temp <= 32) {
            System.out.println("- It's freezing! Stay warm!");
        } else {
            System.out.println("- Maybe stay indoors today.");
        }

        if (isWindy) {
            System.out.println("- Watch out for strong winds!");
        }

        // Example 7: Ternary operator (bonus!)
        System.out.println("\n=== EVEN OR ODD ===");
        System.out.print("Enter a number: ");
        int number = input.nextInt();

        String result = (number % 2 == 0) ? "EVEN" : "ODD";
        System.out.println(number + " is " + result);

        input.close();
    }
}
```

---



**Expected output:**
```
[Output depends on conditions - varies based on input]
```

### How to Run

**Method 1 (Vim - Recommended):**
```java
<Space>r
```

**Method 2 (Terminal):**
```bash
javac Main.java
java Main
```

**Follow all the prompts** and see how the program makes different decisions!

**Example interaction:**
```java
=== DECISION MAKER 3000 ===

Enter your age: 25
You are an adult!

=== GRADE ANALYZER ===
Enter your test score (0-100): 87
Grade: B - Good job!

=== MOVIE TICKET ELIGIBILITY ===
Enter your age: 15
Do you have parental consent? (true/false): true
You can watch R-rated movies!

=== DRIVING LICENSE CHECKER ===
Enter your age: 16
Do you have a learner's permit? (true/false): false
You need to get a learner's permit first.

=== NUMBER COMPARISON ===
Enter first number: 10
Enter second number: 5
10 is GREATER than 5
The numbers are different!

=== WEATHER ADVISOR ===
What's the temperature in Fahrenheit? 75
Is it raining? (true/false): false
Is it windy? (true/false): false

Weather Advice:
- Great day for outdoor activities!

=== EVEN OR ODD ===
Enter a number: 42
42 is EVEN
```

---

### Success Checklist

- [ ] Created/updated `Main.java`
- [ ] Copied all code correctly
- [ ] Compiled without errors
- [ ] Tested with different inputs
- [ ] Understood how if-else works
- [ ] Saw how logical operators combine conditions

---

### What Just Happened?

You learned the foundation of programming logic! Here's what's powerful:

1. **Decision Making**: Programs that respond differently to different inputs
2. **Comparison**: Testing relationships between values
3. **Logic**: Combining multiple conditions with AND/OR
4. **Nesting**: Decisions within decisions for complex logic

---

### Try This (Optional Challenges)

1. Add a BMI calculator that categorizes results
2. Create a simple login system (check username AND password)
3. Build a calculator that handles division by zero
4. Make a grade calculator that also checks for extra credit

---

## Quick Reference

### Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `true` |
| `!=` | Not equal to | `5 != 3` | `true` |
| `>` | Greater than | `5 > 3` | `true` |
| `<` | Less than | `3 < 5` | `true` |
| `>=` | Greater than or equal | `5 >= 5` | `true` |
| `<=` | Less than or equal | `3 <= 5` | `true` |

### Logical Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `&&` | AND (both must be true) | `true && false` | `false` |
| `||` | OR (at least one true) | `true || false` | `true` |
| `!` | NOT (inverts) | `!true` | `false` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```java
if (age >= 18) {
    System.out.println("You are an adult!");
} else {
    System.out.println("You are a minor.");
}
```
- **`if`** = Tests a condition
- **`age >= 18`** = Condition (must be true or false)
- **`{}`** = Code block that runs if condition is true
- **`else`** = Runs if condition is false

```java
if (score >= 90) {
    System.out.println("Grade: A");
} else if (score >= 80) {
    System.out.println("Grade: B");
} else if (score >= 70) {
    System.out.println("Grade: C");
} else {
    System.out.println("Grade: F");
}
```
- **`else if`** = Tests another condition if previous was false
- **Order matters!** Checks from top to bottom
- **First match wins**: Once a condition is true, rest are skipped

```java
if (movieAge >= 17 || (movieAge >= 13 && hasConsent)) {
    System.out.println("You can watch R-rated movies!");
}
```
- **`||`** = OR operator (either condition can be true)
- **`&&`** = AND operator (both conditions must be true)
- **`()`** = Parentheses control order of evaluation

```java
if (drivingAge >= 16) {
    if (hasPermit) {
        System.out.println("You can drive!");
    }
}
```
- **Nested if** = An if statement inside another if statement
- **Both conditions** must be true to reach inner code
- **Useful for** complex decision trees

```java
String result = (number % 2 == 0) ? "EVEN" : "ODD";
```
- **Ternary operator** = Shorthand if-else for simple assignments
- **Format**: `condition ? valueIfTrue : valueIfFalse`
- **Same as**:
  ```java
  String result;
  if (number % 2 == 0) {
      result = "EVEN";
  } else {
      result = "ODD";
  }
  ```

### Understanding Logical Operators

**AND (&&) - Both must be true:**
```java
true  && true  = true
true  && false = false
false && true  = false
false && false = false
```

**OR (||) - At least one must be true:**
```java
true  || true  = true
true  || false = true
false || true  = true
false || false = false
```

**NOT (!) - Inverts the value:**
```java
!true  = false
!false = true
```

### Operator Precedence

When combining conditions, Java evaluates in this order:
1. **`!`** (NOT) - highest priority
2. **`&&`** (AND)
3. **`||`** (OR) - lowest priority

**Example:**
```java
// Without parentheses:
if (age > 18 || age == 18 && hasLicense)
// Evaluates as: age > 18 || (age == 18 && hasLicense)

// With parentheses (recommended for clarity):
if ((age > 18 || age == 18) && hasLicense)
```

### Short-Circuit Evaluation

Java is smart! It doesn't waste time:

**AND (`&&`):**
```java
if (false && expensiveFunction()) {
    // expensiveFunction() is NEVER called!
    // Because false && anything = false
}
```

**OR (`||`):**
```java
if (true || expensiveFunction()) {
    // expensiveFunction() is NEVER called!
    // Because true || anything = true
}
```

**Practical use:**
```java
// Prevents division by zero:
if (denominator != 0 && numerator / denominator > 10) {
    // Safe! Division only happens if denominator != 0
}
```

### Common Mistakes

**1. Using `=` instead of `==`:**
```java
// WRONG:
if (age = 18) {  // Assignment, not comparison!

// RIGHT:
if (age == 18) {  // Comparison
```

**2. Comparing strings with `==`:**
```java
// WRONG:
if (name == "John") {  // Compares memory addresses!

// RIGHT:
if (name.equals("John")) {  // Compares content
```

**3. Missing braces in if statements:**
```java
// DANGEROUS:
if (age < 18)
    System.out.println("Minor");
    System.out.println("Cannot vote");  // Always executes!

// SAFE:
if (age < 18) {
    System.out.println("Minor");
    System.out.println("Cannot vote");
}
```

**4. Redundant conditions:**
```java
// REDUNDANT:
if (age >= 18 && age < 65) {
    // ...
} else if (age >= 65) {  // Could just be "else"
    // ...
}

// BETTER:
if (age >= 18 && age < 65) {
    // ...
} else {  // Automatically means age < 18 or age >= 65
    // ...
}
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `incompatible types: int cannot be converted to boolean` | Used `=` instead of `==` | Use `==` for comparison |
| `cannot find symbol: method equals(int)` | Comparing primitive with equals | Use `==` for primitives, `equals()` for objects |
| Unexpected behavior | Missing braces | Always use `{}` even for single statements |
| `NullPointerException` | Calling method on null | Check for null before calling methods |

### Advanced Patterns

**1. Range checking:**
```java
if (score >= 90 && score <= 100) {
    System.out.println("A");
}

// Better for readability:
if (90 <= score && score <= 100) {  // Math notation
    System.out.println("A");
}
```

**2. Flag variables:**
```java
boolean isEligible = (age >= 18 && hasID && !isBanned);
if (isEligible) {
    System.out.println("Welcome!");
}
```

**3. Guard clauses (early returns):**
```java
public static void processAge(int age) {
    if (age < 0) {
        System.out.println("Invalid age");
        return;  // Exit early
    }
    if (age < 18) {
        System.out.println("Minor");
        return;
    }
    System.out.println("Adult");
}
```

**4. Switch statement (alternative to many else-if):**
```java
int day = 3;
switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Other day");
}
```

### Bonus Knowledge

- **Boolean History**: Named after George Boole, mathematician (1815-1864)
- **Compiler Optimization**: Modern Java compilers can optimize away impossible conditions
- **Defensive Programming**: Always validate user input with conditionals
- **Code Coverage**: Testing should check all branches (true and false paths)

### Real-World Applications

Conditionals are everywhere:
1. **Authentication**: If username AND password match, grant access
2. **E-commerce**: If item in stock AND payment valid, process order
3. **Games**: If player health <= 0, game over
4. **GPS**: If distance < 100 meters, "you have arrived"
5. **Form Validation**: If email is valid AND age >= 13, create account

### Testing Your Conditionals

Always test boundary cases:
- **Exact boundaries**: age == 18, score == 90
- **Just below**: age == 17, score == 89
- **Just above**: age == 19, score == 91
- **Extreme values**: age == 0, score == 0 or 100
- **Invalid values**: age == -5, score == 150

---

**Fantastic! You've mastered conditional logic in Java!**

*Next up: Repeating actions with loops!*
