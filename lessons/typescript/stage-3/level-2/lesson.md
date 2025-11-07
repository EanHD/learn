# Level 2: Data Structure Planning

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window**. The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 3: Problem to Pseudocode

### Today's Mission

Time to think like a programmer! You'll analyze real problems and design solutions using pseudocode before writing any code. This is the most important skill in programming.

**The Process:**
1. Read and understand the problem requirements
2. Break the problem into smaller sub-problems
3. Design an algorithm in pseudocode
4. Identify edge cases and constraints
5. Implement the solution in Typescript

---

### Learning Goals

- Develop problem analysis skills
- Learn to design algorithms before coding
- Practice breaking complex problems into steps
- Master pseudocode notation and planning
- Understand edge cases and constraints

---

### Your Task

**Problem Statement:**

Data Structure Planning - Design an algorithm to solve this problem, then implement it.

**Your Process:**
1. **Understand**: Read the problem 3 times
2. **Plan**: Write pseudocode outlining your approach
3. **Code**: Implement your design in Typescript
4. **Test**: Verify with multiple test cases
5. **Refine**: Optimize and improve

**Deliverables:**
- Written pseudocode (comments in your code)
- Working Typescript implementation
- Test cases showing it works

---


### How to Run

1. **Run the code**:
   ```bash
   ts-node hello.ts
   ```type

**Expected output:**
```type
Hello, World!
```type

### How to Approach This

**Step 1: Understand**
- Read all requirements carefully
- Identify inputs, outputs, and constraints
- Ask yourself: "What is the core problem?"

**Step 2: Plan**
- Sketch out your approach on paper
- List the steps needed
- Identify potential challenges

**Step 3: Implement**
- Start with a basic version
- Add features incrementally
- Test after each addition

**Step 4: Test**
- Try normal cases
- Try edge cases (empty, max, min)
- Try invalid inputs
- Verify all requirements met

**Step 5: Refine**
- Review your code
- Add comments
- Optimize if needed
- Ensure it's readable

---

### Success Checklist

- [ ] Understood the problem/requirements completely
- [ ] Designed a solution approach
- [ ] Wrote pseudocode or algorithm design
- [ ] Implemented in Typescript correctly
- [ ] Tested with multiple scenarios
- [ ] Code is clean and well-commented
- [ ] All requirements met
- [ ] Program runs without errors

---

### Key Concepts

**Problem Decomposition:**
- Break big problems into smaller ones
- Solve each part individually
- Combine solutions together
- Always start simple, then expand

**Algorithm Design:**
- Clear input/output definition
- Step-by-step logic
- Consider edge cases
- Plan before coding

---

### Try This (Optional Challenges)

1. Extend the solution with additional features
2. Handle more edge cases
3. Optimize for performance
4. Add a user interface
5. Write unit tests

---

### Helpful Resources

- Review previous lessons for syntax help
- Check WORKSPACE_INSTRUCTIONS.md for setup
- Use `<Space>h` in Vim for keyboard shortcuts
- Test frequently to catch errors early

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study after attempting!)

### Solution Approach

**Problem-Solving Framework:**

1. **Input Analysis**: What data do we receive?
2. **Output Requirements**: What should we produce?
3. **Process Design**: How do we transform input to output?
4. **Edge Cases**: What could go wrong?

**Pseudocode Template:**
```typescript
ALGORITHM: [Name]
INPUT: [What we need]
OUTPUT: [What we produce]

BEGIN
    1. Initialize variables
    2. Get input from user
    3. Process the data
        - Step 1
        - Step 2
        - Step 3
    4. Display results
END
```type

Then translate this directly to Typescript code.

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Logic error | Algorithm design flaw | Review pseudocode, trace by hand |
| Syntax error | Language rules violated | Check language documentation |
| Runtime error | Invalid operation | Add validation, handle edge cases |
| Wrong output | Misunderstanding requirements | Re-read problem carefully |

### Next Steps

1. Review your solution critically
2. Compare with best practices
3. Optimize if needed
4. Move to next level when ready
5. Keep practicing!

---

**Excellent work on this advanced challenge!**

*Continue building your skills - you're doing great!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```ts
console.log("Hello, World!");

```ts

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard typescript conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
