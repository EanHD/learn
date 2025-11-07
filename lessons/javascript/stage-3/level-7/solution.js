let evenCount = 0;
let oddCount = 0;

for (let i = 1; i <= 20; i++) {
  if (i % 2 === 0) {
    evenCount = evenCount + 1;
  } else {
    oddCount = oddCount + 1;
  }
}

console.log("Even numbers: " + evenCount);
console.log("Odd numbers: " + oddCount);
