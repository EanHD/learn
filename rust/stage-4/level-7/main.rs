use std::fs;
use std::io::{self, Write};
use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};

#[derive(Debug, Clone)]
enum BookStatus {
    Available,
    Borrowed { user_id: u32, due_date: u64 },
    Overdue { user_id: u32, due_date: u64 },
}

#[derive(Debug, Clone)]
struct Book {
    id: u32,
    title: String,
    author: String,
    isbn: String,
    status: BookStatus,
}

#[derive(Debug, Clone)]
struct User {
    id: u32,
    name: String,
    email: String,
    borrowed_books: Vec<u32>, // Book IDs
    max_books: u32,
}

#[derive(Debug, Clone)]
struct Transaction {
    id: u32,
    book_id: u32,
    user_id: u32,
    checkout_date: u64,
    due_date: u64,
    return_date: Option<u64>,
    status: TransactionStatus,
}

#[derive(Debug, Clone)]
enum TransactionStatus {
    Active,
    Returned,
    Overdue,
}

#[derive(Debug)]
struct Library {
    books: HashMap<u32, Book>,
    users: HashMap<u32, User>,
    transactions: HashMap<u32, Transaction>,
    next_book_id: u32,
    next_user_id: u32,
    next_transaction_id: u32,
}

impl Library {
    fn new() -> Self {
        Library {
            books: HashMap::new(),
            users: HashMap::new(),
            transactions: HashMap::new(),
            next_book_id: 1,
            next_user_id: 1,
            next_transaction_id: 1,
        }
    }

    // ===== BOOK MANAGEMENT =====

    fn add_book(&mut self, title: String, author: String, isbn: String) {
        let book = Book {
            id: self.next_book_id,
            title,
            author,
            isbn,
            status: BookStatus::Available,
        };
        self.books.insert(self.next_book_id, book);
        self.next_book_id += 1;
        println!("✅ Book added successfully with ID: {}", self.next_book_id - 1);
    }

    fn remove_book(&mut self, book_id: u32) -> Result<(), String> {
        // Check if book exists and get its title before removal
        let book_title = match self.books.get(&book_id) {
            Some(book) => {
                match book.status {
                    BookStatus::Available => book.title.clone(),
                    _ => return Err("Cannot remove book that is currently borrowed".to_string())
                }
            }
            None => return Err("Book not found".to_string())
        };

        // Now remove the book
        self.books.remove(&book_id);
        println!("✅ Book '{}' removed successfully", book_title);
        Ok(())
    }

    fn search_books(&self, search_type: &str, term: &str) -> Vec<&Book> {
        let term_lower = term.to_lowercase();
        self.books.values().filter(|book| {
            match search_type {
                "title" => book.title.to_lowercase().contains(&term_lower),
                "author" => book.author.to_lowercase().contains(&term_lower),
                "isbn" => book.isbn.contains(&term_lower),
                _ => book.title.to_lowercase().contains(&term_lower) ||
                     book.author.to_lowercase().contains(&term_lower) ||
                     book.isbn.contains(&term_lower)
            }
        }).collect()
    }

    // ===== USER MANAGEMENT =====

    fn add_user(&mut self, name: String, email: String) {
        let user = User {
            id: self.next_user_id,
            name,
            email,
            borrowed_books: Vec::new(),
            max_books: 3, // Default limit
        };
        self.users.insert(self.next_user_id, user);
        self.next_user_id += 1;
        println!("✅ User added successfully with ID: {}", self.next_user_id - 1);
    }

    fn get_user(&self, user_id: u32) -> Option<&User> {
        self.users.get(&user_id)
    }

    // ===== TRANSACTION MANAGEMENT =====

