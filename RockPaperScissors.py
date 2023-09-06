import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))


if player_choice < 0 and player_choice > 2:
  print("Invalid choice")
else:
  print("\nYou chose: ")
  
  if player_choice == 0:
    print("Rock")
    print(rock)
  elif player_choice == 1:
    print("Paper")
    print(paper)
  else:
    print("Scissors")
    print(scissors)

  print("\nComputer chooses ")
  computer_choice = random.randint(0,2)

  if computer_choice == 0:
    print("Rock")
    print(rock)
  elif computer_choice == 1:
    print("Paper")
    print(paper)
  else:
    print("Scissors")
    print(scissors)
    
  if player_choice == computer_choice:
    print("Tie")
  elif player_choice == 0 and computer_choice == 1:
    print("You loose")
  elif player_choice == 1 and computer_choice == 2:
    print("You loose")
  elif player_choice == 2 and computer_choice == 0:
    print("You loose")
  else:
    print("You win")