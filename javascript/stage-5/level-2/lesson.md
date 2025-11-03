# Level 2: Inventory Management System

## Stage 5: Capstone Project

### Your Project

Build an inventory system:

1. Store products with name, price, quantity
2. Add/remove items
3. Calculate total value
4. Display inventory report

---

## ANSWER KEY

```javascript
let inventory = [
    {name: "Apples", price: 1.50, quantity: 50},
    {name: "Bananas", price: 0.75, quantity: 80},
    {name: "Oranges", price: 2.00, quantity: 30}
];

function addItem(name, price, quantity) {
    inventory.push({name: name, price: price, quantity: quantity});
}

function getTotalValue() {
    let total = 0;
    for (let i = 0; i < inventory.length; i++) {
        let item = inventory[i];
        total = total + (item.price * item.quantity);
    }
    return total;
}

function displayInventory() {
    console.log("INVENTORY REPORT");
    console.log("================");
    for (let i = 0; i < inventory.length; i++) {
        let item = inventory[i];
        let value = item.price * item.quantity;
        console.log(item.name + ": " + item.quantity + " units @ $" + item.price + " = $" + value.toFixed(2));
    }
    console.log("Total Value: $" + getTotalValue().toFixed(2));
}

displayInventory();
```

---

**Advanced data structures and reporting!**