    fn checkout_book(&mut self, book_id: u32, user_id: u32, days: u32) -> Result<(), String> {
        // Validate book exists and is available
        let book = self.books.get_mut(&book_id).ok_or("Book not found")?;
        match book.status {
            BookStatus::Available => {},
            _ => return Err("Book is not available".to_string())
        }

        // Validate user exists and has capacity
        let user = self.users.get(&user_id).ok_or("User not found")?;
        if user.borrowed_books.len() >= user.max_books as usize {
            return Err("User has reached maximum book limit".to_string());
        }

        // Create transaction
        let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
        let due_date = now + (days as u64 * 24 * 60 * 60); // days to seconds

        let transaction = Transaction {
            id: self.next_transaction_id,
            book_id,
            user_id,
            checkout_date: now,
            due_date,
            return_date: None,
            status: TransactionStatus::Active,
        };

        // Update book status
        book.status = BookStatus::Borrowed { user_id, due_date };

        // Update user borrowed books
        if let Some(user) = self.users.get_mut(&user_id) {
            user.borrowed_books.push(book_id);
        }

        // Store transaction
        self.transactions.insert(self.next_transaction_id, transaction);
        self.next_transaction_id += 1;

        println!("✅ Book checked out successfully!");
        println!("   Due date: {}", format_timestamp(due_date));

        Ok(())
    }

    fn return_book(&mut self, book_id: u32, user_id: u32) -> Result<(), String> {
        // Find active transaction
        let transaction = self.transactions.values_mut()
            .find(|t| t.book_id == book_id && t.user_id == user_id &&
                  matches!(t.status, TransactionStatus::Active))
            .ok_or("No active transaction found for this book and user")?;

        // Update transaction
        let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
        transaction.return_date = Some(now);
        transaction.status = TransactionStatus::Returned;

        // Update book status
        if let Some(book) = self.books.get_mut(&book_id) {
            book.status = BookStatus::Available;
        }

        // Update user borrowed books
        if let Some(user) = self.users.get_mut(&user_id) {
            user.borrowed_books.retain(|&id| id != book_id);
        }

        println!("✅ Book returned successfully!");
        Ok(())
    }

    // ===== REPORTS & ANALYTICS =====

    fn get_overdue_books(&self) -> Vec<&Book> {
        let now = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
        self.books.values().filter(|book| {
            matches!(book.status, BookStatus::Borrowed { .. } | BookStatus::Overdue { .. }) &&
            match book.status {
                BookStatus::Borrowed { due_date, .. } => due_date < now,
                BookStatus::Overdue { .. } => true,
                _ => false
            }
        }).collect()
    }

    fn generate_statistics(&self) {
        println!("📊 LIBRARY STATISTICS");
        println!("====================");
        println!("Total Books: {}", self.books.len());
        println!("Total Users: {}", self.users.len());
        println!("Active Transactions: {}",
                 self.transactions.values().filter(|t| matches!(t.status, TransactionStatus::Active)).count());

        let available_books = self.books.values().filter(|b| matches!(b.status, BookStatus::Available)).count();
        println!("Available Books: {}", available_books);
        println!("Borrowed Books: {}", self.books.len() - available_books);

        let overdue = self.get_overdue_books();
        println!("Overdue Books: {}", overdue.len());
    }

    // ===== DATA PERSISTENCE =====

