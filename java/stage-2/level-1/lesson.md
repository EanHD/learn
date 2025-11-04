# Level 1: Basic Pseudocode Translation

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Stage 2! You've mastered copying code - now it's time to think like a programmer! Today you'll learn to translate written instructions (pseudocode) into working Java programs. This is where programming becomes creative problem-solving!

---

### Learning Goals

- Understand what pseudocode is and why it's useful
- Learn to read and interpret algorithmic descriptions
- Practice translating simple algorithms into Java code
- Develop logical thinking for programming
- Create working programs from written instructions

---

### What is Pseudocode?

**Pseudocode** is a way to write programming logic in plain English (or your native language) before writing actual code. It's like writing a recipe or instructions for a task.

**Example:**
```java
Algorithm: Make a sandwich
1. Get bread from pantry
2. Get peanut butter from fridge
3. Get jelly from pantry
4. Spread peanut butter on one bread slice
5. Spread jelly on the other bread slice
6. Put slices together
7. Enjoy your sandwich!
```

This is much easier to understand than trying to write code first!

---

### Your Task

**For each pseudocode algorithm below, translate it into working Java code.**

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
```
Hello, World!
```

## Algorithm 1: Greeting Program

**Pseudocode:**
```java
Algorithm: Display Personal Greeting
1. Display "Hello! What's your name?" to the user
2. Get the user's name from input
3. Display "Nice to meet you, " followed by the user's name
4. Display "Welcome to programming!"
```

**Your Task:** Create a Java program that follows these exact steps.

---

## Algorithm 2: Simple Calculator

**Pseudocode:**
```java
Algorithm: Add Two Numbers
1. Ask user for first number
2. Get first number from user
3. Ask user for second number
4. Get second number from user
5. Calculate sum of the two numbers
6. Display "The sum is: " followed by the sum
```

**Your Task:** Create a Java program that implements this calculator.

---

## Algorithm 3: Age Calculator

**Pseudocode:**
```java
Algorithm: Calculate Age in Days
1. Display "Enter your age in years: "
2. Get age in years from user
3. Calculate days = age × 365
4. Display "You are approximately " + days + " days old"
5. Display "That's a lot of days!"
```

**Your Task:** Create a program that calculates approximate age in days.

---

## Algorithm 4: Temperature Converter

**Pseudocode:**
```java
Algorithm: Celsius to Fahrenheit Converter
1. Display "Enter temperature in Celsius: "
2. Get temperature in Celsius from user
3. Calculate Fahrenheit = (Celsius × 9/5) + 32
4. Display the Celsius temperature
5. Display "°C = "
6. Display the Fahrenheit temperature
7. Display "°F"
```

**Your Task:** Create a temperature conversion program.

---

## Algorithm 5: Rectangle Area Calculator

**Pseudocode:**
```java
Algorithm: Calculate Rectangle Area
1. Display "Rectangle Area Calculator"
2. Display "Enter length: "
3. Get length from user
4. Display "Enter width: "
5. Get width from user
6. Calculate area = length × width
7. Calculate perimeter = 2 × (length + width)
8. Display "Area: " + area
9. Display "Perimeter: " + perimeter
```

**Your Task:** Create a program that calculates both area and perimeter.

---

## Algorithm 6: Simple Interest Calculator

**Pseudocode:**
```java
Algorithm: Calculate Simple Interest
1. Display "Simple Interest Calculator"
2. Display "Enter principal amount: $"
3. Get principal from user
4. Display "Enter interest rate (%): "
5. Get rate from user
6. Display "Enter time in years: "
7. Get time from user
8. Calculate interest = (principal × rate × time) ÷ 100
9. Calculate total = principal + interest
10. Display "Principal: $" + principal
11. Display "Interest: $" + interest
12. Display "Total: $" + total
```

**Your Task:** Implement the complete interest calculation.

---

### How to Approach Each Algorithm

**Step-by-Step Process:**

