# Level 5: Decision-Based Problems

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

Decision-based problems require complex conditional logic and multiple decision paths. You'll design a solution for a problem with many possible outcomes.

---

### Learning Goals

- Analyze complex decision requirements
- Design nested conditional logic
- Handle multiple decision criteria
- Create comprehensive decision trees

---

### Your Task

**Read the problem below, then write pseudocode to solve it. Create a file called `decision_based_problems.md` with your pseudocode solution.**

### Problem: Travel Recommendation System

**Description:**
Create a travel recommendation system that suggests destinations based on user preferences. The program should:

1. Ask for budget range (low, medium, high)
2. Ask for preferred climate (cold, temperate, warm)
3. Ask for activity preference (relaxation, adventure, culture)
4. Ask for travel duration (weekend, week, month)
5. Recommend 2-3 destinations based on all criteria
6. Explain why each destination matches their preferences

**Decision Criteria:**

**Budget Ranges:**
- Low: Under $1000 total
- Medium: $1000-$3000 total
- High: Over $3000 total

**Climate Options:**
- Cold: Snowy/mountain destinations
- Temperate: Mild weather destinations
- Warm: Beach/tropical destinations

**Activity Types:**
- Relaxation: Spa/beach destinations
- Adventure: Hiking/outdoor activities
- Culture: Historical/city destinations

**Duration Impact:**
- Weekend: Closer destinations
- Week: Regional destinations
- Month: International destinations

**Example Interaction:**
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

3. **Costa Rica (Pacific Coast)**
   - Why: Warm climate with relaxation options
   - Cost estimate: $1800-2500 total
   - Duration: 7-14 days recommended
   - Activities: Beach relaxation, optional light adventure
