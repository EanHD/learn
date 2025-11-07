# NoSQL Workspace Instructions

## Getting Started with NoSQL (MongoDB)

Welcome to document databases!

---

## Installation

**MongoDB Shell (mongosh):**

**Linux:**
```bash
sudo apt install mongodb-org-shell
```

**macOS:**
```bash
brew install mongodb-community-shell
```

**Windows:**
Download from [MongoDB](https://www.mongodb.com/try/download/shell)

### Verify Installation

```bash
mongosh --version
```

---

## Running NoSQL Scripts

**Method 1 (Vim):** `<Space>r`

**Method 2 (Terminal):**
```bash
mongosh < main.js
```

---

## Your First Script

Create `main.js`:

```javascript
// Connect to local MongoDB
use test_db;
db.greeting.insertOne({ message: "Hello, NoSQL!" });
db.greeting.findOne();
```

---

## NoSQL Basics

### Insert Documents

```javascript
db.collection.insertOne({ name: "Alice", age: 25 });
db.collection.insertMany([
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 35 }
]);
```

### Query Documents

```javascript
db.collection.find();
db.collection.findOne({ name: "Alice" });
db.collection.find({ age: { $gt: 25 } });
```

### Update Documents

```javascript
db.collection.updateOne(
  { name: "Alice" },
  { $set: { age: 26 } }
);
```

### Delete Documents

```javascript
db.collection.deleteOne({ name: "Alice" });
```

---

## Resources

- [MongoDB Documentation](https://docs.mongodb.com/)
- [MongoDB University](https://university.mongodb.com/)
- [MongoDB Compass (GUI)](https://www.mongodb.com/products/tools/compass)

Store and query!
