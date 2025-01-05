from random import randint

from art import logo
print(logo)

from random import randint

def difficulty_of_game():
    global number_of_attempts
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        number_of_attempts = 10
    elif difficulty == "hard":
         number_of_attempts = 5
    else:
        print("Invalid choice. Defaulting to 'hard' difficulty.")
        number_of_attempts = 5

print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number 1 and 100.")

def proceed_game():
    global number_of_attempts
    while number_of_attempts > 0:
        guess = int(input("Make a guess:"))
        if guess < winning_number:
            number_of_attempts -= 1
            print ("Too low. Try again.")
        elif guess > winning_number:
            number_of_attempts -= 1
            print ("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number.")
            return

    if number_of_attempts == 0:
        print("You've run out of attempts. Game Over.")
        print(f"The correct number was {winning_number}.")
    else:
        print(f"You have {number_of_attempts} attempts remaining.")

winning_number = randint(1,100)
difficulty_of_game()
print(f"You have {number_of_attempts} attempts remaining to guess the number.")
proceed_game()

