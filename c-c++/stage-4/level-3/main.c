#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// Constants
#define MAX_MATRIX_SIZE 10
#define PI 3.14159265358979323846

// Data structures
typedef struct {
    int rows;
    int cols;
    double data[MAX_MATRIX_SIZE][MAX_MATRIX_SIZE];
} Matrix;

// Function prototypes
void display_main_menu();
void scientific_calculator();
void equation_solver();
void matrix_operations();
void statistics_calculator();
void geometry_calculator();
void number_theory_tools();
int get_menu_choice();

// Scientific calculator functions
double calculate_sin(double x, int degrees);
double calculate_cos(double x, int degrees);
double calculate_tan(double x, int degrees);
double calculate_log(double x);
double calculate_ln(double x);
double calculate_power(double base, double exp);
double calculate_sqrt(double x);
double calculate_factorial(int n);

// Equation solver functions
void solve_quadratic();
void solve_linear_system();

// Matrix functions
void matrix_addition();
void matrix_multiplication();
void matrix_determinant();
void matrix_transpose();
void create_matrix(Matrix* m, int rows, int cols);
void display_matrix(const Matrix* m);
double calculate_determinant(const Matrix* m, int n);

// Statistics functions
void calculate_mean_median_mode();
void calculate_standard_deviation();
void linear_regression();

// Geometry functions
void calculate_circle_properties();
void calculate_triangle_properties();
void calculate_rectangle_properties();
void calculate_sphere_properties();

// Number theory functions
void check_prime();
void find_factors();
void calculate_gcd_lcm();
void generate_primes();

// Utility functions
double get_double_input(const char* prompt);
int get_int_input(const char* prompt);
void clear_input_buffer();

int main() {
    printf("🔢 MATHEMATICAL TOOLBOX\n");
    printf("=======================\n\n");

    int choice;
    do {
        display_main_menu();
        choice = get_menu_choice();

        switch(choice) {
            case 1:
                scientific_calculator();
                break;
            case 2:
                equation_solver();
                break;
            case 3:
                matrix_operations();
                break;
            case 4:
                statistics_calculator();
                break;
            case 5:
                geometry_calculator();
                break;
            case 6:
                number_theory_tools();
                break;
            case 7:
                printf("Thank you for using the Mathematical Toolbox!\n");
                break;
            default:
                printf("❌ Invalid choice. Please try again.\n");
        }
        printf("\n");
    } while (choice != 7);

    return 0;
}

void display_main_menu() {
    printf("🧮 MAIN MENU\n");
    printf("============\n");
    printf("1. Scientific Calculator\n");
    printf("2. Equation Solver\n");
    printf("3. Matrix Operations\n");
    printf("4. Statistics Calculator\n");
    printf("5. Geometry Calculator\n");
    printf("6. Number Theory Tools\n");
    printf("7. Exit\n");
    printf("Enter choice (1-7): ");
}

