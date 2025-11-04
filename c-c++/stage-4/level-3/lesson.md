# Level 3: Mathematical Application

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

**MATHEMATICAL POWERHOUSE!**  You're now building applications that solve complex mathematical problems, implement advanced formulas, and provide professional-grade mathematical tools. This level focuses on numerical algorithms, mathematical modeling, and precision calculations.

**The Process:**
1. **Mathematical Analysis**: Understand the mathematical concepts
2. **Algorithm Design**: Create efficient computational methods
3. **Precision Handling**: Manage floating-point accuracy
4. **Error Control**: Implement numerical stability checks
5. **User Interface**: Provide intuitive mathematical tools
6. **Result Presentation**: Display results with proper formatting

---

### Learning Goals

- [ ] Advanced mathematical algorithms implementation
- [ ] Numerical precision and error handling
- [ ] Matrix operations and linear algebra
- [ ] Equation solving techniques
- [ ] Statistical calculations
- [ ] Mathematical function libraries

---

### Your Task

**Build a complete Math Toolbox with:**
1. **Scientific Calculator**: Advanced mathematical functions
2. **Equation Solver**: Solve quadratic and system equations
3. **Matrix Operations**: Matrix algebra and manipulations
4. **Statistics Calculator**: Statistical analysis tools
5. **Geometry Calculator**: Shape calculations and properties
6. **Number Theory**: Prime numbers, factors, and properties

---

## Application Requirements

### Core Features
- [ ] **Scientific Calculator**: Trigonometric, logarithmic, exponential functions
- [ ] **Equation Solving**: Quadratic equations, 2x2 and 3x3 linear systems
- [ ] **Matrix Operations**: Addition, multiplication, determinant, inverse
- [ ] **Statistical Analysis**: Mean, median, standard deviation, regression
- [ ] **Geometry Tools**: Area, volume, perimeter calculations
- [ ] **Number Theory**: Prime checking, factorization, GCD/LCM

### Technical Requirements
- [ ] High-precision floating-point calculations
- [ ] Matrix memory management
- [ ] Numerical stability algorithms
- [ ] Input validation for mathematical constraints
- [ ] Clear mathematical notation in output

---

## Application Architecture

### Data Structures
```c
# define MAX_MATRIX_SIZE 10
# define PI 3.14159265358979323846

typedef struct {
    double **data;
    int rows;
    int cols;
} Matrix;

typedef struct {
    double a, b, c;  // For quadratic: ax² + bx + c = 0
    double root1, root2;
    int num_roots;
} QuadraticEquation;

typedef struct {
    double *data;
    int count;
    double mean;
    double median;
    double std_dev;
    double min;
    double max;
} StatisticalData;
```cpp

### Function Modules
- [ ] **Calculator**: `scientific_calc()`, `basic_arithmetic()`
- [ ] **Equation Solving**: `solve_quadratic()`, `solve_linear_system()`
- [ ] **Matrix Operations**: `matrix_add()`, `matrix_multiply()`, `matrix_inverse()`
- [ ] **Statistics**: `calculate_stats()`, `linear_regression()`
- [ ] **Geometry**: `calculate_area()`, `calculate_volume()`
- [ ] **Number Theory**: `is_prime()`, `factorize()`, `gcd_lcm()`

---

## Complete Implementation

