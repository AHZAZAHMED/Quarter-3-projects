# -*- coding: utf-8 -*-
"""Countdown_Timer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x3jy88gDwc9J498vypKQCQg0cj8scn6q
"""

import time
import sys

def countdown(time_in_secs):
  while time_in_secs > 0:
      mins , secs = divmod(time_in_secs , 60)
      timer = '{:02d}:{:02d}'.format(mins , secs)
      sys.stdout.write('\r' + timer)
      sys.stdout.flush()
      time.sleep(1)
      time_in_secs -= 1
  print("\n")
  print("Timer completed")

time_in_secs = input("Enter the time in seconds: ")

if time_in_secs.isdigit():
  time_in_secs = int(time_in_secs)
  countdown(time_in_secs)
else:
  print("Invalid input")