# Level 4: User Input

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Get ready to make your programs interactive! Today you'll learn how to talk to your users - getting information from them and responding to what they type. This is where Java programs start to feel like real applications!

---

### Learning Goals

- Learn how to read user input with `Scanner`
- Understand different input methods for various data types
- Practice with strings, integers, and floating-point input
- Create interactive programs that respond to user data
- Handle input errors gracefully

---

### Your Task

**Copy the following code EXACTLY as shown below into `Main.java`**

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Create Scanner object for reading input
        Scanner input = new Scanner(System.in);

        System.out.println("=== Personal Information Form ===\n");

        // Get user's name
        System.out.print("What's your first name? ");
        String name = input.nextLine();

        // Get user's age
        System.out.print("How old are you? ");
        int age = input.nextInt();

        // Get user's height
        System.out.print("What's your height in inches? ");
        double height = input.nextDouble();

        // Clear the newline character
        input.nextLine();

        // Get user's grade
        System.out.print("What's your letter grade (A, B, C, D, F)? ");
        String gradeStr = input.nextLine();
        char grade = gradeStr.charAt(0);

        System.out.println("\n=== Your Information Summary ===");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age + " years old");
        System.out.println("Height: " + height + " inches");
        System.out.println("Grade: " + grade);

        // Calculate some interesting facts
        System.out.println("\n=== Interesting Facts ===");

        // Height in centimeters
        double heightCm = height * 2.54;
        System.out.printf("Height in centimeters: %.1f cm\n", heightCm);

        // Age in different units
        System.out.println("Age in months: " + (age * 12));
        System.out.println("Age in days (approximately): " + (age * 365));

        // Grade analysis
        System.out.println("\n=== Grade Analysis ===");
        if (grade == 'A' || grade == 'a') {
            System.out.println("Excellent work! You're doing great!");
        } else if (grade == 'B' || grade == 'b') {
            System.out.println("Good job! Keep up the good work!");
        } else if (grade == 'C' || grade == 'c') {
            System.out.println("Not bad, but there's room for improvement.");
        } else {
            System.out.println("Keep trying! You can do this!");
        }

        // Weight and BMI calculation
        System.out.println("\n=== Health Calculator ===");
        System.out.print("Enter your weight in pounds: ");
        double weightPounds = input.nextDouble();

        double bmi = (weightPounds * 703) / (height * height);
        System.out.printf("Your BMI: %.1f\n", bmi);

        if (bmi < 18.5) {
            System.out.println("Category: Underweight");
        } else if (bmi < 25) {
            System.out.println("Category: Normal weight");
        } else if (bmi < 30) {
            System.out.println("Category: Overweight");
        } else {
            System.out.println("Category: Obese");
        }

        // Future prediction
        System.out.println("\n=== Future Prediction ===");
        System.out.print("How many years into the future should we predict? ");
        int futureYears = input.nextInt();

        System.out.println("In " + futureYears + " years, you'll be " + (age + futureYears) + " years old!");

        System.out.println("\nThanks for using the personal info calculator, " + name + "!");

        // Close the scanner
        input.close();
    }
}
```

---



**Expected output:**
```
[Interactive - output varies based on user input]
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

**Follow the prompts** and enter your information when asked!

**Example interaction:**
```java
=== Personal Information Form ===

What's your first name? Alex
How old are you? 25
What's your height in inches? 70
What's your letter grade (A, B, C, D, F)? B

=== Your Information Summary ===
Name: Alex
Age: 25 years old
Height: 70.0 inches
Grade: B

=== Interesting Facts ===
Height in centimeters: 177.8 cm
Age in months: 300
Age in days (approximately): 9125

=== Grade Analysis ===
Good job! Keep up the good work!

=== Health Calculator ===
Enter your weight in pounds: 160
Your BMI: 23.0
Category: Normal weight

=== Future Prediction ===
How many years into the future should we predict? 10
In 10 years, you'll be 35 years old!

Thanks for using the personal info calculator, Alex!
```

---

### Success Checklist

- [ ] Created/updated `Main.java`
- [ ] Copied all code correctly including import statement
- [ ] Compiled without errors
- [ ] Ran the program and entered all requested information
- [ ] Saw personalized output with your data
- [ ] Understood how Scanner reads different data types

---

### What Just Happened?

You created an interactive Java program! Here's what's special:

1. **Scanner Class**: A powerful tool from `java.util` that reads user input
2. **Different Input Methods**: `nextLine()`, `nextInt()`, `nextDouble()` for different data types
3. **Input Buffer**: That mysterious `input.nextLine()` after `nextDouble()` - we'll explain!
4. **Type Safety**: Java ensures you read the right type of data

---

### Try This (Optional Challenges)

1. Add more personal questions (favorite color, hobby, etc.)
2. Calculate years until retirement (age 65)
3. Add error handling for invalid input
4. Create a simple quiz with score calculation

---

### Pro Tip

Always close your Scanner with `input.close()` when you're done! This is good practice and prevents resource leaks.

---

## Quick Reference

| Scanner Method | What it reads | Example |
|----------------|---------------|---------|
| `nextLine()` | Entire line of text | `"Hello World"` |
| `next()` | Single word (until space) | `"Hello"` |
| `nextInt()` | Integer number | `42` |
| `nextDouble()` | Decimal number | `3.14` |
| `nextBoolean()` | true or false | `true` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```java
import java.util.Scanner;
```
- **`import`** = Brings in external classes we need
- **`java.util.Scanner`** = The Scanner class for reading input
- **Why needed?** Scanner isn't built into Java core, must be imported

