# Level 1: Student Grade Calculator

## Stage 5: Capstone Project

### Your Project

Build a complete grade management system:

1. Accept multiple grades
2. Calculate average
3. Assign letter grade
4. Display full report

---

## ANSWER KEY

```javascript
let students = [
    {name: "Alice", grades: [92, 88, 95]},
    {name: "Bob", grades: [78, 82, 80]},
    {name: "Charlie", grades: [65, 70, 68]}
];

function calculateAverage(grades) {
    let sum = 0;
    for (let i = 0; i < grades.length; i++) {
        sum = sum + grades[i];
    }
    return sum / grades.length;
}

function getLetterGrade(avg) {
    if (avg >= 90) return "A";
    if (avg >= 80) return "B";
    if (avg >= 70) return "C";
    if (avg >= 60) return "D";
    return "F";
}

for (let i = 0; i < students.length; i++) {
    let s = students[i];
    let avg = calculateAverage(s.grades);
    let letter = getLetterGrade(avg);
    console.log(s.name + ": " + avg.toFixed(2) + " (" + letter + ")");
}
```

---

**Functions, arrays, and real-world data!**
