# Julia Workspace Instructions

## Getting Started with Julia

Welcome to high-performance computing with Julia!

---

## Installation

**Linux/macOS:**
Download from [julialang.org](https://julialang.org/downloads/)

**macOS (Homebrew):**
```bash
brew install julia
```

### Verify Installation

```bash
julia --version
```

---

## Running Julia Code

**Method 1 (Vim):** `<Space>r`

**Method 2 (Terminal):**
```bash
julia main.jl
```

---

## Your First Program

Create `main.jl`:

```julia
println("Hello, Julia!")
```

Run it:

```bash
julia main.jl
```

---

## Julia Basics

### Variables

```julia
name = "Alice"     # String
age = 25           # Integer
height = 5.7       # Float
```

### Arrays

```julia
numbers = [1, 2, 3, 4, 5]
matrix = [1 2; 3 4]
```

### Functions

```julia
println("Hello")
length([1, 2, 3])
sum([1, 2, 3])
```

---

## Resources

- [Julia Documentation](https://docs.julialang.org/)
- [Pluto.jl Notebooks](https://plutojl.org/)
- [JuliaHub](https://juliahub.com/)

Let's compute!
