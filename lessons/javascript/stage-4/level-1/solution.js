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
