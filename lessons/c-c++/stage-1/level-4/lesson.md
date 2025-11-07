# Level 4: Conditionals and Logic in C

> **LESSON NOTE:** This lesson file is **read-only**. Write your code in `main.c` in the right window.

## Stage 1: Making Decisions

### Learning Goals

- Use `if`, `else if`, `else` statements
- Understand comparison operators
- Use logical operators (&&, ||, !)
- Build a simple decision-making program

---

### Your Task

Create `main.c`:

```c
#include <stdio.h>

int main() {
    int age;
    float temperature;
    char hasUmbrella;

    // Get input
    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Enter temperature (F): ");
    scanf("%f", &temperature);

    printf("Do you have an umbrella? (y/n): ");
    scanf(" %c", &hasUmbrella);

    // Age-based message
    printf("\n--- Analysis ---\n");
    if (age < 13) {
        printf("You're a kid!\n");
    } else if (age < 20) {
        printf("You're a teenager!\n");
    } else if (age < 65) {
        printf("You're an adult!\n");
    } else {
        printf("You're a senior!\n");
    }

    // Weather advice
    if (temperature > 85) {
        printf("It's hot! Stay hydrated.\n");
    } else if (temperature < 32) {
        printf("It's freezing! Bundle up!\n");
    } else {
        printf("Weather is nice!\n");
    }

    // Multiple conditions
    if (temperature < 50 && hasUmbrella == 'n') {
        printf("Warning: Cold and no umbrella!\n");
    }

    // Logical NOT
    if (!(age >= 18)) {
        printf("You're not an adult yet.\n");
    }

    return 0;
}
```

### Compile and Run

```
gcc main.c -o main
./main
```

---

### Comparison Operators

- `==` - Equal to
- `!=` - Not equal to
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal
- `>=` - Greater than or equal

---

### Logical Operators

- `&&` - AND (both must be true)
- `||` - OR (at least one must be true)
- `!` - NOT (inverts the condition)

---

### Try This

1. Add a check: if age is exactly 18, print "You just became an adult!"
2. Create a grade checker (A: 90+, B: 80+, C: 70+, etc.)
3. Make a simple calculator that checks if division by zero
4. Use `&&` to check if someone is a "teenager with an umbrella"

---

### Common Mistakes

- Using `=` instead of `==` for comparison
- Forgetting braces `{}` with multiple statements
- Confusing `&&` (AND) with `||` (OR)
- Not handling all cases (missing `else`)

---

**Next: Transitioning from C to C++!**
