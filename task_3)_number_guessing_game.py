# -*- coding: utf-8 -*-
"""Task-3) Number_Guessing_Game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O8-l8pqGoQ8mKasKeTfyG3Dp7c3K712s
"""

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 5  # You can adjust this to change the number of attempts allowed

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number:", secret_number)
            break
        elif guess < secret_number:
            print("Try again! The number is higher.")
        else:
            print("Try again! The number is lower.")

        attempts += 1

    if attempts == max_attempts:
        print("Sorry, you've run out of attempts. The correct number was:", secret_number)

# Run the game
number_guessing_game()