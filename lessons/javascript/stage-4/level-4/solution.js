function celsiusToFahrenheit(c) {
  return (c * 9 / 5) + 32;
}

function fahrenheitToCelsius(f) {
  return (f - 32) * 5 / 9;
}

function kelvinToCelsius(k) {
  return k - 273.15;
}

console.log("0C = " + celsiusToFahrenheit(0) + "F");
console.log("32F = " + fahrenheitToCelsius(32) + "C");
console.log("273.15K = " + kelvinToCelsius(273.15) + "C");
