# Level 1: Your First Independent Project

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 5: Capstone - Full Integration Project

### Today's Mission

**Welcome to Stage 5!** 

You've completed Stages 1-4 and learned to:
- Copy and understand code (Stage 1)
- Translate pseudocode to programs (Stage 2)
- Analyze problems and design solutions (Stage 3)
- Create problems and implement solutions independently (Stage 4)

**Now it's time for your CAPSTONE PROJECT!**

This is where you create something **meaningful, ambitious, and uniquely yours**. You'll take everything you've learned and build a complete, professional-quality application that solves a real problem or creates real value.

---

### Learning Goals

By completing this capstone level, you will:
- **Design** a complete application from scratch
- **Plan** a multi-feature system with proper architecture
- **Implement** production-ready code in Rust
- **Test** thoroughly with edge cases
- **Document** your work professionally
- **Reflect** on your programming journey
- Create a **portfolio-worthy project**

---

### Capstone Project Scope

Your Level 1 Capstone should:

**Complexity**: Moderate (3-5 main features) 
**Code Size**: 500-1500 lines (depending on scope) 
**Time Estimate**: 10-15 hours of focused work 
**Purpose**: Demonstrate mastery of Core Programming Concepts & Rust Principles

---

### Your Challenge

**Design and implement a complete application of your choice!**

Here are guiding questions to help you choose:

#### Personal Interest
- What problems do YOU want to solve?
- What could you build that would be genuinely useful?
- What excites you to code?

#### Example Domains (Pick ONE or Choose Your Own)

**1. Personal Data Management**
- Student grade tracker with analytics
- Personal finance manager with budgeting
- Employee time tracking system
- Book/movie collection manager with searching and sorting
- Recipe collection with meal planning

**2. Educational Tool**
- Quiz system with scoring and feedback
- Math problem generator and solver
- Language learning flashcard system with statistics
- Programming concept visualizer

**3. Productivity Tool**
- Task management system with priorities and deadlines
- Meeting scheduler with conflict detection
- Note-taking application with organization
- Habit tracker with progress visualization

**4. Data Analysis**
- CSV data processor with filtering and reporting
- Survey analyzer with statistics
- Log file analyzer with anomaly detection
- Sales data analyzer with trend analysis

**5. Game or Simulation**
- Text-based adventure game with inventory
- Number guessing game with AI difficulty
- Simple maze game with pathfinding
- Simulation (traffic, weather, population growth)

---

### Project Requirements

Your capstone MUST have:

#### **Functional Requirements**
- [ ] **Data Persistence**: Save and load data from files (JSON, CSV, or binary)
- [ ] **User Interface**: Menu-driven or interactive command-line interface
- [ ] **Core Features**: At least 3-5 meaningful operations
- [ ] **Search/Filter**: Ability to find and manipulate specific data
- [ ] **Error Handling**: Graceful handling of invalid inputs and edge cases
- [ ] **Reporting**: Display meaningful output (statistics, summaries, etc.)

#### **Code Quality Requirements**
- [ ] **Rust Idioms**: Uses Rust patterns effectively (ownership, Result types, etc.)
- [ ] **Error Handling**: Uses Result types for recoverable errors
- [ ] **Modularity**: Organized into modules and functions with clear purposes
- [ ] **Documentation**: Doc comments explaining complex logic
- [ ] **Validation**: Input validation at all user entry points
- [ ] **Efficiency**: Reasonable performance for typical use cases
- [ ] **Style**: Consistent with Rust conventions (via `rustfmt`)

#### **Testing Requirements**
- [ ] **Happy Path**: Test normal, expected usage
- [ ] **Edge Cases**: Test boundary conditions
- [ ] **Error Cases**: Test invalid inputs
- [ ] **Data Persistence**: Verify save/load functionality
- [ ] **Unit Tests**: Written using Rust's testing framework
- [ ] **Test Documentation**: Record test cases and results

---

### Development Process

Follow these stages:

