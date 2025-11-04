# Level 5: Decision Support Application

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

Now you'll implement a decision support application that uses complex conditional logic to provide personalized recommendations based on multiple criteria.

---

### Learning Goals

- Implement complex decision trees in Rust
- Handle multiple user preferences and criteria
- Create recommendation algorithms
- Design comprehensive conditional logic
- Provide detailed, personalized output

---

### Your Task

**Implement the Travel Recommendation System program in Rust. Create the following files:**

1. **`main.rs`** - The main program file
2. **`README.md`** - Instructions for running the program

### Program Requirements

Based on your Stage 3 pseudocode, implement a travel recommendation system that:

1. **Collects user preferences** for 4 criteria:
   - Budget range (low, medium, high)
   - Climate preference (cold, temperate, warm)
   - Activity type (relaxation, adventure, culture)
   - Travel duration (weekend, week, month)

2. **Uses complex decision logic** to match destinations to preferences
3. **Provides 2-3 personalized recommendations** with detailed information
4. **Includes cost estimates** adjusted by budget level
5. **Displays comprehensive travel information** for each destination

**Decision Criteria:**
- **81 possible combinations** (3×3×3×3) of user preferences
- **Primary matching**: Climate + Activity preferences
- **Secondary filtering**: Budget-appropriate cost estimates
- **Tertiary consideration**: Duration feasibility

---

### Implementation Steps

1. **Create the project structure**:
   ```bash
   cd /home/eanhd/LEARN/rust/stage-4-full-problem-solving/level-5-decision-support-application
   ```

2. **Create `main.rs`** with your Rust implementation

3. **Test your program**:
   ```bash
   rustc main.rs
   ./main
   ```

4. **Create `README.md`** with usage instructions

---

### Success Checklist

- [ ] Created `main.rs` file
- [ ] Program collects all 4 user preferences
- [ ] Complex decision logic implemented correctly
- [ ] 2-3 destinations recommended for each preference combination
- [ ] Cost estimates adjusted by budget level
- [ ] Detailed destination information displayed

---

### What You'll Learn

Decision support applications involve:
- **Complex conditional logic** - Multi-criteria decision making
- **Recommendation algorithms** - Matching preferences to options
- **Data organization** - Structuring destination information
- **Personalization** - Tailored recommendations based on user input

---

### Implementation Tips

1. **Use nested match statements** for decision logic
2. **Create helper functions** for cost estimation and destination display
3. **Organize destination data** in structured format
4. **Test all combinations** to ensure comprehensive coverage
5. **Provide clear, detailed output** for each recommendation

---

## Need Help with Rust?

- **Nested match**: Use `match` inside `match` for complex decisions
- **String concatenation**: Use `format!` for building recommendation text
- **Helper functions**: Break complex logic into smaller functions
- **Data structures**: Consider structs for destination information

---

<div style="page-break-after: always;"></div>

---

## SOLUTION GUIDE (No cheating until you've tried!)

### Expected Program Behavior

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
```

### Sample Implementation

```rust
use std::io::{self, Write};