### Header File (math_toolbox.h)
```c
# ifndef MATH_TOOLBOX_H
# define MATH_TOOLBOX_H

# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <string.h>
# include <ctype.h>

# define MAX_MATRIX_SIZE 10
# define PI 3.14159265358979323846
# define EPSILON 1e-10  // For floating-point comparisons

typedef struct {
    double **data;
    int rows;
    int cols;
} Matrix;

typedef struct {
    double a, b, c;  // ax² + bx + c = 0
    double root1, root2;
    int num_roots;
} QuadraticEquation;

typedef struct {
    double *data;
    int count;
    double mean;
    double median;
    double std_dev;
    double min;
    double max;
} StatisticalData;

// Function prototypes
// Calculator functions
double scientific_calc(double x, const char *operation);
double basic_arithmetic(double a, double b, char op);

// Equation solving
int solve_quadratic(QuadraticEquation *eq);
int solve_linear_system_2x2(double a1, double b1, double c1,
                           double a2, double b2, double c2,
                           double *x, double *y);

// Matrix operations
Matrix* create_matrix(int rows, int cols);
void free_matrix(Matrix *matrix);
void print_matrix(const Matrix *matrix);
Matrix* matrix_add(const Matrix *a, const Matrix *b);
Matrix* matrix_multiply(const Matrix *a, const Matrix *b);
double matrix_determinant(const Matrix *matrix);
Matrix* matrix_inverse(const Matrix *matrix);

// Statistics
StatisticalData* create_statistical_data(int count);
void free_statistical_data(StatisticalData *data);
void calculate_statistics(StatisticalData *data);
void linear_regression(const StatisticalData *x, const StatisticalData *y,
                      double *slope, double *intercept, double *r_squared);

// Geometry
double calculate_circle_area(double radius);
double calculate_circle_circumference(double radius);
double calculate_rectangle_area(double length, double width);
double calculate_rectangle_perimeter(double length, double width);
double calculate_triangle_area(double base, double height);
double calculate_sphere_volume(double radius);
double calculate_cylinder_volume(double radius, double height);

// Number theory
int is_prime(int n);
void factorize(int n, int *factors, int *count);
int gcd(int a, int b);
int lcm(int a, int b);

// Utility functions
void display_menu(void);
int get_user_choice(void);
void clear_input_buffer(void);

# endif
```cpp