```

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your pseudocode file**:
   ```bash
   touch decision_based_problems.md
   ```
3. **Map decision combinations** - Consider all possible preference combinations
4. **Design recommendation logic** - Match destinations to criteria
5. **Plan output formatting** - Clear, informative recommendations

---

### Success Checklist

- [ ] Created `decision_based_problems.md` file
- [ ] Identified all decision criteria combinations
- [ ] Designed nested conditional logic for recommendations
- [ ] Planned destination matching algorithm
- [ ] Created informative recommendation output

---

### What Did You Learn?

Decision-based problem analysis involves:
- **Criteria mapping** - Understanding all possible combinations
- **Logic trees** - Nested conditions for complex decisions
- **Data organization** - Grouping destinations by characteristics
- **User experience** - Clear presentation of options

---

### Try This (Optional Challenges)

1. Add seasonal availability considerations
2. Include travel restrictions or visa requirements
3. Add accommodation type preferences

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Problem Analysis

**Decision Matrix:**
The problem requires a 4-dimensional decision matrix:
- Budget (3 options)
- Climate (3 options)
- Activity (3 options)
- Duration (3 options)

**Total Combinations:** 3 × 3 × 3 × 3 = 81 possible combinations!

**Recommendation Strategy:**
- **Primary Match**: Climate + Activity (most important)
- **Secondary Filter**: Budget range
- **Tertiary Filter**: Duration feasibility

### Sample Pseudocode Solution

```
START PROGRAM
    DISPLAY "Travel Recommendation System"
    DISPLAY "==========================="
    DISPLAY ""
    
    // Get budget preference
    DISPLAY "What's your budget range?"
    DISPLAY "1. Low (under $1000)"
    DISPLAY "2. Medium ($1000-$3000)"
    DISPLAY "3. High (over $3000)"
    DISPLAY "Enter choice (1-3):"
    READ budget_choice AS NUMBER
    
    // Get climate preference
    DISPLAY "What's your preferred climate?"
    DISPLAY "1. Cold"
    DISPLAY "2. Temperate"
    DISPLAY "3. Warm"
    DISPLAY "Enter choice (1-3):"
    READ climate_choice AS NUMBER
    
    // Get activity preference
    DISPLAY "What's your activity preference?"
    DISPLAY "1. Relaxation"
    DISPLAY "2. Adventure"
    DISPLAY "3. Culture"
    DISPLAY "Enter choice (1-3):"
    READ activity_choice AS NUMBER
    
    // Get duration preference
    DISPLAY "How long do you want to travel?"
    DISPLAY "1. Weekend (2-3 days)"
    DISPLAY "2. Week (7 days)"
    DISPLAY "3. Month (30 days)"
    DISPLAY "Enter choice (1-3):"
    READ duration_choice AS NUMBER
    
    // Convert choices to descriptive names
    SET budget_name TO ""
    IF budget_choice == 1 THEN SET budget_name TO "Low"
    ELSE IF budget_choice == 2 THEN SET budget_name TO "Medium"
    ELSE IF budget_choice == 3 THEN SET budget_name TO "High"
    
    SET climate_name TO ""
    IF climate_choice == 1 THEN SET climate_name TO "Cold"
    ELSE IF climate_choice == 2 THEN SET climate_name TO "Temperate"
    ELSE IF climate_choice == 3 THEN SET climate_name TO "Warm"
    
    SET activity_name TO ""
    IF activity_choice == 1 THEN SET activity_name TO "Relaxation"
    ELSE IF activity_choice == 2 THEN SET activity_name TO "Adventure"
    ELSE IF activity_choice == 3 THEN SET activity_name TO "Culture"
    
    SET duration_name TO ""
    IF duration_choice == 1 THEN SET duration_name TO "Weekend"
    ELSE IF duration_choice == 2 THEN SET duration_name TO "Week"
    ELSE IF duration_choice == 3 THEN SET duration_name TO "Month"
    
    // Display preferences summary
    DISPLAY "Based on your preferences (" + budget_name + " budget, " + climate_name + " climate, " + activity_name + ", " + duration_name + "-long trip):"
    DISPLAY ""
    DISPLAY " Recommended Destinations:"
    DISPLAY ""
    
    // Complex decision logic based on climate and activity (primary factors)
    IF climate_choice == 1 THEN  // Cold climate
        IF activity_choice == 1 THEN  // Relaxation + Cold
            DISPLAY "1. **Banff, Canada**"
            DISPLAY "   - Why: Mountain hot springs and luxury resorts"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "banff")
            DISPLAY "   - Duration: 3-7 days ideal"
            DISPLAY "   - Activities: Spa treatments, scenic views"
            DISPLAY ""
            DISPLAY "2. **Aspen, Colorado**"
            DISPLAY "   - Why: Luxury mountain relaxation"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "aspen")
            DISPLAY "   - Duration: 4-10 days recommended"
            DISPLAY "   - Activities: Spas, fine dining, skiing optional"
            
        ELSE IF activity_choice == 2 THEN  // Adventure + Cold
            DISPLAY "1. **Alaska**"
            DISPLAY "   - Why: Extreme outdoor adventures"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "alaska")
            DISPLAY "   - Duration: 7-14 days for full experience"
            DISPLAY "   - Activities: Glacier hiking, wildlife viewing"
            DISPLAY ""
            DISPLAY "2. **Iceland**"
            DISPLAY "   - Why: Volcanic landscapes and northern lights"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "iceland")
            DISPLAY "   - Duration: 5-10 days recommended"
            DISPLAY "   - Activities: Hiking, hot springs, ice caves"
            
        ELSE  // Culture + Cold
            DISPLAY "1. **Prague, Czech Republic**"
            DISPLAY "   - Why: Historic architecture in cooler climate"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "prague")
            DISPLAY "   - Duration: 4-7 days ideal"
            DISPLAY "   - Activities: Castle tours, museums, Christmas markets"
            DISPLAY ""
            DISPLAY "2. **Edinburgh, Scotland**"
            DISPLAY "   - Why: Medieval history and festivals"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "edinburgh")
            DISPLAY "   - Duration: 3-7 days recommended"
            DISPLAY "   - Activities: Castle visits, whiskey tours, festivals"
        END IF
        
    ELSE IF climate_choice == 2 THEN  // Temperate climate
        IF activity_choice == 1 THEN  // Relaxation + Temperate
            DISPLAY "1. **San Francisco, California**"
            DISPLAY "   - Why: Mild weather with luxury amenities"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "sanfrancisco")
            DISPLAY "   - Duration: 3-7 days ideal"
            DISPLAY "   - Activities: Spas, fine dining, bay cruises"
            DISPLAY ""
            DISPLAY "2. **Portland, Oregon**"
            DISPLAY "   - Why: Relaxed Pacific Northwest vibe"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "portland")
            DISPLAY "   - Duration: 4-10 days recommended"
            DISPLAY "   - Activities: Coffee culture, gardens, light hiking"
            
        ELSE IF activity_choice == 2 THEN  // Adventure + Temperate
            DISPLAY "1. **New Zealand South Island**"
            DISPLAY "   - Why: Diverse outdoor adventures"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "nz_south")
            DISPLAY "   - Duration: 7-14 days for full experience"
            DISPLAY "   - Activities: Bungee jumping, hiking, skiing"
            DISPLAY ""
            DISPLAY "2. **Colorado Rockies**"
            DISPLAY "   - Why: Mountain biking and hiking paradise"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "colorado")
            DISPLAY "   - Duration: 5-10 days recommended"
            DISPLAY "   - Activities: Mountain biking, rock climbing, fishing"
            
        ELSE  // Culture + Temperate
            DISPLAY "1. **Paris, France**"
            DISPLAY "   - Why: World-class museums and cuisine"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "paris")
            DISPLAY "   - Duration: 4-7 days ideal"
            DISPLAY "   - Activities: Louvre, Eiffel Tower, cafes"
            DISPLAY ""
            DISPLAY "2. **Rome, Italy**"
            DISPLAY "   - Why: Ancient history and art"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "rome")
            DISPLAY "   - Duration: 5-10 days recommended"
            DISPLAY "   - Activities: Colosseum, Vatican, gelato tours"
        END IF
        
    ELSE  // Warm climate
        IF activity_choice == 1 THEN  // Relaxation + Warm
            DISPLAY "1. **Cancun, Mexico**"
            DISPLAY "   - Why: Perfect warm beach relaxation"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "cancun")
            DISPLAY "   - Duration: 7-10 days ideal"
            DISPLAY "   - Activities: Beach, spa, swimming with dolphins"
            DISPLAY ""
            DISPLAY "2. **Puerto Rico**"
            DISPLAY "   - Why: Caribbean warmth with relaxation focus"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "puerto_rico")
            DISPLAY "   - Duration: 5-14 days flexible"
            DISPLAY "   - Activities: Beach lounging, bioluminescent bays"
            
        ELSE IF activity_choice == 2 THEN  // Adventure + Warm
            DISPLAY "1. **Costa Rica**"
            DISPLAY "   - Why: Rainforest and beach adventures"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "costa_rica")
            DISPLAY "   - Duration: 7-14 days for full experience"
            DISPLAY "   - Activities: Zip-lining, surfing, volcano climbing"
            DISPLAY ""
            DISPLAY "2. **Hawaii Big Island**"
            DISPLAY "   - Why: Volcanic adventures and beaches"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "hawaii")
            DISPLAY "   - Duration: 7-10 days recommended"
            DISPLAY "   - Activities: Volcano tours, snorkeling, hiking"
            
        ELSE  // Culture + Warm
            DISPLAY "1. **Machu Picchu, Peru**"
            DISPLAY "   - Why: Ancient Incan civilization"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "machu_picchu")
            DISPLAY "   - Duration: 7-10 days ideal"
            DISPLAY "   - Activities: Inca Trail, ancient ruins, Andean culture"
            DISPLAY ""
            DISPLAY "2. **Rio de Janeiro, Brazil**"
            DISPLAY "   - Why: Carnival culture and beaches"
            DISPLAY "   - Cost estimate: $" + GET_COST_ESTIMATE(budget_choice, "rio")
            DISPLAY "   - Duration: 5-14 days recommended"
            DISPLAY "   - Activities: Carnival, Christ statue, samba"
        END IF
    END IF
    
    DISPLAY ""
    DISPLAY "Safe travels! "