    fn save_to_file(&self, filename: &str) -> Result<(), Box<dyn std::error::Error>> {
        let mut file = fs::File::create(filename)?;

        // Save metadata
        writeln!(file, "LIBRARY_DATA_V1")?;
        writeln!(file, "NEXT_IDS {} {} {}", self.next_book_id, self.next_user_id, self.next_transaction_id)?;

        // Save books
        writeln!(file, "BOOKS {}", self.books.len())?;
        for book in self.books.values() {
            let status_str = match &book.status {
                BookStatus::Available => "AVAILABLE".to_string(),
                BookStatus::Borrowed { user_id, due_date } => format!("BORROWED {} {}", user_id, due_date),
                BookStatus::Overdue { user_id, due_date } => format!("OVERDUE {} {}", user_id, due_date),
            };
            writeln!(file, "{}|{}|{}|{}|{}", book.id, book.title, book.author, book.isbn, status_str)?;
        }

        // Save users
        writeln!(file, "USERS {}", self.users.len())?;
        for user in self.users.values() {
            let books_str = user.borrowed_books.iter().map(|id| id.to_string()).collect::<Vec<_>>().join(",");
            writeln!(file, "{}|{}|{}|{}", user.id, user.name, user.email, books_str)?;
        }

        // Save transactions
        writeln!(file, "TRANSACTIONS {}", self.transactions.len())?;
        for transaction in self.transactions.values() {
            let return_date_str = transaction.return_date.map_or("NONE".to_string(), |d| d.to_string());
            let status_str = match transaction.status {
                TransactionStatus::Active => "ACTIVE",
                TransactionStatus::Returned => "RETURNED",
                TransactionStatus::Overdue => "OVERDUE",
            };
            writeln!(file, "{}|{}|{}|{}|{}|{}|{}",
                    transaction.id, transaction.book_id, transaction.user_id,
                    transaction.checkout_date, transaction.due_date, return_date_str, status_str)?;
        }

        Ok(())
    }

    fn load_from_file(&mut self, filename: &str) -> Result<(), Box<dyn std::error::Error>> {
        let content = fs::read_to_string(filename)?;
        let mut lines = content.lines();

        // Check version
        let version = lines.next().ok_or("Invalid file format")?;
        if version != "LIBRARY_DATA_V1" {
            return Err("Unsupported file version".into());
        }

        // Load metadata
        let next_ids_line = lines.next().ok_or("Missing metadata")?;
        let parts: Vec<&str> = next_ids_line.split_whitespace().collect();
        if parts.len() >= 4 && parts[0] == "NEXT_IDS" {
            self.next_book_id = parts[1].parse()?;
            self.next_user_id = parts[2].parse()?;
            self.next_transaction_id = parts[3].parse()?;
        }

        // Load books
        let books_header = lines.next().ok_or("Missing books section")?;
        let parts: Vec<&str> = books_header.split_whitespace().collect();
        if parts.len() >= 2 && parts[0] == "BOOKS" {
            let num_books: usize = parts[1].parse()?;
            for _ in 0..num_books {
                let line = lines.next().ok_or("Missing book data")?;
                let parts: Vec<&str> = line.split('|').collect();
                if parts.len() >= 5 {
                    let id: u32 = parts[0].parse()?;
                    let title = parts[1].to_string();
                    let author = parts[2].to_string();
                    let isbn = parts[3].to_string();

                    let status = if parts[4] == "AVAILABLE" {
                        BookStatus::Available
                    } else {
                        let status_parts: Vec<&str> = parts[4].split_whitespace().collect();
                        if status_parts.len() >= 3 {
                            let user_id: u32 = status_parts[1].parse()?;
                            let due_date: u64 = status_parts[2].parse()?;
                            if status_parts[0] == "BORROWED" {
                                BookStatus::Borrowed { user_id, due_date }
                            } else {
                                BookStatus::Overdue { user_id, due_date }
                            }
                        } else {
                            BookStatus::Available
                        }
                    };

                    let book = Book { id, title, author, isbn, status };
                    self.books.insert(id, book);
                }
            }
        }

        // Load users
        let users_header = lines.next().ok_or("Missing users section")?;
        let parts: Vec<&str> = users_header.split_whitespace().collect();
        if parts.len() >= 2 && parts[0] == "USERS" {
            let num_users: usize = parts[1].parse()?;
            for _ in 0..num_users {
                let line = lines.next().ok_or("Missing user data")?;
                let parts: Vec<&str> = line.split('|').collect();
                if parts.len() >= 4 {
                    let id: u32 = parts[0].parse()?;
                    let name = parts[1].to_string();
                    let email = parts[2].to_string();
                    let borrowed_books: Vec<u32> = if parts[3].is_empty() {
                        Vec::new()
                    } else {
                        parts[3].split(',').filter_map(|s| s.parse().ok()).collect()
                    };

                    let user = User {
                        id,
                        name,
                        email,
                        borrowed_books,
                        max_books: 3,
                    };
                    self.users.insert(id, user);
                }
            }
        }

        // Load transactions
        let transactions_header = lines.next().ok_or("Missing transactions section")?;
        let parts: Vec<&str> = transactions_header.split_whitespace().collect();
        if parts.len() >= 2 && parts[0] == "TRANSACTIONS" {
            let num_transactions: usize = parts[1].parse()?;
            for _ in 0..num_transactions {
                let line = lines.next().ok_or("Missing transaction data")?;
                let parts: Vec<&str> = line.split('|').collect();
                if parts.len() >= 7 {
                    let id: u32 = parts[0].parse()?;
                    let book_id: u32 = parts[1].parse()?;
                    let user_id: u32 = parts[2].parse()?;
                    let checkout_date: u64 = parts[3].parse()?;
                    let due_date: u64 = parts[4].parse()?;
                    let return_date = if parts[5] == "NONE" {
                        None
                    } else {
                        Some(parts[5].parse()?)
                    };
                    let status = match parts[6] {
                        "ACTIVE" => TransactionStatus::Active,
                        "RETURNED" => TransactionStatus::Returned,
                        "OVERDUE" => TransactionStatus::Overdue,
                        _ => TransactionStatus::Active,
                    };

                    let transaction = Transaction {
                        id, book_id, user_id, checkout_date, due_date, return_date, status
                    };
                    self.transactions.insert(id, transaction);
                }
            }
        }

        Ok(())
    }
}