void scientific_calculator() {
    printf("🔬 SCIENTIFIC CALCULATOR\n");
    printf("========================\n");

    while (1) {
        printf("\nScientific Calculator Options:\n");
        printf("1. Trigonometric Functions (sin, cos, tan)\n");
        printf("2. Logarithmic Functions (log, ln)\n");
        printf("3. Power and Root Functions\n");
        printf("4. Factorial\n");
        printf("5. Back to Main Menu\n");
        printf("Enter choice (1-5): ");

        int choice = get_menu_choice();
        if (choice == 5) break;

        double input, result;
        int degrees;

        switch(choice) {
            case 1:
                input = get_double_input("Enter angle: ");
                printf("Use degrees? (1=yes, 0=radians): ");
                degrees = get_menu_choice();
                printf("sin(%.2f) = %.6f\n", input, calculate_sin(input, degrees));
                printf("cos(%.2f) = %.6f\n", input, calculate_cos(input, degrees));
                printf("tan(%.2f) = %.6f\n", input, calculate_tan(input, degrees));
                break;
            case 2:
                input = get_double_input("Enter number: ");
                if (input > 0) {
                    printf("log(%.2f) = %.6f\n", input, calculate_log(input));
                    printf("ln(%.2f) = %.6f\n", input, calculate_ln(input));
                } else {
                    printf("❌ Logarithm undefined for non-positive numbers\n");
                }
                break;
            case 3:
                printf("Choose operation:\n");
                printf("1. Power (x^y)\n");
                printf("2. Square Root\n");
                int op = get_menu_choice();
                if (op == 1) {
                    double base = get_double_input("Enter base: ");
                    double exp = get_double_input("Enter exponent: ");
                    result = calculate_power(base, exp);
                    printf("%.2f ^ %.2f = %.6f\n", base, exp, result);
                } else {
                    input = get_double_input("Enter number: ");
                    if (input >= 0) {
                        result = calculate_sqrt(input);
                        printf("√%.2f = %.6f\n", input, result);
                    } else {
                        printf("❌ Square root undefined for negative numbers\n");
                    }
                }
                break;
            case 4:
                int n = get_int_input("Enter non-negative integer: ");
                if (n >= 0) {
                    result = calculate_factorial(n);
                    printf("%d! = %.0f\n", n, result);
                } else {
                    printf("❌ Factorial undefined for negative numbers\n");
                }
                break;
            default:
                printf("❌ Invalid choice.\n");
        }
    }
}

void equation_solver() {
    printf("🔍 EQUATION SOLVER\n");
    printf("==================\n");

    while (1) {
        printf("\nEquation Solver Options:\n");
        printf("1. Quadratic Equation (ax² + bx + c = 0)\n");
        printf("2. 2x2 Linear System\n");
        printf("3. Back to Main Menu\n");
        printf("Enter choice (1-3): ");

        int choice = get_menu_choice();
        if (choice == 3) break;

        switch(choice) {
            case 1:
                solve_quadratic();
                break;
            case 2:
                solve_linear_system();
                break;
            default:
                printf("❌ Invalid choice.\n");
        }
    }
}

void solve_quadratic() {
    printf("Quadratic Equation Solver\n");
    printf("ax² + bx + c = 0\n\n");

    double a = get_double_input("Enter coefficient a: ");
    double b = get_double_input("Enter coefficient b: ");
    double c = get_double_input("Enter coefficient c: ");

    if (a == 0) {
        printf("❌ Not a quadratic equation (a cannot be 0)\n");
        return;
    }

    double discriminant = b*b - 4*a*c;

    if (discriminant > 0) {
        double root1 = (-b + sqrt(discriminant)) / (2*a);
        double root2 = (-b - sqrt(discriminant)) / (2*a);
        printf("Two real roots: x = %.6f, x = %.6f\n", root1, root2);
    } else if (discriminant == 0) {
        double root = -b / (2*a);
        printf("One real root: x = %.6f\n", root);
    } else {
        double real_part = -b / (2*a);
        double imag_part = sqrt(-discriminant) / (2*a);
        printf("Complex roots: x = %.6f ± %.6fi\n", real_part, imag_part);
    }
}

void solve_linear_system() {
    printf("2x2 Linear System Solver\n");
    printf("a₁x + b₁y = c₁\n");
    printf("a₂x + b₂y = c₂\n\n");

    double a1 = get_double_input("Enter a₁: ");
    double b1 = get_double_input("Enter b₁: ");
    double c1 = get_double_input("Enter c₁: ");
    double a2 = get_double_input("Enter a₂: ");
    double b2 = get_double_input("Enter b₂: ");
    double c2 = get_double_input("Enter c₂: ");

    double determinant = a1*b2 - a2*b1;

    if (determinant == 0) {
        printf("❌ System has no unique solution (determinant = 0)\n");
        return;
    }

    double x = (c1*b2 - c2*b1) / determinant;
    double y = (a1*c2 - a2*c1) / determinant;

    printf("Solution: x = %.6f, y = %.6f\n", x, y);
}

