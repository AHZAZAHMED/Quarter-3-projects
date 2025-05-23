# -*- coding: utf-8 -*-
"""Guess_the_number_game_python_project(user).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15NtsyT9-acvk9T4pUY1JwczEzW3aRTwf
"""

import random

def computer_guess(lower_limit, upper_limit):
  feedback = ''
  print(f"Guess the number between {lower_limit} and {upper_limit}.")

  while feedback != 'c':
    guess = random.randint(lower_limit , upper_limit)
    feedback = input(f"Is {guess} too high (H) , too low (L) or correct (c)?").lower()
    if feedback == 'h':
      upper_limit = guess - 1
    elif feedback == "l":
      lower_limit = guess + 1

  print(f"Computer guess the number {guess} correctly")

def main():
    lower_limit = int(input("Enter the lower limit:"))
    upper_limit = int(input("Enter the upper limit: "))
    computer_guess(lower_limit, upper_limit)

if __name__ == '__main__':
  main()