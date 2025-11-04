# Level 3: To-Do List

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 4: Full Problem Solving

### Your Challenge

Build a to-do app that:

1. Store tasks in array
2. Add, view, remove tasks
3. Display with numbers
4. Show status messages

---

## ANSWER KEY

```javascript
let tasks = ["Buy milk", "Do homework", "Walk dog"];

function showMenu() {
    console.log("\nTo-Do List");
    console.log("1. Add task");
    console.log("2. View tasks");
    console.log("3. Remove task");
}

function viewTasks() {
    if (tasks.length === 0) {
        console.log("No tasks");
    } else {
        for (let i = 0; i < tasks.length; i++) {
            console.log((i+1) + ". " + tasks[i]);
        }
    }
}

viewTasks();
```

---

**Array management and functions!**