void matrix_operations() {
    printf("📊 MATRIX OPERATIONS\n");
    printf("====================\n");

    while (1) {
        printf("\nMatrix Operations:\n");
        printf("1. Matrix Addition\n");
        printf("2. Matrix Multiplication\n");
        printf("3. Matrix Determinant\n");
        printf("4. Matrix Transpose\n");
        printf("5. Back to Main Menu\n");
        printf("Enter choice (1-5): ");

        int choice = get_menu_choice();
        if (choice == 5) break;

        switch(choice) {
            case 1:
                matrix_addition();
                break;
            case 2:
                matrix_multiplication();
                break;
            case 3:
                matrix_determinant();
                break;
            case 4:
                matrix_transpose();
                break;
            default:
                printf("❌ Invalid choice.\n");
        }
    }
}

void matrix_addition() {
    printf("Matrix Addition (A + B)\n\n");

    int rows = get_int_input("Enter number of rows: ");
    int cols = get_int_input("Enter number of columns: ");

    if (rows > MAX_MATRIX_SIZE || cols > MAX_MATRIX_SIZE) {
        printf("❌ Matrix too large (max %dx%d)\n", MAX_MATRIX_SIZE, MAX_MATRIX_SIZE);
        return;
    }

    Matrix A, B, C;
    create_matrix(&A, rows, cols);
    create_matrix(&B, rows, cols);
    create_matrix(&C, rows, cols);

    printf("Enter matrix A:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("A[%d][%d]: ", i+1, j+1);
            A.data[i][j] = get_double_input("");
        }
    }

    printf("Enter matrix B:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("B[%d][%d]: ", i+1, j+1);
            B.data[i][j] = get_double_input("");
        }
    }

    // Add matrices
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            C.data[i][j] = A.data[i][j] + B.data[i][j];
        }
    }

    printf("\nResult (A + B):\n");
    display_matrix(&C);
}

void matrix_multiplication() {
    printf("Matrix Multiplication (A × B)\n\n");

    int rowsA = get_int_input("Enter rows for matrix A: ");
    int colsA = get_int_input("Enter columns for matrix A: ");
    int rowsB = get_int_input("Enter rows for matrix B: ");
    int colsB = get_int_input("Enter columns for matrix B: ");

    if (colsA != rowsB) {
        printf("❌ Cannot multiply matrices: columns of A must equal rows of B\n");
        return;
    }

    if (rowsA > MAX_MATRIX_SIZE || colsA > MAX_MATRIX_SIZE ||
        rowsB > MAX_MATRIX_SIZE || colsB > MAX_MATRIX_SIZE) {
        printf("❌ Matrix too large (max %dx%d)\n", MAX_MATRIX_SIZE, MAX_MATRIX_SIZE);
        return;
    }

    Matrix A, B, C;
    create_matrix(&A, rowsA, colsA);
    create_matrix(&B, rowsB, colsB);
    create_matrix(&C, rowsA, colsB);

    printf("Enter matrix A:\n");
    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsA; j++) {
            printf("A[%d][%d]: ", i+1, j+1);
            A.data[i][j] = get_double_input("");
        }
    }

    printf("Enter matrix B:\n");
    for (int i = 0; i < rowsB; i++) {
        for (int j = 0; j < colsB; j++) {
            printf("B[%d][%d]: ", i+1, j+1);
            B.data[i][j] = get_double_input("");
        }
    }

    // Multiply matrices
    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsB; j++) {
            C.data[i][j] = 0;
            for (int k = 0; k < colsA; k++) {
                C.data[i][j] += A.data[i][k] * B.data[k][j];
            }
        }
    }

    printf("\nResult (A × B):\n");
    display_matrix(&C);
}

