# Level 3: User Input with scanf() in C

> **LESSON NOTE:** This lesson file is **read-only**. Write your code in `main.c` in the right window.

## Stage 1: Getting User Input

### Learning Goals

- Use `scanf()` to read user input
- Understand the address-of operator `&`
- Combine input and output
- Handle different data types

---

### Your Task

Create `main.c`:

```c
#include <stdio.h>

int main() {
    int age;
    float height;
    char initial;
    
    // Get user input
    printf("Enter your age: ");
    scanf("%d", &age);
    
    printf("Enter your height in feet: ");
    scanf("%f", &height);
    
    printf("Enter your first initial: ");
    scanf(" %c", &initial);  // Note the space before %c
    
    // Display results
    printf("\n--- Your Info ---\n");
    printf("Initial: %c\n", initial);
    printf("Age: %d years old\n", age);
    printf("Height: %.1f feet\n", height);
    
    // Calculate something
    int months = age * 12;
    printf("That's %d months!\n", months);
    
    return 0;
}
```

### Compile and Run

```
gcc main.c -o main
./main
```

---

### Understanding scanf()

```c
scanf("%d", &age);
```

- `scanf()` - Reads formatted input
- `"%d"` - Format specifier (what type to read)
- `&age` - Address of variable (where to store it)

**Important:** You MUST use `&` with scanf() for basic types!

---

### The & Operator

- `age` - The value in the variable
- `&age` - The memory address where the variable is stored
- `scanf()` needs the address to store the input

---

### Try This

1. Add a question for the user's favorite number
2. Calculate their age in days (age * 365)
3. Ask for two numbers and print their sum
4. Try removing `&` from scanf() - what happens?

---

### Common Issues

- **Forgetting `&`** - Program crashes or weird behavior
- **Space before %c** - Without it, scanf reads leftover newline
- **Wrong format** - Using %d for float causes errors
- **Buffer problems** - We'll learn better input methods later

---

**Next: Conditional logic with if statements!**
