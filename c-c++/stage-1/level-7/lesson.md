# Level 7: Functions - Code Organization

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the pinnacle of Stage 1! Today you'll learn about functions - the building blocks of organized, reusable code. Functions allow you to break complex programs into smaller, manageable pieces. Think of functions as mini-programs within your program!

---

### Learning Goals

- [ ] Understand what functions are and why they're essential
- [ ] Learn function declaration, definition, and calling
- [ ] Master parameters and return values
- [ ] Practice function overloading concepts
- [ ] Learn about scope and lifetime of variables
- [ ] Create modular, organized programs

---

### Your Task

**Copy the following code into a new file called `functions.c`**

```c
# include <stdio.h>

// Function declarations (prototypes)
void print_welcome();
void print_line(char symbol, int length);
int add_numbers(int a, int b);
float calculate_average(int sum, int count);
void display_menu();
int get_user_choice();
void process_choice(int choice);
int factorial(int n);
void print_number_pattern(int rows);
int find_maximum(int a, int b, int c);
void swap_values(int* x, int* y);
int is_prime(int number);
void generate_primes(int limit);

// Global variables (use sparingly!)
int global_counter = 0;

int main() {
    std::cout << "=== Functions: The Building Blocks of Code ===\n\n");
    
    // 1. Simple function calls
    print_welcome();
    print_line('=', 50);
    
    // 2. Functions with return values
    int num1 = 10, num2 = 20;
    int sum = add_numbers(num1, num2);
    std::cout << "Sum of %d and %d is: %d\n", num1, num2, sum);
    
    // 3. Functions with calculations
    int scores[] = {85, 92, 78, 96, 88};
    int total_scores = 0;
    
    for (int i = 0; i < 5; i++) {
        total_scores += scores[i];
    }
    
    float average = calculate_average(total_scores, 5);
    std::cout << "Average score: %.1f%%\n", average);
    print_line('-', 30);
    
    // 4. Interactive menu system
    int choice;
    do {
        display_menu();
        choice = get_user_choice();
        process_choice(choice);
    } while (choice != 5);
    
    // 5. Mathematical functions
    print_line('=', 50);
    std::cout << "=== Mathematical Functions ===\n");
    
    int fact_num;
    std::cout << "Enter a number to calculate factorial: ");
    scanf("%d", &fact_num);
    
    if (fact_num >= 0 && fact_num <= 12) {
        int result = factorial(fact_num);
        std::cout << "%d! = %d\n", fact_num, result);
    } else {
        std::cout << "Please enter a number between 0 and 12.\n");
    }
    
    // 6. Pattern generation
    std::cout << "\n=== Number Patterns ===\n");
    int pattern_rows;
    std::cout << "How many rows for the pattern? ");
    scanf("%d", &pattern_rows);
    print_number_pattern(pattern_rows);
    
    // 7. Functions with multiple parameters
    std::cout << "\n=== Finding Maximum Values ===\n");
    int a, b, c;
    std::cout << "Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    
    int max = find_maximum(a, b, c);
    std::cout << "Maximum of %d, %d, %d is: %d\n", a, b, c, max);
    
    // 8. Functions with pointers (advanced)
    std::cout << "\n=== Swapping Values ===\n");
    int x = 100, y = 200;
    std::cout << "Before swap: x = %d, y = %d\n", x, y);
    swap_values(&x, &y);
    std::cout << "After swap:  x = %d, y = %d\n", x, y);
    
    // 9. Prime number generator
    std::cout << "\n=== Prime Number Generator ===\n");
    int prime_limit;
    std::cout << "Generate primes up to what number? ");
    scanf("%d", &prime_limit);
    
    if (prime_limit > 1 && prime_limit <= 1000) {
        generate_primes(prime_limit);
    } else {
        std::cout << "Please enter a number between 2 and 1000.\n");
    }
    
    // 10. Global variable demonstration
    std::cout << "\n=== Global Variables Demo ===\n");
    std::cout << "Global counter starts at: %d\n", global_counter);
    global_counter += 10;
    std::cout << "After adding 10: %d\n", global_counter);
    
    print_line('=', 50);
    std::cout << " Congratulations! You've mastered functions!\n");
    std::cout << "Your code is now organized, reusable, and maintainable!\n");
    
    return 0;
}

// Function definitions

void print_welcome() {
    std::cout << " Welcome to the Functions Learning Program! \n");
    std::cout << "Functions help us organize code into reusable pieces.\n\n");
}

void print_line(char symbol, int length) {
    for (int i = 0; i < length; i++) {
        std::cout << "%c", symbol);
    }
    std::cout << "\n");
}

int add_numbers(int a, int b) {
    int result = a + b;
    return result;
}

float calculate_average(int sum, int count) {
    if (count == 0) {
        return 0.0f;
    }
    return (float)sum / count;
}

void display_menu() {
    std::cout << "\n=== MAIN MENU ===\n");
    std::cout << "1. Calculate area of circle\n");
    std::cout << "2. Convert temperature (C to F)\n");
    std::cout << "3. Check if number is even or odd\n");
    std::cout << "4. Generate random number\n");
    std::cout << "5. Exit\n");
}

int get_user_choice() {
    int choice;
    std::cout << "Enter your choice (1-5): ");
    scanf("%d", &choice);
    return choice;
}

void process_choice(int choice) {
    switch (choice) {
        case 1: {
            float radius;
            std::cout << "Enter radius: ");
            scanf("%f", &radius);
            float area = 3.14159 * radius * radius;
            std::cout << "Area of circle: %.2f\n", area);
            break;
        }
        case 2: {
            float celsius;
            std::cout << "Enter temperature in Celsius: ");
            scanf("%f", &celsius);
            float fahrenheit = (celsius * 9.0/5.0) + 32;
            std::cout << "%.1f°C = %.1f°F\n", celsius, fahrenheit);
            break;
        }
        case 3: {
            int num;
            std::cout << "Enter a number: ");
            scanf("%d", &num);
            if (num % 2 == 0) {
                std::cout << "%d is even\n", num);
            } else {
                std::cout << "%d is odd\n", num);
            }
            break;
        }
        case 4: {
            // Simple pseudo-random number
            int random_num = (global_counter * 7 + 13) % 100;
            global_counter++;
            std::cout << "Random number: %d\n", random_num);
            break;
        }
        case 5:
            std::cout << "Goodbye!\n");
            break;
        default:
            std::cout << "Invalid choice! Please try again.\n");
            break;
    }
}

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

void print_number_pattern(int rows) {
    for (int i = 1; i <= rows; i++) {
        // Print spaces
        for (int space = 1; space <= rows - i; space++) {
            std::cout << " ");
        }
        
        // Print numbers
        for (int num = 1; num <= i; num++) {
            std::cout << "%d ", num);
        }
        
        std::cout << "\n");
    }
}

int find_maximum(int a, int b, int c) {
    int max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    return max;
}

void swap_values(int* x, int* y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

int is_prime(int number) {
    if (number <= 1) return 0;
    if (number <= 3) return 1;
    if (number % 2 == 0 || number % 3 == 0) return 0;
    
    for (int i = 5; i * i <= number; i += 6) {
        if (number % i == 0 || number % (i + 2) == 0) {
            return 0;
        }
    }
    return 1;
}

void generate_primes(int limit) {
    std::cout << "Prime numbers up to %d:\n", limit);
    int count = 0;
    
    for (int num = 2; num <= limit; num++) {
        if (is_prime(num)) {
            std::cout << "%d ", num);
            count++;
            
            if (count % 10 == 0) { // New line every 10 primes
                std::cout << "\n");
            }
        }
    }
    
    if (count % 10 != 0) {
        std::cout << "\n");
    }
    std::cout << "Total primes found: %d\n", count);
}
```bash

