# Level 6: Weather Analyzer

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 5: Capstone Project

### Your Project

Build a weather analysis tool:

1. Store daily temperatures
2. Calculate avg, min, max
3. Analyze trends
4. Generate report

---

## ANSWER KEY

```javascript
let weatherData = [
    {day: "Monday", temp: 72},
    {day: "Tuesday", temp: 75},
    {day: "Wednesday", temp: 68},
    {day: "Thursday", temp: 80},
    {day: "Friday", temp: 78}
];

function getStats() {
    let temps = [];
    for (let i = 0; i < weatherData.length; i++) {
        temps.push(weatherData[i].temp);
    }

    let sum = 0;
    let min = temps[0];
    let max = temps[0];

    for (let i = 0; i < temps.length; i++) {
        sum = sum + temps[i];
        if (temps[i] < min) min = temps[i];
        if (temps[i] > max) max = temps[i];
    }

    return {
        avg: sum / temps.length,
        min: min,
        max: max
    };
}

let stats = getStats();
console.log("Average: " + stats.avg.toFixed(1) + "F");
console.log("Low: " + stats.min + "F");
console.log("High: " + stats.max + "F");
```

---

**Data analysis and statistics!**