fn main() {
    println!("Travel Recommendation System");
    println!("===========================");
    println!();

    // Get user preferences
    let budget_choice = get_user_choice("What's your budget range?", 
                                       &["Low (under $1000)", "Medium ($1000-$3000)", "High (over $3000)"]);

    let climate_choice = get_user_choice("What's your preferred climate?", 
                                        &["Cold", "Temperate", "Warm"]);

    let activity_choice = get_user_choice("What's your activity preference?", 
                                         &["Relaxation", "Adventure", "Culture"]);

    let duration_choice = get_user_choice("How long do you want to travel?", 
                                         &["Weekend (2-3 days)", "Week (7 days)", "Month (30 days)"]);

    // Convert choices to descriptive names
    let budget_name = match budget_choice {
        1 => "Low",
        2 => "Medium",
        3 => "High",
        _ => "Unknown"
    };

    let climate_name = match climate_choice {
        1 => "Cold",
        2 => "Temperate", 
        3 => "Warm",
        _ => "Unknown"
    };

    let activity_name = match activity_choice {
        1 => "Relaxation",
        2 => "Adventure",
        3 => "Culture",
        _ => "Unknown"
    };

    let duration_name = match duration_choice {
        1 => "Weekend",
        2 => "Week",
        3 => "Month",
        _ => "Unknown"
    };

    // Display preferences summary
    println!("Based on your preferences ({} budget, {} climate, {}, {}-long trip):", 
             budget_name, climate_name, activity_name, duration_name);
    println!();
    println!(" Recommended Destinations:");
    println!();

    // Complex decision logic based on climate and activity (primary factors)
    match climate_choice {
        1 => { // Cold climate
            match activity_choice {
                1 => recommend_cold_relaxation(budget_choice),    // Relaxation + Cold
                2 => recommend_cold_adventure(budget_choice),     // Adventure + Cold
                3 => recommend_cold_culture(budget_choice),       // Culture + Cold
                _ => println!("Invalid activity choice.")
            }
        }
        2 => { // Temperate climate
            match activity_choice {
                1 => recommend_temperate_relaxation(budget_choice),    // Relaxation + Temperate
                2 => recommend_temperate_adventure(budget_choice),     // Adventure + Temperate
                3 => recommend_temperate_culture(budget_choice),       // Culture + Temperate
                _ => println!("Invalid activity choice.")
            }
        }
        3 => { // Warm climate
            match activity_choice {
                1 => recommend_warm_relaxation(budget_choice),    // Relaxation + Warm
                2 => recommend_warm_adventure(budget_choice),     // Adventure + Warm
                3 => recommend_warm_culture(budget_choice),       // Culture + Warm
                _ => println!("Invalid activity choice.")
            }
        }
        _ => println!("Invalid climate choice.")
    }

    println!();
    println!("Safe travels! ");
}

fn get_user_choice(question: &str, options: &[&str]) -> u32 {
    println!("{}", question);
    for (i, option) in options.iter().enumerate() {
        println!("{}. {}", i + 1, option);
    }
    print!("Enter choice (1-{}): ", options.len());
    io::stdout().flush().unwrap();

    loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<u32>() {
            Ok(choice) if choice >= 1 && choice <= options.len() as u32 => return choice,
            Ok(_) => {
                print!("Please enter a number between 1 and {}: ", options.len());
                io::stdout().flush().unwrap();
            }
            Err(_) => {
                print!("Please enter a valid number: ");
                io::stdout().flush().unwrap();
            }
        }
    }
}

fn get_cost_estimate(budget_level: u32, destination: &str) -> String {
    match budget_level {
        1 => match destination {
            "banff" | "aspen" => "600-900",
            "alaska" | "iceland" => "800-1200",
            "prague" | "edinburgh" => "400-700",
            "sanfrancisco" | "portland" => "300-600",
            "nz_south" | "colorado" => "800-1200",
            "paris" | "rome" => "500-800",
            "cancun" | "puerto_rico" => "400-700",
            "costa_rica" | "hawaii" => "600-900",
            "machu_picchu" | "rio" => "700-1000",
            _ => "500-800"
        },
        2 => match destination {
            "banff" | "aspen" => "1500-2500",
            "alaska" | "iceland" => "2000-3000",
            "prague" | "edinburgh" => "1000-1500",
            "sanfrancisco" | "portland" => "800-1200",
            "nz_south" | "colorado" => "1800-2800",
            "paris" | "rome" => "1200-1800",
            "cancun" | "puerto_rico" => "1200-1800",
            "costa_rica" | "hawaii" => "1500-2200",
            "machu_picchu" | "rio" => "1600-2400",
            _ => "1200-1800"
        },
        3 => match destination {
            "banff" | "aspen" => "4000-8000",
            "alaska" | "iceland" => "5000-10000",
            "prague" | "edinburgh" => "2500-4000",
            "sanfrancisco" | "portland" => "2000-3500",
            "nz_south" | "colorado" => "4500-9000",
            "paris" | "rome" => "3000-5000",
            "cancun" | "puerto_rico" => "2800-4500",
            "costa_rica" | "hawaii" => "3500-6000",
            "machu_picchu" | "rio" => "3800-6500",
            _ => "3000-5000"
        },
        _ => "1000-2000"
    }.to_string()
}