#### **Phase 1: Planning (2-3 hours)**
1. Write a detailed **project proposal** (what, why, how)
2. Define **core features** (what MUST work)
3. Design **data structures** (what data do you need)
4. Create **architecture diagram** (how do components interact)
5. Write **pseudocode** for main functions

#### **Phase 2: Implementation (8-10 hours)**
1. Set up **project structure** with `cargo` (files, folders, organization)
2. Implement **core features** one at a time
3. Build **user interface** for interactions
4. Add **file I/O** for data persistence
5. Implement **search/filtering/reporting**
6. Add **unit tests** for core functionality

#### **Phase 3: Testing & Refinement (2-3 hours)**
1. Test **normal cases** (expected usage)
2. Test **edge cases** (boundaries, limits)
3. Test **error cases** (invalid inputs)
4. Fix **bugs** found during testing
5. Optimize **performance** if needed
6. Run **`cargo clippy`** to check code quality

#### **Phase 4: Documentation (1-2 hours)**
1. Write **README.md** explaining the project
2. Add **doc comments** for public items
3. Create **usage guide** showing how to use
4. Document **design decisions** and trade-offs
5. Record **test results** and validation

---

### Success Criteria

Your capstone will be evaluated on:

#### **Functionality** (40 points)
- All required features work correctly
- Data persists between sessions
- User interface is intuitive
- Error handling is graceful

#### **Code Quality** (30 points)
- Code is well-organized and modular
- Functions have clear purposes
- Follows Rust idioms and conventions
- Doc comments explain public API
- No compiler warnings or clippy issues

#### **Completeness** (20 points)
- Project is fully implemented (not partial)
- Testing is documented
- Documentation is thorough
- Handles edge cases

#### **Creativity** (10 points)
- Project solves a real problem
- Implementation shows thought and care
- Features are well-integrated
- Goes beyond minimum requirements

---

### Project Proposal Template

Before coding, submit a proposal addressing:

```rust
PROJECT TITLE: [Name]
DOMAIN: [Category - e.g., Personal Finance, Education]
PURPOSE: [What problem does it solve?]

CORE FEATURES:
1. [Feature 1 description]
2. [Feature 2 description]
3. [Feature 3 description]

DATA STRUCTURES:
- Struct 1: [What data does it hold?]
- Struct 2: [What data does it hold?]

MAIN OPERATIONS:
1. [What can users do?]
2. [What can users do?]
3. [What can users do?]

PERSISTENCE:
- [How will data be saved?]
- [How will data be loaded?]

USER INTERFACE:
- [How will users interact?]
- [What menus or prompts?]

ESTIMATED EFFORT: [X hours of work]
```rust

---

### Getting Started

**Step 1: Choose Your Project**
Pick something you're genuinely interested in building.

**Step 2: Write Your Proposal**
Use the template above to plan your approach.

**Step 3: Design Your Architecture**
Sketch out data structures and main functions.

**Step 4: Write Pseudocode**
Plan the logic before implementing.

**Step 5: Create Cargo Project**
```bash
cargo new my_capstone
cd my_capstone
```rust

**Step 6: Start Coding**
Implement one feature at a time, testing as you go.

**Step 7: Test Thoroughly**
Try to break your program - fix issues found.

**Step 8: Document**
Write a comprehensive README and code comments.

**Step 9: Reflect**
Think about what you learned and what you'd do differently.

---

### Success Checklist

- [ ] I've chosen a project that interests me
- [ ] I've written a detailed proposal
- [ ] I've designed my data structures
- [ ] I've created pseudocode for main functions
- [ ] I've implemented all core features
- [ ] I've added file I/O for persistence
- [ ] I've written unit tests
- [ ] I've tested normal, edge, and error cases
- [ ] I've written comprehensive documentation
- [ ] I've included meaningful doc comments
- [ ] My code compiles without warnings
- [ ] `cargo clippy` shows no issues
- [ ] My program handles invalid inputs gracefully
- [ ] I can demonstrate the complete workflow
- [ ] I've reflected on what I learned

---

### Enhancement Ideas

Once your core capstone is complete, consider these extensions:

