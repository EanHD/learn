# Level 6: Loops and Repetition
## Stage 1: Copying Code

### Today's Mission

Welcome to the world of automation! Today you'll discover the power of loops - the ability to repeat actions automatically. Loops are what make computers truly powerful - they can do the same task thousands or millions of times without getting tired or bored!

---

### Learning Goals

- Master the for loop for counted repetitions
- Learn the while loop for conditional repetition
- Understand the do-while loop for guaranteed execution
- Practice nested loops for complex patterns
- Learn loop control statements (break, continue)
- Create programs that automate repetitive tasks

---

### Your Task

**Copy the following code into a new file called `loops.c`**

```c
# include <stdio.h>

int main() {
    printf("=== The Power of Loops: Automation Unleashed! ===\n\n");
    
    // 1. Basic for loop - counting
    printf("--- 1. Counting with For Loops ---\n");
    printf("Counting from 1 to 5:\n");
    
    for (int i = 1; i <= 5; i++) {
        printf("Count: %d\n", i);
    }
    
    printf("\nCounting backwards from 10 to 1:\n");
    for (int i = 10; i >= 1; i--) {
        printf("%d ", i);
    }
    printf("\n\n");
    
    // 2. For loop with calculations
    printf("--- 2. Multiplication Table Generator ---\n");
    int number;
    printf("Enter a number to see its multiplication table: ");
    scanf("%d", &number);
    
    printf("Multiplication table for %d:\n", number);
    for (int i = 1; i <= 10; i++) {
        int result = number * i;
        printf("%d × %d = %d\n", number, i, result);
    }
    printf("\n");
    
    // 3. While loop - conditional repetition
    printf("--- 3. While Loops: Keep Going Until... ---\n");
    printf("Let's count how many times you can enter positive numbers!\n");
    
    int positive_count = 0;
    int user_input;
    
    printf("Enter positive numbers (enter 0 or negative to stop):\n");
    scanf("%d", &user_input);
    
    while (user_input > 0) {
        positive_count++;
        printf(" Positive number #%d: %d\n", positive_count, user_input);
        scanf("%d", &user_input);
    }
    
    printf("You entered %d positive numbers!\n\n", positive_count);
    
    // 4. Do-while loop - guaranteed execution
    printf("--- 4. Do-While Loops: Always Run At Least Once ---\n");
    printf("Guess the secret number game!\n");
    
    int secret_number = 42;
    int guess;
    int attempts = 0;
    
    do {
        printf("Enter your guess (1-100): ");
        scanf("%d", &guess);
        attempts++;
        
        if (guess < secret_number) {
            printf("Too low! Try higher.\n");
        } else if (guess > secret_number) {
            printf("Too high! Try lower.\n");
        } else {
            printf(" CORRECT! You found it in %d attempts!\n", attempts);
        }
    } while (guess != secret_number);
    
    printf("\n");
    
    // 5. Nested loops - patterns
    printf("--- 5. Nested Loops: Creating Patterns ---\n");
    printf("Building a pyramid pattern:\n");
    
    int rows;
    printf("How many rows for the pyramid? ");
    scanf("%d", &rows);
    
    for (int i = 1; i <= rows; i++) {
        // Print spaces for alignment
        for (int space = 1; space <= rows - i; space++) {
            printf(" ");
        }
        
        // Print stars
        for (int star = 1; star <= (2 * i - 1); star++) {
            printf("*");
        }
        
        printf("\n");
    }
    printf("\n");
    
    // 6. Loop control: break and continue
    printf("--- 6. Loop Control: Break and Continue ---\n");
    printf("Finding the first multiple of 7 between 1 and 50:\n");
    
    for (int i = 1; i <= 50; i++) {
        if (i % 7 == 0) {
            printf("Found it! %d is the first multiple of 7.\n", i);
            break; // Exit the loop immediately
        }
    }
    
    printf("\nSkipping multiples of 3, printing others from 1 to 20:\n");
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0) {
            continue; // Skip to next iteration
        }
        printf("%d ", i);
    }
    printf("\n\n");
    
    // 7. Practical application: Grade calculator
    printf("--- 7. Real-World Application: Grade Calculator ---\n");
    printf("Enter student grades (enter -1 to finish):\n");
    
    int grade;
    int grade_count = 0;
    int sum = 0;
    int highest = -1;
    int lowest = 101;
    
    while (1) { // Infinite loop - we'll break when done
        printf("Enter grade #%d: ", grade_count + 1);
        scanf("%d", &grade);
        
        if (grade == -1) {
            break; // Exit when user enters -1
        }
        
        if (grade < 0 || grade > 100) {
            printf("Invalid grade! Please enter 0-100.\n");
            continue; // Skip this iteration, ask again
        }
        
        grade_count++;
        sum += grade;
        
        if (grade > highest) highest = grade;
        if (grade < lowest) lowest = grade;
        
        printf(" Recorded grade: %d\n", grade);
    }
    
    if (grade_count > 0) {
        float average = (float)sum / grade_count;
        printf("\n=== Grade Statistics ===\n");
        printf("Number of grades: %d\n", grade_count);
        printf("Average: %.1f%%\n", average);
        printf("Highest: %d%%\n", highest);
        printf("Lowest: %d%%\n", lowest);
        
        // Letter grade distribution
        printf("\nLetter grade distribution:\n");
        for (int i = 0; i < grade_count; i++) {
            // We'll need to collect grades in an array for this
            // For now, just show the concept
        }
    } else {
        printf("No grades entered.\n");
    }
    
    // 8. Advanced: Factorial calculator
    printf("\n--- 8. Advanced: Factorial Calculator ---\n");
    printf("Calculate n! (n factorial)\n");
    
    int n;
    printf("Enter a number (0-12): ");
    scanf("%d", &n);
    
    if (n < 0 || n > 12) {
        printf("Please enter a number between 0 and 12.\n");
    } else {
        long long factorial = 1;
        
        printf("%d! = ", n);
        for (int i = n; i >= 1; i--) {
            factorial *= i;
            printf("%d", i);
            if (i > 1) printf(" × ");
        }
        
        printf(" = %lld\n", factorial);
        
        // Fun fact about factorials
        if (n == 0 || n == 1) {
            printf("Fun fact: 0! and 1! both equal 1 by definition!\n");
        } else if (n == 5) {
            printf("Fun fact: 5! = 120, which is the number of ways to arrange 5 distinct items!\n");
        }
    }
    
    // 9. Loop with user validation
    printf("\n--- 9. Input Validation with Loops ---\n");
    printf("Let's create a simple menu system:\n");
    
    int choice;
    do {
        printf("\n=== MENU ===\n");
        printf("1. Calculate square of a number\n");
        printf("2. Check if number is even or odd\n");
        printf("3. Exit\n");
        printf("Enter your choice (1-3): ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1: {
                int num;
                printf("Enter a number: ");
                scanf("%d", &num);
                printf("%d squared = %d\n", num, num * num);
                break;
            }
            case 2: {
                int num;
                printf("Enter a number: ");
                scanf("%d", &num);
                if (num % 2 == 0) {
                    printf("%d is even\n", num);
                } else {
                    printf("%d is odd\n", num);
                }
                break;
            }
            case 3:
                printf("Goodbye!\n");
                break;
            default:
                printf("Invalid choice! Please select 1-3.\n");
                break;
        }
    } while (choice != 3);
    
    printf("\n Congratulations! You've mastered loops and automation!\n");
    printf("Your programs can now repeat tasks efficiently!\n");
    
    return 0;
}
```