---

### How to Run

1. **Compile the code**:
   ```bash
   g++ functions.c -o functions
   ```bash
2. **Run your program**:
   ```bash
   ./functions
   ```bash
3. **Explore all the different function examples!**

---

### Success Checklist

- [ ] Created a file named `functions.c`
- [ ] Copied all code correctly
- [ ] Compiled without errors
- [ ] Ran the program and tested all function types
- [ ] Used the interactive menu system
- [ ] Experienced mathematical functions, patterns, and prime generation
- [ ] Understood how functions organize and reuse code

---

### Key Function Concepts

1. **Function Declaration** - Tells compiler about function (prototype)
2. **Function Definition** - The actual function implementation
3. **Function Call** - Using the function in your code
4. **Parameters** - Input values passed to functions
5. **Return Values** - Output values from functions
6. **Scope** - Where variables are accessible

---

### Try This (Optional Challenges)

1. Add a new menu option to the program
2. Create a function to calculate Fibonacci numbers
3. Modify the prime generator to show prime factors
4. Add input validation to the menu system

---

## Quick Reference

### Function Components
| Component | Example | Purpose |
|-----------|---------|---------|
| Return type | `int`, `void`, `float` | What the function returns |
| Function name | `calculate_sum` | How to call the function |
| Parameters | `(int a, int b)` | Input values |
| Body | `{ return a + b; }` | Function implementation |