fn format_timestamp(timestamp: u64) -> String {
    // Simple timestamp formatting (could be enhanced with chrono crate)
    format!("Timestamp: {}", timestamp)
}

fn main() {
    println!("🏛️  LIBRARY MANAGEMENT SYSTEM");
    println!("==============================\n");

    let mut library = Library::new();

    // Load existing data if available
    if let Err(e) = library.load_from_file("library_data.txt") {
        println!("No existing library data found ({}), starting fresh...", e);
    } else {
        println!("Library data loaded successfully!");
    }
    println!();

    // Main menu loop
    loop {
        display_main_menu();
        let choice = get_menu_choice(1, 5);

        match choice {
            1 => book_management_menu(&mut library),
            2 => user_management_menu(&mut library),
            3 => transaction_management_menu(&mut library),
            4 => reports_menu(&library),
            5 => {
                // Save and exit
                if let Err(e) = library.save_to_file("library_data.txt") {
                    println!("Warning: Could not save library data: {}", e);
                } else {
                    println!("✅ Library data saved successfully!");
                }
                println!("Thank you for using the Library Management System!");
                break;
            }
            _ => println!("Invalid choice. Please try again.")
        }
        println!();
    }
}

fn display_main_menu() {
    println!("Main Menu:");
    println!("1. Book Management");
    println!("2. User Management");
    println!("3. Transaction Management");
    println!("4. Reports & Analytics");
    println!("5. Save & Exit");
    print!("Enter choice (1-5): ");
    io::stdout().flush().unwrap();
}

fn book_management_menu(library: &mut Library) {
    loop {
        println!("📚 BOOK MANAGEMENT");
        println!("==================");
        println!("1. Add New Book");
        println!("2. Remove Book");
        println!("3. Search Books");
        println!("4. Display All Books");
        println!("5. Display Available Books");
        println!("6. Back to Main Menu");
        print!("Enter choice (1-6): ");
        io::stdout().flush().unwrap();

        let choice = get_menu_choice(1, 6);
        println!();

        match choice {
            1 => add_book_interactive(library),
            2 => remove_book_interactive(library),
            3 => search_books_interactive(library),
            4 => display_all_books(library),
            5 => display_available_books(library),
            6 => break,
            _ => println!("Invalid choice.")
        }
        println!();
    }
}

