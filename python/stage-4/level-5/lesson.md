# Level 5: Decision Support Application - Study Plan Advisor

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



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
```

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

- **Decision Support Systems**: Applications that help users make informed choices
- **Expert Systems**: Rule-based systems that mimic human decision-making
- **User Profiling**: Collecting and analyzing user characteristics
- **Recommendation Algorithms**: Logic for providing personalized suggestions
- **Structured Interviews**: Systematic data collection through questions
- **Conditional Logic**: Complex if-elif chains for decision making

## Potential Enhancements

- Add more detailed assessment questions
- Implement scoring system for recommendations
- Save user profiles for future sessions
- Add progress tracking features
- Include resource recommendations (books, courses, etc.)
- Create visual progress charts

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
