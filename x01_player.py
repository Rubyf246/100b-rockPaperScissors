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
  choice = input("Enter your choice: ")
  value = " "
  if choice == "rock":
    value = 0
  elif choice == "paper":
    value = 1
  elif choice == "scissors":
    value = 2
  else: 
    print ("Enter a valid input; rock, paper or scissor")
  return value

if __name__ == "__main__":
  player = playerChoice()
  print(player)