---

### How to Compile and Run

1. **Compile the code**:
   ```bash
   gcc loops.c -o loops
   ```
2. **Run your program**:
   ```bash
   ./loops
   ```
3. **Interact with all the different loop examples!**

---

### Success Checklist

- [ ] Created a file named `loops.c`
- [ ] Copied all code correctly
- [ ] Compiled without errors
- [ ] Ran the program and tested all loop types
- [ ] Experienced counting, conditional repetition, and pattern generation
- [ ] Used break and continue to control loop flow
- [ ] Completed the interactive menu system

---

### Key Loop Concepts

1. **for loop** - Best for known number of iterations
2. **while loop** - Best for unknown iterations (condition-based)
3. **do-while loop** - Always executes at least once
4. **break** - Exit loop immediately
5. **continue** - Skip to next iteration
6. **Nested loops** - Loops inside loops for complex patterns

---

### Try This (Optional Challenges)

1. Modify the pyramid to use different characters
2. Add more menu options to the final program
3. Create a loop that finds prime numbers
4. Make the grade calculator show letter grade distribution

---

## Quick Reference

### Loop Types
| Loop Type | When to Use | Example |
|-----------|-------------|---------|
| `for` | Known number of iterations | `for(int i=0; i<10; i++)` |
| `while` | Condition-based repetition | `while(x > 0)` |
| `do-while` | Must run at least once | `do { ... } while(condition);` |

