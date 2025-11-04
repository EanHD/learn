# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Get ready to make your programs interactive! Today you'll learn how to talk to your users - getting information from them and responding to what they type. This is where programs start to feel like real applications instead of just calculators.

---

### Learning Goals

- [ ] Learn how to read user input with `scanf()`
- [ ] Understand format specifiers for input
- [ ] Practice with different data types (int, float, char, strings)
- [ ] Learn input validation techniques
- [ ] Create interactive programs that respond to user data

---

### Your Task

**Copy the following code into a new file called `user_input.c`**

```c
# include <stdio.h>

int main() {
    // Variables to store user input
    int age;
    float height;
    char grade;
    char name[50];  // String for name (character array)
    
    std::cout << "=== Personal Information Form ===\n\n");
    
    // Get user's name
    std::cout << "What's your first name? ");
    scanf("%s", name);
    
    // Get user's age
    std::cout << "How old are you? ");
    scanf("%d", &age);
    
    // Get user's height
    std::cout << "What's your height in inches? ");
    scanf("%f", &height);
    
    // Get user's grade
    std::cout << "What's your letter grade (A, B, C, D, F)? ");
    scanf(" %c", &grade);  // Note the space before %c!
    
    std::cout << "\n=== Your Information Summary ===\n");
    std::cout << "Name: %s\n", name);
    std::cout << "Age: %d years old\n", age);
    std::cout << "Height: %.1f inches\n", height);
    std::cout << "Grade: %c\n", grade);
    
    // Calculate some interesting facts
    std::cout << "\n=== Interesting Facts ===\n");
    
    // Height in centimeters
    float height_cm = height * 2.54;
    std::cout << "Height in centimeters: %.1f cm\n", height_cm);
    
    // Age in different units
    std::cout << "Age in months: %d\n", age * 12);
    std::cout << "Age in days (approximately): %d\n", age * 365);
    
    // Grade analysis
    std::cout << "\n=== Grade Analysis ===\n");
    if (grade == 'A' || grade == 'a') {
        std::cout << "Excellent work! You're doing great!\n");
    } else if (grade == 'B' || grade == 'b') {
        std::cout << "Good job! Keep up the good work!\n");
    } else if (grade == 'C' || grade == 'c') {
        std::cout << "Not bad, but there's room for improvement.\n");
    } else {
        std::cout << "Keep trying! You can do this!\n");
    }
    
    // BMI calculation (simplified)
    std::cout << "\n=== Health Calculator ===\n");
    float weight_pounds;
    std::cout << "Enter your weight in pounds: ");
    scanf("%f", &weight_pounds);
    
    float bmi = (weight_pounds * 703) / (height * height);
    std::cout << "Your BMI: %.1f\n", bmi);
    
    if (bmi < 18.5) {
        std::cout << "Category: Underweight\n");
    } else if (bmi < 25) {
        std::cout << "Category: Normal weight\n");
    } else if (bmi < 30) {
        std::cout << "Category: Overweight\n");
    } else {
        std::cout << "Category: Obese\n");
    }
    
    std::cout << "\n=== Future Prediction ===\n");
    int future_years;
    std::cout << "How many years into the future should we predict? ");
    scanf("%d", &future_years);
    
    std::cout << "In %d years, you'll be %d years old!\n", future_years, age + future_years);
    
    std::cout << "\nThanks for using the personal info calculator, %s!\n", name);
    
    return 0;
}
```bash

---

### How to Run

1. **Compile the code**:
   ```bash
   g++ user_input.c -o user_input
   ```bash
2. **Run your program**:
   ```bash
   ./user_input
   ```bash
3. **Follow the prompts** and enter your information when asked!

**Example interaction:**
```bash
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
Enter your weight in pounds: 150
Your BMI: 21.5
Category: Normal weight

=== Future Prediction ===
How many years into the future should we predict? 10
In 10 years, you'll be 35 years old!

Thanks for using the personal info calculator, Alex!
```bash

---

### Success Checklist

