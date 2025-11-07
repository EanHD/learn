# Interactive Travel Planner

A comprehensive C application for interactive travel planning, featuring destination browsing, trip planning, itinerary generation, and budget management.

## Features

- **Destination Database**: Pre-loaded database of 8 diverse destinations across different categories
- **Advanced Search**: Search destinations by category, country, budget range, or rating
- **Travel Plan Creation**: Create personalized travel plans with preferences and budget
- **Itinerary Generation**: Automatically generate day-by-day activity schedules
- **Budget Calculator**: Detailed budget analysis with cost breakdowns
- **Data Persistence**: Save and load travel plans to/from files
- **Interactive Menus**: User-friendly console interface with clear navigation

## Quick Start

1. **Compile the program**:
   ```bash
   gcc main.c -o travel_planner
   ```

2. **Run the application**:
   ```bash
   ./travel_planner
   ```

3. **Navigate using the main menu** to explore destinations and create travel plans

## Menu Structure

### Main Menu
- **1.   Browse Destinations** - View all available travel destinations
- **2.  Search Destinations** - Find destinations by category, country, budget, or rating
- **3.  Create Travel Plan** - Set up your trip with destination, duration, and preferences
- **4.   View Current Plan** - Review your current travel plan details
- **5.  Generate Itinerary** - Create a detailed day-by-day activity schedule
- **6.  Calculate Budget** - Analyze budget vs. estimated costs with breakdowns
- **7.  Save Plan** - Save your travel plan to a file
- **8.  Load Plan** - Load a previously saved travel plan
- **9.  Help** - Display help and usage instructions
- **0.  Exit** - Exit the application

## Destination Categories

### Beach Destinations
- **Maldives**: Crystal clear waters, overwater bungalows, snorkeling, diving
- **Bali**: Tropical beaches, rice terraces, surfing, cultural experiences

### Mountain Destinations
- **Swiss Alps**: Skiing, snowboarding, hiking, cable car rides
- **Patagonia**: Glaciers, wildlife, trekking, photography

### City Destinations
- **Paris**: Museums, Seine cruises, cafés, shopping
- **Tokyo**: Temples, shopping districts, robot restaurants, street food

### Cultural Destinations
- **Rome**: Colosseum, Vatican Museums, ancient ruins, gelato

### Adventure Destinations
- **New Zealand**: Bungee jumping, skydiving, hiking, movie tours

## Search Functionality

### Search by Category
Find destinations by type: beach, mountain, city, cultural, adventure

### Search by Country
Locate destinations in specific countries

### Search by Budget Range
Filter destinations by daily cost range

### Search by Rating
Find destinations with minimum star ratings (1-5)

## Travel Plan Creation

### Required Information
- **Destination**: Choose from available destinations
- **Duration**: Number of days for the trip
- **Season**: Preferred time of year
- **Budget**: Total available budget
- **Preferences**: Up to 5 personal preferences (optional)

### Plan Storage
Plans are stored in memory and can be saved to files for persistence

## Itinerary Generation

### Automatic Scheduling
- **Morning Activities**: Selected from destination's available activities
- **Afternoon Activities**: Different activities for continued engagement
- **Evening Activities**: Relaxation and dining suggestions

### Randomized Selection
Activities are randomly selected from the destination's activity list to create varied itineraries

### Day-by-Day Format
Clear daily breakdown with time slots and activity descriptions

## Budget Calculator

### Cost Analysis
- **Estimated Total Cost**: Based on destination's average daily cost × duration
- **Budget Comparison**: Surplus or deficit analysis
- **Daily Breakdown**: Cost per day calculation

### Cost Categories
- **Accommodation**: 50% of daily cost
- **Food & Drinks**: 25% of daily cost
- **Activities**: 15% of daily cost
- **Transportation**: 10% of daily cost

## File Operations

### Save Plan
- Saves complete travel plan to text file
- Includes destination, duration, budget, preferences
- Saves generated itinerary if available
- User-specified filename

### Load Plan
- Loads previously saved travel plans
- Parses plan details and itinerary
- Restores complete plan state

## Technical Details

### Data Structures
- **Destination Structure**: Name, country, description, category, cost, rating, activities
- **TravelPlan Structure**: Destination, duration, season, budget, preferences
- **ItineraryItem Structure**: Day, time slot, activity, description

### Memory Management
- **Fixed-size Arrays**: Pre-allocated arrays for destinations and itinerary
- **String Handling**: Safe string operations with bounds checking
- **File I/O**: Standard C file operations for plan persistence

### Randomization
- **Activity Selection**: Random activity assignment for itinerary variety
- **Seed Management**: Time-based random seed for different results

## Usage Examples

### Creating a Travel Plan
```
 CREATE TRAVEL PLAN
=====================

Available destinations:
1. Maldives (Maldives)
2. Bali (Indonesia)
...
8. New Zealand (New Zealand)

Select destination (1-8): 2
Enter trip duration (days): 7
Enter preferred season: April-October
Enter total budget: $1500
Enter your preferences (max 5, press Enter after each):
Preference 1 (or press Enter to finish): beach relaxation
Preference 2 (or press Enter to finish): cultural experiences
Preference 3 (or press Enter to finish):

 Travel plan created successfully!
```

