# Level 5: Decision Support Application - Study Plan Advisor

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Learning Objectives

By completing this level, you will:

- Understand the principles of decision support systems
- Learn to implement simple expert systems and recommendation engines
- Practice collecting and analyzing user preferences
- Design algorithms that provide personalized recommendations
- Create user-friendly assessment and feedback interfaces

## Code Analysis

### Application Structure

The Study Plan Advisor follows a decision support system pattern:

1. **Data Collection Phase**: Gather user preferences through structured questions
2. **Analysis Phase**: Process responses to determine learning profile
3. **Recommendation Engine**: Generate personalized advice based on collected data
4. **Presentation Phase**: Display results in a clear, actionable format

### Key Components

**Assessment Functions:**
- `assess_learning_style()`: Determines preferred learning methods
- `assess_goals_and_time()`: Identifies objectives and constraints
- `get_user_input()`: Validates menu-based responses

**Recommendation Logic:**
The system uses conditional logic to map user responses to specific recommendations:
- Learning styles map to study methods
- Goals determine focus areas
- Time availability sets scheduling recommendations

**Data Flow:**
```python
User Input → Assessment → Analysis → Recommendation → Display
```python

### Decision-Making Algorithm

The recommendation engine uses a rule-based approach:
- **Rules**: If user prefers hands-on learning AND wants to master skills → Recommend practical exercises
- **Combinations**: Multiple preferences are combined to create comprehensive plans
- **Defaults**: Fallback recommendations for edge cases

## Success Checklist

- [ ] Application collects learning style preferences
- [ ] Goal and time availability are assessed
- [ ] Recommendations vary based on different input combinations
- [ ] Output includes focus, schedule, methods, and tips
- [ ] Input validation prevents invalid choices
- [ ] Results are presented in a clear, organized format
- [ ] Code uses functions to separate concerns
- [ ] Assessment questions are clear and unambiguous

## Key Concepts Demonstrated

- [ ] **Decision Support Systems**: Applications that help users make informed choices
- [ ] **Expert Systems**: Rule-based systems that mimic human decision-making
- [ ] **User Profiling**: Collecting and analyzing user characteristics
- [ ] **Recommendation Algorithms**: Logic for providing personalized suggestions
- [ ] **Structured Interviews**: Systematic data collection through questions
- [ ] **Conditional Logic**: Complex if-elif chains for decision making

## Potential Enhancements

- [ ] Add more detailed assessment questions
- [ ] Implement scoring system for recommendations
- [ ] Save user profiles for future sessions
- [ ] Add progress tracking features
- [ ] Include resource recommendations (books, courses, etc.)
- [ ] Create visual progress charts

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to Python
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**


### Learning Goals

- Understand core concepts
- Practice implementation


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