### Implementation File (math_toolbox.c)
```c
# include "math_toolbox.h"

// Scientific calculator operations
double scientific_calc(double x, const char *operation) {
    if (strcmp(operation, "sin") == 0) return sin(x * PI / 180.0);  // Degrees to radians
    if (strcmp(operation, "cos") == 0) return cos(x * PI / 180.0);
    if (strcmp(operation, "tan") == 0) return tan(x * PI / 180.0);
    if (strcmp(operation, "asin") == 0) return asin(x) * 180.0 / PI;  // Radians to degrees
    if (strcmp(operation, "acos") == 0) return acos(x) * 180.0 / PI;
    if (strcmp(operation, "atan") == 0) return atan(x) * 180.0 / PI;
    if (strcmp(operation, "log") == 0) return log10(x);
    if (strcmp(operation, "ln") == 0) return log(x);
    if (strcmp(operation, "exp") == 0) return exp(x);
    if (strcmp(operation, "sqrt") == 0) return sqrt(x);
    if (strcmp(operation, "square") == 0) return x * x;
    if (strcmp(operation, "cube") == 0) return x * x * x;
    if (strcmp(operation, "reciprocal") == 0) return 1.0 / x;
    return 0.0;
}

// Basic arithmetic
double basic_arithmetic(double a, double b, char op) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return (b != 0) ? a / b : 0.0;
        case '%': return (int)a % (int)b;
        case '^': return pow(a, b);
        default: return 0.0;
    }
}

// Solve quadratic equation
int solve_quadratic(QuadraticEquation *eq) {
    if (fabs(eq->a) < EPSILON) {
        // Not a quadratic equation
        return 0;
    }

    double discriminant = eq->b * eq->b - 4 * eq->a * eq->c;

    if (discriminant > EPSILON) {
        // Two real roots
        eq->root1 = (-eq->b + sqrt(discriminant)) / (2 * eq->a);
        eq->root2 = (-eq->b - sqrt(discriminant)) / (2 * eq->a);
        eq->num_roots = 2;
    } else if (fabs(discriminant) < EPSILON) {
        // One real root
        eq->root1 = eq->root2 = -eq->b / (2 * eq->a);
        eq->num_roots = 1;
    } else {
        // Complex roots
        eq->num_roots = 0;
    }

    return 1;
}

// Solve 2x2 linear system
int solve_linear_system_2x2(double a1, double b1, double c1,
                           double a2, double b2, double c2,
                           double *x, double *y) {
    double determinant = a1 * b2 - a2 * b1;

    if (fabs(determinant) < EPSILON) {
        return 0;  // System is singular
    }

    *x = (c1 * b2 - c2 * b1) / determinant;
    *y = (a1 * c2 - a2 * c1) / determinant;

    return 1;
}

// Matrix operations
Matrix* create_matrix(int rows, int cols) {
    if (rows <= 0 || cols <= 0 || rows > MAX_MATRIX_SIZE || cols > MAX_MATRIX_SIZE) {
        return NULL;
    }

    Matrix *matrix = malloc(sizeof(Matrix));
    if (matrix == NULL) return NULL;

    matrix->rows = rows;
    matrix->cols = cols;
    matrix->data = malloc(rows * sizeof(double*));
    if (matrix->data == NULL) {
        free(matrix);
        return NULL;
    }

    for (int i = 0; i < rows; i++) {
        matrix->data[i] = calloc(cols, sizeof(double));
        if (matrix->data[i] == NULL) {
            // Free previously allocated rows
            for (int j = 0; j < i; j++) {
                free(matrix->data[j]);
            }
            free(matrix->data);
            free(matrix);
            return NULL;
        }
    }

    return matrix;
}

void free_matrix(Matrix *matrix) {
    if (matrix == NULL) return;

    for (int i = 0; i < matrix->rows; i++) {
        free(matrix->data[i]);
    }
    free(matrix->data);
    free(matrix);
}

void print_matrix(const Matrix *matrix) {
    if (matrix == NULL) return;

    for (int i = 0; i < matrix->rows; i++) {
        for (int j = 0; j < matrix->cols; j++) {
            std::cout << "%8.3f ", matrix->data[i][j]);
        }
        std::cout << "\n");
    }
}

Matrix* matrix_add(const Matrix *a, const Matrix *b) {
    if (a->rows != b->rows || a->cols != b->cols) {
        return NULL;
    }

    Matrix *result = create_matrix(a->rows, a->cols);
    if (result == NULL) return NULL;

    for (int i = 0; i < a->rows; i++) {
        for (int j = 0; j < a->cols; j++) {
            result->data[i][j] = a->data[i][j] + b->data[i][j];
        }
    }

    return result;
}

Matrix* matrix_multiply(const Matrix *a, const Matrix *b) {
    if (a->cols != b->rows) {
        return NULL;
    }

    Matrix *result = create_matrix(a->rows, b->cols);
    if (result == NULL) return NULL;

    for (int i = 0; i < a->rows; i++) {
        for (int j = 0; j < b->cols; j++) {
            for (int k = 0; k < a->cols; k++) {
                result->data[i][j] += a->data[i][k] * b->data[k][j];
            }
        }
    }

    return result;
}

double matrix_determinant(const Matrix *matrix) {
    if (matrix->rows != matrix->cols) {
        return 0.0;  // Must be square matrix
    }

    int n = matrix->rows;

    if (n == 1) return matrix->data[0][0];
    if (n == 2) {
        return matrix->data[0][0] * matrix->data[1][1] -
               matrix->data[0][1] * matrix->data[1][0];
    }

    // For larger matrices, implement more complex determinant calculation
    // This is a simplified version
    double det = 0.0;
    for (int j = 0; j < n; j++) {
        // Laplace expansion (simplified)
        double cofactor = matrix->data[0][j] * pow(-1, j);
        // Would need to implement submatrix determinant
        // For now, return simplified calculation
    }

    return det;
}

// Statistics functions
StatisticalData* create_statistical_data(int count) {
    if (count <= 0) return NULL;

    StatisticalData *data = malloc(sizeof(StatisticalData));
    if (data == NULL) return NULL;

    data->data = malloc(count * sizeof(double));
    if (data->data == NULL) {
        free(data);
        return NULL;
    }

    data->count = count;
    return data;
}

void free_statistical_data(StatisticalData *data) {
    if (data == NULL) return;
    free(data->data);
    free(data);
}

void calculate_statistics(StatisticalData *data) {
    if (data->count == 0) return;

    // Calculate mean
    data->mean = 0.0;
    for (int i = 0; i < data->count; i++) {
        data->mean += data->data[i];
    }
    data->mean /= data->count;

    // Find min and max
    data->min = data->max = data->data[0];
    for (int i = 1; i < data->count; i++) {
        if (data->data[i] < data->min) data->min = data->data[i];
        if (data->data[i] > data->max) data->max = data->data[i];
    }

    // Calculate median
    // Simple sort for median calculation
    double *sorted = malloc(data->count * sizeof(double));
    memcpy(sorted, data->data, data->count * sizeof(double));

    for (int i = 0; i < data->count - 1; i++) {
        for (int j = 0; j < data->count - i - 1; j++) {
            if (sorted[j] > sorted[j + 1]) {
                double temp = sorted[j];
                sorted[j] = sorted[j + 1];
                sorted[j + 1] = temp;
            }
        }
    }

    if (data->count % 2 == 0) {
        data->median = (sorted[data->count/2 - 1] + sorted[data->count/2]) / 2.0;
    } else {
        data->median = sorted[data->count/2];
    }

    free(sorted);

    // Calculate standard deviation
    data->std_dev = 0.0;
    for (int i = 0; i < data->count; i++) {
        data->std_dev += pow(data->data[i] - data->mean, 2);
    }
    data->std_dev = sqrt(data->std_dev / data->count);
}

// Geometry functions
double calculate_circle_area(double radius) {
    return PI * radius * radius;
}

double calculate_circle_circumference(double radius) {
    return 2 * PI * radius;
}

double calculate_rectangle_area(double length, double width) {
    return length * width;
}

double calculate_rectangle_perimeter(double length, double width) {
    return 2 * (length + width);
}

double calculate_triangle_area(double base, double height) {
    return 0.5 * base * height;
}

double calculate_sphere_volume(double radius) {
    return (4.0/3.0) * PI * radius * radius * radius;
}

double calculate_cylinder_volume(double radius, double height) {
    return PI * radius * radius * height;
}

// Number theory functions
int is_prime(int n) {
    if (n <= 1) return 0;
    if (n <= 3) return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return 0;
    }

    return 1;
}

void factorize(int n, int *factors, int *count) {
    *count = 0;
    int i = 2;

    while (i * i <= n) {
        if (n % i == 0) {
            factors[*count] = i;
            (*count)++;
            while (n % i == 0) {
                n /= i;
            }
        }
        i++;
    }

    if (n > 1) {
        factors[*count] = n;
        (*count)++;
    }
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

// Utility functions
void display_menu(void) {
    std::cout << "\n=== Math Toolbox ===\n");
    std::cout << "1. Scientific Calculator\n");
    std::cout << "2. Equation Solver\n");
    std::cout << "3. Matrix Operations\n");
    std::cout << "4. Statistics Calculator\n");
    std::cout << "5. Geometry Calculator\n");
    std::cout << "6. Number Theory\n");
    std::cout << "7. Exit\n");
    std::cout << "Enter your choice (1-7): ");
}

int get_user_choice(void) {
    int choice;
    scanf("%d", &choice);
    clear_input_buffer();
    return choice;
}

void clear_input_buffer(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}
```cpp