### Budget Analysis
```
 BUDGET CALCULATOR
====================

Budget Analysis:
===============
Destination: Bali
Duration: 7 days
Average daily cost: $150.00
Estimated total cost: $1050.00
Your budget: $1500.00
 You have $450.00 surplus in your budget!

Cost Breakdown (estimated):
==========================
Accommodation: $525.00 (50% of daily cost)
Food & Drinks: $262.50 (25% of daily cost)
Activities: $157.50 (15% of daily cost)
Transportation: $105.00 (10% of daily cost)
```

### Generated Itinerary
```
 YOUR 7-DAY ITINERARY
========================

Day 1 - Morning:
Activity: Beach relaxation
Description: Enjoy Beach relaxation in the morning

Day 1 - Afternoon:
Activity: Cooking classes
Description: Continue with Cooking classes in the afternoon

Day 1 - Evening:
Activity: Relaxation/Dining
Description: Relax and enjoy local cuisine in the evening

Day 2 - Morning:
Activity: Temple visits
Description: Enjoy Temple visits in the morning
...
```

## Search Examples

### Search by Category
```
 SEARCH DESTINATIONS
======================

Search Options:
1. By Category (beach, mountain, city, cultural, adventure)
2. By Country
3. By Budget Range
4. By Rating
Enter choice (1-4): 1
Enter category: beach

Destinations in category 'beach':
=====================================
• Maldives (Maldives) - $500/day
• Bali (Indonesia) - $150/day
```

### Search by Budget
```
Enter minimum daily budget: $100
Enter maximum daily budget: $250

Destinations in budget range $100 - $250:
===========================================
• Bali (Indonesia) - $150/day
• Patagonia (Chile/Argentina) - $200/day
• Tokyo (Japan) - $200/day
• Rome (Italy) - $180/day
• New Zealand (New Zealand) - $220/day
```

## File Operations

### Saving a Plan
```
 SAVE TRAVEL PLAN
===================

Enter filename to save (without extension): my_bali_trip
 Travel plan saved to 'my_bali_trip.txt' successfully!
```

### Loading a Plan
```
 LOAD TRAVEL PLAN
===================

Enter filename to load (without extension): my_bali_trip
 Travel plan loaded from 'my_bali_trip.txt' successfully!
```

## Destination Details

### Maldives
- **Category**: Beach
- **Rating**: 5
- **Best Season**: December-March
- **Activities**: Snorkeling, Diving, Spa treatments, Water sports

### Swiss Alps
- **Category**: Mountain
- **Rating**: 5
- **Best Season**: December-March (winter), June-September (summer)
- **Activities**: Skiing, Snowboarding, Hiking, Cable car rides

### Paris
- **Category**: City
- **Rating**: 5
- **Best Season**: April-June, September-October
- **Activities**: Museum visits, Seine River cruise, Café hopping, Shopping

## Error Handling

### Input Validation
- **Menu Choices**: Range checking for menu selections
- **Numeric Input**: Validation for budget and duration values
- **String Input**: Safe string handling with buffer limits
- **File Operations**: Error checking for file open/close operations

### Runtime Checks
- **Plan Existence**: Verification before itinerary generation or budget calculation
- **Destination Availability**: Validation of selected destinations
- **Memory Bounds**: Array bounds checking for all data structures

## Limitations

- Fixed number of destinations (8 pre-loaded)
- Simple text-based file format
- No advanced itinerary customization
- Basic budget estimation (no real-time pricing)
- No user account management
- Limited search filters

## Future Enhancements

### Advanced Features
- **Real-time Pricing**: Integration with travel APIs for current prices
- **Custom Itineraries**: User-defined activity preferences and scheduling
- **Weather Integration**: Real-time weather data for planning
- **Multi-destination Trips**: Support for complex itineraries
- **Group Planning**: Multiple users collaborating on plans

### User Experience
- **GUI Interface**: Web or desktop graphical interface
- **Mobile App**: Smartphone application for travel planning
- **Offline Mode**: Local storage without internet dependency
- **Social Features**: Plan sharing and travel community

### Data Management
- **Database Integration**: SQL database for destination and plan storage
- **User Accounts**: Personal profiles with travel history
- **Advanced Search**: Filters, sorting, and recommendation algorithms
- **Data Analytics**: Travel pattern analysis and insights

## Learning Outcomes

This application demonstrates:
- **Interactive Programming**: User input handling and menu-driven interfaces
- **Data Management**: Complex data structures and memory management
- **File I/O Operations**: Reading and writing structured data to files
- **Search Algorithms**: Implementing various search and filter operations
- **Randomization**: Using random number generation for varied outputs
- **Error Handling**: Robust input validation and error recovery
- **Modular Design**: Organized functions and clear code structure

## Compilation

### Requirements
- GCC compiler
- Standard C libraries (stdio.h, stdlib.h, string.h, ctype.h, time.h)

### Build Command
```bash
gcc main.c -o travel_planner -Wall -Wextra
```

### Debug Build
```bash
gcc main.c -o travel_planner_debug -Wall -Wextra -g -O0
```

### Clean Build
```bash
rm -f travel_planner travel_planner_debug
gcc main.c -o travel_planner -Wall -Wextra
```

---

*Built as Level 4 of Stage 4: Full Problem Solving in the C/C++ Programming Curriculum*