void matrix_determinant() {
    printf("Matrix Determinant\n\n");

    int size = get_int_input("Enter matrix size (NxN): ");

    if (size > MAX_MATRIX_SIZE) {
        printf("❌ Matrix too large (max %dx%d)\n", MAX_MATRIX_SIZE, MAX_MATRIX_SIZE);
        return;
    }

    Matrix M;
    create_matrix(&M, size, size);

    printf("Enter matrix elements:\n");
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("M[%d][%d]: ", i+1, j+1);
            M.data[i][j] = get_double_input("");
        }
    }

    double det = calculate_determinant(&M, size);
    printf("\nDeterminant = %.6f\n", det);
}

void matrix_transpose() {
    printf("Matrix Transpose\n\n");

    int rows = get_int_input("Enter number of rows: ");
    int cols = get_int_input("Enter number of columns: ");

    if (rows > MAX_MATRIX_SIZE || cols > MAX_MATRIX_SIZE) {
        printf("❌ Matrix too large (max %dx%d)\n", MAX_MATRIX_SIZE, MAX_MATRIX_SIZE);
        return;
    }

    Matrix M, T;
    create_matrix(&M, rows, cols);
    create_matrix(&T, cols, rows);

    printf("Enter matrix elements:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("M[%d][%d]: ", i+1, j+1);
            M.data[i][j] = get_double_input("");
        }
    }

    // Transpose
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            T.data[j][i] = M.data[i][j];
        }
    }

    printf("\nTranspose:\n");
    display_matrix(&T);
}

void statistics_calculator() {
    printf("📈 STATISTICS CALCULATOR\n");
    printf("========================\n");

    while (1) {
        printf("\nStatistics Options:\n");
        printf("1. Mean, Median, Mode\n");
        printf("2. Standard Deviation\n");
        printf("3. Linear Regression\n");
        printf("4. Back to Main Menu\n");
        printf("Enter choice (1-4): ");

        int choice = get_menu_choice();
        if (choice == 4) break;

        switch(choice) {
            case 1:
                calculate_mean_median_mode();
                break;
            case 2:
                calculate_standard_deviation();
                break;
            case 3:
                linear_regression();
                break;
            default:
                printf("❌ Invalid choice.\n");
        }
    }
}

void calculate_mean_median_mode() {
    int n = get_int_input("Enter number of data points: ");
    if (n <= 0 || n > 100) {
        printf("❌ Invalid number of data points (1-100)\n");
        return;
    }

    double data[100];
    printf("Enter %d data points:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Data[%d]: ", i+1);
        data[i] = get_double_input("");
    }

    // Calculate mean
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += data[i];
    }
    double mean = sum / n;

    // Calculate median
    // Simple bubble sort for median
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (data[j] > data[j+1]) {
                double temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }

    double median;
    if (n % 2 == 0) {
        median = (data[n/2 - 1] + data[n/2]) / 2.0;
    } else {
        median = data[n/2];
    }

    // Calculate mode (simplified - finds most frequent value)
    double mode = data[0];
    int max_count = 1;
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (data[j] == data[i]) count++;
        }
        if (count > max_count) {
            max_count = count;
            mode = data[i];
        }
    }

    printf("\nResults:\n");
    printf("Mean: %.6f\n", mean);
    printf("Median: %.6f\n", median);
    printf("Mode: %.6f (appears %d times)\n", mode, max_count);
}

void calculate_standard_deviation() {
    int n = get_int_input("Enter number of data points: ");
    if (n <= 1 || n > 100) {
        printf("❌ Need at least 2 data points (max 100)\n");
        return;
    }

    double data[100];
    printf("Enter %d data points:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Data[%d]: ", i+1);
        data[i] = get_double_input("");
    }

    // Calculate mean
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += data[i];
    }
    double mean = sum / n;

    // Calculate variance
    double variance = 0;
    for (int i = 0; i < n; i++) {
        variance += (data[i] - mean) * (data[i] - mean);
    }
    variance /= (n - 1); // Sample standard deviation

    double std_dev = sqrt(variance);

    printf("\nResults:\n");
    printf("Mean: %.6f\n", mean);
    printf("Variance: %.6f\n", variance);
    printf("Standard Deviation: %.6f\n", std_dev);
}

