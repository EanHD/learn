# Level 7: Employee Management

## Stage 5: Capstone Project

### Your Project

Build HR management system:

1. Store employees with name, salary, department
2. Calculate payroll
3. Filter by department
4. Show reports

---

## ANSWER KEY

```javascript
let employees = [
    {name: "Alice", salary: 50000, dept: "Engineering"},
    {name: "Bob", salary: 45000, dept: "Engineering"},
    {name: "Charlie", salary: 40000, dept: "Sales"},
    {name: "Diana", salary: 48000, dept: "Sales"}
];

function getTotalPayroll() {
    let total = 0;
    for (let i = 0; i < employees.length; i++) {
        total = total + employees[i].salary;
    }
    return total;
}

function getDepartmentEmployees(dept) {
    let deptEmps = [];
    for (let i = 0; i < employees.length; i++) {
        if (employees[i].dept === dept) {
            deptEmps.push(employees[i]);
        }
    }
    return deptEmps;
}

function displayDepartmentReport(dept) {
    let emps = getDepartmentEmployees(dept);
    console.log("=== " + dept + " ===");
    let sum = 0;
    for (let i = 0; i < emps.length; i++) {
        console.log(emps[i].name + ": $" + emps[i].salary);
        sum = sum + emps[i].salary;
    }
    console.log("Department Total: $" + sum);
}

displayDepartmentReport("Engineering");
console.log("Total Payroll: $" + getTotalPayroll());
```

---

**HR systems and complex filtering!**
