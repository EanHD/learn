# Level 4: Temperature Converter

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
