# Level 6: Loops in C++

> **LESSON NOTE:** This lesson file is **read-only**. Write your code in `main.cpp` in the right window.

## Stage 1: Repetition with Loops

### Learning Goals

- Use `for` loops for counting
- Use `while` loops for conditions
- Use `do-while` loops (at least once)
- Understand loop control (`break`, `continue`)

---

### Your Task

Create `main.cpp`:

```
#include <iostream>
using namespace std;

int main() {
    // FOR LOOP - count from 1 to 5
    cout << "For loop:\n";
    for (int i = 1; i <= 5; i++) {
        cout << "Count: " << i << "\n";
    }
    
    // WHILE LOOP - keep asking until valid input
    cout << "\nWhile loop example:\n";
    int number = 0;
    while (number < 1 || number > 10) {
        cout << "Enter a number between 1-10: ";
        cin >> number;
        if (number < 1 || number > 10) {
            cout << "Invalid! Try again.\n";
        }
    }
    cout << "You entered: " << number << "\n";
    
    // DO-WHILE - runs at least once
    cout << "\nDo-while loop:\n";
    char again;
    do {
        cout << "Hello from do-while!\n";
        cout << "Run again? (y/n): ";
        cin >> again;
    } while (again == 'y' || again == 'Y');
    
    // BREAK and CONTINUE
    cout << "\nLoop control:\n";
    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            continue;  // Skip 5
        }
        if (i == 8) {
            break;     // Stop at 8
        }
        cout << i << " ";
    }
    cout << "\n";
    
    return 0;
}
```

### Compile and Run

```
g++ main.cpp -o main
./main
```

---

### Loop Types

**FOR** - When you know how many iterations:
```
for (initialization; condition; increment) {
    // code
}
```

**WHILE** - When condition is checked first:
```
while (condition) {
    // code
}
```

**DO-WHILE** - When code must run at least once:
```
do {
    // code
} while (condition);
```

---

### Loop Control

- `break` - Exit loop immediately
- `continue` - Skip to next iteration
- Both work in for, while, and do-while

---

### Try This

1. Write a countdown from 10 to 1 using a for loop
2. Create a guessing game with a while loop
3. Make a menu that keeps showing until user picks "quit"
4. Print multiplication table (nested loops!)

---

### Common Mistakes

- Infinite loops (forgetting to increment/change condition)
- Off-by-one errors (`< 10` vs `<= 10`)
- Using `=` instead of `==` in condition
- Forgetting `break` in menu loops

---

**Next: Functions and introduction to classes!**