**Advanced Features:**
- [ ] Sorting and complex filtering
- [ ] Data analysis and statistics
- [ ] Configuration files for customization
- [ ] Export to multiple formats (JSON, CSV, XML)
- [ ] Search with pattern matching
- [ ] Undo/redo functionality

**Professional Touches:**
- [ ] Command-line argument parsing (`clap` crate)
- [ ] Configuration files
- [ ] Logging system (`log` and `env_logger` crates)
- [ ] Performance metrics
- [ ] Data validation with `serde`

**Integration:**
- [ ] Async operations (`tokio` crate)
- [ ] Network communication (if applicable)
- [ ] Database integration (if applicable)
- [ ] Web API design (if applicable)

---

### Reference Materials

**Concepts You'll Need:**

From **Stage 1**: Syntax, operators, basic I/O 
From **Stage 2**: Loops, conditionals, algorithms 
From **Stage 3**: Functions, modularity, code organization 
From **Stage 4**: File I/O, data structures, system design 

**Rust-Specific Concepts:**
- Ownership and borrowing
- Pattern matching
- Result and Option types
- Trait design
- Module organization

---

### Getting Help

**When stuck:**
1. Review related Stage 1-4 lessons
2. Check your pseudocode - is the logic sound?
3. Consult the Rust documentation or `rustlings`
4. Add debugging output to understand flow
5. Test smaller pieces in isolation
6. Ask for code review from peers

**Common Challenges:**
- **"Ownership issues?"** → Review Stage 1-3 materials
- **"Data structure confusing?"** → Draw it on paper first
- **"Result type handling?"** → Use `?` operator and pattern matching
- **"Performance issues?"** → Profile with `cargo flamegraph` if available

---

### Capstone Best Practices

 **DO:**
- Start with clear planning
- Write pseudocode first
- Implement incrementally
- Test frequently
- Document as you go
- Commit to version control
- Get peer feedback
- Refactor when needed

 **DON'T:**
- Write 1000 lines before testing
- Skip the planning phase
- Ignore edge cases
- Over-engineer early
- Assume your code is obvious
- Skip error handling
- Forget to test thoroughly
- Ignore compiler warnings

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to Rust
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**


---

## CAPSTONE PLANNING GUIDE

### Phase 1: Project Selection

**Questions to Ask Yourself:**

1. **Interest**: What am I genuinely interested in?
 - Build something YOU want to exist
 - Solving a real (even small) problem is more motivating than abstract exercises

2. **Scope**: Can I complete this in 10-15 hours?
 - Too simple = not enough challenge
 - Too complex = frustration and abandonment
 - Aim for "ambitious but achievable"

3. **Learning**: What will I learn from this?
 - File I/O - required
 - Complex data structures - yes
 - Algorithms - yes
 - System design - yes
 - Rust idioms and patterns - yes

4. **Uniqueness**: Can I make it mine?
 - Your project should reflect YOUR interests
 - Don't just copy the Stage 4 examples
 - Add YOUR twist to make it unique

### Phase 2: Project Planning

**Essential Planning Steps:**

1. **Write a Problem Statement**
```rust
 "My application solves [problem]
 by [approach]
 for [users]
 so that [outcome]."
 ```rust

2. **Define Core Features** (3-5 minimum)
```rust
 MUST HAVE (critical):
 - Feature A
 - Feature B
 
 SHOULD HAVE (important):
 - Feature C
 - Feature D
 
 NICE TO HAVE (bonus):
 - Feature E
 ```rust

3. **Design Data Structures**
 ```rust
 #[derive(Clone, Debug, Serialize, Deserialize)]
 pub struct Person {
 pub id: usize,
 pub name: String,
 // ... other fields
 }
 
 pub struct Company {
 pub employees: Vec<Person>,
 pub name: String,
 // ... other fields
 }
 ```rust

4. **Create Architecture Diagram**
```rust
 USER INPUT
 ↓
 MENU SYSTEM
 ↓
 BUSINESS LOGIC (functions)
 ↓
 DATA STORAGE (structs)
 ↓
 FILE I/O (persistence)
 ```rust

