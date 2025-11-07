# Level 7: Functions and First Look at Classes

> **LESSON NOTE:** This lesson file is **read-only**. Write your code in `main.cpp` in the right window.

## Stage 1: Organizing Code with Functions

### Learning Goals

- Create and call functions
- Understand parameters and return values
- See a preview of C++ classes
- Understand code organization

---

### Your Task

Create `main.cpp`:

```
#include <iostream>
using namespace std;

// Function declarations
int add(int a, int b);
float calculateBMI(float weight, float height);
void printWelcome(string name);

// Simple class preview
class Calculator {
public:
    int multiply(int a, int b) {
        return a * b;
    }

    float divide(float a, float b) {
        if (b != 0) {
            return a / b;
        }
        return 0;
    }
};

int main() {
    // Using functions
    cout << "=== Functions Demo ===\n";

    string name;
    cout << "Enter your name: ";
    cin >> name;
    printWelcome(name);

    int x = 10, y = 5;
    int sum = add(x, y);
    cout << x << " + " << y << " = " << sum << "\n";

    float weight, height;
    cout << "\nEnter weight (kg): ";
    cin >> weight;
    cout << "Enter height (m): ";
    cin >> height;

    float bmi = calculateBMI(weight, height);
    cout << "Your BMI: " << bmi << "\n";

    // Using a class (preview!)
    cout << "\n=== Class Demo ===\n";
    Calculator calc;
    cout << "15 * 3 = " << calc.multiply(15, 3) << "\n";
    cout << "20 / 4 = " << calc.divide(20, 4) << "\n";

    return 0;
}

// Function definitions
void printWelcome(string name) {
    cout << "\nWelcome, " << name << "!\n";
}

int add(int a, int b) {
    return a + b;
}

float calculateBMI(float weight, float height) {
    return weight / (height * height);
}
```

### Compile and Run

```
g++ main.cpp -o main
./main
```

---

### Function Structure

```
returnType functionName(parameters) {
    // code
    return value;
}
```

- **Return type**: `int`, `float`, `void` (no return), etc.
- **Parameters**: Input values (optional)
- **Return**: Send a value back to caller

---

### Classes - A Preview

```
class ClassName {
public:
    // Functions (called "methods")
    returnType methodName() {
        // code
    }
};
```

Classes group related functions together. We'll learn more in Stage 2!

---

### Why Functions?

- **Reusability**: Write once, use many times
- **Organization**: Break big problems into small pieces
- **Readability**: Named functions explain what code does
- **Testing**: Easier to test small functions

---

### Try This

1. Create a `square()` function that returns n * n
2. Make a `greet()` function that takes name and age
3. Write an `isEven()` function that returns true/false
4. Add another method to the Calculator class (like `subtract()`)

---

### Common Mistakes

- Forgetting return statement in non-void functions
- Mismatched parameter types
- Calling function before declaring it
- Forgetting semicolon after class definition

---

### What's Next?

You've completed Stage 1! You now know:
- ✓ C basics (printf, scanf, variables)
- ✓ C++ improvements (cout, cin, strings)
- ✓ Control flow (if, loops)
- ✓ Functions and basic classes

**Stage 2** will dive deeper into:
- Object-Oriented Programming (OOP)
- Classes and objects
- Pointers and memory
- Data structures

---

**Congratulations on finishing Stage 1! 🎉**

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```
#include <iostream>
using namespace std;

// Function declarations
int add(int a, int b);
float calculateBMI(float weight, float height);
void printWelcome(string name);

// Simple class preview
class Calculator {
public:
    int multiply(int a, int b) {
        return a * b;
    }

    float divide(float a, float b) {
        if (b != 0) {
            return a / b;
        }
        return 0;
    }
};

int main() {
    // Using functions
    cout << "=== Functions Demo ===\n";

    string name;
    cout << "Enter your name: ";
    cin >> name;
    printWelcome(name);

    int x = 10, y = 5;
    int sum = add(x, y);
    cout << x << " + " << y << " = " << sum << "\n";

    float weight, height;
    cout << "\nEnter weight (kg): ";
    cin >> weight;
    cout << "Enter height (m): ";
    cin >> height;

    float bmi = calculateBMI(weight, height);
    cout << "Your BMI: " << bmi << "\n";

    // Using a class (preview!)
    cout << "\n=== Class Demo ===\n";
    Calculator calc;
    cout << "15 * 3 = " << calc.multiply(15, 3) << "\n";
    cout << "20 / 4 = " << calc.divide(20, 4) << "\n";

    return 0;
}

// Function definitions
void printWelcome(string name) {
    cout << "\nWelcome, " << name << "!\n";
}

int add(int a, int b) {
    return a + b;
}

float calculateBMI(float weight, float height) {
    return weight / (height * height);
}
```

### Explanation

This solution demonstrates the key concepts from this lesson:

1. **Basic Structure**: The program follows the standard structure for this language
2. **Output**: The code produces the expected output
3. **Syntax**: Pay attention to the syntax details - they're important!

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
