let transactions = [
  { amount: 2000, type: "income", desc: "Salary" },
  { amount: 50, type: "expense", desc: "Gas" },
  { amount: 30, type: "expense", desc: "Lunch" }
];

function getBalance() {
  let balance = 0;
  for (let i = 0; i < transactions.length; i++) {
    if (transactions[i].type === "income") {
      balance = balance + transactions[i].amount;
    } else {
      balance = balance - transactions[i].amount;
    }
  }
  return balance;
}

console.log("Balance: $" + getBalance());
