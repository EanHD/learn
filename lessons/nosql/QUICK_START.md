# 🚀 NoSQL - Quick Start Guide

> **Status:** ✅ Production Ready | **Total Lessons:** 35 | **Stages:** 5

---

## Installation (Choose Your Database)

### MongoDB (Primary Focus)

**Linux:**
```bash
sudo apt install mongodb
```

**macOS:**
```bash
brew install mongodb-community
```

**Windows:**
Download from [mongodb.com](https://www.mongodb.com/try/download/community)

### Redis (Stage 3+)

**Linux:**
```bash
sudo apt install redis-server
```

**macOS:**
```bash
brew install redis
```

### ✅ Verify Installation

```bash
mongo --version
redis-cli --version
```

---

## Learning Path

### 🟢 Beginner (Stages 1-2: ~20 hours)
- **Stage 1:** MongoDB Basics (Hello World, Queries, CRUD)
- **Stage 2:** Advanced MongoDB (Indexing, Aggregation, Transactions)

### 🟡 Intermediate (Stage 3: ~15 hours)
- **Stage 3:** Multiple NoSQL DBs (Redis, CouchDB, DynamoDB comparison)

### 🔴 Advanced (Stages 4-5: ~30 hours)
- **Stage 4:** Real Applications (Database Design, Optimization, Scaling)
- **Stage 5:** Capstone Projects (Full Data Solutions)

---

## Running Lessons

### 📝 Method 1: Vim (Recommended)
```vim
<Space>r        " Run database commands
```

### 💻 Method 2: Terminal (MongoDB)
```bash
mongo
> use mydb
> db.collection.find()
```

### 💻 Method 2: Terminal (Redis)
```bash
redis-cli
> SET key value
> GET key
```

---

## Lesson Structure

Every lesson includes:
- ✅ **Learning Goals** - What you'll learn
- ✅ **Task/Challenge** - What to implement
- ✅ **Code Examples** - Working database queries
- ✅ **Success Checklist** - Progress tracking
- ✅ **Optional Challenges** - Extended learning

---

## Progress Tracking

Track your progress:
- [ ] Stage 1: MongoDB Fundamentals (Levels 1-7)
- [ ] Stage 2: Advanced MongoDB (Levels 1-7)
- [ ] Stage 3: NoSQL Diversity (Levels 1-7)
- [ ] Stage 4: Real Applications (Levels 1-7)
- [ ] Stage 5: Capstone Project (Levels 1-7)

---

## Key Resources

| Resource | Location |
|----------|----------|
| **Lessons** | `stage-*/level-*/lesson.md` |
| **Table of Contents** | `TABLE_OF_CONTENTS.md` |
| **Setup Guide** | `WORKSPACE_INSTRUCTIONS.md` |
| **All Stages** | 5 stages × 7 levels = 35 lessons |

---

## Quick Tips

💡 **Working with Vim:**
- Press `Ctrl+h` to switch to lesson window
- Press `Ctrl+l` to switch to code window
- Use `<Space>r` to run your database commands

💡 **Getting Help:**
- MongoDB Docs: https://docs.mongodb.com/
- Redis Docs: https://redis.io/documentation/
- NoSQL Guide: https://www.nosql-database.org/

💡 **Best Practices:**
- Start with Stage 1 fundamentals
- Learn MongoDB deeply in Stage 2
- Explore other NoSQL platforms in Stage 3
- Build real applications in Stage 4
- Build the Stage 5 capstone project for your portfolio

---

## Common Tasks

### MongoDB - Start Server
```bash
mongod  # Server
mongo   # Client
```

### MongoDB - Basic Queries
```bash
mongo
> use testdb
> db.users.insertOne({ name: "Alice", age: 30 })
> db.users.find()
```

### Redis - Start Server
```bash
redis-server  # Server
redis-cli     # Client
```

### Redis - Basic Commands
```bash
redis-cli
> SET mykey "Hello"
> GET mykey
> DEL mykey
```

---

## Next Steps

1. ✅ Install MongoDB and/or Redis
2. ✅ Navigate to Stage 1, Level 1
3. ✅ Open `lesson.md` in Vim
4. ✅ Complete the Hello World lesson
5. ✅ Progress through all 35 lessons
6. ✅ Build your portfolio capstone project

---

**Happy Learning! 🎉**

For issues or questions, refer to the lesson files or check the NoSQL documentation.
