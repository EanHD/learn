# Level 4: Temperature Converter

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 4: Full Problem Solving

### Your Challenge

Build a converter for:

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Kelvin to Celsius
4. Display results

---

## ANSWER KEY

```javascript
function celsiusToFahrenheit(c) {
    return (c * 9/5) + 32;
}

function fahrenheitToCelsius(f) {
    return (f - 32) * 5/9;
}

function kelvinToCelsius(k) {
    return k - 273.15;
}

console.log("0C = " + celsiusToFahrenheit(0) + "F");
console.log("32F = " + fahrenheitToCelsius(32) + "C");
console.log("273.15K = " + kelvinToCelsius(273.15) + "C");
```

---

**Functions with return values!**