1. **Read Carefully**: Understand what the algorithm does
2. **Identify Inputs**: What information does the user provide?
3. **Identify Outputs**: What should the program display?
4. **Identify Calculations**: What math is needed?
5. **Plan the Code Structure**:
   - `import java.util.Scanner;`
   - `public class Main {`
   - `public static void main(String[] args) {`
   - `Scanner input = new Scanner(System.in);`
   - Variable declarations
   - Input statements
   - Calculations
   - Output statements
   - `input.close();`
   - `}`
   - `}`

**Example Planning for Algorithm 1:**
- **Inputs**: User's name (String)
- **Outputs**: Greeting messages
- **No calculations needed**
- **Structure**: Simple input/output program

---

### Success Checklist

**For Each Algorithm:**
- [ ] Created a Java file with proper class structure
- [ ] Program compiles without errors (`javac Main.java`)
- [ ] Program runs and produces expected output (`java Main`)
- [ ] Followed the pseudocode steps exactly
- [ ] Used appropriate variable names
- [ ] Included clear output messages
- [ ] Closed the Scanner object

**Overall Progress:**
- [ ] Completed all 6 algorithms
- [ ] All programs work correctly
- [ ] Code is well-organized and readable

---

### Try This (Optional Challenges)

1. **Modify Algorithm 1**: Add a question about favorite color and respond to it
2. **Modify Algorithm 3**: Make the calculation more accurate (account for leap years)
3. **Combine Algorithms**: Create a program that does temperature conversion AND age calculation
4. **Add Validation**: Check if user enters valid numbers (no negative ages, etc.)

---

## Pseudocode Best Practices

### Good Pseudocode
```java
Algorithm: Process User Data
1. Get user's name
2. Get user's age
3. If age >= 18 then
   Display "Adult user"
Else
   Display "Minor user"
4. Display "Data processed"
```

### Bad Pseudocode (Too Vague)
```java
Algorithm: Do stuff
1. Get things
2. Calculate something
3. Show results
```

### Good Pseudocode (Clear and Specific)
```java
Algorithm: Calculate BMI
1. Display "BMI Calculator"
2. Display "Enter weight in kg: "
3. Get weight from user
4. Display "Enter height in meters: "
5. Get height from user
6. Calculate BMI = weight ÷ (height × height)
7. Display "Your BMI is: " + BMI
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Greeting Program

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Hello! What's your name? ");
        String name = input.nextLine();
        
        System.out.println("Nice to meet you, " + name);
        System.out.println("Welcome to programming!");
        
        input.close();
    }
}
```

**Key Concepts:**
- `Scanner input = new Scanner(System.in);` - Create Scanner for user input
- `String name = input.nextLine();` - Read full line of text
- `System.out.println("Nice to meet you, " + name);` - Concatenate strings with +
- `input.close();` - Always close Scanner when done

---

### Algorithm 2: Simple Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter first number: ");
        int num1 = input.nextInt();
        
        System.out.print("Enter second number: ");
        int num2 = input.nextInt();
        
        int sum = num1 + num2;
        
        System.out.println("The sum is: " + sum);
        
        input.close();
    }
}
```

**Key Concepts:**
- `int num1 = input.nextInt();` - Read integer from user
- Multiple variables: `num1`, `num2`, `sum`
- Arithmetic operation: `sum = num1 + num2;`
- Clear input prompts for each value

---

### Algorithm 3: Age Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter your age in years: ");
        int ageYears = input.nextInt();
        
        int ageDays = ageYears * 365;
        
        System.out.println("You are approximately " + ageDays + " days old");
        System.out.println("That's a lot of days!");
        
        input.close();
    }
}
```

**Key Concepts:**
- Simple multiplication: `ageDays = ageYears * 365;`
- CamelCase naming convention: `ageYears`, `ageDays`
- String concatenation with numbers

---

