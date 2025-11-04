# Java Workspace Instructions

## Getting Started with Java

Welcome to Java programming! This section explains how to set up your workspace and get ready to code.

---

## Prerequisites

### 1. Install Java Development Kit (JDK)

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install default-jdk
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install java-devel
```

**macOS:**
```bash
brew install openjdk
# Or use:
brew cask install adoptopenjdk
```

**Windows:**
- Download from [Oracle JDK](https://www.oracle.com/java/technologies/downloads/)
- Or use Windows Package Manager: `winget install Oracle.JDK.21`

### 2. Verify Installation

```bash
javac -version
java -version
```

Both should return version information. If not, Java isn't in your PATH.

---

## Workspace Setup

When you run `learn open java 1`, the system creates:

```
java/
├── stage-1/
│   └── level-1/
│       ├── lesson.md          (Read-only lesson)
│       └── main.java          (Blank file for your code)
└── [more stages and levels]
```

### Key Files

- **lesson.md** - The lesson (read-only, left window)
- **main.java** - Your code goes here (blank, right window)

---

## Compilation and Execution

### Method 1: Vim Shortcut (Recommended)

When editing `main.java` in Vim:

```
<Space>r   → Compile and run
<Space>h   → Show help for current language
```

This automatically:
1. Saves your file
2. Compiles with `javac`
3. Runs with `java Main`
4. Shows output

### Method 2: Terminal Commands

```bash
# Compile
javac main.java

# Run
java Main
```

### Important: Class Name

Java requires the **class name** to match the **filename**:

```java
public class Main {  // Must match main.java
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

If you get `Error: Main class not found`, check:
1. Class name is `Main` (capitalized)
2. File is named `main.java`
3. No typos in the class declaration

---

## Your First Program

Create this in `main.java`:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

Then compile and run:

```bash
javac main.java
java Main
```

Expected output:
```
Hello, Java!
```

---

## Common Setup Issues

### Issue: "javac: command not found"

**Solution:** Java isn't installed or not in PATH.

```bash
# Check Java location
which javac

# If empty, install Java (see Prerequisites above)
```

### Issue: "Main class not found in file Main.java"

**Solution:** Class name must match filename exactly.

```java
// WRONG - filename is main.java but class is Main
public class Main {  // This is correct capitalization

// CORRECT - both match
public class Main {
    public static void main(String[] args) { ... }
}
```

### Issue: Cannot access jdk.internal

**Solution:** You likely used an old Java version or mixed JDK versions.

```bash
# Check version
java -version

# Update to JDK 11+
```

---

## Best Practices

### 1. File Structure
- Always name your file `main.java`
- Class name should be `Main` (public)
- Follow Java naming conventions (CamelCase for classes)

### 2. Code Style
- Indentation: 4 spaces (configured automatically)
- Use meaningful variable names
- Add comments explaining complex logic

### 3. Debugging
- Use `System.out.println()` to debug
- Watch indentation carefully (Java requires proper braces)
- Check for semicolons at end of statements

---

## Editor Setup

### Neovim (Recommended)

Neovim automatically loads:
- Syntax highlighting for Java
- LSP (Language Server Protocol) for errors/completions
- Keybindings for compile/run

No additional setup needed!

### VS Code

```bash
# Install Extensions
- "Extension Pack for Java" by Microsoft
- "Language Support for Java" (Red Hat)

# Then open main.java and start coding
```

---

## Learning Java: Key Concepts

### Basic Structure
Every Java program needs a class and a `main` method:

```java
public class MyProgram {
    public static void main(String[] args) {
        // Your code goes here
    }
}
```

### The `public static void main` Line

- `public` - Accessible everywhere
- `static` - Belongs to class, not objects
- `void` - Doesn't return anything
- `main` - Entry point
- `String[] args` - Command-line arguments

Don't worry about this now - you'll understand it through practice!

### Common Java Gotchas

1. **Semicolons required** - Each statement ends with `;`
2. **Braces matter** - `{` and `}` structure your code
3. **Case-sensitive** - `main` ≠ `Main` (though they're different things)
4. **Type declarations** - Variables need types: `int x = 5;`

---

## Next Steps

1. ✅ Install Java and verify with `javac -version`
2. ✅ Open your first lesson: `learn open java 1 1`
3. ✅ Copy the code from the lesson into `main.java`
4. ✅ Press `<Space>r` to run it
5. ✅ See your program work!

---

## Resources

- [Oracle Java Documentation](https://docs.oracle.com/en/java/)
- [Java Tutorials](https://docs.oracle.com/javase/tutorial/)
- [Stack Overflow Tag: java](https://stackoverflow.com/questions/tagged/java)

---

Happy coding! Java is powerful - take your time and enjoy the journey.
