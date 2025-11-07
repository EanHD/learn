let tasks = [
  { name: "Finish report", priority: 1, done: false },
  { name: "Email client", priority: 2, done: false },
  { name: "Fix bug", priority: 1, done: true },
  { name: "Update docs", priority: 3, done: false }
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
