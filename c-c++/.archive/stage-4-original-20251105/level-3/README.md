# Mathematical Toolbox

A comprehensive C application providing advanced mathematical tools including scientific calculations, equation solving, matrix operations, statistics, geometry, and number theory functions.

## Features

- **Scientific Calculator**: Trigonometric, logarithmic, exponential, and power functions
- **Equation Solver**: Quadratic equations and linear systems
- **Matrix Operations**: Addition, multiplication, determinants, and transposition
- **Statistics Calculator**: Mean, median, mode, standard deviation, and linear regression
- **Geometry Calculator**: Circle, triangle, rectangle, and sphere calculations
- **Number Theory Tools**: Prime checking, factorization, GCD/LCM, and prime generation

## Quick Start

1. **Compile the program**:
   ```bash
   gcc main.c -o math_toolbox -lm
   ```

2. **Run the application**:
   ```bash
   ./math_toolbox
   ```

3. **Select from the main menu** to access different mathematical tools

## Menu Structure

### Main Menu
- **1. Scientific Calculator** - Advanced mathematical functions
- **2. Equation Solver** - Solve equations and systems
- **3. Matrix Operations** - Matrix algebra and manipulations
- **4. Statistics Calculator** - Statistical analysis tools
- **5. Geometry Calculator** - Shape calculations and properties
- **6. Number Theory Tools** - Prime numbers and number theory
- **7. Exit** - Exit the program

## Scientific Calculator

### Trigonometric Functions
- Sine, cosine, tangent with degree/radian support
- Example: sin(30°) = 0.500000

### Logarithmic Functions
- Common logarithm (log) and natural logarithm (ln)
- Example: log(100) = 2.000000, ln(e) ≈ 1.000000

### Power and Root Functions
- Power calculations (x^y) and square roots
- Example: 2^8 = 256.000000, √16 = 4.000000

### Factorial
- Factorial calculations for non-negative integers
- Example: 5! = 120

## Equation Solver

### Quadratic Equations
Solves equations of the form ax² + bx + c = 0
- Real and complex roots
- Discriminant analysis
- Example: x² - 5x + 6 = 0 → x = 2, x = 3

### Linear Systems
Solves 2x2 systems of equations
- Cramer's rule implementation
- Determinant-based solutions
- Example: 2x + y = 5, x - y = 1 → x = 2, y = 1

## Matrix Operations

### Matrix Addition
- Element-wise addition of compatible matrices
- Dimension validation
- Result display in matrix format

### Matrix Multiplication
- Standard matrix multiplication
- Dimension compatibility checking
- Efficient computation algorithms

### Matrix Determinant
- Recursive determinant calculation
- Support for matrices up to 10x10
- Laplace expansion method

### Matrix Transpose
- Row-column interchange
- Dimension preservation
- Standard mathematical operation

## Statistics Calculator

### Mean, Median, Mode
- Central tendency measures
- Sorted data processing
- Frequency analysis for mode

### Standard Deviation
- Population and sample standard deviation
- Variance calculations
- Data spread analysis

### Linear Regression
- Best-fit line calculation
- Slope and intercept determination
- Correlation analysis

## Geometry Calculator

### Circle Properties
- Area, circumference, diameter calculations
- Radius-based computations
- Precise π usage