### Loop Control
| Statement | What it does | Example |
|-----------|--------------|---------|
| `break` | Exit loop immediately | `if(x == 5) break;` |
| `continue` | Skip to next iteration | `if(x % 2 == 0) continue;` |

---

### Common Loop Mistakes

1. **Infinite loops**
   ```c
   while (1) { // No exit condition!
       printf("Forever!");
   }
   ```

2. **Off-by-one errors**
   ```c
   for (int i = 0; i <= 10; i++) { // Runs 11 times!
       // ...
   }
   ```

3. **Forgetting to update loop variable**
   ```c
   int i = 0;
   while (i < 10) {
       printf("%d ", i);
       // Forgot: i++;
   }
   ```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

#### 1. Basic For Loop

```c
for (int i = 1; i <= 5; i++) {
    printf("Count: %d\n", i);
}
```

**For Loop Anatomy:**
- **`int i = 1`** = Initialization (starting value)
- **`i <= 5`** = Condition (when to continue)
- **`i++`** = Increment (what to do each iteration)
- **`{ ... }`** = Loop body (code to repeat)

**Execution Flow:**
1. Initialize: `i = 1`
2. Check condition: `1 <= 5` (true) → execute body
3. Increment: `i = 2`
4. Check condition: `2 <= 5` (true) → execute body
5. ... continues until `i = 6`
6. Check condition: `6 <= 5` (false) → exit loop

#### 2. While Loop

```c
while (user_input > 0) {
    positive_count++;
    printf(" Positive number #%d: %d\n", positive_count, user_input);
    scanf("%d", &user_input);
}
```

**Key Difference from For Loop:**
- Only has a condition, no initialization or increment
- Perfect for situations where you don't know how many times to loop
- Condition is checked BEFORE each iteration

**Common While Loop Patterns:**
```c
// Reading until end of file
while (scanf("%d", &num) == 1) {
    // process num
}

// Menu systems
while (choice != 0) {
    // show menu, get choice
}

// Game loops
while (!game_over) {
    // update game state
}
```

#### 3. Do-While Loop

```c
do {
    printf("Enter your guess: ");
    scanf("%d", &guess);
    attempts++;
    
    if (guess < secret_number) {
        printf("Too low!\n");
    } else if (guess > secret_number) {
        printf("Too high!\n");
    } else {
        printf("CORRECT!\n");
    }
} while (guess != secret_number);
```

**Critical Difference:**
- Body executes BEFORE condition is checked
- Guaranteed to run at least once
- Perfect for input validation and menus

#### 4. Nested Loops

```c
for (int i = 1; i <= rows; i++) {
    // Print spaces
    for (int space = 1; space <= rows - i; space++) {
        printf(" ");
    }
    
    // Print stars
    for (int star = 1; star <= (2 * i - 1); star++) {
        printf("*");
    }
    
    printf("\n");
}
```

**Understanding Nested Loops:**
- Outer loop: controls rows
- Inner loops: control what happens in each row
- Variables in outer scope are visible to inner loops
- Each iteration of outer loop runs all iterations of inner loop

#### 5. Break and Continue

```c
// Break example
for (int i = 1; i <= 50; i++) {
    if (i % 7 == 0) {
        printf("Found: %d\n", i);
        break; // Exit immediately
    }
}

// Continue example
for (int i = 1; i <= 20; i++) {
    if (i % 3 == 0) {
        continue; // Skip to next i
    }
    printf("%d ", i);
}
```

