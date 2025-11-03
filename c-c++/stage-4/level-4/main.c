#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

// Constants
#define MAX_DESTINATIONS 50
#define MAX_ACTIVITIES 20
#define MAX_ITINERARY_ITEMS 100
#define MAX_NAME_LENGTH 100
#define MAX_DESCRIPTION_LENGTH 500

// Data Structures
typedef struct {
    char name[MAX_NAME_LENGTH];
    char country[MAX_NAME_LENGTH];
    char description[MAX_DESCRIPTION_LENGTH];
    char best_season[50];
    char category[50]; // beach, mountain, city, cultural, adventure
    double average_cost_per_day;
    int rating; // 1-5 stars
    char activities[MAX_ACTIVITIES][MAX_NAME_LENGTH];
    int activity_count;
} Destination;

typedef struct {
    char destination[MAX_NAME_LENGTH];
    int duration_days;
    char season[50];
    double budget;
    char preferences[5][50]; // array of preferences
    int preference_count;
} TravelPlan;

typedef struct {
    char day_activity[MAX_NAME_LENGTH];
    int day_number;
    char time_slot[20]; // morning, afternoon, evening
    char description[MAX_DESCRIPTION_LENGTH];
} ItineraryItem;

// Global Variables
Destination destinations[MAX_DESTINATIONS];
int destination_count = 0;
TravelPlan current_plan;
ItineraryItem itinerary[MAX_ITINERARY_ITEMS];
int itinerary_count = 0;

// Function Prototypes
void initialize_destinations();
void display_main_menu();
void display_destinations();
void search_destinations();
void create_travel_plan();
void view_travel_plan();
void generate_itinerary();
void calculate_budget();
void save_plan_to_file();
void load_plan_from_file();
void display_help();

// Utility Functions
void clear_screen() {
    system("clear");
}

void pause() {
    printf("\nPress Enter to continue...");
    getchar();
    getchar(); // consume newline
}

