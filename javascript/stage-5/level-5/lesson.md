# Level 5: Library Catalog

## Stage 5: Capstone Project

### Your Project

Build a library system:

1. Store books with title, author, ISBN, available
2. Search books
3. Check out/return
4. Show catalog

---

## ANSWER KEY

```javascript
let books = [
    {title: "JavaScript Basics", author: "Jane Doe", isbn: "001", available: true},
    {title: "Web Programming", author: "John Smith", isbn: "002", available: false},
    {title: "Functions & Objects", author: "Alice Brown", isbn: "003", available: true}
];

function findBook(isbn) {
    for (let i = 0; i < books.length; i++) {
        if (books[i].isbn === isbn) {
            return books[i];
        }
    }
    return null;
}

function checkout(isbn) {
    let book = findBook(isbn);
    if (book && book.available) {
        book.available = false;
        return "Checked out: " + book.title;
    }
    return "Book not available";
}

function returnBook(isbn) {
    let book = findBook(isbn);
    if (book && !book.available) {
        book.available = true;
        return "Returned: " + book.title;
    }
    return "Book not checked out";
}

console.log(checkout("001"));
console.log(returnBook("001"));
```

---

**Search, state management, and real-world app!**