fn add_book_interactive(library: &mut Library) {
    println!("📖 ADD NEW BOOK");
    println!("===============");

    print!("Enter book title: ");
    io::stdout().flush().unwrap();
    let mut title = String::new();
    io::stdin().read_line(&mut title).unwrap();
    let title = title.trim().to_string();

    print!("Enter author name: ");
    io::stdout().flush().unwrap();
    let mut author = String::new();
    io::stdin().read_line(&mut author).unwrap();
    let author = author.trim().to_string();

    print!("Enter ISBN: ");
    io::stdout().flush().unwrap();
    let mut isbn = String::new();
    io::stdin().read_line(&mut isbn).unwrap();
    let isbn = isbn.trim().to_string();

    library.add_book(title, author, isbn);
}

fn remove_book_interactive(library: &mut Library) {
    println!("🗑️  REMOVE BOOK");
    println!("===============");

    print!("Enter book ID to remove: ");
    io::stdout().flush().unwrap();
    let book_id: u32 = match get_numeric_input() {
        Ok(id) => id,
        Err(_) => {
            println!("❌ Invalid book ID");
            return;
        }
    };

    match library.remove_book(book_id) {
        Ok(_) => {},
        Err(e) => println!("❌ Error: {}", e)
    }
}

fn search_books_interactive(library: &Library) {
    println!("🔍 SEARCH BOOKS");
    println!("===============");
    println!("Search by:");
    println!("1. Title");
    println!("2. Author");
    println!("3. ISBN");
    println!("4. All fields");
    print!("Enter choice (1-4): ");
    io::stdout().flush().unwrap();

    let search_type_choice = get_menu_choice(1, 4);
    let search_type = match search_type_choice {
        1 => "title",
        2 => "author",
        3 => "isbn",
        4 => "all",
        _ => "all"
    };

    print!("Enter search term: ");
    io::stdout().flush().unwrap();
    let mut term = String::new();
    io::stdin().read_line(&mut term).unwrap();
    let term = term.trim();

    let results = library.search_books(search_type, term);

    println!("\nSearch Results:");
    println!("---------------");
    if results.is_empty() {
        println!("No books found matching '{}'", term);
    } else {
        for book in &results {
            display_book(book);
            println!();
        }
        println!("Found {} book(s) matching \"{}\"", results.len(), term);
    }
}

fn display_all_books(library: &Library) {
    println!("📚 ALL BOOKS");
    println!("============");
    if library.books.is_empty() {
        println!("No books in the library.");
    } else {
        for book in library.books.values() {
            display_book(book);
            println!();
        }
    }
}

fn display_available_books(library: &Library) {
    println!("📚 AVAILABLE BOOKS");
    println!("==================");
    let available: Vec<&Book> = library.books.values()
        .filter(|b| matches!(b.status, BookStatus::Available))
        .collect();

    if available.is_empty() {
        println!("No books currently available.");
    } else {
        for book in available {
            display_book(book);
            println!();
        }
    }
}

fn display_book(book: &Book) {
    println!("Title: {}", book.title);
    println!("Author: {}", book.author);
    println!("ISBN: {}", book.isbn);
    print!("Status: ");
    match &book.status {
        BookStatus::Available => println!("Available"),
        BookStatus::Borrowed { user_id, due_date } => {
            println!("Borrowed by user {} (Due: {})", user_id, format_timestamp(*due_date));
        }
        BookStatus::Overdue { user_id, due_date } => {
            println!("Overdue - borrowed by user {} (Was due: {})", user_id, format_timestamp(*due_date));
        }
    }
}