**Break vs Continue:**
- `break`: Exit the entire loop
- `continue`: Skip current iteration, continue with next

### Advanced Loop Concepts

#### Loop Efficiency

```c
// Less efficient - recalculates size each time
for (int i = 0; i < strlen(str); i++) {
    // ...
}

// More efficient - calculate once
int len = strlen(str);
for (int i = 0; i < len; i++) {
    // ...
}
```

#### Sentinel Values

```c
// Using -1 as sentinel to end input
printf("Enter numbers (enter -1 to finish):\n");
while (1) {
    scanf("%d", &num);
    if (num == -1) break;
    // process num
}
```

#### Loop Invariants

A loop invariant is a condition that remains true throughout the loop:

```c
// Sum of first n natural numbers
int sum = 0;
for (int i = 1; i <= n; i++) {
    sum += i;
    // Invariant: sum = i*(i+1)/2 at this point
}
```

### Common Loop Patterns

#### Counting

```c
int count = 0;
for (int i = 0; i < size; i++) {
    if (condition) count++;
}
```

#### Finding Maximum/Minimum

```c
int max = INT_MIN;
for (int i = 0; i < size; i++) {
    if (array[i] > max) max = array[i];
}
```

#### Accumulating

```c
double sum = 0.0;
int count = 0;
for (int i = 0; i < size; i++) {
    sum += array[i];
    count++;
}
double average = sum / count;
```

#### Searching

```c
int target = 42;
int found_index = -1;
for (int i = 0; i < size; i++) {
    if (array[i] == target) {
        found_index = i;
        break; // Found it, no need to continue
    }
}
```

### Debugging Loops

#### Common Debugging Techniques

```c
// Add debug prints
for (int i = 0; i < 10; i++) {
    printf("DEBUG: i = %d\n", i);
    // ... rest of loop body
}

// Check loop conditions
while (condition) {
    printf("DEBUG: Entering loop, condition = %s\n", 
           condition ? "true" : "false");
    // ... loop body
}
```

#### Infinite Loop Detection

```c
int iterations = 0;
while (condition && iterations < 1000) { // Safety limit
    // ... loop body
    iterations++;
    
    if (iterations >= 1000) {
        printf("ERROR: Possible infinite loop detected!\n");
        break;
    }
}
```

### Real-World Loop Applications

#### File Processing

```c
FILE* file = fopen("data.txt", "r");
char line[256];

while (fgets(line, sizeof(line), file) != NULL) {
    // Process each line
    printf("Read: %s", line);
}
fclose(file);
```

#### Animation/Game Loops

```c
while (!quit) {
    // Handle input
    // Update game state
    // Render graphics
    // Control frame rate
}
```

#### Data Validation

```c
int get_valid_age() {
    int age;
    do {
        printf("Enter age (1-120): ");
        scanf("%d", &age);
    } while (age < 1 || age > 120);
    
    return age;
}
```

### Performance Considerations

#### Cache-Friendly Loops

```c
// Good - sequential access
for (int i = 0; i < size; i++) {
    array[i] = i * 2;
}

// Bad - random access (cache unfriendly)
for (int i = 0; i < size; i++) {
    array[random_indices[i]] = i * 2;
}
```

#### Loop Unrolling

```c
// Manual unrolling for performance
for (int i = 0; i < size; i += 4) {
    array[i] = i;
    if (i + 1 < size) array[i + 1] = i + 1;
    if (i + 2 < size) array[i + 2] = i + 2;
    if (i + 3 < size) array[i + 3] = i + 3;
}
```

### Loop Best Practices

1. **Use the right loop type** for the job
2. **Initialize loop variables** properly
3. **Update loop variables** correctly
4. **Avoid infinite loops** with proper exit conditions
5. **Use meaningful variable names** (i, j, k are OK for simple counters)
6. **Consider loop efficiency** for performance-critical code
7. **Add bounds checking** to prevent array overruns
8. **Use break and continue** judiciously

---

 **Outstanding! You've harnessed the power of loops and automation!** 

*Your programs can now repeat tasks efficiently and intelligently! Next: Functions to organize your code! *