```java
Scanner input = new Scanner(System.in);
```
- **`Scanner input`** = Declares a Scanner variable named "input"
- **`new Scanner`** = Creates a new Scanner object
- **`System.in`** = Standard input stream (keyboard)
- **Think of it as**: Creating a tool that listens to the keyboard

```java
String name = input.nextLine();
```
- **`nextLine()`** = Reads entire line of text until Enter is pressed
- **Best for**: Names, sentences, any text with spaces
- **Returns**: String data type

```java
int age = input.nextInt();
```
- **`nextInt()`** = Reads the next integer number
- **Warning**: Doesn't consume the newline character!
- **Returns**: int data type

```java
input.nextLine();  // Clear the newline
```
- **Why this line?** After `nextInt()` or `nextDouble()`, a newline character remains in the buffer
- **Problem**: Next `nextLine()` would read that empty line
- **Solution**: Call `nextLine()` once to consume it
- **This is a common Java gotcha!**

```java
char grade = gradeStr.charAt(0);
```
- **Why not direct char input?** Scanner has no `nextChar()` method
- **Solution**: Read as String, extract first character
- **`charAt(0)`** = Gets character at index 0 (first character)

```java
System.out.printf("Height in centimeters: %.1f cm\n", heightCm);
```
- **`printf`** = Formatted print (like C's printf)
- **`%.1f`** = Float with 1 decimal place
- **`\n`** = Newline character

```java
input.close();
```
- **Purpose**: Closes the Scanner and releases resources
- **Best practice**: Always close resources when done
- **Prevents**: Resource leaks in larger applications

### The Newline Buffer Problem (IMPORTANT!)

This is one of the most confusing issues for Java beginners:

**The Problem:**
```java
int age = input.nextInt();      // User types: 25[Enter]
// nextInt() reads "25" but leaves "[Enter]" in buffer!
String name = input.nextLine();  // Reads that leftover Enter = empty string!
```

**The Solution:**
```java
int age = input.nextInt();
input.nextLine();  // Consume the leftover newline
String name = input.nextLine();  // Now this works correctly!
```

**Rule of Thumb**: After using `nextInt()`, `nextDouble()`, or `nextFloat()`, always call `input.nextLine()` once to clear the buffer before reading more text.

### Scanner Method Comparison

| Method | Reads | Stops At | Consumes Newline? |
|--------|-------|----------|-------------------|
| `nextLine()` | Whole line | Newline | Yes |
| `next()` | One word | Whitespace | No |
| `nextInt()` | Integer | Whitespace | No |
| `nextDouble()` | Double | Whitespace | No |

### Input Validation

Scanner will crash if you enter the wrong type! Here's what happens:

```java
// If you enter "hello" when it expects int:
int age = input.nextInt();  // Throws InputMismatchException!
```

**Better approach (we'll learn this later):**
```java
if (input.hasNextInt()) {
    int age = input.nextInt();
} else {
    System.out.println("Please enter a valid number!");
}
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `InputMismatchException` | Wrong data type entered | Check input type matches Scanner method |
| `NoSuchElementException` | Reading when no input available | Check Scanner is open and has data |
| Empty string read | Didn't clear newline buffer | Add `input.nextLine()` after numeric input |
| `Cannot find symbol: Scanner` | Missing import | Add `import java.util.Scanner;` |

### String Concatenation in Java

We used two ways to combine strings and values:

**Method 1: Using + operator**
```java
System.out.println("Name: " + name);
System.out.println("Age: " + age + " years old");
```
- Simple and readable
- Java automatically converts numbers to strings

**Method 2: Using printf**
```java
System.out.printf("Height: %.1f cm\n", heightCm);
System.out.printf("BMI: %.1f\n", bmi);
```
- More control over formatting
- Better for numbers with specific decimal places

### Scanner vs BufferedReader

You might see `BufferedReader` in some Java code:

**Scanner (What we use):**
- ✅ Easy to use
- ✅ Built-in parsing (nextInt, nextDouble, etc.)
- ✅ Perfect for beginners
- ❌ Slightly slower (not noticeable for small programs)

**BufferedReader (Alternative):**
- ✅ Faster for large amounts of data
- ✅ More efficient for reading files
- ❌ Only reads strings, must parse manually
- ❌ More complex to use

**For learning, stick with Scanner!**

### Bonus Knowledge

- **Scanner Class History**: Introduced in Java 5 (2004) to make input easier
- **System.in**: A static InputStream that's been part of Java since the beginning
- **Why "Scanner"?** The name comes from "scanning" (reading) text input
- **Thread Safety**: Scanner is not thread-safe (doesn't matter for beginner programs)

### Real-World Applications

User input is everywhere:
1. **Login Systems**: Username and password
2. **Online Forms**: Name, email, address
3. **Games**: Player choices, character names
4. **Calculators**: Numbers for calculations
5. **Search Engines**: Search queries

### Advanced Challenge (For the Brave!)

Create a simple restaurant order system:

```java
Scanner input = new Scanner(System.in);

System.out.println("Welcome to Java Cafe!");
System.out.print("Enter your name: ");
String customerName = input.nextLine();

System.out.print("How many coffees? ");
int coffees = input.nextInt();

System.out.print("How many sandwiches? ");
int sandwiches = input.nextInt();

double coffeePrice = 4.50;
double sandwichPrice = 7.95;
double total = (coffees * coffeePrice) + (sandwiches * sandwichPrice);

System.out.println("\n=== Order Summary ===");
System.out.println("Customer: " + customerName);
System.out.println("Coffees: " + coffees + " × $" + coffeePrice);
System.out.println("Sandwiches: " + sandwiches + " × $" + sandwichPrice);
System.out.printf("Total: $%.2f\n", total);

input.close();
```

---

**Excellent work! You've mastered user input in Java!**

*Next up: Making decisions with if-else statements!*