END PROGRAM

// Helper function for cost estimates
FUNCTION GET_COST_ESTIMATE(budget_level, destination)
    // This would contain cost logic based on budget level and destination
    // Simplified version for pseudocode
    IF budget_level == 1 THEN RETURN "800-1200"
    ELSE IF budget_level == 2 THEN RETURN "1500-2500"
    ELSE RETURN "3000-8000"
END FUNCTION
```

### Analysis Breakdown

**Decision Logic:**
- **Primary Criteria**: Climate + Activity (nested IF statements)
- **Cost Estimation**: Helper function for budget-appropriate ranges
- **Destination Selection**: 2-3 options per combination
- **Detailed Information**: Why, cost, duration, activities for each

**Why this approach?**
- **Hierarchical Logic**: Most important factors first (climate/activity)
- **Comprehensive Coverage**: All 9 climate-activity combinations covered
- **Budget Integration**: Cost estimates adjusted by budget level
- **Rich Information**: Each recommendation includes multiple details

**Potential improvements:**
- Duration-based filtering (closer destinations for weekends)
- Seasonal availability considerations
- Group size pricing adjustments
- Accessibility requirements

### Common Analysis Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Too many nested IFs | Complex logic becomes unreadable | Consider lookup tables or functions |
| Missing combinations | Not covering all preference combinations | Create decision matrix first |
| Poor data organization | Hard to maintain destination data | Use structured data storage |
| No prioritization | All criteria treated equally | Weight criteria by importance |

### Bonus Knowledge

- **Decision Trees**: Formalizing complex conditional logic
- **Recommendation Systems**: Matching user preferences to options
- **Data Modeling**: Organizing complex preference combinations
- **User Experience**: Clear presentation of multiple options

---

 **Great! You designed a complex travel recommendation system!** 

*Next: Repetitive Problems!*