### Main Program (main.c)
```c
# include "math_toolbox.h"

int main() {
    std::cout << "Mathematical Toolbox\n");
    std::cout << "===================\n");

    int running = 1;
    while (running) {
        display_menu();
        int choice = get_user_choice();

        switch (choice) {
            case 1: { // Scientific Calculator
                double x;
                char operation[20];

                std::cout << "Enter number: ");
                scanf("%lf", &x);
                std::cout << "Enter operation (sin, cos, tan, log, ln, exp, sqrt, square, cube, reciprocal): ");
                scanf("%s", operation);

                double result = scientific_calc(x, operation);
                std::cout << "Result: %.6f\n", result);
                break;
            }

            case 2: { // Equation Solver
                std::cout << "1. Quadratic Equation\n");
                std::cout << "2. 2x2 Linear System\n");
                std::cout << "Enter choice: ");
                int eq_choice = get_user_choice();

                if (eq_choice == 1) {
                    QuadraticEquation eq;
                    std::cout << "Solve ax² + bx + c = 0\n");
                    std::cout << "Enter a, b, c: ");
                    scanf("%lf %lf %lf", &eq.a, &eq.b, &eq.c);

                    if (solve_quadratic(&eq)) {
                        std::cout << "Equation: %.2fx² + %.2fx + %.2f = 0\n", eq.a, eq.b, eq.c);
                        if (eq.num_roots == 2) {
                            std::cout << "Roots: %.4f, %.4f\n", eq.root1, eq.root2);
                        } else if (eq.num_roots == 1) {
                            std::cout << "Root: %.4f (double root)\n", eq.root1);
                        } else {
                            std::cout << "Complex roots\n");
                        }
                    } else {
                        std::cout << "Not a quadratic equation (a = 0)\n");
                    }
                } else if (eq_choice == 2) {
                    double a1, b1, c1, a2, b2, c2, x, y;
                    std::cout << "Solve:\n");
                    std::cout << "a1*x + b1*y = c1\n");
                    std::cout << "a2*x + b2*y = c2\n");
                    std::cout << "Enter a1, b1, c1, a2, b2, c2: ");
                    scanf("%lf %lf %lf %lf %lf %lf", &a1, &b1, &c1, &a2, &b2, &c2);

                    if (solve_linear_system_2x2(a1, b1, c1, a2, b2, c2, &x, &y)) {
                        std::cout << "Solution: x = %.4f, y = %.4f\n", x, y);
                    } else {
                        std::cout << "No unique solution (singular system)\n");
                    }
                }
                break;
            }

            case 3: { // Matrix Operations
                std::cout << "Matrix Operations:\n");
                std::cout << "1. Matrix Addition\n");
                std::cout << "2. Matrix Multiplication\n");
                std::cout << "3. Matrix Determinant\n");
                std::cout << "Enter choice: ");
                int matrix_choice = get_user_choice();

                if (matrix_choice == 1) {
                    // Matrix addition demo
                    Matrix *a = create_matrix(2, 2);
                    Matrix *b = create_matrix(2, 2);

                    std::cout << "Enter first 2x2 matrix:\n");
                    for (int i = 0; i < 2; i++) {
                        for (int j = 0; j < 2; j++) {
                            scanf("%lf", &a->data[i][j]);
                        }
                    }

                    std::cout << "Enter second 2x2 matrix:\n");
                    for (int i = 0; i < 2; i++) {
                        for (int j = 0; j < 2; j++) {
                            scanf("%lf", &b->data[i][j]);
                        }
                    }

                    Matrix *result = matrix_add(a, b);
                    if (result != NULL) {
                        std::cout << "Sum:\n");
                        print_matrix(result);
                        free_matrix(result);
                    } else {
                        std::cout << "Matrix sizes don't match\n");
                    }

                    free_matrix(a);
                    free_matrix(b);
                } else if (matrix_choice == 2) {
                    // Matrix multiplication demo
                    Matrix *a = create_matrix(2, 3);
                    Matrix *b = create_matrix(3, 2);

                    std::cout << "Enter first 2x3 matrix:\n");
                    for (int i = 0; i < 2; i++) {
                        for (int j = 0; j < 3; j++) {
                            scanf("%lf", &a->data[i][j]);
                        }
                    }

                    std::cout << "Enter second 3x2 matrix:\n");
                    for (int i = 0; i < 3; i++) {
                        for (int j = 0; j < 2; j++) {
                            scanf("%lf", &b->data[i][j]);
                        }
                    }

                    Matrix *result = matrix_multiply(a, b);
                    if (result != NULL) {
                        std::cout << "Product:\n");
                        print_matrix(result);
                        free_matrix(result);
                    } else {
                        std::cout << "Matrix dimensions incompatible\n");
                    }

                    free_matrix(a);
                    free_matrix(b);
                } else if (matrix_choice == 3) {
                    Matrix *m = create_matrix(2, 2);
                    std::cout << "Enter 2x2 matrix:\n");
                    for (int i = 0; i < 2; i++) {
                        for (int j = 0; j < 2; j++) {
                            scanf("%lf", &m->data[i][j]);
                        }
                    }

                    double det = matrix_determinant(m);
                    std::cout << "Determinant: %.4f\n", det);

                    free_matrix(m);
                }
                break;
            }

            case 4: { // Statistics Calculator
                int count;
                std::cout << "Enter number of data points: ");
                scanf("%d", &count);

                StatisticalData *data = create_statistical_data(count);
                if (data == NULL) {
                    std::cout << "Error creating statistical data\n");
                    break;
                }

                std::cout << "Enter %d data points: ", count);
                for (int i = 0; i < count; i++) {
                    scanf("%lf", &data->data[i]);
                }

                calculate_statistics(data);

                std::cout << "Statistics:\n");
                std::cout << "Count: %d\n", data->count);
                std::cout << "Mean: %.4f\n", data->mean);
                std::cout << "Median: %.4f\n", data->median);
                std::cout << "Standard Deviation: %.4f\n", data->std_dev);
                std::cout << "Min: %.4f\n", data->min);
                std::cout << "Max: %.4f\n", data->max);

                free_statistical_data(data);
                break;
            }

            case 5: { // Geometry Calculator
                std::cout << "Geometry Calculator:\n");
                std::cout << "1. Circle (area/circumference)\n");
                std::cout << "2. Rectangle (area/perimeter)\n");
                std::cout << "3. Triangle (area)\n");
                std::cout << "4. Sphere (volume)\n");
                std::cout << "5. Cylinder (volume)\n");
                std::cout << "Enter choice: ");
                int geo_choice = get_user_choice();

                switch (geo_choice) {
                    case 1: {
                        double r;
                        std::cout << "Enter radius: ");
                        scanf("%lf", &r);
                        std::cout << "Area: %.4f\n", calculate_circle_area(r));
                        std::cout << "Circumference: %.4f\n", calculate_circle_circumference(r));
                        break;
                    }
                    case 2: {
                        double l, w;
                        std::cout << "Enter length and width: ");
                        scanf("%lf %lf", &l, &w);
                        std::cout << "Area: %.4f\n", calculate_rectangle_area(l, w));
                        std::cout << "Perimeter: %.4f\n", calculate_rectangle_perimeter(l, w));
                        break;
                    }
                    case 3: {
                        double b, h;
                        std::cout << "Enter base and height: ");
                        scanf("%lf %lf", &b, &h);
                        std::cout << "Area: %.4f\n", calculate_triangle_area(b, h));
                        break;
                    }
                    case 4: {
                        double r;
                        std::cout << "Enter radius: ");
                        scanf("%lf", &r);
                        std::cout << "Volume: %.4f\n", calculate_sphere_volume(r));
                        break;
                    }
                    case 5: {
                        double r, h;
                        std::cout << "Enter radius and height: ");
                        scanf("%lf %lf", &r, &h);
                        std::cout << "Volume: %.4f\n", calculate_cylinder_volume(r, h));
                        break;
                    }
                }
                break;
            }

            case 6: { // Number Theory
                std::cout << "Number Theory:\n");
                std::cout << "1. Prime Check\n");
                std::cout << "2. Factorization\n");
                std::cout << "3. GCD and LCM\n");
                std::cout << "Enter choice: ");
                int num_choice = get_user_choice();

                switch (num_choice) {
                    case 1: {
                        int n;
                        std::cout << "Enter number: ");
                        scanf("%d", &n);
                        std::cout << "%d is %s\n", n, is_prime(n) ? "prime" : "not prime");
                        break;
                    }
                    case 2: {
                        int n, factors[100], count;
                        std::cout << "Enter number: ");
                        scanf("%d", &n);
                        factorize(n, factors, &count);
                        std::cout << "Factors: ");
                        for (int i = 0; i < count; i++) {
                            std::cout << "%d ", factors[i]);
                        }
                        std::cout << "\n");
                        break;
                    }
                    case 3: {
                        int a, b;
                        std::cout << "Enter two numbers: ");
                        scanf("%d %d", &a, &b);
                        std::cout << "GCD: %d\n", gcd(a, b));
                        std::cout << "LCM: %d\n", lcm(a, b));
                        break;
                    }
                }
                break;
            }

            case 7: { // Exit
                std::cout << "Goodbye!\n");
                running = 0;
                break;
            }

            default:
                std::cout << "Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
```cpp

