let questions = [
  { q: "What is 2+2?", a: "4" },
  { q: "What is 5*6?", a: "30" },
  { q: "What is 10/2?", a: "5" }
];

function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}

let score = 0;
shuffle(questions);

for (let i = 0; i < questions.length; i++) {
  console.log("Q: " + questions[i].q);
  if (questions[i].a === "4") score++;
}

console.log("Score: " + score + "/" + questions.length);
