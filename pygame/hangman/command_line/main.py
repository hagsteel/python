import random
import sys
from words import word_list
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import gui.main
print(gui.main.WORD)

letter_guessed = ""
turn = 6


def display_hangman(turn):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[turn]


if __name__ == "__main__":
    random_fruit = random.choice(word_list)

    for letter in random_fruit:
        print("_", end=" ")

    print("\n")

    while turn > 0:
        guess = input("Guess a letter: ")
        letter_guessed += guess
        failed = 0

        if guess == "":
            print("ENTER A LETTER!")
        elif guess != "":
            for char in random_fruit:
                if char in letter_guessed:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
                    failed += 1

            if guess in random_fruit:
                print("\nCorrect")
            else:
                print("\nWrong")
                turn -= 1
                print(display_hangman(turn))

            if failed == 0:
                sys.exit("You won")

        print(f"All guesses: {letter_guessed}")
        print(f"You have {turn} more chance to guess")
    print(f"The word was: {random_fruit}")
