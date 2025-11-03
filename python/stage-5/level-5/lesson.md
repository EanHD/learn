# Level 5: Budget Tracker

## Stage 5: Capstone Project

### Your Project

Build a budget tracker that:

1. Tracks income and expenses
2. Calculate balance
3. Show transaction history
4. Filter by type
5. Show summary

---

## ANSWER KEY

```python
transactions = []

def add_transaction(amount, trans_type, description):
    trans = {
        "amount": amount,
        "type": trans_type,
        "description": description
    }
    transactions.append(trans)

def get_balance():
    income = 0
    expenses = 0
    for t in transactions:
        if t["type"] == "income":
            income = income + t["amount"]
        else:
            expenses = expenses + t["amount"]
    return income - expenses

while True:
    print("\nBudget Tracker")
    print("Balance: $" + str(get_balance()))
    print("1. Add income")
    print("2. Add expense")
    print("3. View all")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        amt = float(input("Amount: $"))
        desc = input("Description: ")
        add_transaction(amt, "income", desc)
        print("Added!")

    elif choice == "2":
        amt = float(input("Amount: $"))
        desc = input("Description: ")
        add_transaction(amt, "expense", desc)
        print("Added!")

    elif choice == "3":
        for i in range(len(transactions)):
            t = transactions[i]
            print(str(i+1) + ". " + t["type"] + ": $" + str(t["amount"]) + " - " + t["description"])

    elif choice == "4":
        break
```

---

**Dictionaries, functions, and financial data!**