fn display_destination(number: u32, name: &str, why: &str, cost_key: &str, duration: &str, activities: &str, budget_level: u32) {
    println!("{}. **{}**", number, name);
    println!("   - Why: {}", why);
    println!("   - Cost estimate: ${} total", get_cost_estimate(budget_level, cost_key));
    println!("   - Duration: {}", duration);
    println!("   - Activities: {}", activities);
    println!();
}

// ===== DESTINATION RECOMMENDATION FUNCTIONS =====

fn recommend_cold_relaxation(budget: u32) {
    display_destination(1, "Banff, Canada", "Mountain hot springs and luxury resorts", 
                      "banff", "3-7 days ideal", "Spa treatments, scenic views", budget);
    display_destination(2, "Aspen, Colorado", "Luxury mountain relaxation", 
                      "aspen", "4-10 days recommended", "Spas, fine dining, skiing optional", budget);
}

fn recommend_cold_adventure(budget: u32) {
    display_destination(1, "Alaska", "Extreme outdoor adventures", 
                      "alaska", "7-14 days for full experience", "Glacier hiking, wildlife viewing", budget);
    display_destination(2, "Iceland", "Volcanic landscapes and northern lights", 
                      "iceland", "5-10 days recommended", "Hiking, hot springs, ice caves", budget);
}

fn recommend_cold_culture(budget: u32) {
    display_destination(1, "Prague, Czech Republic", "Historic architecture in cooler climate", 
                      "prague", "4-7 days ideal", "Castle tours, museums, Christmas markets", budget);
    display_destination(2, "Edinburgh, Scotland", "Medieval history and festivals", 
                      "edinburgh", "3-7 days recommended", "Castle visits, whiskey tours, festivals", budget);
}

fn recommend_temperate_relaxation(budget: u32) {
    display_destination(1, "San Francisco, California", "Mild weather with luxury amenities", 
                      "sanfrancisco", "3-7 days ideal", "Spas, fine dining, bay cruises", budget);
    display_destination(2, "Portland, Oregon", "Relaxed Pacific Northwest vibe", 
                      "portland", "4-10 days recommended", "Coffee culture, gardens, light hiking", budget);
}

fn recommend_temperate_adventure(budget: u32) {
    display_destination(1, "New Zealand South Island", "Diverse outdoor adventures", 
                      "nz_south", "7-14 days for full experience", "Bungee jumping, hiking, skiing", budget);
    display_destination(2, "Colorado Rockies", "Mountain biking and hiking paradise", 
                      "colorado", "5-10 days recommended", "Mountain biking, rock climbing, fishing", budget);
}

fn recommend_temperate_culture(budget: u32) {
    display_destination(1, "Paris, France", "World-class museums and cuisine", 
                      "paris", "4-7 days ideal", "Louvre, Eiffel Tower, cafes", budget);
    display_destination(2, "Rome, Italy", "Ancient history and art", 
                      "rome", "5-10 days recommended", "Colosseum, Vatican, gelato tours", budget);
}

fn recommend_warm_relaxation(budget: u32) {
    display_destination(1, "Cancun, Mexico", "Perfect warm beach relaxation", 
                      "cancun", "7-10 days ideal", "Beach, spa, swimming with dolphins", budget);
    display_destination(2, "Puerto Rico", "Caribbean warmth with relaxation focus", 
                      "puerto_rico", "5-14 days flexible", "Beach lounging, bioluminescent bays", budget);
}

fn recommend_warm_adventure(budget: u32) {
    display_destination(1, "Costa Rica", "Rainforest and beach adventures", 
                      "costa_rica", "7-14 days for full experience", "Zip-lining, surfing, volcano climbing", budget);
    display_destination(2, "Hawaii Big Island", "Volcanic adventures and beaches", 
                      "hawaii", "7-10 days recommended", "Volcano tours, snorkeling, hiking", budget);
}

