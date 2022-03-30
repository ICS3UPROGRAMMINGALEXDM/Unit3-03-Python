#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/30/2022
# Description: This program generates a random number that
# the user must guess correctly to win the game

import math
import random
import sys


def main():
    # loop to run the game again if user responds yes
    while True:

        # Creating the random number
        r_num = random.randint(1, 15)
        print(
            "I just generated a random number between 1-15. Can you Guess it correctly?"
        )
        print(r_num)

        # Loop allows user to keep guessing until they get it right
        while True:
            u_num = int(input("Input your number below:\n"))

            # Comparing user number with random number
            if u_num == r_num:
                print("Congratulations, you guessed the number correctly!!")
                answer = input("Would you like to play again? (y/n):").strip().lower()

                # what to do with user answer
                if answer == "y":
                    print("Okay")
                    break
                else:
                    print("Okay")
                    # Ends program
                    sys.exit()

            else:
                print("Uh oh, wrong answer. Guess again!")


if __name__ == "__main__":
    main()