```py
#!/usr/bin/env python3
"""
Study Plan Advisor - Decision Support Application
A simple expert system that recommends study plans based on user preferences and goals.
"""

def get_user_input(prompt, options):
    """Get validated user input from a list of options."""
    while True:
        print(f"\n{prompt}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Please enter a valid number.")

def assess_learning_style():
    """Assess the user's preferred learning style."""
    print("Let's determine your learning style!")

    question1 = "How do you prefer to learn new information?"
    options1 = [
        "By reading books or articles",
        "By watching videos or demonstrations",
        "By doing hands-on activities",
        "By discussing with others"
    ]
    style = get_user_input(question1, options1)

    question2 = "When studying, you prefer:"
    options2 = [
        "Structured schedules and outlines",
        "Flexible, exploratory approach",
        "Group study sessions",
        "Independent, focused work"
    ]
    preference = get_user_input(question2, options2)

    return style, preference

def assess_goals_and_time():
    """Assess user's goals and available time."""
    print("\nNow let's understand your goals and schedule!")

    question3 = "What is your primary learning goal?"
    options3 = [
        "Master a specific skill",
        "Gain broad knowledge in a field",
        "Prepare for certification/exam",
        "Personal development"
    ]
    goal = get_user_input(question3, options3)

    question4 = "How much time can you dedicate daily?"
    options4 = [
        "Less than 1 hour",
        "1-2 hours",
        "2-4 hours",
        "More than 4 hours"
    ]
    time_available = get_user_input(question4, options4)

    return goal, time_available

def generate_recommendation(style, preference, goal, time_available):
    """Generate a personalized study plan recommendation."""
    print("\n" + "="*60)
    print("          YOUR PERSONALIZED STUDY PLAN")
    print("="*60)

    # Base recommendation
    plan = {
        'focus': '',
        'methods': [],
        'schedule': '',
        'tips': []
    }

    # Determine focus based on goal
    if goal == "Master a specific skill":
        plan['focus'] = "Skill-focused intensive practice"
    elif goal == "Gain broad knowledge in a field":
        plan['focus'] = "Comprehensive knowledge building"
    elif goal == "Prepare for certification/exam":
        plan['focus'] = "Exam-oriented structured preparation"
    else:  # Personal development
        plan['focus'] = "Well-rounded personal growth"

    # Determine methods based on learning style
    if style == "By reading books or articles":
        plan['methods'].extend(["Reading textbooks", "Writing summaries", "Research papers"])
    elif style == "By watching videos or demonstrations":
        plan['methods'].extend(["Online video tutorials", "Interactive demonstrations", "Recorded lectures"])
    elif style == "By doing hands-on activities":
        plan['methods'].extend(["Practical exercises", "Projects", "Experiments"])
    else:  # By discussing with others
        plan['methods'].extend(["Study groups", "Discussion forums", "Teaching others"])

    # Adjust for preference
    if preference == "Structured schedules and outlines":
        plan['methods'].append("Detailed planning and checklists")
    elif preference == "Flexible, exploratory approach":
        plan['methods'].append("Exploratory learning and curiosity-driven research")
    elif preference == "Group study sessions":
        plan['methods'].append("Collaborative learning activities")
    else:  # Independent, focused work
        plan['methods'].append("Solo deep work sessions")

    # Determine schedule based on time
    if time_available == "Less than 1 hour":
        plan['schedule'] = "15-30 minute focused sessions, 4-6 days per week"
    elif time_available == "1-2 hours":
        plan['schedule'] = "1-2 hour daily sessions with weekends off"
    elif time_available == "2-4 hours":
        plan['schedule'] = "2-3 hour intensive daily study blocks"
    else:  # More than 4 hours
        plan['schedule'] = "4+ hour comprehensive daily study with breaks"

    # Add general tips
    plan['tips'] = [
        "Track your progress weekly",
        "Review material regularly for retention",
        "Take breaks to avoid burnout",
        "Adjust plan as needed based on progress"
    ]

    return plan

def display_recommendation(plan):
    """Display the study plan recommendation."""
    print(f"\nFocus: {plan['focus']}")
    print(f"\nRecommended Schedule: {plan['schedule']}")

    print("\nStudy Methods:")
    for i, method in enumerate(plan['methods'], 1):
        print(f"  {i}. {method}")

    print("\nAdditional Tips:")
    for i, tip in enumerate(plan['tips'], 1):
        print(f"  {i}. {tip}")

    print("\n" + "="*60)
    print("Remember: This is a starting point. Adjust based on your experience!")
    print("="*60)

def main():
    """Main application function."""
    print("Welcome to the Study Plan Advisor!")
    print("Answer a few questions and get a personalized study plan recommendation.")

    # Get user preferences
    style, preference = assess_learning_style()
    goal, time_available = assess_goals_and_time()

    # Generate and display recommendation
    plan = generate_recommendation(style, preference, goal, time_available)
    display_recommendation(plan)

    print("\nThank you for using the Study Plan Advisor!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard python conventions with proper imports and main function
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
