let secret = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

console.log("I'm thinking of a number 1-100");

let guesses = [45, 72, 88, 92, 95, 97, 98, 99];
for (let i = 0; i < guesses.length; i++) {
  let guess = guesses[i];
  attempts++;
  console.log("Guess: " + guess);
  if (guess === secret) {
    console.log("Correct! Got it in " + attempts + " attempts");
    break;
  } else if (guess < secret) {
    console.log("Too low");
  } else {
    console.log("Too high");
  }
}