- [ ] Created a file named `user_input.c`
- [ ] Copied all code correctly
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Entered data for all prompts
- [ ] Saw personalized output based on your input

---

### Important New Concepts

- [ ] **`scanf()`**: Function to read user input
- [ ] **`&` operator**: Gets the memory address of a variable
- [ ] **`%s`**: Format specifier for strings (character arrays)
- [ ] **Space before `%c`**: Helps avoid issues with previous input

---

### Try This (Optional Challenges)

1. Try entering invalid data (like "abc" for age) - what happens?
2. Add more questions to the program
3. Create a simpler version that only asks for 2-3 pieces of information
4. Try entering a very long name - what happens?

---

## Quick Reference

| Format Specifier | What it reads | Variable type | Example |
|------------------|---------------|---------------|---------|
| `%d` | Integer | `int` | `scanf("%d", &age);` |
| `%f` | Float | `float` | `scanf("%f", &height);` |
| `%c` | Character | `char` | `scanf(" %c", &grade);` |
| `%s` | String | `char[]` | `scanf("%s", name);` |

**Pro Tips:**
- [ ] Always use `&` with `scanf()` except for strings (arrays)
- [ ] Use `" %c"` instead of `"%c"` for single characters to skip whitespace
- [ ] Strings (`%s`) get stored in character arrays, not regular variables

---

### Common scanf Issues

1. **Don't forget the `&` (ampersand)!**
   ```c
   scanf("%d", age);    // WRONG!
   scanf("%d", &age);   // CORRECT
   ```bash

2. **For characters, use a space:**
   ```c
   scanf("%c", &ch);   // Can cause problems
   scanf(" %c", &ch);  // Much safer
   ```bash

3. **Strings don't need `&`:**
   ```c
   scanf("%s", &name);  // WRONG!
   scanf("%s", name);   // CORRECT
   ```bash

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```c
# include <stdio.h>

int main() {
    // Variables to store user input
    int age;
    float height;
    char grade;
    char name[50];  // String for name (character array)
```bash
- [ ] We declare variables that will hold the user's input
- [ ] **`char name[50]`** creates a character array that can hold up to 49 characters + '\0' (null terminator)

```c
    std::cout << "What's your first name? ");
    scanf("%s", name);
```bash
- [ ] **`%s`** reads a string (sequence of characters)
- [ ] **No `&`** for strings because arrays already represent addresses
- [ ] **Note**: `scanf("%s", name)` stops reading at whitespace (spaces, tabs, newlines)

```c
    std::cout << "How old are you? ");
    scanf("%d", &age);
```bash
- [ ] **`%d`** reads an integer
- [ ] **`&age`** passes the memory address of the `age` variable
- [ ] **`&`** is required because `scanf()` needs to know WHERE to store the data

```c
    std::cout << "What's your letter grade (A, B, C, D, F)? ");
    scanf(" %c", &grade);
```bash
- [ ] **`" %c"`** has a space before `%c`
- [ ] This space tells `scanf()` to skip any whitespace (including the newline from previous input)
- [ ] Without the space, you might read the newline character instead of the actual grade

### Understanding `scanf()` In Detail

**How `scanf()` works:**
1. Waits for user to type input and press Enter
2. Parses the input according to format specifiers
3. Stores parsed values in the specified variables
4. Returns the number of items successfully read (useful for error checking)

**Example**: `scanf("%d %f %c", &age, &height, &grade);`
- [ ] User types: `25 70.5 B`
- [ ] `age` gets `25`, `height` gets `70.5`, `grade` gets `'B'`
- [ ] Returns `3` (three items successfully read)

### Memory and the `&` Operator

**Why do we need `&` for most variables but not for strings?**

```c
int age;     // Regular variable, stored somewhere in memory
char name[50]; // Array, the array name represents the address of first element

// scanf needs the address of where to store data:
scanf("%d", &age);    // &age gets the memory address
scanf("%s", name);    // name already IS the address (array name = &name[0])
```bash

### Input Validation: Making Programs Safer

