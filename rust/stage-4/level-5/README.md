# Travel Recommendation System

A sophisticated Rust program that provides personalized travel destination recommendations based on user preferences for budget, climate, activities, and duration.

## How to Run

1. **Compile the program:**
   ```bash
   rustc main.rs
   ```

2. **Run the program:**
   ```bash
   ./main
   ```

3. **Answer the preference questions** to get personalized recommendations.

## Features

- **4-criteria preference matching**: Budget, climate, activity type, and travel duration
- **81 possible preference combinations**: Comprehensive decision matrix (3×3×3×3)
- **2-3 personalized destination recommendations** per combination
- **Budget-adjusted cost estimates**: Pricing scales with budget level
- **Detailed destination information**: Why recommended, duration, activities
- **Robust input validation**: Ensures valid user choices

## Decision Criteria

### Budget Levels
- **Low**: Under $1000
- **Medium**: $1000-$3000
- **High**: Over $3000

### Climate Preferences
- **Cold**: Mountain regions, northern destinations
- **Temperate**: Mild weather, moderate climates
- **Warm**: Tropical, beach, and hot climates

### Activity Types
- **Relaxation**: Spas, beaches, leisure activities
- **Adventure**: Outdoor sports, hiking, extreme activities
- **Culture**: Museums, historical sites, festivals

### Travel Duration
- **Weekend**: 2-3 days
- **Week**: 7 days
- **Month**: 30 days

## Example Output

```
Travel Recommendation System
===========================

What's your budget range?
1. Low (under $1000)
2. Medium ($1000-$3000)
3. High (over $3000)
Enter choice (1-3): 2

What's your preferred climate?
1. Cold
2. Temperate
3. Warm
Enter choice (1-3): 3

What's your activity preference?
1. Relaxation
2. Adventure
3. Culture
Enter choice (1-3): 1

How long do you want to travel?
1. Weekend (2-3 days)
2. Week (7 days)
3. Month (30 days)
Enter choice (1-3): 2

Based on your preferences (Medium budget, Warm climate, Relaxation, Week-long trip):

 Recommended Destinations:

1. **Cancun, Mexico**
   - Why: Perfect warm beach relaxation within medium budget
   - Cost estimate: $1500-2200 for flights + resort
   - Duration: 7-10 days ideal
   - Activities: Beach, spa, swimming with dolphins

2. **Puerto Rico**
   - Why: Caribbean warmth with relaxation focus
   - Cost estimate: $1200-1800 total
   - Duration: 5-14 days flexible
   - Activities: Beach lounging, bioluminescent bays

Safe travels! 
```

## Program Architecture

### Core Components

1. **Preference Collection**: Interactive menu system for gathering user criteria
2. **Decision Engine**: Nested match statements implementing complex logic
3. **Recommendation Functions**: Modular functions for each preference combination
4. **Cost Calculator**: Budget-based pricing system
5. **Output Formatter**: Consistent display of destination information

### Decision Logic Flow

```
User Input → Preference Validation → Decision Matrix → Recommendation Functions → Formatted Output
```

### Destination Coverage

- **Cold Climate**: Banff, Aspen, Alaska, Iceland, Prague, Edinburgh
- **Temperate Climate**: San Francisco, Portland, New Zealand South Island, Colorado, Paris, Rome
- **Warm Climate**: Cancun, Puerto Rico, Costa Rica, Hawaii, Machu Picchu, Rio de Janeiro

## Testing the Program

### Test Different Combinations

1. **Warm + Relaxation + Medium budget** → Cancun, Puerto Rico
2. **Cold + Adventure + High budget** → Alaska, Iceland
3. **Temperate + Culture + Low budget** → Paris, Rome (budget-adjusted)
4. **All budget levels** → Verify cost estimates scale appropriately

### Input Validation Testing

- Try entering invalid numbers (0, 4, etc.)
- Try entering non-numeric input
- Verify error messages and re-prompting

## Learning Outcomes

This program demonstrates:
- **Complex conditional logic** with nested match statements
- **Modular function design** for maintainable code
- **Data organization** and structured output formatting
- **Input validation** and error handling
- **Algorithm design** for multi-criteria decision making

## Technical Details

- **Language**: Rust
- **Input/Output**: Standard library (std::io)
- **Control Flow**: Match expressions and functions
- **Data Types**: Strings, integers, arrays
- **Error Handling**: Input validation loops

## Future Enhancements

- **Duration filtering**: Adjust recommendations based on trip length
- **Seasonal recommendations**: Consider best time to visit
- **Group size pricing**: Adjust costs for different party sizes
- **Accessibility options**: Include destinations for different abilities
- **Real-time pricing**: Integration with travel APIs
- **User profiles**: Save and load preference combinations

## Troubleshooting

### Compilation Issues
- Ensure you have Rust installed: `rustc --version`
- Check for syntax errors in the code
- Verify file permissions for execution

### Runtime Issues
- Program expects numeric input (1-3) for all questions
- Invalid input will prompt for re-entry
- All combinations should produce valid recommendations

### Common Errors
- **"No such file or directory"**: Make sure you're in the correct directory
- **Permission denied**: Use `chmod +x main` if needed (though usually not required)
- **Invalid input**: Program handles this gracefully with re-prompting

---

*Built as part of Stage 4: Full Problem Solving in the Rust Programming Curriculum*