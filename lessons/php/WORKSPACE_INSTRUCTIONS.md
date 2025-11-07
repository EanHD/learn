# PHP Workspace Instructions

## Getting Started with PHP

Welcome to PHP programming! This section explains how to set up your workspace and get ready to code.

---

## Prerequisites

### 1. Install PHP

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install php php-cli
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install php php-cli
```

**macOS:**
```bash
brew install php
```

**Windows:**
- Download from [php.net](https://windows.php.net/)
- Or use: `winget install PHP.PHP`

### 2. Verify Installation

```bash
php --version
```

Should return PHP version information.

---

## Compilation and Execution

### Method 1: Vim Shortcut (Recommended)

When editing `main.php` in Vim:

```
<Space>r   → Run the PHP script
<Space>h   → Show help for current language
```

### Method 2: Terminal Commands

```bash
php main.php
```

---

## Your First Program

Create this in `main.php`:

```php
<?php
echo "Hello, PHP!";
?>
```

Then run:

```bash
php main.php
```

Expected output:
```
Hello, PHP!
```

---

## Important Notes

### PHP Opening/Closing Tags

Always start PHP code with `<?php` and end with `?>`:

```php
<?php
// Your code here
echo "Hello!";
?>
```

### Semicolons Required

Each statement must end with `;`:

```php
<?php
echo "Hello";  // Correct
echo "World"   // Wrong - missing semicolon
?>
```

### Common Gotchas

1. **No opening tag** - Code won't execute
2. **Missing semicolons** - Parse errors
3. **String quotes** - Use single `'` or double `"` consistently
4. **Case sensitivity** - `echo` ≠ `ECHO` (keywords are case-insensitive but variables are not)

---

## PHP Basics

### Variables

```php
<?php
$name = "Alice";     // String variable
$age = 25;           // Integer variable
$height = 5.7;       // Float variable
?>
```

### Printing Output

```php
<?php
echo "Hello, World!";      // Print text
echo $name;                // Print variable
echo "Age: " . $age;       // Concatenate with .
?>
```

### Data Types

- `string` - Text ("Hello")
- `int` - Whole numbers (42)
- `float` - Decimal numbers (3.14)
- `bool` - True/False
- `array` - Lists of values
- `object` - Objects

---

## Best Practices

### 1. File Structure

- Always name your main file `main.php`
- Use descriptive variable names
- Follow PSR-2 coding standards

### 2. Code Style

- Indentation: 4 spaces (configured automatically)
- Use meaningful variable names
- Add comments explaining logic

### 3. Error Handling

- Watch for parse errors (syntax mistakes)
- Use `echo` to debug values
- Check for typos in variable names

---

## Useful PHP Functions

```php
<?php
// String functions
strlen($string);           // Length of string
strtoupper($string);       // Convert to uppercase
str_replace($find, $replace, $string);

// Array functions
count($array);             // Count elements
array_push($array, $item); // Add to array
array_pop($array);         // Remove last element

// Type checking
is_string($var);
is_int($var);
is_array($var);
gettype($var);             // Get variable type
?>
```

---

## Common Setup Issues

### Issue: "php: command not found"

**Solution:** PHP isn't installed or not in PATH.

```bash
# Check PHP location
which php

# If empty, install PHP (see Prerequisites)
```

### Issue: "Parse error: syntax error"

**Solution:** Check for missing semicolons or unclosed braces.

```php
<?php
echo "Test"   // Wrong - missing ;
echo "Test";  // Correct
?>
```

### Issue: Variable undefined

**Solution:** Check spelling matches declaration.

```php
<?php
$name = "Alice";
echo $nam;  // Wrong - typo
echo $name; // Correct
?>
```

---

## Next Steps

1. ✅ Install PHP and verify with `php --version`
2. ✅ Open your first lesson: `learn open php 1 1`
3. ✅ Copy the code from the lesson into `main.php`
4. ✅ Press `<Space>r` to run it
5. ✅ See your program work!

---

## Resources

- [PHP Official Documentation](https://www.php.net/docs.php)
- [PHP: The Right Way](https://phptherightway.com/)
- [Laravel (Popular PHP Framework)](https://laravel.com/)

---

Happy coding! PHP powers the web - let's get started!
