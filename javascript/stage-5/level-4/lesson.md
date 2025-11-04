# Level 4: Bank Account System

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 5: Capstone Project

### Your Project

Build a simple banking system:

1. Store accounts with owner, balance, transactions
2. Deposit and withdraw
3. Calculate interest
4. Show statements

---

## ANSWER KEY

```javascript
let accounts = [
    {owner: "Alice", balance: 1000, transactions: []},
    {owner: "Bob", balance: 500, transactions: []}
];

function deposit(accountIndex, amount) {
    accounts[accountIndex].balance = accounts[accountIndex].balance + amount;
    accounts[accountIndex].transactions.push({type: "deposit", amount: amount});
}

function withdraw(accountIndex, amount) {
    if (amount <= accounts[accountIndex].balance) {
        accounts[accountIndex].balance = accounts[accountIndex].balance - amount;
        accounts[accountIndex].transactions.push({type: "withdrawal", amount: amount});
        return true;
    }
    return false;
}

function calculateInterest(accountIndex, rate) {
    let interest = accounts[accountIndex].balance * rate / 100;
    accounts[accountIndex].balance = accounts[accountIndex].balance + interest;
    return interest;
}

deposit(0, 100);
withdraw(0, 50);
let interest = calculateInterest(0, 2);

console.log("Alice Balance: $" + accounts[0].balance.toFixed(2));
console.log("Interest earned: $" + interest.toFixed(2));
```

---

**Financial calculations and transactions!**
