import random
import sys
import os.path

# Import gui/main.py
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import gui.main

HANGMAN_STATUS = gui.main.HANGMAN_STATUS
HANGMAN_STATUS = 6


def display_hangman(HANGMAN_STATUS):
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
    return stages[HANGMAN_STATUS]


if __name__ == "__main__":
    while True:
        gui.main.display_word = ""

        for letter in gui.main.WORD:
            if letter in gui.main.GUESSED:
                gui.main.display_word += letter + " "
            else:
                gui.main.display_word += "_ "
        print(gui.main.display_word)

        guess = input("Guess a letter: ").upper()
        gui.main.GUESSED.append(guess)

        if guess not in gui.main.WORD:
            HANGMAN_STATUS -= 1
            print(display_hangman(HANGMAN_STATUS))

        gui.main.won = True
        for letter in gui.main.WORD:
            if letter not in gui.main.GUESSED:
                gui.main.won = False
                break

        if gui.main.won:
            print("You Won")
            break

        if HANGMAN_STATUS == 0:
            print("You lose")
            break

        print(f"All guesses: {gui.main.GUESSED}")
    print(f"The word was: {gui.main.WORD}")