### Algorithm 4: Temperature Converter

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter temperature in Celsius: ");
        double celsius = input.nextDouble();
        
        double fahrenheit = (celsius * 9.0/5.0) + 32;
        
        System.out.printf("%.1f°C = %.1f°F%n", celsius, fahrenheit);
        
        input.close();
    }
}
```

**Key Concepts:**
- `double` variables for decimal temperatures
- Complex formula: `(celsius * 9.0/5.0) + 32`
- `System.out.printf()` for formatted output
- Format specifier `%.1f` for one decimal place

---

### Algorithm 5: Rectangle Area Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Rectangle Area Calculator");
        System.out.print("Enter length: ");
        double length = input.nextDouble();
        
        System.out.print("Enter width: ");
        double width = input.nextDouble();
        
        double area = length * width;
        double perimeter = 2 * (length + width);
        
        System.out.printf("Area: %.2f%n", area);
        System.out.printf("Perimeter: %.2f%n", perimeter);
        
        input.close();
    }
}
```

**Key Concepts:**
- Multiple calculations: area and perimeter
- Parentheses for order of operations: `2 * (length + width)`
- Format specifier `%.2f` for two decimal places

---

### Algorithm 6: Simple Interest Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Simple Interest Calculator");
        System.out.print("Enter principal amount: $");
        double principal = input.nextDouble();
        
        System.out.print("Enter interest rate (%): ");
        double rate = input.nextDouble();
        
        System.out.print("Enter time in years: ");
        double time = input.nextDouble();
        
        double interest = (principal * rate * time) / 100;
        double total = principal + interest;
        
        System.out.printf("Principal: $%.2f%n", principal);
        System.out.printf("Interest: $%.2f%n", interest);
        System.out.printf("Total: $%.2f%n", total);
        
        input.close();
    }
}
```

**Key Concepts:**
- Complex formula: `(principal * rate * time) / 100`
- Multiple output lines with `printf()`
- Dollar sign formatting in output
- Always close Scanner to prevent resource leaks

---

### Common Translation Patterns

| Pseudocode Pattern | Java Code Equivalent |
|-------------------|---------------------|
| `Display "message"` | `System.out.println("message");` |
| `Get variable from user` | `variable = input.nextInt();` |
| `Calculate result = a + b` | `result = a + b;` |
| `If condition then` | `if (condition) {` |
| `Display variable` | `System.out.println(variable);` |

### Debugging Tips

**"Program doesn't compile":**
- Check semicolons at end of statements
- Verify variable declarations
- Ensure proper braces `{ }`
- Check that class name matches filename
- Verify Scanner is imported

**"Wrong output":**
- Check variable names match (Java is case-sensitive)
- Verify Scanner methods (`nextInt()` for int, `nextDouble()` for double)
- Check mathematical formulas
- Ensure string concatenation uses `+`

**"Program crashes":**
- Make sure Scanner is imported: `import java.util.Scanner;`
- Check variables are declared before use
- Verify Scanner is reading correct type
- Always close Scanner with `input.close();`

### Variable Naming Best Practices

**Java Conventions (camelCase):**
- `userAge` (clear what it stores)
- `temperatureCelsius` (descriptive)
- `rectangleArea` (specific purpose)

**Bad Names:**
- `x` (too vague)
- `temp` (unclear what kind of temperature)
- `var1` (meaningless)

**Java Naming Rules:**
- Start with lowercase letter
- Use camelCase for multi-word names
- Use descriptive, meaningful names
- Avoid single letters except for loop counters

---

### Input/Output Patterns

**Getting Integers:**
```java
Scanner input = new Scanner(System.in);
System.out.print("Enter age: ");
int age = input.nextInt();
```

**Getting Decimals:**
```java
System.out.print("Enter price: $");
double price = input.nextDouble();
```

**Getting Text:**
```java
System.out.print("Enter name: ");
String name = input.nextLine();
```

**Displaying Results:**
```java
System.out.println("Result: " + result);
System.out.printf("Price: $%.2f%n", price);
System.out.println("Hello, " + name + "!");
```

**Important Scanner Note:**
When mixing `nextInt()` or `nextDouble()` with `nextLine()`, you may need to add an extra `input.nextLine()` to clear the buffer:

```java
int age = input.nextInt();
input.nextLine();  // Clear the newline
String name = input.nextLine();  // Now this works correctly
```

---

**Congratulations! You've translated your first pseudocode algorithms into working Java programs!**

*This is a major milestone - you're now thinking like a programmer! Next up: Variables in pseudocode!*
