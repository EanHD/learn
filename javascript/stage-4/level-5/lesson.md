# Level 5: Budget Tracker

## Stage 4: Full Problem Solving

### Your Challenge

Track income/expenses:

1. Store transactions as objects
2. Calculate balance
3. Show by type
4. Display summary

---

## ANSWER KEY

```javascript
let transactions = [
    {amount: 2000, type: "income", desc: "Salary"},
    {amount: 50, type: "expense", desc: "Gas"},
    {amount: 30, type: "expense", desc: "Lunch"}
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
```

---

**Objects and data structures!**