void linear_regression() {
    int n = get_int_input("Enter number of data points: ");
    if (n <= 1 || n > 50) {
        printf("❌ Need at least 2 data points (max 50)\n");
        return;
    }

    double x[50], y[50];
    printf("Enter %d (x, y) data points:\n", n);
    for (int i = 0; i < n; i++) {
        printf("Point %d:\n", i+1);
        printf("  x: ");
        x[i] = get_double_input("");
        printf("  y: ");
        y[i] = get_double_input("");
    }

    // Calculate sums
    double sum_x = 0, sum_y = 0, sum_xy = 0, sum_x2 = 0;
    for (int i = 0; i < n; i++) {
        sum_x += x[i];
        sum_y += y[i];
        sum_xy += x[i] * y[i];
        sum_x2 += x[i] * x[i];
    }

    // Calculate slope (m) and intercept (b)
    double m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x);
    double b = (sum_y - m * sum_x) / n;

    printf("\nLinear Regression Results:\n");
    printf("Equation: y = %.6fx + %.6f\n", m, b);
    printf("Slope (m): %.6f\n", m);
    printf("Intercept (b): %.6f\n", b);
}

void geometry_calculator() {
    printf("📐 GEOMETRY CALCULATOR\n");
    printf("======================\n");

    while (1) {
        printf("\nGeometry Options:\n");
        printf("1. Circle Properties\n");
        printf("2. Triangle Properties\n");
        printf("3. Rectangle Properties\n");
        printf("4. Sphere Properties\n");
        printf("5. Back to Main Menu\n");
        printf("Enter choice (1-5): ");

        int choice = get_menu_choice();
        if (choice == 5) break;

        switch(choice) {
            case 1:
                calculate_circle_properties();
                break;
            case 2:
                calculate_triangle_properties();
                break;
            case 3:
                calculate_rectangle_properties();
                break;
            case 4:
                calculate_sphere_properties();
                break;
            default:
                printf("❌ Invalid choice.\n");
        }
    }
}

void calculate_circle_properties() {
    double radius = get_double_input("Enter radius: ");
    if (radius <= 0) {
        printf("❌ Radius must be positive\n");
        return;
    }

    double area = PI * radius * radius;
    double circumference = 2 * PI * radius;
    double diameter = 2 * radius;

    printf("\nCircle Properties (r = %.2f):\n", radius);
    printf("Diameter: %.6f\n", diameter);
    printf("Circumference: %.6f\n", circumference);
    printf("Area: %.6f\n", area);
}

void calculate_triangle_properties() {
    printf("Triangle Type:\n");
    printf("1. Right Triangle (by sides)\n");
    printf("2. General Triangle (by sides)\n");
    printf("3. Triangle by base and height\n");
    int type = get_menu_choice();

    if (type == 1) {
        double a = get_double_input("Enter side a: ");
        double b = get_double_input("Enter side b: ");
        if (a <= 0 || b <= 0) {
            printf("❌ Sides must be positive\n");
            return;
        }

        double hypotenuse = sqrt(a*a + b*b);
        double perimeter = a + b + hypotenuse;
        double area = (a * b) / 2;

        printf("\nRight Triangle Properties:\n");
        printf("Sides: %.2f, %.2f, %.2f\n", a, b, hypotenuse);
        printf("Perimeter: %.6f\n", perimeter);
        printf("Area: %.6f\n", area);
    } else if (type == 2) {
        double a = get_double_input("Enter side a: ");
        double b = get_double_input("Enter side b: ");
        double c = get_double_input("Enter side c: ");

        if (a <= 0 || b <= 0 || c <= 0) {
            printf("❌ Sides must be positive\n");
            return;
        }

        if (a + b <= c || a + c <= b || b + c <= a) {
            printf("❌ Invalid triangle sides\n");
            return;
        }

        double perimeter = a + b + c;
        double s = perimeter / 2;
        double area = sqrt(s * (s - a) * (s - b) * (s - c));

        printf("\nTriangle Properties:\n");
        printf("Sides: %.2f, %.2f, %.2f\n", a, b, c);
        printf("Perimeter: %.6f\n", perimeter);
        printf("Area: %.6f\n", area);
    } else {
        double base = get_double_input("Enter base: ");
        double height = get_double_input("Enter height: ");
        if (base <= 0 || height <= 0) {
            printf("❌ Base and height must be positive\n");
            return;
        }

        double area = (base * height) / 2;

        printf("\nTriangle Properties:\n");
        printf("Base: %.2f, Height: %.2f\n", base, height);
        printf("Area: %.6f\n", area);
    }
}