fn user_management_menu(library: &mut Library) {
    loop {
        println!("👥 USER MANAGEMENT");
        println!("==================");
        println!("1. Add New User");
        println!("2. View User Information");
        println!("3. Display All Users");
        println!("4. Back to Main Menu");
        print!("Enter choice (1-4): ");
        io::stdout().flush().unwrap();

        let choice = get_menu_choice(1, 4);
        println!();

        match choice {
            1 => add_user_interactive(library),
            2 => view_user_interactive(library),
            3 => display_all_users(library),
            4 => break,
            _ => println!("Invalid choice.")
        }
        println!();
    }
}

fn add_user_interactive(library: &mut Library) {
    println!("👤 ADD NEW USER");
    println!("===============");

    print!("Enter user name: ");
    io::stdout().flush().unwrap();
    let mut name = String::new();
    io::stdin().read_line(&mut name).unwrap();
    let name = name.trim().to_string();

    print!("Enter email address: ");
    io::stdout().flush().unwrap();
    let mut email = String::new();
    io::stdin().read_line(&mut email).unwrap();
    let email = email.trim().to_string();

    library.add_user(name, email);
}

fn view_user_interactive(library: &Library) {
    println!("👤 VIEW USER INFORMATION");
    println!("========================");

    print!("Enter user ID: ");
    io::stdout().flush().unwrap();
    let user_id: u32 = match get_numeric_input() {
        Ok(id) => id,
        Err(_) => {
            println!("❌ Invalid user ID");
            return;
        }
    };

    if let Some(user) = library.get_user(user_id) {
        println!("User ID: {}", user.id);
        println!("Name: {}", user.name);
        println!("Email: {}", user.email);
        println!("Max Books: {}", user.max_books);
        println!("Currently Borrowed: {} books", user.borrowed_books.len());
        if !user.borrowed_books.is_empty() {
            println!("Borrowed Book IDs: {:?}", user.borrowed_books);
        }
    } else {
        println!("❌ User not found");
    }
}

fn display_all_users(library: &Library) {
    println!("👥 ALL USERS");
    println!("============");
    if library.users.is_empty() {
        println!("No users registered.");
    } else {
        for user in library.users.values() {
            println!("ID: {}, Name: {}, Email: {}, Borrowed: {} books",
                    user.id, user.name, user.email, user.borrowed_books.len());
        }
    }
}

fn transaction_management_menu(library: &mut Library) {
    loop {
        println!("🔄 TRANSACTION MANAGEMENT");
        println!("=========================");
        println!("1. Checkout Book");
        println!("2. Return Book");
        println!("3. View Active Transactions");
        println!("4. Back to Main Menu");
        print!("Enter choice (1-4): ");
        io::stdout().flush().unwrap();

        let choice = get_menu_choice(1, 4);
        println!();

        match choice {
            1 => checkout_book_interactive(library),
            2 => return_book_interactive(library),
            3 => view_active_transactions(library),
            4 => break,
            _ => println!("Invalid choice.")
        }
        println!();
    }
}

fn checkout_book_interactive(library: &mut Library) {
    println!("📖 CHECKOUT BOOK");
    println!("=================");

    print!("Enter book ID: ");
    io::stdout().flush().unwrap();
    let book_id: u32 = match get_numeric_input() {
        Ok(id) => id,
        Err(_) => {
            println!("❌ Invalid book ID");
            return;
        }
    };

    print!("Enter user ID: ");
    io::stdout().flush().unwrap();
    let user_id: u32 = match get_numeric_input() {
        Ok(id) => id,
        Err(_) => {
            println!("❌ Invalid user ID");
            return;
        }
    };

    print!("Enter loan period in days: ");
    io::stdout().flush().unwrap();
    let days: u32 = match get_numeric_input() {
        Ok(d) => d,
        Err(_) => {
            println!("❌ Invalid number of days");
            return;
        }
    };

    match library.checkout_book(book_id, user_id, days) {
        Ok(_) => {},
        Err(e) => println!("❌ Error: {}", e)
    }
}

