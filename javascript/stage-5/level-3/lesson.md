# Level 3: Task Scheduler

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 5: Capstone Project

### Your Project

Build a task scheduler:

1. Store tasks with name, priority, due date
2. Sort by priority
3. Mark complete
4. Show pending tasks

---

## ANSWER KEY

```javascript
let tasks = [
    {name: "Finish report", priority: 1, done: false},
    {name: "Email client", priority: 2, done: false},
    {name: "Fix bug", priority: 1, done: true},
    {name: "Update docs", priority: 3, done: false}
];

function getSortedTasks() {
    let sorted = [];
    for (let i = 0; i < tasks.length; i++) {
        sorted.push(tasks[i]);
    }
    for (let i = 0; i < sorted.length; i++) {
        for (let j = i + 1; j < sorted.length; j++) {
            if (sorted[j].priority < sorted[i].priority) {
                let temp = sorted[i];
                sorted[i] = sorted[j];
                sorted[j] = temp;
            }
        }
    }
    return sorted;
}

function displayPending() {
    let sorted = getSortedTasks();
    console.log("PENDING TASKS");
    for (let i = 0; i < sorted.length; i++) {
        if (!sorted[i].done) {
            console.log("[P" + sorted[i].priority + "] " + sorted[i].name);
        }
    }
}

displayPending();
```

---

**Sorting algorithms and task management!**
