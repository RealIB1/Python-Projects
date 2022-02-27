
print("Welcome to the Python Basic Test, Good Luck!!")


def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("------------------------------------------")
        print(key)
        for i in options[question_number - 1]:
            print(i)

        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    display_score(correct_guesses, guesses)


# ---------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print(answer, "is CORRECT!")
        return 1
    else:
        print(guess, "is WRONG!")
        return 0


# ----------------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------------------")
    print("RESULTS")
    print("-----------------------------------------")

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print("")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    score = int((correct_guesses / len(guesses)) * 100)
    print("\nYour Score is " + str(score) + "%")
    if score >= 80:
        print("CONGRATULATION!! YOU PASSED THE TEST!!")
    else:
        print("PASS MARK IS 80%, TRY AGAIN!!")


# ---------------------------------

def play_again():
    response = input("Would you like to play again? (Yes or No): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python s tribute to which comedy group?: ": "C",
    "Python is a programming language?:": "D"
}

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. Sometimes", "B. False", "C. No Idea", "D. True"]]

new_game()

while play_again():
    new_game()

print("Ouch, Nice Play!!\nSee you again!!")
