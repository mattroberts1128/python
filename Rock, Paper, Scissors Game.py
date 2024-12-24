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
#rock beats scissors
#paper beats rock
#scisscors beats paper
import random
game_images = [rock, paper, scissors]

print("Rock, Paper, Scissors?")
player_number_1 = int(input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
if player_number_1 >= 0 and player_number_1 <= 2:
    print(game_images[player_number_1])

computer_choice = random.randint(0, 2)
print(f"The Computer chose:")
print(game_images[computer_choice])

rock_paper_scissors = ["Rock", "Paper", "Scissors"]
if player_number_1 >= 3 or player_number_1 < 0:
    print("The input was invalid. You lose!")
elif player_number_1 == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and player_number_1 == 2:
    print("You Lose!")
elif computer_choice > player_number_1:
    print("You Lose!")
elif player_number_1 >computer_choice:
    print("You Win!")
elif player_number_1 == computer_choice:
    print("Draw!")