### Triangle Properties
- Right triangle calculations
- General triangle (Heron's formula)
- Base-height area calculations

### Rectangle Properties
- Perimeter and area calculations
- Diagonal length computation
- Pythagorean theorem application

### Sphere Properties
- Volume and surface area calculations
- 3D geometry formulas
- Precise mathematical constants

## Number Theory Tools

### Prime Checking
- Efficient primality testing
- Optimized algorithms for large numbers
- Clear true/false results

### Factor Finding
- Complete factorization
- Divisor enumeration
- Mathematical factor analysis

### GCD and LCM
- Euclidean algorithm implementation
- Greatest common divisor
- Least common multiple calculations

### Prime Generation
- Sieve of Eratosthenes approach
- Prime number listing
- Configurable upper limits

## Technical Details

### Data Structures
- **Matrix Structure**: 2D array with row/column dimensions
- **Fixed-size Arrays**: Simple memory management
- **Double Precision**: High accuracy floating-point calculations

### Mathematical Libraries
- **math.h Integration**: Standard mathematical functions
- **Trigonometric Functions**: sin, cos, tan with angle conversions
- **Power Functions**: pow, sqrt for advanced calculations

### Algorithm Implementations
- **Euclidean Algorithm**: Efficient GCD calculations
- **Recursive Determinant**: Laplace expansion for matrices
- **Statistical Sorting**: Bubble sort for median calculations

## Usage Examples

### Scientific Calculator
```
 SCIENTIFIC CALCULATOR
========================

Scientific Calculator Options:
1. Trigonometric Functions (sin, cos, tan)
2. Logarithmic Functions (log, ln)
3. Power and Root Functions
4. Factorial
5. Back to Main Menu
Enter choice (1-5): 1
Enter angle: 45
Use degrees? (1=yes, 0=radians): 1
sin(45.00) = 0.707107
cos(45.00) = 0.707107
tan(45.00) = 1.000000
```

### Matrix Operations
```
 MATRIX OPERATIONS
====================

Matrix Operations:
1. Matrix Addition
2. Matrix Multiplication
3. Matrix Determinant
4. Matrix Transpose
5. Back to Main Menu
Enter choice (1-5): 3
Enter matrix size (NxN): 2
Enter matrix elements:
M[1][1]: 1
M[1][2]: 2
M[2][1]: 3
M[2][2]: 4

Determinant = -2.000000
```

### Statistics Calculator
```
 STATISTICS CALCULATOR
========================

Statistics Options:
1. Mean, Median, Mode
2. Standard Deviation
3. Linear Regression
4. Back to Main Menu
Enter choice (1-4): 1
Enter number of data points: 5
Enter 5 data points:
Data[1]: 10
Data[2]: 20
Data[3]: 30
Data[4]: 20
Data[5]: 40

Results:
Mean: 24.000000
Median: 20.000000
Mode: 20.000000 (appears 2 times)
```

## Mathematical Constants

- **π (PI)**: 3.141592653589793
- **E**: Natural logarithm base (available through exp(1))
- **Degree to Radian**: π/180 conversion
- **High Precision**: Double precision floating-point

## Error Handling

### Input Validation
- **Numeric Input**: Robust number parsing
- **Range Checking**: Appropriate limits for calculations
- **Dimension Validation**: Matrix compatibility checking
- **Mathematical Constraints**: Domain validation for functions

### Runtime Checks
- **Division by Zero**: Protected mathematical operations
- **Invalid Dimensions**: Matrix operation validation
- **Domain Errors**: Function input range checking
- **Memory Bounds**: Array size limitations

## Limitations

- Matrix size limited to 10x10
- Fixed-size data arrays
- Recursive determinant (not optimal for large matrices)
- Simple sorting algorithms
- No symbolic mathematics

## Future Enhancements

### Advanced Mathematics
- **Symbolic Computation**: Algebraic manipulation
- **Complex Numbers**: Complex arithmetic support
- **Advanced Calculus**: Derivatives and integrals
- **3D Geometry**: Advanced spatial calculations

### Performance Improvements
- **Optimized Algorithms**: Faster matrix operations
- **Dynamic Memory**: Flexible data structures
- **Parallel Processing**: Multi-threaded calculations
- **GPU Acceleration**: Hardware-accelerated computations

### Additional Features
- **Graphing Capabilities**: Function plotting
- **Unit Conversions**: Scientific unit systems
- **Advanced Statistics**: Hypothesis testing, distributions
- **Equation Systems**: Larger linear systems (3x3, 4x4)

## Learning Outcomes

This application demonstrates:
- **Advanced C Programming**: Complex data structures and algorithms
- **Mathematical Implementation**: Real-world mathematical algorithms
- **Precision Handling**: Floating-point accuracy and error analysis
- **User Interface Design**: Multi-level menu systems
- **Error Management**: Robust input validation and error recovery
- **Modular Architecture**: Organized code structure and functions

## Compilation

### Requirements
- GCC compiler with math library support
- Standard C libraries (stdio.h, stdlib.h, math.h, string.h)

### Build Command
```bash
gcc main.c -o math_toolbox -lm -Wall -Wextra
```

### Clean Build
```bash
rm -f math_toolbox
gcc main.c -o math_toolbox -lm -Wall -Wextra
```

### Debug Build
```bash
gcc main.c -o math_toolbox_debug -lm -Wall -Wextra -g -O0
```

---

*Built as Level 3 of Stage 4: Full Problem Solving in the C/C++ Programming Curriculum*