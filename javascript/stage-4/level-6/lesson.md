# Level 6: Quiz Game

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 4: Full Problem Solving

### Your Challenge

Build an interactive quiz:

1. Store questions with answers
2. Shuffle questions
3. Track score
4. Show results

---

## ANSWER KEY

```javascript
let questions = [
    {q: "What is 2+2?", a: "4"},
    {q: "What is 5*6?", a: "30"},
    {q: "What is 10/2?", a: "5"}
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
```

---

**Shuffle algorithm and scoring!**
