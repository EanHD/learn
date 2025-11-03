#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "gradebook.h"

// Function prototypes
void display_menu();
void add_student();
void add_grade();
void view_student();
void view_all_students();
void calculate_gpa();
void save_data();
void load_data();
int get_menu_choice();
float get_float_input(const char* prompt);
int get_int_input(const char* prompt);
void get_string_input(const char* prompt, char* buffer, int size);

// Global variables for data management
Student students[MAX_STUDENTS];
int student_count = 0;
Grade grades[MAX_GRADES];
int grade_count = 0;

int main() {
    printf("🎓 GRADE MANAGEMENT SYSTEM\n");
    printf("==========================\n\n");

    // Load existing data if available
    load_data();
    printf("System ready! %d students and %d grades loaded.\n\n", student_count, grade_count);

    // Main menu loop
    int choice;
    do {
        display_menu();
        choice = get_menu_choice();

        switch(choice) {
            case 1:
                add_student();
                break;
            case 2:
                add_grade();
                break;
            case 3:
                view_student();
                break;
            case 4:
                view_all_students();
                break;
            case 5:
                calculate_gpa();
                break;
            case 6:
                save_data();
                break;
            case 7:
                printf("Saving data...\n");
                save_data();
                printf("Thank you for using the Grade Management System!\n");
                break;
            default:
                printf("❌ Invalid choice. Please try again.\n");
        }
        printf("\n");
    } while (choice != 7);

    return 0;
}

void display_menu() {
    printf("📋 MAIN MENU\n");
    printf("============\n");
    printf("1. Add Student\n");
    printf("2. Add Grade\n");
    printf("3. View Student Details\n");
    printf("4. View All Students\n");
    printf("5. Calculate GPA\n");
    printf("6. Save Data\n");
    printf("7. Exit\n");
    printf("Enter choice (1-7): ");
}

void add_student() {
    if (student_count >= MAX_STUDENTS) {
        printf("❌ Maximum number of students reached!\n");
        return;
    }

    printf("👤 ADD NEW STUDENT\n");
    printf("=================\n");

    Student new_student;
    new_student.id = get_int_input("Enter student ID: ");

    // Check if student ID already exists
    for (int i = 0; i < student_count; i++) {
        if (students[i].id == new_student.id) {
            printf("❌ Student with ID %d already exists!\n", new_student.id);
            return;
        }
    }

    get_string_input("Enter student name: ", new_student.name, sizeof(new_student.name));
    new_student.grade_count = 0;

    students[student_count] = new_student;
    student_count++;

    printf("✅ Student '%s' added successfully with ID: %d\n", new_student.name, new_student.id);
}

void add_grade() {
    if (grade_count >= MAX_GRADES) {
        printf("❌ Maximum number of grades reached!\n");
        return;
    }

    printf("📝 ADD GRADE\n");
    printf("============\n");

    int student_id = get_int_input("Enter student ID: ");

    // Find student
    int student_index = -1;
    for (int i = 0; i < student_count; i++) {
        if (students[i].id == student_id) {
            student_index = i;
            break;
        }
    }

    if (student_index == -1) {
        printf("❌ Student with ID %d not found!\n", student_id);
        return;
    }

    Grade new_grade;
    new_grade.student_id = student_id;

    get_string_input("Enter assignment name: ", new_grade.assignment_name, sizeof(new_grade.assignment_name));
    new_grade.score = get_float_input("Enter score (0-100): ");

    if (new_grade.score < 0 || new_grade.score > 100) {
        printf("❌ Score must be between 0 and 100!\n");
        return;
    }

    new_grade.max_score = get_float_input("Enter maximum score: ");
    if (new_grade.max_score <= 0) {
        printf("❌ Maximum score must be greater than 0!\n");
        return;
    }

    grades[grade_count] = new_grade;
    grade_count++;

    // Update student's grade count
    students[student_index].grade_count++;

    printf("✅ Grade added for %s: %.1f/%.1f\n",
           new_grade.assignment_name, new_grade.score, new_grade.max_score);
}

