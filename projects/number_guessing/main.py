import random
import time

play_again = 'Y'
while play_again == 'Y':
    random_num = random.randrange(0, 5)
    user_guess = input("Guess the number: ")
    if user_guess == str(random_num):
        print(f"You guess it right the number was {random_num}")
    else:
        print(f"You guess it wrong the number was {random_num}")
        time.sleep(1)
    play_again = input("Play again [Y/N]: ")
