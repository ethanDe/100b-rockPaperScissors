#! python3

"""
Create a function that asks the player for their choice
The function should return:
  rock     : 0
  paper    : 1
  scissors : 2

```
Sample Run:
Enter your choice:
rock

Output: 0
"""

def playerChoice():
  x = str(input("Rock, Paper, Scissors: ")) #input
  if x == "Rock" or x == "rock": #rock
    x = 0
  elif x== "Paper" or x == "paper": #paper
    x = 1
  elif x == "Scissors" or x == "scissors": #scissors
    x = 2
  else: #fault
    x = "Invalid"
  return x #output
  
  '''
  No input parameters needed.
  Function should ask the players to make their choice.  How you ask is unimportant, but the
  output must be consistent:
  0: rock
  1: paper
  2: scissors
  '''
  return value


if __name__ == "__main__":
  player = playerChoice()
  print(player)
