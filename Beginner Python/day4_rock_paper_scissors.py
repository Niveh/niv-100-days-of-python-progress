import random

draw_rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

draw_paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

draw_scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
moves = [draw_rock, draw_paper, draw_scissors]
ROCK = 1
PAPER = 2
SCISSORS = 3

player_move = int(input(
    "What do you choose?\nType 1 for Rock.\nType 2 for Paper.\nType 3 for Scissors.\n"))

if player_move < 1 or player_move > 3:
    print("Invalid move! Game will now exit...")
    exit()

computer_move = random.randint(1, 3)

print(f"You chose:\n{moves[player_move - 1]}")
print(f"Computer chose:\n{moves[computer_move - 1]}")

if player_move == computer_move:
    print("It's a tie!")
    exit()

if player_move == ROCK:
    if computer_move == PAPER:
        print("You lose!")
    elif computer_move == SCISSORS:
        print("You win!")

elif player_move == PAPER:
    if computer_move == SCISSORS:
        print("You lose!")
    elif computer_move == ROCK:
        print("You win!")

elif player_move == SCISSORS:
    if computer_move == ROCK:
        print("You lose!")
    elif computer_move == PAPER:
        print("You win!")
