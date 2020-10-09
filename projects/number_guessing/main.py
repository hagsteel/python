import random

play_again = 'y'
while play_again == 'y':
    random_num = random.randrange(0, 5)
    user_guess = input("Guess the number: ")
    if user_guess == str(random_num):
        print(f"You guess it right the number was {random_num}")
    else:
        print(f"You guess it wrong the number was {random_num}")
    play_again = input("Play again [Y/N]: ").lower()
