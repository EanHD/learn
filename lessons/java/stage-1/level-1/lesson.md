# Level 1: Hello World

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Welcome to your first step into programming with Java! Today, you'll learn how to create your very first Java program. Don't worry about understanding everything yet - just focus on getting the code typed correctly and watching it work!

---

### Learning Goals

- Understand the basic structure of a Java program
- Learn how to run Java code
- See your first program output "Hello, World!"
- Get comfortable with your text editor and Java syntax

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.java`**

```
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

---

### How to Run

**Method 1 (Vim - Recommended):**
```
<Space>r
```

**Method 2 (Terminal):**
```
javac main.java
java Main
```

**Expected output:**
```
Hello, World!
```

---

### Success Checklist

- [ ] Created a file named `main.java`
- [ ] Copied all the code exactly as shown
- [ ] Compiled with `javac main.java`
- [ ] Ran with `java Main`
- [ ] Saw "Hello, World!" printed on screen

---

### What Happened?

You just created your first real Java program! Here's what each part does:

- `public class Main` - Declares a class (must match filename)
- `public static void main(String[] args)` - The entry point where Java starts
- `System.out.println(...)` - Prints text to the screen
- `"Hello, World!"` - The message to print (a string)

---

### Try This (Optional Challenges)

If you're feeling brave, try these small changes:

1. Change the message to "Hello, Java!"
2. Add another `System.out.println()` with your name
3. Remove one semicolon and see what error appears

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

- **`public class Main`** = Class declaration (public = accessible everywhere)
- **`main`** = Special method where Java starts execution
- **`String[] args`** = Command-line arguments (ignore for now)
- **`System.out.println()`** = Built-in function that prints text and adds newline
- **`"Hello, World!"`** = String literal enclosed in double quotes
- **`;`** = Semicolon ends each statement
- **`{` and `}`** = Braces group code blocks

### Execution Process

1. **Compilation**: `javac` translates Java to bytecode
2. **Execution**: `java Main` starts the JVM and runs your code
3. **Output**: "Hello, World!" prints to console
4. **Termination**: Program exits

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: class Main is public, should be declared in a file named Main.java` | Filename doesn't match class name | Rename to `main.java` and class to `Main` |
| `Exception in thread "main" java.lang.NoClassDefFoundError: Main` | Main class not found | Check file is compiled: `javac main.java` first |
| `error: ';' expected` | Missing semicolon | Add `;` at end of each statement |
| `error: cannot find symbol` | Typo in code | Check spelling exactly (Java is case-sensitive) |
| `javac: command not found` | Java not installed | Install JDK: `sudo apt install default-jdk` |

### Bonus Knowledge

- **Java History**: Created by James Gosling at Sun Microsystems (1995)
- **"Write Once, Run Anywhere"**: Java bytecode runs on any JVM
- **Case Sensitive**: `main` ≠ `Main` ≠ `MAIN`
- **Mandatory Class**: Every Java program must have at least one class

---

**Congratulations! You've written your first Java program!**

*Keep moving forward - next up: Variables!*