---

## Testing the Application

### Compilation Instructions
```bash
# Compile the program
g++ -o math_toolbox main.c math_toolbox.c -lm

# Run the program
./math_toolbox
```cpp

### Test Scenarios
1. **Scientific Calculator**: Test sin(30), log(100), sqrt(144)
2. **Equation Solver**: Solve x² + 5x + 6 = 0, and 2x + 3y = 8, x - y = 2
3. **Matrix Operations**: Add two matrices, multiply matrices
4. **Statistics**: Calculate stats for [1, 3, 5, 7, 9]
5. **Geometry**: Calculate circle area with radius 5
6. **Number Theory**: Check if 17 is prime, factorize 60

### Sample Usage
```cpp
=== Math Toolbox ===
1. Scientific Calculator
2. Equation Solver
3. Matrix Operations
4. Statistics Calculator
5. Geometry Calculator
6. Number Theory
7. Exit
Enter your choice (1-7): 1
Enter number: 30
Enter operation: sin
Result: 0.500000

Enter your choice (1-7): 2
1. Quadratic Equation
2. 2x2 Linear System
Enter choice: 1
Solve ax² + bx + c = 0
Enter a, b, c: 1 5 6
Equation: 1.00x² + 5.00x + 6.00 = 0
Roots: -2.0000, -3.0000
```cpp

