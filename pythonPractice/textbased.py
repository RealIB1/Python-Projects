import random


def process_guess(theAnswer, theGuess):
    position = 0
    clue = ""
    for letter in theGuess:
        if letter == theAnswer[position]:
            clue += "G"
        elif letter in theAnswer:
            clue += "Y"
        else:
            clue += "_"
        position += 1
    print(clue)
    return "GGGGG"  # True of correct, otherwise False.


"""Text-Base Game
Tip 1: Load words and store them in a list.
"""
word_list = []
words_file = open("C:/Python310/Doc/text game/words.txt.txt")
for word in words_file:
    word_list.append(word.strip())

"""
Tip 2:
Pick a word from the word list.
"""

answer = random.choice(word_list)
print(answer)
"""
Tip 3:
Number of guess up to 6.
"""
num_of_guesses = 0
guessed_correctly = False

while num_of_guesses < 6 and not guessed_correctly:
    """Get guess from user"""

    guess = input("Input a 5-letter word and press enter: ")
    print("You've guessed", guess)
    num_of_guesses += 1
    guessed_correctly = process_guess(answer, guess)  # Tip 4:Processed guess

"""
Tip 5:
Display end of game message.
"""

if guessed_correctly:
    print("Congratulations, you guessed the correct word in ", num_of_guesses, "attempts.")
else:
    print("You have used all your guesses... The correct word is", answer)