void calculate_rectangle_properties() {
    double length = get_double_input("Enter length: ");
    double width = get_double_input("Enter width: ");
    if (length <= 0 || width <= 0) {
        printf("❌ Length and width must be positive\n");
        return;
    }

    double perimeter = 2 * (length + width);
    double area = length * width;
    double diagonal = sqrt(length*length + width*width);

    printf("\nRectangle Properties:\n");
    printf("Length: %.2f, Width: %.2f\n", length, width);
    printf("Perimeter: %.6f\n", perimeter);
    printf("Area: %.6f\n", area);
    printf("Diagonal: %.6f\n", diagonal);
}

void calculate_sphere_properties() {
    double radius = get_double_input("Enter radius: ");
    if (radius <= 0) {
        printf("❌ Radius must be positive\n");
        return;
    }

    double volume = (4.0/3.0) * PI * radius * radius * radius;
    double surface_area = 4 * PI * radius * radius;
    double diameter = 2 * radius;

    printf("\nSphere Properties (r = %.2f):\n", radius);
    printf("Diameter: %.6f\n", diameter);
    printf("Surface Area: %.6f\n", surface_area);
    printf("Volume: %.6f\n", volume);
}

void number_theory_tools() {
    printf("🔢 NUMBER THEORY TOOLS\n");
    printf("=======================\n");

    while (1) {
        printf("\nNumber Theory Options:\n");
        printf("1. Check if Prime\n");
        printf("2. Find Factors\n");
        printf("3. Calculate GCD and LCM\n");
        printf("4. Generate Primes\n");
        printf("5. Back to Main Menu\n");
        printf("Enter choice (1-5): ");

        int choice = get_menu_choice();
        if (choice == 5) break;

        switch(choice) {
            case 1:
                check_prime();
                break;
            case 2:
                find_factors();
                break;
            case 3:
                calculate_gcd_lcm();
                break;
            case 4:
                generate_primes();
                break;
            default:
                printf("❌ Invalid choice.\n");
        }
    }
}

void check_prime() {
    int n = get_int_input("Enter a positive integer: ");
    if (n <= 1) {
        printf("❌ Number must be greater than 1\n");
        return;
    }

    int is_prime = 1;
    if (n > 2 && n % 2 == 0) {
        is_prime = 0;
    } else {
        for (int i = 3; i*i <= n; i += 2) {
            if (n % i == 0) {
                is_prime = 0;
                break;
            }
        }
    }

    if (is_prime) {
        printf("%d is a prime number\n", n);
    } else {
        printf("%d is not a prime number\n", n);
    }
}