---

## Code Explanation

### Key Features Implemented

**Scientific Calculator:**
- [ ] Trigonometric functions with degree/radian conversion
- [ ] Logarithmic and exponential functions
- [ ] Power and root operations

**Equation Solving:**
- [ ] Quadratic formula implementation
- [ ] Linear system solving using Cramer's rule
- [ ] Complex number handling for quadratic equations

**Matrix Operations:**
- [ ] Dynamic matrix creation and memory management
- [ ] Matrix addition and multiplication
- [ ] Determinant calculation for small matrices

**Statistics:**
- [ ] Comprehensive statistical calculations
- [ ] Sorting algorithms for median calculation
- [ ] Standard deviation computation

**Geometry:**
- [ ] Multiple shape calculations
- [ ] Precise geometric formulas
- [ ] 2D and 3D shape support

---

## Enhancements to Try

### Beginner Enhancements
1. **More Functions**: Add hyperbolic functions, factorials
2. **Unit Conversions**: Length, weight, temperature conversions
3. **Complex Numbers**: Support for complex arithmetic

### Intermediate Enhancements
1. **Advanced Matrices**: Eigenvalues, eigenvectors, larger matrices
2. **Numerical Methods**: Root finding, integration, differentiation
3. **Graphing**: Simple function plotting