fn recommend_warm_culture(budget: u32) {
    display_destination(1, "Machu Picchu, Peru", "Ancient Incan civilization", 
                      "machu_picchu", "7-10 days ideal", "Inca Trail, ancient ruins, Andean culture", budget);
    display_destination(2, "Rio de Janeiro, Brazil", "Carnival culture and beaches", 
                      "rio", "5-14 days recommended", "Carnival, Christ statue, samba", budget);
}
```

### Implementation Analysis

**Key Rust Concepts Used:**
- **Nested match statements**: Complex decision logic with multiple criteria
- **Functions**: Modular recommendation functions for each preference combination
- **Arrays and slices**: `&[&str]` for menu options
- **String formatting**: `format!` and `println!` with placeholders
- **Helper functions**: `get_cost_estimate()` and `display_destination()` for code reuse

**Program Structure:**
- **Preference collection**: Gather all 4 user criteria
- **Decision matrix**: 9 primary combinations (3 climate × 3 activity)
- **Recommendation functions**: Separate function for each preference pair
- **Cost estimation**: Budget-based pricing for each destination
- **Structured output**: Consistent formatting for all recommendations

**Why this structure?**
- **Modular design**: Each recommendation combination in separate function
- **Scalable logic**: Easy to add new destinations or criteria
- **Maintainable code**: Clear separation of concerns
- **Comprehensive coverage**: All 9 climate-activity combinations handled

### Common Implementation Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Too many nested matches | Complex code becomes hard to read | Use functions to break up logic |
| Inconsistent data | Different destination info formats | Create standard display function |
| Hard-coded costs | Difficult to maintain pricing | Use helper function for cost logic |
| Missing combinations | Not all preference pairs covered | Plan all combinations upfront |
| Poor function names | Unclear what each function does | Use descriptive names like `recommend_warm_relaxation` |

### Testing Your Program

**Test Different Combinations:**
1. **Warm + Relaxation + Medium budget**: Should recommend Cancun, Puerto Rico
2. **Cold + Adventure + High budget**: Should recommend Alaska, Iceland
3. **Temperate + Culture + Low budget**: Should recommend Paris, Rome (adjusted for budget)
4. **All budget levels**: Verify cost estimates change appropriately

### README.md Template

```markdown
# Travel Recommendation System

A Rust program that provides personalized travel destination recommendations based on user preferences for budget, climate, activities, and duration.

## How to Run

1. Compile the program:
   ```bash
   rustc main.rs
   ```

2. Run the program:
   ```bash
   ./main
   ```

3. Answer the preference questions to get recommendations.

## Features

- 4-criteria preference matching (budget, climate, activity, duration)
- 81 possible preference combinations
- 2-3 personalized destination recommendations per combination
- Budget-adjusted cost estimates
- Detailed destination information (why, duration, activities)

## Decision Criteria

- **Budget**: Low (<$1000), Medium ($1000-$3000), High (>$3000)
- **Climate**: Cold, Temperate, Warm
- **Activity**: Relaxation, Adventure, Culture
- **Duration**: Weekend, Week, Month

## Example Output

```
Based on your preferences (Medium budget, Warm climate, Relaxation, Week-long trip):

 Recommended Destinations:

1. **Cancun, Mexico**
   - Why: Perfect warm beach relaxation within medium budget
   - Cost estimate: $1500-2200 for flights + resort
   - Duration: 7-10 days ideal
   - Activities: Beach, spa, swimming with dolphins
```
```

### Bonus Challenges

1. **Duration filtering** - Adjust recommendations based on trip length
2. **Seasonal recommendations** - Consider best time to visit destinations
3. **Group size pricing** - Adjust costs for different party sizes
4. **Accessibility options** - Include destinations suitable for different abilities

---

 **Excellent! You built a sophisticated decision support system!** 

*Next: Automated Application (Student Grade Analyzer)!*