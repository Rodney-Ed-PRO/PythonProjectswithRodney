# import random module
import random
# ASCII Art
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


# Ask the user if they want to choose rock, paper, or scissor
player_move = input("Rock, Paper, or Scissors? Type out your choice: ").lower()
# Create the randomly-generated computer move
rps = ["rock", "paper", "scissors"]
index = random.randint(0,2)
computer_move = rps[index]


if player_move == computer_move:
  print("It's a Draw!")
elif player_move == "scissors" and computer_move == "paper":
  print(f"Your Move:{scissors}\nComputer Move: {paper}.\nScissors beats Paper, You Win!")
elif player_move == "paper" and computer_move == "rock":
  print(f"Your Move:{paper}\nComputer Move: {rock}.\nPaper beats Rock, You Win!")
elif player_move == "rock" and computer_move == "scissors":
  print(f"Your Move:{rock}\nComputer Move: {scissors}. Rock beats Scissors, You Win!")
elif player_move == "scissors" and computer_move == "rock":
  print(f"You chose {player_move}\n{scissors} and the computer chose {computer_move}\n{rock}\n{computer_move} beats {player_move}!. The computer won!")
elif player_move == "rock" and computer_move == "paper":
  print(f"You chose {player_move}\n{rock} and the computer chose {computer_move}\n{paper}\n{computer_move} beats {player_move}!. The computer won!")
elif player_move == "paper" and computer_move == "scissors":
  print(f"You chose {player_move}\n{paper} and the computer chose {computer_move}\n{scissors}\n{computer_move} beats {player_move}. The computer won!")
else:
  print("You've typed an invalid move. Try again.")
