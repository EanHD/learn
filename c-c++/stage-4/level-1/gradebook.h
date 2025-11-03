#ifndef GRADEBOOK_H
#define GRADEBOOK_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100
#define MAX_GRADES 500
#define MAX_NAME_LENGTH 50
#define MAX_ASSIGNMENT_LENGTH 50

// Student structure
typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    int grade_count;
} Student;

// Grade structure
typedef struct {
    int student_id;
    char assignment_name[MAX_ASSIGNMENT_LENGTH];
    float score;
    float max_score;
} Grade;

// Function prototypes for utility functions
int get_menu_choice();
float get_float_input(const char* prompt);
int get_int_input(const char* prompt);
void get_string_input(const char* prompt, char* buffer, int size);

#endif