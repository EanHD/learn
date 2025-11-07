import random

questions = [
    {"q": "What is 2+2?", "a": "4"},
    {"q": "What is 5*3?", "a": "15"},
    {"q": "What is 10-3?", "a": "7"},
    {"q": "What is 20/4?", "a": "5"},
    {"q": "What is 7+8?", "a": "15"}
]

def play_quiz():
    score = 0
    random.shuffle(questions)

    for i in range(len(questions)):
        q = questions[i]
        print("\nQuestion " + str(i+1) + ": " + q["q"])
        answer = input("Your answer: ")

        if answer == q["a"]:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong! Answer was " + q["a"])

    print("\nFinal Score: " + str(score) + "/" + str(len(questions)))
    return score

while True:
    play_quiz()
    again = input("Play again? (yes/no): ")
    if again != "yes":
        break

print("Thanks for playing!")
