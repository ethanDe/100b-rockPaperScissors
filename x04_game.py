#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import *
from x02_computer import *
from x03_winner import *

if __name__ == "__main__":
  pass
while True:
  x = playerChoice()
  y = computerChoice()
  z = playerWins(y,x)

  if x == 0:
    if y == 0:
      print("tie")
    elif y == 1:
      print("win")
    elif y ==2:
      print("loss")
  elif x == 1:
    if y == 0:
      print("win")
    elif y == 1:
      print("tie")
    elif y == 2:
      print("loss")
  elif x == 2:
    if y == 0:
      print("loss")
    elif y== 1:
      print("win")
    elif y == 2:
      print("tie")