5. **Write Pseudocode for Main Functions**
```rust
 Function: add_new_record(collection)
 1. Get input from user
 2. Validate input (return error if invalid)
 3. Create new record
 4. Add to collection
 5. Save to file
 6. Return success
 
 Function: search_records(collection, criteria)
 1. Filter collection by criteria
 2. Return matching records
 3. Handle no matches case
 ```rust

### Phase 3: Data Structure Design

**Key Questions:**

1. **What data do I need to track?**
 - Customer name, email, phone, purchase history
 - Product name, price, inventory, category
 - Etc.

2. **How should data be organized?**
 - Single entity struct? Multiple structs?
 - Vectors or custom collections?
 - When should I use owned vs. borrowed data?

3. **What operations are needed?**
 - Add, view, edit, delete
 - Search, sort, filter
 - Report generation

**Design Pattern:**

```rust
use serde::{Serialize, Deserialize};
use std::error::Error;

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct Entity {
 pub id: usize,
 pub name: String,
 // ... domain-specific fields
}

pub struct EntityManager {
 pub entities: Vec<Entity>,
 pub filename: String,
}

impl EntityManager {
 pub fn new(filename: &str) -> Self {
 EntityManager {
 entities: Vec::new(),
 filename: filename.to_string(),
 }
 }
 
 pub fn add(&mut self, entity: Entity) -> Result<(), Box<dyn Error>> {
 // Validation
 self.entities.push(entity);
 self.save()?;
 Ok(())
 }
 
 pub fn save(&self) -> Result<(), Box<dyn Error>> {
 // Serialization
 Ok(())
 }
 
 pub fn load(&mut self) -> Result<(), Box<dyn Error>> {
 // Deserialization
 Ok(())
 }
 
 pub fn search(&self, criteria: &str) -> Vec<&Entity> {
 self.entities.iter()
 .filter(|e| e.name.contains(criteria))
 .collect()
 }
}
```rust

### Phase 4: Implementation Strategy

**Build in Stages:**

1. **Stage 1**: Core data structure + display
2. **Stage 2**: Add creation + deletion
3. **Stage 3**: Add search + filtering
4. **Stage 4**: File I/O for persistence
5. **Stage 5**: Reporting + statistics
6. **Stage 6**: Error handling + edge cases
7. **Stage 7**: Polish + optimization
8. **Stage 8**: Unit tests

**Test After Each Stage:**
- Does it compile without warnings?
- Do core operations work?
- Are edge cases handled?

### Phase 5: Testing Strategy

**Create a Test Plan:**

```rust
TEST CASE 1: Add New Record
Input: Valid record data
Expected: Record added, saved to file
Result: PASS / FAIL

TEST CASE 2: Add Record with Invalid Data
Input: Empty name, ID = 0
Expected: Error returned, record not added
Result: PASS / FAIL

TEST CASE 3: Search Empty Database
Input: Search query on empty data
Expected: Empty results
Result: PASS / FAIL


> **NEEDS_AUTHOR:** Removed placeholder - verify completeness

```rust

**Unit Test Example:**

```rust
#[cfg(test)]
mod tests {
 use super::*;
 
 #[test]
 fn test_add_entity() {
 let mut manager = EntityManager::new("test.json");
 let entity = Entity { id: 1, name: "Test".to_string() };
 assert!(manager.add(entity).is_ok());
 }
 
 #[test]
 fn test_search_empty() {
 let manager = EntityManager::new("test.json");
 let results = manager.search("test");
 assert_eq!(results.len(), 0);
 }
}
```rust

### Phase 6: Code Quality Checklist

**Before submitting, verify:**

- [ ] Code compiles with `cargo build`
- [ ] No compiler warnings
- [ ] `cargo clippy` shows no issues
- [ ] `cargo fmt` passes (properly formatted)
- [ ] All public items have doc comments
- [ ] All inputs are validated
- [ ] Error handling uses Result types
- [ ] File I/O works correctly
- [ ] Program doesn't panic on invalid input
- [ ] Variable names are meaningful
- [ ] Functions are focused and modular
- [ ] Complex logic has comments
- [ ] No code duplication
- [ ] Tests cover main functionality

