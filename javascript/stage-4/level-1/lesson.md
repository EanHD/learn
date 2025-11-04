# Level 1: Grade Averager

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 4: Full Problem Solving

### Your Challenge

Build a program that:

1. Accepts 5 test grades (1-100)
2. Calculates the average
3. Displays letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (<60)

---

## ANSWER KEY

```javascript
let grades = [92, 88, 95, 87, 90];
let sum = 0;

for (let i = 0; i < grades.length; i++) {
    sum = sum + grades[i];
}

let average = sum / grades.length;
let letterGrade;

if (average >= 90) {
    letterGrade = "A";
} else if (average >= 80) {
    letterGrade = "B";
} else if (average >= 70) {
    letterGrade = "C";
} else if (average >= 60) {
    letterGrade = "D";
} else {
    letterGrade = "F";
}

console.log("Average: " + average);
console.log("Grade: " + letterGrade);
```

---

**Combine arrays, loops, and conditional logic!**
