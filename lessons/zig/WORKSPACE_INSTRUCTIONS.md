# Zig Workspace Instructions

## Getting Started with Zig

Welcome to systems programming with Zig!

---

## Installation

**Linux:**
Download from [ziglang.org](https://ziglang.org/download/)
```bash
tar xf zig-linux-*.tar.xz
export PATH=$PATH:/path/to/zig
```

**macOS:**
```bash
brew install zig
```

**Windows:**
Download installer from [ziglang.org](https://ziglang.org/download/)

### Verify Installation

```bash
zig version
```

---

## Compiling and Running

**Method 1 (Vim):** `<Space>r`

**Method 2 (Terminal):**
```bash
zig build-exe main.zig
./main
```

---

## Your First Program

Create `main.zig`:

```zig
const std = @import("std");

pub fn main() void {
    std.debug.print("Hello, Zig!\n", .{});
}
```

Run it:

```bash
zig build-exe main.zig
./main
```

---

## Zig Basics

### Variables

```zig
const name = "Alice";     // Constant
var age: i32 = 25;        // Signed 32-bit integer
var height: f64 = 5.7;    // 64-bit float
```

### Functions

```zig
fn add(a: i32, b: i32) i32 {
    return a + b;
}
```

### Print

```zig
std.debug.print("Hello!\n", .{});
```

---

## Resources

- [Zig Documentation](https://ziglang.org/documentation/master/)
- [Ziglearn](https://ziglearn.org/)

Build fast!
