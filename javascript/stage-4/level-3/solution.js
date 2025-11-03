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
      console.log((i + 1) + ". " + tasks[i]);
    }
  }
}

viewTasks();