void to_lowercase(char *str) {
    for(int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int string_compare_case_insensitive(const char *str1, const char *str2) {
    char temp1[MAX_NAME_LENGTH], temp2[MAX_NAME_LENGTH];
    strcpy(temp1, str1);
    strcpy(temp2, str2);
    to_lowercase(temp1);
    to_lowercase(temp2);
    return strcmp(temp1, temp2);
}

// Core Functions
void initialize_destinations() {
    // Beach Destinations
    strcpy(destinations[0].name, "Maldives");
    strcpy(destinations[0].country, "Maldives");
    strcpy(destinations[0].description, "Crystal clear waters, overwater bungalows, world-class snorkeling and diving");
    strcpy(destinations[0].best_season, "December-March");
    strcpy(destinations[0].category, "beach");
    destinations[0].average_cost_per_day = 500.0;
    destinations[0].rating = 5;
    strcpy(destinations[0].activities[0], "Snorkeling");
    strcpy(destinations[0].activities[1], "Diving");
    strcpy(destinations[0].activities[2], "Spa treatments");
    strcpy(destinations[0].activities[3], "Water sports");
    destinations[0].activity_count = 4;

    strcpy(destinations[1].name, "Bali");
    strcpy(destinations[1].country, "Indonesia");
    strcpy(destinations[1].description, "Tropical paradise with beautiful beaches, rice terraces, and vibrant culture");
    strcpy(destinations[1].best_season, "April-October");
    strcpy(destinations[1].category, "beach");
    destinations[1].average_cost_per_day = 150.0;
    destinations[1].rating = 4;
    strcpy(destinations[1].activities[0], "Beach relaxation");
    strcpy(destinations[1].activities[1], "Temple visits");
    strcpy(destinations[1].activities[2], "Surfing");
    strcpy(destinations[1].activities[3], "Cooking classes");
    destinations[1].activity_count = 4;

    // Mountain Destinations
    strcpy(destinations[2].name, "Swiss Alps");
    strcpy(destinations[2].country, "Switzerland");
    strcpy(destinations[2].description, "Majestic mountains, pristine lakes, charming villages, and world-class skiing");
    strcpy(destinations[2].best_season, "December-March (winter), June-September (summer)");
    strcpy(destinations[2].category, "mountain");
    destinations[2].average_cost_per_day = 300.0;
    destinations[2].rating = 5;
    strcpy(destinations[2].activities[0], "Skiing");
    strcpy(destinations[2].activities[1], "Snowboarding");
    strcpy(destinations[2].activities[2], "Hiking");
    strcpy(destinations[2].activities[3], "Cable car rides");
    destinations[2].activity_count = 4;

    strcpy(destinations[3].name, "Patagonia");
    strcpy(destinations[3].country, "Chile/Argentina");
    strcpy(destinations[3].description, "Dramatic landscapes, glaciers, mountains, and unique wildlife");
    strcpy(destinations[3].best_season, "November-March");
    strcpy(destinations[3].category, "mountain");
    destinations[3].average_cost_per_day = 200.0;
    destinations[3].rating = 4;
    strcpy(destinations[3].activities[0], "Glacier hiking");
    strcpy(destinations[3].activities[1], "Wildlife watching");
    strcpy(destinations[3].activities[2], "Trekking");
    strcpy(destinations[3].activities[3], "Photography");
    destinations[3].activity_count = 4;

    // City Destinations
    strcpy(destinations[4].name, "Paris");
    strcpy(destinations[4].country, "France");
    strcpy(destinations[4].description, "City of Light with iconic landmarks, world-class museums, and romantic atmosphere");
    strcpy(destinations[4].best_season, "April-June, September-October");
    strcpy(destinations[4].category, "city");
    destinations[4].average_cost_per_day = 250.0;
    destinations[4].rating = 5;
    strcpy(destinations[4].activities[0], "Museum visits");
    strcpy(destinations[4].activities[1], "Seine River cruise");
    strcpy(destinations[4].activities[2], "Café hopping");
    strcpy(destinations[4].activities[3], "Shopping");
    destinations[4].activity_count = 4;

    strcpy(destinations[5].name, "Tokyo");
    strcpy(destinations[5].country, "Japan");
    strcpy(destinations[5].description, "Futuristic city blending traditional culture with cutting-edge technology");
    strcpy(destinations[5].best_season, "March-May, September-November");
    strcpy(destinations[5].category, "city");
    destinations[5].average_cost_per_day = 200.0;
    destinations[5].rating = 5;
    strcpy(destinations[5].activities[0], "Temple visits");
    strcpy(destinations[5].activities[1], "Shopping districts");
    strcpy(destinations[5].activities[2], "Robot restaurants");
    strcpy(destinations[5].activities[3], "Street food");
    destinations[5].activity_count = 4;

    // Cultural Destinations
    strcpy(destinations[6].name, "Rome");
    strcpy(destinations[6].country, "Italy");
    strcpy(destinations[6].description, "Eternal City with ancient ruins, Vatican City, and incredible history");
    strcpy(destinations[6].best_season, "April-June, September-October");
    strcpy(destinations[6].category, "cultural");
    destinations[6].average_cost_per_day = 180.0;
    destinations[6].rating = 5;
    strcpy(destinations[6].activities[0], "Colosseum tour");
    strcpy(destinations[6].activities[1], "Vatican Museums");
    strcpy(destinations[6].activities[2], "Gelato tasting");
    strcpy(destinations[6].activities[3], "Ancient ruins");
    destinations[6].activity_count = 4;

    // Adventure Destinations
    strcpy(destinations[7].name, "New Zealand");
    strcpy(destinations[7].country, "New Zealand");
    strcpy(destinations[7].description, "Adventure paradise with bungee jumping, hiking, and stunning landscapes");
    strcpy(destinations[7].best_season, "December-March");
    strcpy(destinations[7].category, "adventure");
    destinations[7].average_cost_per_day = 220.0;
    destinations[7].rating = 4;
    strcpy(destinations[7].activities[0], "Bungee jumping");
    strcpy(destinations[7].activities[1], "Skydiving");
    strcpy(destinations[7].activities[2], "Hiking");
    strcpy(destinations[7].activities[3], "Lord of the Rings tours");
    destinations[7].activity_count = 4;

    destination_count = 8;
}

void display_main_menu() {
    clear_screen();
    printf("🌍 INTERACTIVE TRAVEL PLANNER 🌍\n");
    printf("================================\n\n");
    printf("Main Menu:\n");
    printf("1. 🏖️  Browse Destinations\n");
    printf("2. 🔍 Search Destinations\n");
    printf("3. 📝 Create Travel Plan\n");
    printf("4. 👁️  View Current Plan\n");
    printf("5. 📅 Generate Itinerary\n");
    printf("6. 💰 Calculate Budget\n");
    printf("7. 💾 Save Plan\n");
    printf("8. 📂 Load Plan\n");
    printf("9. ❓ Help\n");
    printf("0. 🚪 Exit\n\n");
    printf("Enter your choice (0-9): ");
}

void display_destinations() {
    clear_screen();
    printf("🏖️  AVAILABLE DESTINATIONS 🏖️\n");
    printf("=============================\n\n");

    for(int i = 0; i < destination_count; i++) {
        printf("%d. %s (%s)\n", i+1, destinations[i].name, destinations[i].country);
        printf("   Category: %s | Rating: %d⭐ | Cost: $%.0f/day\n",
               destinations[i].category, destinations[i].rating, destinations[i].average_cost_per_day);
        printf("   Best Season: %s\n", destinations[i].best_season);
        printf("   Description: %s\n", destinations[i].description);
        printf("   Activities: ");
        for(int j = 0; j < destinations[i].activity_count; j++) {
            printf("%s", destinations[i].activities[j]);
            if(j < destinations[i].activity_count - 1) printf(", ");
        }
        printf("\n\n");
    }
    pause();
}

void search_destinations() {
    clear_screen();
    printf("🔍 SEARCH DESTINATIONS 🔍\n");
    printf("========================\n\n");

    printf("Search Options:\n");
    printf("1. By Category (beach, mountain, city, cultural, adventure)\n");
    printf("2. By Country\n");
    printf("3. By Budget Range\n");
    printf("4. By Rating\n");
    printf("Enter choice (1-4): ");

    int choice;
    scanf("%d", &choice);
    getchar(); // consume newline

    int found = 0;

    switch(choice) {
        case 1: {
            char category[MAX_NAME_LENGTH];
            printf("Enter category: ");
            fgets(category, sizeof(category), stdin);
            category[strcspn(category, "\n")] = 0;

            printf("\nDestinations in category '%s':\n", category);
            printf("=====================================\n");
            for(int i = 0; i < destination_count; i++) {
                if(string_compare_case_insensitive(destinations[i].category, category) == 0) {
                    printf("• %s (%s) - $%.0f/day\n",
                           destinations[i].name, destinations[i].country, destinations[i].average_cost_per_day);
                    found = 1;
                }
            }
            break;
        }
        case 2: {
            char country[MAX_NAME_LENGTH];
            printf("Enter country: ");
            fgets(country, sizeof(country), stdin);
            country[strcspn(country, "\n")] = 0;

            printf("\nDestinations in %s:\n", country);
            printf("===================\n");
            for(int i = 0; i < destination_count; i++) {
                if(string_compare_case_insensitive(destinations[i].country, country) == 0) {
                    printf("• %s - $%.0f/day\n", destinations[i].name, destinations[i].average_cost_per_day);
                    found = 1;
                }
            }
            break;
        }
        case 3: {
            double min_budget, max_budget;
            printf("Enter minimum daily budget: $");
            scanf("%lf", &min_budget);
            printf("Enter maximum daily budget: $");
            scanf("%lf", &max_budget);

            printf("\nDestinations in budget range $%.0f - $%.0f:\n", min_budget, max_budget);
            printf("==============================================\n");
            for(int i = 0; i < destination_count; i++) {
                if(destinations[i].average_cost_per_day >= min_budget &&
                   destinations[i].average_cost_per_day <= max_budget) {
                    printf("• %s (%s) - $%.0f/day\n",
                           destinations[i].name, destinations[i].country, destinations[i].average_cost_per_day);
                    found = 1;
                }
            }
            break;
        }
        case 4: {
            int min_rating;
            printf("Enter minimum rating (1-5): ");
            scanf("%d", &min_rating);

            printf("\nDestinations with rating %d+ stars:\n", min_rating);
            printf("===================================\n");
            for(int i = 0; i < destination_count; i++) {
                if(destinations[i].rating >= min_rating) {
                    printf("• %s (%s) - %d⭐\n",
                           destinations[i].name, destinations[i].country, destinations[i].rating);
                    found = 1;
                }
            }
            break;
        }
        default:
            printf("Invalid choice!\n");
            return;
    }

    if(!found) {
        printf("No destinations found matching your criteria.\n");
    }

    pause();
}

void create_travel_plan() {
    clear_screen();
    printf("📝 CREATE TRAVEL PLAN 📝\n");
    printf("========================\n\n");

    printf("Available destinations:\n");
    for(int i = 0; i < destination_count; i++) {
        printf("%d. %s (%s)\n", i+1, destinations[i].name, destinations[i].country);
    }

    printf("\nSelect destination (1-%d): ", destination_count);
    int dest_choice;
    scanf("%d", &dest_choice);
    getchar(); // consume newline

    if(dest_choice < 1 || dest_choice > destination_count) {
        printf("Invalid destination choice!\n");
        pause();
        return;
    }

    Destination selected = destinations[dest_choice - 1];
    strcpy(current_plan.destination, selected.name);

    printf("Enter trip duration (days): ");
    scanf("%d", &current_plan.duration_days);
    getchar();

    printf("Enter preferred season: ");
    fgets(current_plan.season, sizeof(current_plan.season), stdin);
    current_plan.season[strcspn(current_plan.season, "\n")] = 0;

    printf("Enter total budget: $");
    scanf("%lf", &current_plan.budget);
    getchar();

    printf("Enter your preferences (max 5, press Enter after each):\n");
    current_plan.preference_count = 0;
    for(int i = 0; i < 5; i++) {
        printf("Preference %d (or press Enter to finish): ", i+1);
        fgets(current_plan.preferences[i], sizeof(current_plan.preferences[i]), stdin);
        current_plan.preferences[i][strcspn(current_plan.preferences[i], "\n")] = 0;
        if(strlen(current_plan.preferences[i]) == 0) break;
        current_plan.preference_count++;
    }

    printf("\n✅ Travel plan created successfully!\n");
    printf("Destination: %s\n", current_plan.destination);
    printf("Duration: %d days\n", current_plan.duration_days);
    printf("Season: %s\n", current_plan.season);
    printf("Budget: $%.2f\n", current_plan.budget);

    pause();
}

void view_travel_plan() {
    clear_screen();
    printf("👁️  CURRENT TRAVEL PLAN 👁️\n");
    printf("==========================\n\n");

    if(strlen(current_plan.destination) == 0) {
        printf("No travel plan created yet. Please create a plan first.\n");
    } else {
        printf("Destination: %s\n", current_plan.destination);
        printf("Duration: %d days\n", current_plan.duration_days);
        printf("Preferred Season: %s\n", current_plan.season);
        printf("Total Budget: $%.2f\n", current_plan.budget);
        printf("Daily Budget: $%.2f\n", current_plan.budget / current_plan.duration_days);

        printf("\nPreferences:\n");
        for(int i = 0; i < current_plan.preference_count; i++) {
            printf("• %s\n", current_plan.preferences[i]);
        }
    }

    pause();
}

void generate_itinerary() {
    clear_screen();
    printf("📅 GENERATE ITINERARY 📅\n");
    printf("========================\n\n");

    if(strlen(current_plan.destination) == 0) {
        printf("No travel plan available. Please create a plan first.\n");
        pause();
        return;
    }

    // Find the destination details
    Destination *dest = NULL;
    for(int i = 0; i < destination_count; i++) {
        if(strcmp(destinations[i].name, current_plan.destination) == 0) {
            dest = &destinations[i];
            break;
        }
    }

    if(dest == NULL) {
        printf("Destination details not found.\n");
        pause();
        return;
    }

    // Generate itinerary based on preferences and activities
    itinerary_count = 0;
    srand(time(NULL));

    for(int day = 1; day <= current_plan.duration_days && itinerary_count < MAX_ITINERARY_ITEMS; day++) {
        // Morning activity
        if(itinerary_count < MAX_ITINERARY_ITEMS) {
            int activity_idx = rand() % dest->activity_count;
            strcpy(itinerary[itinerary_count].day_activity, dest->activities[activity_idx]);
            itinerary[itinerary_count].day_number = day;
            strcpy(itinerary[itinerary_count].time_slot, "Morning");
            sprintf(itinerary[itinerary_count].description, "Enjoy %s in the morning", dest->activities[activity_idx]);
            itinerary_count++;
        }

        // Afternoon activity
        if(itinerary_count < MAX_ITINERARY_ITEMS) {
            int activity_idx = rand() % dest->activity_count;
            strcpy(itinerary[itinerary_count].day_activity, dest->activities[activity_idx]);
            itinerary[itinerary_count].day_number = day;
            strcpy(itinerary[itinerary_count].time_slot, "Afternoon");
            sprintf(itinerary[itinerary_count].description, "Continue with %s in the afternoon", dest->activities[activity_idx]);
            itinerary_count++;
        }

        // Evening activity (relaxation or dining)
        if(itinerary_count < MAX_ITINERARY_ITEMS) {
            strcpy(itinerary[itinerary_count].day_activity, "Relaxation/Dining");
            itinerary[itinerary_count].day_number = day;
            strcpy(itinerary[itinerary_count].time_slot, "Evening");
            strcpy(itinerary[itinerary_count].description, "Relax and enjoy local cuisine in the evening");
            itinerary_count++;
        }
    }

    printf("✅ Itinerary generated for %d days!\n\n", current_plan.duration_days);

    // Display itinerary
    printf("📅 YOUR %d-DAY ITINERARY 📅\n", current_plan.duration_days);
    printf("=============================\n");

    for(int i = 0; i < itinerary_count; i++) {
        printf("\nDay %d - %s:\n", itinerary[i].day_number, itinerary[i].time_slot);
        printf("Activity: %s\n", itinerary[i].day_activity);
        printf("Description: %s\n", itinerary[i].description);
    }

    pause();
}

void calculate_budget() {
    clear_screen();
    printf("💰 BUDGET CALCULATOR 💰\n");
    printf("=======================\n\n");

    if(strlen(current_plan.destination) == 0) {
        printf("No travel plan available. Please create a plan first.\n");
        pause();
        return;
    }

    // Find destination cost
    double daily_cost = 0;
    for(int i = 0; i < destination_count; i++) {
        if(strcmp(destinations[i].name, current_plan.destination) == 0) {
            daily_cost = destinations[i].average_cost_per_day;
            break;
        }
    }

    double total_estimated = daily_cost * current_plan.duration_days;
    double difference = current_plan.budget - total_estimated;

    printf("Budget Analysis:\n");
    printf("===============\n");
    printf("Destination: %s\n", current_plan.destination);
    printf("Duration: %d days\n", current_plan.duration_days);
    printf("Average daily cost: $%.2f\n", daily_cost);
    printf("Estimated total cost: $%.2f\n", total_estimated);
    printf("Your budget: $%.2f\n", current_plan.budget);

    if(difference >= 0) {
        printf("✅ You have $%.2f surplus in your budget!\n", difference);
    } else {
        printf("⚠️  You are $%.2f over budget. Consider:\n", -difference);
        printf("   • Reducing trip duration\n");
        printf("   • Choosing cheaper activities\n");
        printf("   • Looking for budget accommodations\n");
    }

    // Breakdown by categories
    printf("\nCost Breakdown (estimated):\n");
    printf("==========================\n");
    printf("Accommodation: $%.2f (50%% of daily cost)\n", total_estimated * 0.5);
    printf("Food & Drinks: $%.2f (25%% of daily cost)\n", total_estimated * 0.25);
    printf("Activities: $%.2f (15%% of daily cost)\n", total_estimated * 0.15);
    printf("Transportation: $%.2f (10%% of daily cost)\n", total_estimated * 0.1);

    pause();
}

void save_plan_to_file() {
    clear_screen();
    printf("💾 SAVE TRAVEL PLAN 💾\n");
    printf("======================\n\n");

    if(strlen(current_plan.destination) == 0) {
        printf("No travel plan to save. Please create a plan first.\n");
        pause();
        return;
    }

    char filename[100];
    printf("Enter filename to save (without extension): ");
    fgets(filename, sizeof(filename), stdin);
    filename[strcspn(filename, "\n")] = 0;
    strcat(filename, ".txt");

    FILE *file = fopen(filename, "w");
    if(file == NULL) {
        printf("Error opening file for writing!\n");
        pause();
        return;
    }

    fprintf(file, "TRAVEL PLAN\n");
    fprintf(file, "===========\n\n");
    fprintf(file, "Destination: %s\n", current_plan.destination);
    fprintf(file, "Duration: %d days\n", current_plan.duration_days);
    fprintf(file, "Season: %s\n", current_plan.season);
    fprintf(file, "Budget: $%.2f\n", current_plan.budget);
    fprintf(file, "\nPreferences:\n");
    for(int i = 0; i < current_plan.preference_count; i++) {
        fprintf(file, "- %s\n", current_plan.preferences[i]);
    }

    if(itinerary_count > 0) {
        fprintf(file, "\nITINERARY:\n");
        fprintf(file, "==========\n");
        for(int i = 0; i < itinerary_count; i++) {
            fprintf(file, "\nDay %d - %s:\n", itinerary[i].day_number, itinerary[i].time_slot);
            fprintf(file, "Activity: %s\n", itinerary[i].day_activity);
            fprintf(file, "Description: %s\n", itinerary[i].description);
        }
    }

    fclose(file);
    printf("✅ Travel plan saved to '%s' successfully!\n", filename);
    pause();
}

void load_plan_from_file() {
    clear_screen();
    printf("📂 LOAD TRAVEL PLAN 📂\n");
    printf("=====================\n\n");

    char filename[100];
    printf("Enter filename to load (without extension): ");
    fgets(filename, sizeof(filename), stdin);
    filename[strcspn(filename, "\n")] = 0;
    strcat(filename, ".txt");

    FILE *file = fopen(filename, "r");
    if(file == NULL) {
        printf("File '%s' not found!\n", filename);
        pause();
        return;
    }

    // Simple parsing - in a real application, you'd want more robust parsing
    char line[500];
    int in_itinerary = 0;
    itinerary_count = 0;

    while(fgets(line, sizeof(line), file)) {
        if(strstr(line, "Destination:")) {
            sscanf(line, "Destination: %[^\n]", current_plan.destination);
        } else if(strstr(line, "Duration:")) {
            sscanf(line, "Duration: %d days", &current_plan.duration_days);
        } else if(strstr(line, "Season:")) {
            sscanf(line, "Season: %[^\n]", current_plan.season);
        } else if(strstr(line, "Budget:")) {
            sscanf(line, "Budget: $%lf", &current_plan.budget);
        } else if(strstr(line, "ITINERARY:")) {
            in_itinerary = 1;
        } else if(in_itinerary && strstr(line, "Day")) {
            sscanf(line, "Day %d - %[^\n]", &itinerary[itinerary_count].day_number,
                   itinerary[itinerary_count].time_slot);
            itinerary_count++;
        }
    }

    fclose(file);
    printf("✅ Travel plan loaded from '%s' successfully!\n", filename);
    pause();
}

void display_help() {
    clear_screen();
    printf("❓ HELP & INSTRUCTIONS ❓\n");
    printf("=========================\n\n");

    printf("Welcome to the Interactive Travel Planner!\n\n");

    printf("HOW TO USE:\n");
    printf("===========\n");
    printf("1. 🏖️  Browse Destinations: View all available travel destinations\n");
    printf("2. 🔍 Search Destinations: Find destinations by category, country, budget, or rating\n");
    printf("3. 📝 Create Travel Plan: Set up your trip details and preferences\n");
    printf("4. 👁️  View Current Plan: Review your current travel plan\n");
    printf("5. 📅 Generate Itinerary: Create a day-by-day activity schedule\n");
    printf("6. 💰 Calculate Budget: Analyze your budget vs. estimated costs\n");
    printf("7. 💾 Save Plan: Save your plan to a file for later use\n");
    printf("8. 📂 Load Plan: Load a previously saved travel plan\n");
    printf("9. ❓ Help: Display this help information\n");
    printf("0. 🚪 Exit: Exit the application\n\n");

    printf("TIPS:\n");
    printf("=====\n");
    printf("• Start by browsing destinations to see what's available\n");
    printf("• Use search to find destinations that match your interests\n");
    printf("• Create a travel plan with your preferred destination and budget\n");
    printf("• Generate an itinerary to see a sample daily schedule\n");
    printf("• Use budget calculator to ensure you're within your spending limit\n");
    printf("• Save your plans to review or share later\n\n");

    printf("DESTINATION CATEGORIES:\n");
    printf("======================\n");
    printf("• Beach: Tropical islands and coastal destinations\n");
    printf("• Mountain: Alpine regions and high-altitude adventures\n");
    printf("• City: Urban destinations with culture and attractions\n");
    printf("• Cultural: Historical sites and heritage locations\n");
    printf("• Adventure: Extreme sports and outdoor activities\n\n");

    pause();
}

int main() {
    initialize_destinations();

    int choice;
    do {
        display_main_menu();
        scanf("%d", &choice);
        getchar(); // consume newline

        switch(choice) {
            case 1:
                display_destinations();
                break;
            case 2:
                search_destinations();
                break;
            case 3:
                create_travel_plan();
                break;
            case 4:
                view_travel_plan();
                break;
            case 5:
                generate_itinerary();
                break;
            case 6:
                calculate_budget();
                break;
            case 7:
                save_plan_to_file();
                break;
            case 8:
                load_plan_from_file();
                break;
            case 9:
                display_help();
                break;
            case 0:
                printf("\nThank you for using the Interactive Travel Planner! 🌍\n");
                break;
            default:
                printf("Invalid choice! Please enter 0-9.\n");
                pause();
        }
    } while(choice != 0);

    return 0;
}