### Common Function Types
| Type | Example | Use Case |
|------|---------|----------|
| Void functions | `void print_menu()` | Display information |
| Return functions | `int add(int a, int b)` | Calculate and return values |
| Parameter functions | `void process(int x)` | Take input, perform actions |

---

### Common Function Mistakes

1. **Missing return type**
   ```c
   add_numbers(int a, int b) { // WRONG - missing int!
       return a + b;
   }
   ```bash

2. **Wrong parameter types**
   ```c
   void print_number(int num) {
       std::cout << "%f", num); // WRONG - %f for int!
   }
   ```bash

3. **Not calling the function**
   ```c
   int result = add_numbers; // WRONG - missing ()!
   ```bash

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

#### 1. Function Declaration vs Definition

```c
// Declaration (prototype) - tells compiler about function
void print_welcome();

// Definition - the actual implementation
void print_welcome() {
    std::cout << " Welcome to the Functions Learning Program! \n");
}
```bash

**Why declarations?**
- [ ] Allows functions to be defined after `main()`
- [ ] Enables mutual recursion
- [ ] Helps catch type mismatches

#### 2. Function Parameters and Return Values

```c
int add_numbers(int a, int b) {
    int result = a + b;
    return result;
}

// Usage:
int sum = add_numbers(10, 20); // sum = 30
```bash

