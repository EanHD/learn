# R Workspace Instructions

## Getting Started with R

Welcome to data science with R! This guide covers setup and basic execution.

---

## Installation

**Linux (Ubuntu/Debian):**
```bash
sudo apt install r-base
```

**macOS:**
```bash
brew install r
```

**Windows:**
Download from [CRAN](https://cran.r-project.org/)

### Verify Installation

```bash
R --version
```

---

## Running R Code

**Method 1 (Vim):** `<Space>r`

**Method 2 (Terminal):**
```bash
Rscript main.R
```

---

## Your First Program

Create `main.R`:

```r
print("Hello, R!")
```

Run it:

```bash
Rscript main.R
```

---

## R Basics

### Variables

```r
name <- "Alice"    # String
age <- 25          # Integer
height <- 5.7      # Numeric
```

### Vectors

```r
numbers <- c(1, 2, 3, 4, 5)
names <- c("Alice", "Bob", "Charlie")
```

### Functions

```r
print("Hello")
length(c(1, 2, 3))
sum(c(1, 2, 3))
```

---

## Resources

- [R Documentation](https://www.r-project.org/)
- [RStudio IDE](https://posit.co/download/rstudio-desktop/)
- [R for Data Science](https://r4ds.had.co.nz/)

Happy analyzing!
