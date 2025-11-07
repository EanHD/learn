def get_score():
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0-100")
        except:
            print("Enter a valid number")

def calculate_average(scores):
    return sum(scores) / len(scores)

name = input("Enter student name: ")
scores = []
for i in range(5):
    print("Test " + str(i + 1))
    score = get_score()
    scores.append(score)

average = calculate_average(scores)
print("\nStudent: " + name)
print("Average: " + str(round(average, 2)))