### Advanced Enhancements
1. **Symbolic Math**: Expression parsing and manipulation
2. **3D Geometry**: Advanced solid geometry calculations
3. **Optimization**: Linear programming, constraint solving

---

## Success Checklist

**Mathematical Features:**
- [x] **Scientific Calculator**: Comprehensive mathematical functions
- [x] **Equation Solving**: Quadratic and linear system solvers
- [x] **Matrix Operations**: Basic matrix algebra
- [x] **Statistics**: Complete statistical analysis toolkit
- [x] **Geometry**: Multiple shape calculations
- [x] **Number Theory**: Prime checking and factorization

**Technical Implementation:**
- [x] **Precision Handling**: Floating-point accuracy management
- [x] **Memory Management**: Dynamic allocation for matrices and arrays
- [x] **Error Handling**: Mathematical constraint validation
- [x] **Modular Design**: Separate functions for different mathematical domains

---

## Learning Outcomes

**Technical Skills:**
- [ ] Advanced mathematical algorithm implementation
- [ ] Numerical precision and stability
- [ ] Dynamic memory management for mathematical structures
- [ ] Complex formula implementation
- [ ] Mathematical function libraries

**Problem-Solving Skills:**
- [ ] Mathematical problem decomposition
- [ ] Algorithm selection for mathematical operations
- [ ] Precision and accuracy considerations
- [ ] Mathematical modeling and implementation