void view_student() {
    printf("👤 VIEW STUDENT DETAILS\n");
    printf("======================\n");

    int student_id = get_int_input("Enter student ID: ");

    // Find student
    int student_index = -1;
    for (int i = 0; i < student_count; i++) {
        if (students[i].id == student_id) {
            student_index = i;
            break;
        }
    }

    if (student_index == -1) {
        printf("❌ Student with ID %d not found!\n", student_id);
        return;
    }

    Student student = students[student_index];
    printf("Student ID: %d\n", student.id);
    printf("Name: %s\n", student.name);
    printf("Total Grades: %d\n", student.grade_count);

    if (student.grade_count > 0) {
        printf("\n📊 GRADES:\n");
        printf("----------\n");

        int grade_found = 0;
        for (int i = 0; i < grade_count; i++) {
            if (grades[i].student_id == student_id) {
                float percentage = (grades[i].score / grades[i].max_score) * 100;
                printf("%s: %.1f/%.1f (%.1f%%)\n",
                       grades[i].assignment_name,
                       grades[i].score,
                       grades[i].max_score,
                       percentage);
                grade_found++;
            }
        }

        if (grade_found == 0) {
            printf("No grades recorded yet.\n");
        }
    }
}

void view_all_students() {
    printf("👥 ALL STUDENTS\n");
    printf("===============\n");

    if (student_count == 0) {
        printf("No students registered yet.\n");
        return;
    }

    for (int i = 0; i < student_count; i++) {
        printf("ID: %d, Name: %s, Grades: %d\n",
               students[i].id, students[i].name, students[i].grade_count);
    }
}

void calculate_gpa() {
    printf("📊 GPA CALCULATION\n");
    printf("==================\n");

    int student_id = get_int_input("Enter student ID: ");

    // Find student
    int student_index = -1;
    for (int i = 0; i < student_count; i++) {
        if (students[i].id == student_id) {
            student_index = i;
            break;
        }
    }

    if (student_index == -1) {
        printf("❌ Student with ID %d not found!\n", student_id);
        return;
    }

    // Calculate GPA
    float total_percentage = 0;
    int grade_count_for_student = 0;

    for (int i = 0; i < grade_count; i++) {
        if (grades[i].student_id == student_id) {
            float percentage = (grades[i].score / grades[i].max_score) * 100;
            total_percentage += percentage;
            grade_count_for_student++;
        }
    }

    if (grade_count_for_student == 0) {
        printf("❌ No grades found for student %s\n", students[student_index].name);
        return;
    }

    float average_percentage = total_percentage / grade_count_for_student;

    // Convert to GPA (4.0 scale)
    float gpa;
    if (average_percentage >= 90) gpa = 4.0;
    else if (average_percentage >= 80) gpa = 3.0;
    else if (average_percentage >= 70) gpa = 2.0;
    else if (average_percentage >= 60) gpa = 1.0;
    else gpa = 0.0;

    printf("Student: %s\n", students[student_index].name);
    printf("Average Score: %.1f%%\n", average_percentage);
    printf("GPA: %.1f/4.0\n", gpa);
    printf("Letter Grade: %s\n",
           average_percentage >= 90 ? "A" :
           average_percentage >= 80 ? "B" :
           average_percentage >= 70 ? "C" :
           average_percentage >= 60 ? "D" : "F");
}

void save_data() {
    FILE* file = fopen("grades.dat", "wb");
    if (!file) {
        printf("❌ Error opening file for saving!\n");
        return;
    }

    // Save student count and students
    fwrite(&student_count, sizeof(int), 1, file);
    fwrite(students, sizeof(Student), student_count, file);

    // Save grade count and grades
    fwrite(&grade_count, sizeof(int), 1, file);
    fwrite(grades, sizeof(Grade), grade_count, file);

    fclose(file);
    printf("✅ Data saved successfully!\n");
}

void load_data() {
    FILE* file = fopen("grades.dat", "rb");
    if (!file) {
        printf("No existing data file found. Starting fresh.\n");
        return;
    }

    // Load student count and students
    fread(&student_count, sizeof(int), 1, file);
    if (student_count > MAX_STUDENTS) student_count = MAX_STUDENTS;
    fread(students, sizeof(Student), student_count, file);

    // Load grade count and grades
    fread(&grade_count, sizeof(int), 1, file);
    if (grade_count > MAX_GRADES) grade_count = MAX_GRADES;
    fread(grades, sizeof(Grade), grade_count, file);

    fclose(file);
    printf("✅ Data loaded successfully!\n");
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

float get_float_input(const char* prompt) {
    float value;
    printf("%s", prompt);
    while (scanf("%f", &value) != 1) {
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

void get_string_input(const char* prompt, char* buffer, int size) {
    printf("%s", prompt);
    fgets(buffer, size, stdin);
    // Remove newline character
    buffer[strcspn(buffer, "\n")] = 0;
}