void find_factors() {
    int n = get_int_input("Enter a positive integer: ");
    if (n <= 0) {
        printf("❌ Number must be positive\n");
        return;
    }

    printf("Factors of %d: ", n);
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

void calculate_gcd_lcm() {
    int a = get_int_input("Enter first positive integer: ");
    int b = get_int_input("Enter second positive integer: ");
    if (a <= 0 || b <= 0) {
        printf("❌ Both numbers must be positive\n");
        return;
    }

    // Calculate GCD using Euclidean algorithm
    int gcd = a;
    int temp_b = b;
    while (temp_b != 0) {
        int temp = temp_b;
        temp_b = gcd % temp_b;
        gcd = temp;
    }

    // Calculate LCM
    int lcm = (a * b) / gcd;

    printf("GCD(%d, %d) = %d\n", a, b, gcd);
    printf("LCM(%d, %d) = %d\n", a, b, lcm);
}

void generate_primes() {
    int limit = get_int_input("Enter upper limit: ");
    if (limit < 2) {
        printf("❌ Limit must be at least 2\n");
        return;
    }

    printf("Prime numbers up to %d:\n", limit);

    for (int n = 2; n <= limit; n++) {
        int is_prime = 1;
        if (n > 2 && n % 2 == 0) {
            is_prime = 0;
        } else {
            for (int i = 3; i*i <= n; i += 2) {
                if (n % i == 0) {
                    is_prime = 0;
                    break;
                }
            }
        }

        if (is_prime) {
            printf("%d ", n);
        }
    }
    printf("\n");
}

// Utility functions
int get_menu_choice() {
    int choice;
    while (scanf("%d", &choice) != 1) {
        while (getchar() != '\n'); // Clear input buffer
        printf("Please enter a valid number: ");
    }
    while (getchar() != '\n'); // Clear newline
    return choice;
}

double get_double_input(const char* prompt) {
    double value;
    printf("%s", prompt);
    while (scanf("%lf", &value) != 1) {
        while (getchar() != '\n'); // Clear input buffer
        printf("Please enter a valid number: ");
    }
    while (getchar() != '\n'); // Clear newline
    return value;
}

int get_int_input(const char* prompt) {
    int value;
    printf("%s", prompt);
    while (scanf("%d", &value) != 1) {
        while (getchar() != '\n'); // Clear input buffer
        printf("Please enter a valid number: ");
    }
    while (getchar() != '\n'); // Clear newline
    return value;
}

void create_matrix(Matrix* m, int rows, int cols) {
    m->rows = rows;
    m->cols = cols;
    // Initialize to zero
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            m->data[i][j] = 0.0;
        }
    }
}

void display_matrix(const Matrix* m) {
    for (int i = 0; i < m->rows; i++) {
        for (int j = 0; j < m->cols; j++) {
            printf("%.2f ", m->data[i][j]);
        }
        printf("\n");
    }
}

double calculate_determinant(const Matrix* m, int n) {
    if (n == 1) {
        return m->data[0][0];
    }

    if (n == 2) {
        return m->data[0][0] * m->data[1][1] - m->data[0][1] * m->data[1][0];
    }

    // For larger matrices, use basic expansion (not optimized)
    double det = 0;
    for (int j = 0; j < n; j++) {
        Matrix submatrix;
        create_matrix(&submatrix, n-1, n-1);

        // Create submatrix
        for (int i = 1; i < n; i++) {
            int col = 0;
            for (int k = 0; k < n; k++) {
                if (k != j) {
                    submatrix.data[i-1][col] = m->data[i][k];
                    col++;
                }
            }
        }

        double sign = (j % 2 == 0) ? 1 : -1;
        det += sign * m->data[0][j] * calculate_determinant(&submatrix, n-1);
    }

    return det;
}

// Mathematical functions
double calculate_sin(double x, int degrees) {
    if (degrees) x = x * PI / 180.0;
    return sin(x);
}

double calculate_cos(double x, int degrees) {
    if (degrees) x = x * PI / 180.0;
    return cos(x);
}

double calculate_tan(double x, int degrees) {
    if (degrees) x = x * PI / 180.0;
    return tan(x);
}

double calculate_log(double x) {
    return log10(x);
}

double calculate_ln(double x) {
    return log(x);
}

double calculate_power(double base, double exp) {
    return pow(base, exp);
}

double calculate_sqrt(double x) {
    return sqrt(x);
}

double calculate_factorial(int n) {
    if (n == 0 || n == 1) return 1.0;
    double result = 1.0;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}