# Level 2: Variables and Data Types

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.java`). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window.

## Stage 1: Copying Code

### Today's Mission

Now that you can run Java code, let's learn about **variables** - containers that store information. Variables are fundamental to all programming!

---

### Learning Goals

- Understand what variables are and why they're useful
- Learn Java's basic data types (int, String, double)
- Declare and assign values to variables
- Print variable values to the screen

---

### Your Task

**Copy the following code EXACTLY into `main.java`**

```
public class Main {
    public static void main(String[] args) {
        String name = "Alice";
        int age = 25;
        double height = 5.7;

        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
    }
}
```

---

### How to Run

**Vim:** `<Space>r`

**Terminal:**
```
javac main.java
java Main
```

**Expected output:**
```
Name: Alex
Age: 25
Price: $29.99
```

---

### Success Checklist

- [ ] Created the file `main.java` with all the code
- [ ] Compiled successfully with `javac main.java`
- [ ] Ran the program with `java Main`
- [ ] Saw all three lines of output
- [ ] Output matches exactly what's shown

---

### What Happened?

You just used **three different data types** in Java:

- **`String`** - Text (enclosed in double quotes)
- **`int`** - Whole numbers (no decimal point)
- **`double`** - Decimal numbers (with decimal point)

Each line follows this pattern:
```
[type] [variableName] = [value];
```

When you use `+` between strings and variables, Java converts them to text and joins them together!

---

### Try This (Optional Challenges)

1. Change the variable values to your own information
2. Add more variables (try `boolean canCode = true;`)
3. Create a variable, then use it twice in println statements

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY

### Code Breakdown

```
String name = "Alice";     // Text variable
int age = 25;              // Whole number variable
double height = 5.7;       // Decimal number variable
```

Each variable has:
- **Type**: What kind of data (String, int, double)
- **Name**: What to call it (name, age, height)
- **Value**: The actual data ("Alice", 25, 5.7)

### String Concatenation

```
System.out.println("Name: " + name);
```

The `+` operator concatenates (joins) strings and converts variables to text!

### Java Data Types (Overview)

| Type | Purpose | Example |
|------|---------|---------|
| `String` | Text | `"Hello"` |
| `int` | Whole numbers | `42` |
| `double` | Decimal numbers | `3.14` |
| `boolean` | True/False | `true` or `false` |
| `char` | Single character | `'A'` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: incompatible types` | Wrong data type | Match the type to the value |
| `error: ';' expected` | Missing semicolon | Add `;` at end of statement |
| `error: cannot find symbol` | Typo in variable name | Check spelling matches declaration |

### Bonus Knowledge

- **Type Safety**: Java forces you to declare types upfront (prevents bugs!)
- **Variable Naming**: Use camelCase like `myVariable`, not `my_variable` or `MYVARIABLE`
- **Scope**: Variables exist within their `{ }` block

---

**Great progress! You're learning the building blocks of programming.**

*Next: Basic Math Operations!*