**Basic input checking:**
```c
int result = scanf("%d", &age);
if (result == 1) {
    std::cout << "Successfully read age: %d\n", age);
} else {
    std::cout << "Invalid input for age! Please enter a number.\n");
    // Clear the input buffer
    while (getchar() != '\n');
}
```bash

**Better approach with error handling:**
```c
# include <stdio.h>
# include <stdbool.h>

bool get_integer_input(const char* prompt, int* value) {
    std::cout << "%s", prompt);
    int result = scanf("%d", value);
    
    if (result != 1) {
        // Clear bad input
        while (getchar() != '\n');
        return false;
    }
    return true;
}

int main() {
    int age;
    
    while (!get_integer_input("Enter your age: ", &age)) {
        std::cout << "Invalid input! Please try again.\n");
    }
    
    std::cout << "Your age is: %d\n", age);
    return 0;
}
```bash

### Advanced Input Techniques

**Reading multiple values at once:**
```c
int day, month, year;
std::cout << "Enter date (DD MM YYYY): ");
scanf("%d %d %d", &day, &month, &year);
```bash

**Reading text with spaces (using fgets):**
```c
char full_name[100];
std::cout << "Enter your full name: ");
getchar(); // Clear newline from previous input
fgets(full_name, sizeof(full_name), stdin);

// Remove trailing newline if present
full_name[strcspn(full_name, "\n")] = '\0';
std::cout << "Hello, %s!\n", full_name);
```bash

### Common scanf Pitfalls and Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| Program skips input | Leftover newline in buffer | Use `getchar()` to clear buffer |
| Can't read spaces in strings | `%s` stops at whitespace | Use `fgets()` instead |
| Crashes with long input | Buffer overflow | Use field width specifiers: `%49s` |
| Invalid input not handled | No input validation | Check scanf return value |

### Buffer Management

**Understanding the input buffer:**
```c
char ch1, ch2;
std::cout << "Enter first character: ");
scanf("%c", &ch1);
std::cout << "Enter second character: ");
scanf(" %c", &ch2);  // Space consumes leftover newline
```bash

**Clearing the entire input buffer:**
```c
void clear_input_buffer() {
    int ch;
    while ((ch = getchar()) != '\n' && ch != EOF);
}
```bash

### Real-World Input Example

```c
# include <stdio.h>
# include <string.h>

int main() {
    char first_name[30], last_name[30];
    int birth_year;
    char city[50];
    
    std::cout << "=== Registration Form ===\n");
    
    std::cout << "First name: ");
    scanf("%29s", first_name);  // %29s prevents buffer overflow
    
    std::cout << "Last name: ");
    scanf("%29s", last_name);
    
    std::cout << "Birth year: ");
    while (scanf("%d", &birth_year) != 1) {
        std::cout << "Invalid year! Try again: ");
        while (getchar() != '\n');  // Clear bad input
    }
    
    std::cout << "City: ");
    getchar();  // Clear newline
    fgets(city, sizeof(city), stdin);
    city[strcspn(city, "\n")] = '\0';  // Remove newline
    
    std::cout << "\n=== Registration Complete ===\n");
    std::cout << "Name: %s %s\n", first_name, last_name);
    std::cout << "Age in 2024: %d\n", 2024 - birth_year);
    std::cout << "From: %s\n", city);
    
    return 0;
}
```bash

### Security Considerations

**1. Buffer Overflow Protection:**
```c
char username[20];
scanf("%19s", username);  // One less than array size for null terminator
```bash

**2. Input Length Limits:**
```c
# define MAX_NAME_LEN 50
char name[MAX_NAME_LEN];
scanf("%49s", name);  // Always leave room for null terminator
```bash

### Debugging scanf Issues

**Common debugging technique:**
```c
int age;
std::cout << "Enter age: ");
int items_read = scanf("%d", &age);
std::cout << "scanf returned %d, age = %d\n", items_read, age);
```bash

This helps you see if `scanf` successfully read the input and what value was actually stored.

---

 **Amazing! Your programs can now talk to users! You're building real interactive software!** 

*Get ready for conditionals - making decisions in your programs!* 

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