**Parameter Passing:**
- [ ] **By value**: Copies are made (changes don't affect original)
- [ ] **By reference**: Uses pointers (changes affect original)

#### 3. Void Functions

```c
void print_line(char symbol, int length) {
    for (int i = 0; i < length; i++) {
        std::cout << "%c", symbol);
    }
    std::cout << "\n");
}
```bash

**Characteristics:**
- [ ] No return value
- [ ] Used for actions (printing, modifying global state)
- [ ] Can have parameters

#### 4. Functions with Calculations

```c
float calculate_average(int sum, int count) {
    if (count == 0) {
        return 0.0f; // Handle edge case
    }
    return (float)sum / count; // Cast to float for decimal division
}
```bash

**Best Practices:**
- [ ] Handle edge cases (division by zero, empty arrays)
- [ ] Use appropriate return types
- [ ] Document what the function does

#### 5. Modular Menu System

```c
void display_menu() {
    std::cout << "\n=== MAIN MENU ===\n");
    // ... menu options
}

int get_user_choice() {
    int choice;
    std::cout << "Enter your choice (1-5): ");
    scanf("%d", &choice);
    return choice;
}

void process_choice(int choice) {
    switch (choice) {
        case 1: /* handle choice 1 */ break;
        case 2: /* handle choice 2 */ break;
        // ...
    }
}
```bash

**Benefits of modular design:**
- [ ] Each function has a single responsibility
- [ ] Easy to test individual components
- [ ] Code is more readable and maintainable

### Advanced Function Concepts

#### Recursion

```c
int factorial_recursive(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial_recursive(n - 1);
}
```bash

**Recursion vs Iteration:**
- [ ] **Recursion**: Function calls itself, uses stack memory
- [ ] **Iteration**: Uses loops, generally more efficient
- [ ] **When to use recursion**: Natural recursive problems (trees, factorial)

#### Function Pointers

```c
int add(int a, int b) { return a + b; }
int multiply(int a, int b) { return a * b; }

int main() {
    int (*operation)(int, int); // Function pointer
    
    operation = add;
    std::cout << "5 + 3 = %d\n", operation(5, 3));
    
    operation = multiply;
    std::cout << "5 * 3 = %d\n", operation(5, 3));
    
    return 0;
}
```bash

**Uses:**
- [ ] Callbacks
- [ ] Strategy patterns
- [ ] Dynamic function selection

#### Variable Scope and Lifetime

```c
int global_var = 10; // Global scope - accessible everywhere

void function() {
    int local_var = 20; // Local scope - only in this function
    static int static_var = 30; // Static - persists between calls
}

int main() {
    function();
    // Can access global_var here
    // Cannot access local_var or static_var here
    return 0;
}
```bash

**Scope Rules:**
- [ ] **Global**: Accessible everywhere in the file
- [ ] **Local**: Only within the function/block
- [ ] **Static**: Persists but scoped to function
- [ ] **Block**: Within `{}` braces

#### Function Overloading (C++ concept, not C)

```c
// This doesn't work in C, but here's the concept:
// int add(int a, int b);
// float add(float a, float b);
// char* add(char* a, char* b); // Concatenate strings
```bash

**C equivalent:**
```c
int add_int(int a, int b);
float add_float(float a, float b);
char* concat_strings(char* a, char* b);
```bash

### Best Practices for Functions

#### 1. Single Responsibility Principle

```c
// Good - one clear purpose
void print_student_report(Student s) {
    std::cout << "Name: %s\n", s.name);
    std::cout << "Grade: %c\n", s.grade);
    std::cout << "GPA: %.2f\n", s.gpa);
}

// Bad - multiple responsibilities
void process_student(Student s) {
    // Calculate GPA
    // Print report
    // Save to file
    // Send email
}
```bash

#### 2. Meaningful Names

```c
// Good
int calculate_monthly_payment(float principal, float rate, int months);
void validate_user_input(char* input, int max_length);

// Bad
int calc(float p, float r, int m);
void check(char* i, int l);
```bash

#### 3. Parameter Validation

```c
int divide(int dividend, int divisor) {
    if (divisor == 0) {
        std::cout << "Error: Division by zero!\n");
        return 0;
    }
    return dividend / divisor;
}
```bash

#### 4. Documentation

```c
/**
 * Calculates the area of a circle given its radius.
 * @param radius The radius of the circle (must be positive)
 * @return The area of the circle
 */
float calculate_circle_area(float radius) {
    if (radius < 0) {
        return 0.0f; // Invalid input
    }
    return 3.14159f * radius * radius;
}
```bash

### Common Function Patterns

#### Calculator Functions

```c
float add(float a, float b) { return a + b; }
float subtract(float a, float b) { return a - b; }
float multiply(float a, float b) { return a + b; }
float divide(float a, float b) {
    return (b != 0) ? a / b : 0;
}
```bash

#### Validation Functions

```c
int is_valid_email(char* email) {
    // Check for @ symbol, proper format, etc.
    return 1; // or 0
}

int is_valid_age(int age) {
    return age >= 0 && age <= 150;
}
```bash

#### Utility Functions

```c
void clear_screen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void pause_program() {
    std::cout << "Press Enter to continue...");
    getchar();
}
```bash

### Debugging Functions

#### Function Entry/Exit Logging

```c
void debug_enter(const char* function_name) {
    std::cout << "DEBUG: Entering %s()\n", function_name);
}

void debug_exit(const char* function_name) {
    std::cout << "DEBUG: Exiting %s()\n", function_name);
}

int add_with_debug(int a, int b) {
    debug_enter("add_with_debug");
    int result = a + b;
    std::cout << "DEBUG: %d + %d = %d\n", a, b, result);
    debug_exit("add_with_debug");
    return result;
}
```bash

#### Parameter Validation

```c
# define ASSERT(condition, message) \
    if (!(condition)) { \
        std::cout << "ASSERTION FAILED: %s\n", message); \
        return; \
    }

void process_data(int* data, int size) {
    ASSERT(data != NULL, "data pointer cannot be NULL");
    ASSERT(size > 0, "size must be positive");
    // ... rest of function
}
```bash

### Performance Considerations

#### Inline Functions (C99)

```c
inline int max(int a, int b) {
    return (a > b) ? a : b;
}
```bash

**Benefits:**
- [ ] Eliminates function call overhead
- [ ] Good for small, frequently called functions

#### Function Call Overhead

```c
// Less efficient - function call for simple operation
for (int i = 0; i < 1000000; i++) {
    result += increment_by_one(i);
}

// More efficient - inline the operation
for (int i = 0; i < 1000000; i++) {
    result += i + 1;
}
```bash

### Real-World Function Examples

#### File Operations

```c
int load_config(const char* filename, Config* config) {
    FILE* file = fopen(filename, "r");
    if (!file) return 0;
    
    // Read configuration
    // ...
    
    fclose(file);
    return 1;
}
```bash

#### Error Handling

```c
typedef enum {
    ERROR_NONE = 0,
    ERROR_FILE_NOT_FOUND,
    ERROR_INVALID_DATA,
    ERROR_MEMORY_ALLOCATION
} ErrorCode;

ErrorCode process_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) return ERROR_FILE_NOT_FOUND;
    
    // Process file
    // ...
    
    if (/* some error condition */) {
        fclose(file);
        return ERROR_INVALID_DATA;
    }
    
    fclose(file);
    return ERROR_NONE;
}
```bash

---

 **INCREDIBLE! You've mastered functions - the cornerstone of organized programming!** 

*Congratulations on completing Stage 1: Copying Code! You're now ready to move to Stage 2: Making Code from Pseudocode! *

---

### STAGE 1 COMPLETE! 

**What you've learned:**
- [ ]  Basic program structure
- [ ]  Variables and data types  
- [ ]  Mathematical operations
- [ ]  User input and output
- [ ]  Decision making with conditionals
- [ ]  Repetition with loops
- [ ]  Code organization with functions

**Next Steps:**
1. Practice these concepts by redoing lessons
2. Move to Stage 2: Pseudocode to Code
3. Start thinking about problems before coding solutions

*Keep coding! Your programming journey has just begun! *

### Additional Content

Understand the key concepts:

- [ ] Review each function
- [ ] Understand the flow
- [ ] Learn the patterns used


### Code Review

Key functions and their purpose:

- [ ] Main function: Entry point
- [ ] Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses std::cout to print messages to the console
3. **Standard Library**: Includes iostream for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `g++ hello.cpp -o hello`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: g++` | Compiler not installed | `sudo apt install g++` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: unknown type name 'cout'` | Missing iostream | Add `#include <iostream>` |

### Tips for Learning

- C++ is a superset of C with additional features
- `std::cout` is the C++ way to print (replaces `printf`)
- `std::endl` adds a newline and flushes the buffer
- The `std::` prefix means these are from the "standard" namespace