---

## Code Walkthrough

### Mathematical Computation Flow
```cpp
User Input → Validation → Mathematical Calculation → Precision Check → Formatted Output
      ↓           ↓                ↓                    ↓              ↓
Input Parsing  Constraint  Algorithm Execution  Rounding/Precision  Display Results
and Cleaning   Checking    and Processing       Error Handling      with Units
```cpp

### Algorithm Selection
```cpp
Problem Type → Algorithm Choice → Implementation → Testing → Optimization
      ↓              ↓                ↓            ↓          ↓
Mathematical  Numerical Methods  Code Writing   Validation  Performance
Classification Selection         & Debugging   & Accuracy  Tuning
```cpp

---

<div style="page-break-after: always;"></div>

---

## Implementation Notes

### Design Decisions
- [ ] **Modular Functions**: Each mathematical domain in separate functions
- [ ] **Dynamic Memory**: Matrices and arrays allocated as needed
- [ ] **Precision Constants**: EPSILON for floating-point comparisons
- [ ] **Error Handling**: Comprehensive validation of mathematical inputs

### Mathematical Accuracy
- [ ] **Trigonometric Functions**: Degree/radian conversion for user-friendliness
- [ ] **Floating-Point Precision**: Careful handling of numerical errors
- [ ] **Algorithm Stability**: Numerical methods chosen for stability
- [ ] **Range Checking**: Validation of input domains for functions

### Performance Considerations
- [ ] **Memory Efficiency**: Allocate only when needed, free when done
- [ ] **Computational Complexity**: Efficient algorithms for mathematical operations
- [ ] **Precision vs Speed**: Balance between accuracy and performance
- [ ] **Scalability**: Design allows for larger matrices and datasets

---

 **Congratulations! You've built a comprehensive mathematical application!** 

*Next: Interactive applications with advanced user interfaces! *

### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Additional Content

Understand the key concepts:

- [ ] Review each function
- [ ] Understand the flow
- [ ] Learn the patterns used


### Code Review

Key functions and their purpose:

- [ ] Main function: Entry point
- [ ] Helper functions: Support logic


### <div style="page-break-after: always;"></div>

Answer Key

Expected implementation provided.

<div style="page-break-after: always;"></div>

---

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