fn return_book_interactive(library: &mut Library) {
    println!("📚 RETURN BOOK");
    println!("==============");

    print!("Enter book ID: ");
    io::stdout().flush().unwrap();
    let book_id: u32 = match get_numeric_input() {
        Ok(id) => id,
        Err(_) => {
            println!("❌ Invalid book ID");
            return;
        }
    };

    print!("Enter user ID: ");
    io::stdout().flush().unwrap();
    let user_id: u32 = match get_numeric_input() {
        Ok(id) => id,
        Err(_) => {
            println!("❌ Invalid user ID");
            return;
        }
    };

    match library.return_book(book_id, user_id) {
        Ok(_) => {},
        Err(e) => println!("❌ Error: {}", e)
    }
}

fn view_active_transactions(library: &Library) {
    println!("🔄 ACTIVE TRANSACTIONS");
    println!("======================");

    let active: Vec<&Transaction> = library.transactions.values()
        .filter(|t| matches!(t.status, TransactionStatus::Active))
        .collect();

    if active.is_empty() {
        println!("No active transactions.");
    } else {
        for transaction in active {
            println!("Transaction ID: {}", transaction.id);
            println!("Book ID: {}, User ID: {}", transaction.book_id, transaction.user_id);
            println!("Checkout: {}, Due: {}",
                    format_timestamp(transaction.checkout_date),
                    format_timestamp(transaction.due_date));
            println!();
        }
    }
}

fn reports_menu(library: &Library) {
    loop {
        println!("📊 REPORTS & ANALYTICS");
        println!("=======================");
        println!("1. Library Statistics");
        println!("2. Overdue Books");
        println!("3. Popular Books");
        println!("4. Back to Main Menu");
        print!("Enter choice (1-4): ");
        io::stdout().flush().unwrap();

        let choice = get_menu_choice(1, 4);
        println!();

        match choice {
            1 => library.generate_statistics(),
            2 => display_overdue_books(library),
            3 => display_popular_books(library),
            4 => break,
            _ => println!("Invalid choice.")
        }
        println!();
    }
}

fn display_overdue_books(library: &Library) {
    println!("⚠️  OVERDUE BOOKS");
    println!("=================");
    let overdue = library.get_overdue_books();

    if overdue.is_empty() {
        println!("No overdue books! 🎉");
    } else {
        for book in &overdue {
            display_book(book);
            println!("---");
        }
        println!("Total overdue: {} books", overdue.len());
    }
}

fn display_popular_books(library: &Library) {
    println!("📈 POPULAR BOOKS");
    println!("=================");
    // Simple popularity based on transaction count
    let mut book_transactions = HashMap::new();

    for transaction in library.transactions.values() {
        *book_transactions.entry(transaction.book_id).or_insert(0) += 1;
    }

    let mut popular: Vec<(u32, u32)> = book_transactions.into_iter().collect();
    popular.sort_by(|a, b| b.1.cmp(&a.1));

    if popular.is_empty() {
        println!("No transaction data available.");
    } else {
        for (book_id, count) in popular.iter().take(5) {
            if let Some(book) = library.books.get(book_id) {
                println!("'{}' by {} - {} transactions", book.title, book.author, count);
            }
        }
    }
}

fn get_menu_choice(min: u32, max: u32) -> u32 {
    loop {
        let input = get_numeric_input();
        match input {
            Ok(choice) if choice >= min && choice <= max => return choice,
            Ok(_) => {
                print!("Please enter a number between {} and {}: ", min, max);
                io::stdout().flush().unwrap();
            }
            Err(_) => {
                print!("Please enter a valid number: ");
                io::stdout().flush().unwrap();
            }
        }
    }
}

fn get_numeric_input() -> Result<u32, std::num::ParseIntError> {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    input.trim().parse::<u32>()
}