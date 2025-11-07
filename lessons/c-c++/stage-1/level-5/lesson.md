# Level 5: Transition from C to C++

> **LESSON NOTE:** This is where we transition from C to C++! Write your code in `main.cpp` (note the .cpp extension).

## Stage 1: Welcome to C++

### Learning Goals

- Understand the relationship between C and C++
- Learn C++ input/output (`cout`, `cin`)
- Compare C style vs C++ style
- Use `using namespace std`

---

### Your Task - C++ Style!

Create `main.cpp` (note: `.cpp` not `.c`):

```
#include <iostream>
using namespace std;

int main() {
    // C++ style variables (same as C)
    int age;
    float height;
    string name;  // New! C++ has built-in strings

    // C++ style output (no printf!)
    cout << "Enter your name: ";
    cin >> name;

    cout << "Enter your age: ";
    cin >> age;

    cout << "Enter your height (feet): ";
    cin >> height;

    // Output with cout (replaces printf)
    cout << "\n--- Your Info ---\n";
    cout << "Name: " << name << "\n";
    cout << "Age: " << age << " years\n";
    cout << "Height: " << height << " feet\n";

    // Conditionals work the same!
    if (age >= 18) {
        cout << "You're an adult!\n";
    } else {
        cout << "You're a minor.\n";
    }

    return 0;
}
```

### Compile and Run (note g++ not gcc!)

```
g++ main.cpp -o main
./main
```

---

### C vs C++ Comparison

| Feature | C | C++ |
|---------|---|-----|
| Compiler | `gcc` | `g++` |
| Extension | `.c` | `.cpp` |
| Output | `printf()` | `cout <<` |
| Input | `scanf()` | `cin >>` |
| Strings | `char arrays` | `string` type |
| Header | `<stdio.h>` | `<iostream>` |

---

### Understanding cout and cin

```
cout << "Hello";  // Output - arrows point LEFT (out of program)
cin >> age;       // Input - arrows point RIGHT (into variable)
```

Think of the arrows as direction of data flow!

---

### Why C++?

- **All C code works in C++** (backward compatible)
- **Easier input/output** (no format specifiers needed!)
- **Better strings** (no char arrays needed)
- **Object-oriented** (classes - we'll learn soon!)
- **Modern features** (but still fast like C)

---

### Try This

1. Create a C program with printf/scanf, then convert it to C++ with cout/cin
2. Try using `string` to store a full name with spaces
3. Chain multiple outputs: `cout << "A" << "B" << "C" << "\n";`
4. Compare compilation: try compiling .cpp with gcc (fails!) and .c with g++ (works!)

---

### Common Transition Issues

- Forgetting to change `.c` to `.cpp`
- Using `gcc` instead of `g++`
- Mixing `printf` with `cout` (works but inconsistent)
- Forgetting `using namespace std;` (then need `std::cout`)

---

**Next: Loops in C++!**
