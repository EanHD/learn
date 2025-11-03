# Level 1: Hello World

## Stage 1: Copying Code

### Today's Mission

Welcome to Kotlin! Today, you'll create your first Kotlin program. Kotlin is a modern, concise language that runs on the JVM and is the official language for Android development.

### Learning Goals

- Understand Kotlin program structure
- Learn how to compile and run Kotlin
- Create your first output
- Get comfortable with Kotlin syntax

### Your Task

Copy the following code EXACTLY as shown into a new file called `hello.kt`:

```kotlin
fun main() {
    println("Hello, World!")
}
```

### How to Execute

```bash
kotlinc hello.kt -include-runtime -d hello.jar
java -jar hello.jar
```

Expected output:

```
Hello, World!
```

### Success Checklist

- [ ] Created a file named `hello.kt`
- [ ] Copied the code exactly as shown
- [ ] Program compiled without errors
- [ ] Saw "Hello, World!" printed

---

**Kotlin interoperates seamlessly with Java and is fully interoperable with existing JVM code!**