### Phase 7: Documentation Requirements

**README.md Should Include:**

1. **Project Overview** (2-3 sentences)
 - What does it do?
 - Who is it for?
 - What problems does it solve?

2. **Features** (bulleted list)
 - List all implemented features
 - Note which are core vs. bonus

3. **Building Instructions**
 ```bash
 cargo build --release
 ```rust

4. **Usage Guide**
 - How to run: `cargo run`
 - How to use each feature
 - Example workflows

5. **Design Decisions**
 - Why you chose certain data structures
 - Trade-offs you made
 - Why you organized code that way
 - Rust idioms you used

6. **Known Limitations**
 - What could be improved
 - What's not implemented
 - Performance limitations

7. **Author and Date**
 - Your name
 - Date completed
 - What you learned

**Doc Comments Should:**
- Explain what functions do
- Show expected usage
- Document error conditions
- Provide examples

---

## Capstone Excellence Examples

**An excellent capstone has:**

 **Clear Purpose**: Solves a real or interesting problem 
 **Complete Implementation**: All features work, no partial functionality 
 **Robust Error Handling**: Uses Result types, handles edge cases 
 **Professional Code**: Follows Rust conventions, no warnings 
 **Thoughtful Design**: Data structures fit the problem 
 **Thorough Testing**: Unit tests + documented test cases 
 **Great Documentation**: README, doc comments, usage guide 
 **Personal Touch**: Shows creativity and individuality 

---

## Capstone Grading Rubric

| Category | Excellent (10) | Good (7-8) | Acceptable (5-6) | Poor (0-4) |
|----------|---|---|---|---|
| **Functionality** | All features work perfectly, no panics | All core features work | Core features mostly work | Missing features or crashes |
| **Code Quality** | Excellent organization, follows idioms | Well-organized Rust code | Reasonable structure | Disorganized or unsafe |
| **Error Handling** | Result types throughout, graceful | Mostly uses Results | Some error handling | Crashes on errors |
| **Data Persistence** | Reliable save/load | Works correctly | Works mostly | Unreliable or missing |
| **Testing** | Comprehensive unit tests, documented | Good test coverage | Basic tests | Minimal or no tests |
| **Documentation** | Excellent README, doc comments | Good README, useful docs | Basic README, minimal docs | Little documentation |
| **Ambition** | Goes beyond requirements | Meets all requirements | Barely meets requirements | Minimal effort |

---

## After Your Capstone

**Next Steps:**

1. **Portfolio**: Add your capstone to your programming portfolio
2. **Showcase**: Share your project on GitHub or crates.io
3. **Reflection**: Write about what you learned
4. **Advancement**: Move to advanced Rust topics (async, web frameworks, systems programming)
5. **Contribution**: Consider contributing to open source Rust projects

---

## Real-World Capstone Examples

### Example 1: Personal Finance Manager
```rust
PURPOSE: Help track personal spending and savings goals
FEATURES: 
 - Add/categorize expenses
 - Set and track savings goals
 - Generate spending reports
 - Export to CSV for analysis
COMPLEXITY: Moderate (5-7 hours)
```rust

### Example 2: Quiz Application
```rust
PURPOSE: Interactive quiz system for learning
FEATURES:
 - Load questions from file
 - Track user scores
 - Provide instant feedback
 - Show statistics and progress
COMPLEXITY: Moderate (6-8 hours)
```rust

### Example 3: Data Processor
```rust
PURPOSE: Analyze CSV files and generate reports
FEATURES:
 - Parse CSV files
 - Filter and sort data
 - Calculate statistics
 - Generate reports
 - Export results
COMPLEXITY: Moderate to Advanced (8-12 hours)
```rust

---

 **Congratulations on reaching Stage 5!** 

You've completed your programming education journey. Now create something amazing!

*Your capstone project is your proof to the world that you can program.* 



### Your Task

1. Review the code structure
2. Implement the required functionality
3. Test your solution


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


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

```rs
fn main() {
    println!("Hello, World!");
}

```rs

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard rust conventions with proper imports and main function
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
