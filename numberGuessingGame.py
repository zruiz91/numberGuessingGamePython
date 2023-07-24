#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


# def choose_difficulty():
#   difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#   if difficulty_level == "easy":
#     guesses = 10
#   elif difficulty_level == "hard":
#     guesses = 5
#   else:
#     print("Invalid input")

from art import logo
import random
target_number = random.randint(1, 100)
guesses = 0
game_over = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"Pssst, the correct answer is {target_number}")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
  guesses = 10
elif difficulty_level == "hard":
  guesses = 5
else:
  print("Invalid input")

while game_over == False:
  if guesses != 0:
    print(f"You have {guesses} attempts remaining to guess the number.")
    new_guess = int(input("Make a guess: "))

    if new_guess > target_number:
      guesses -= 1
      print("Too High")
      print("Guess Again")
    elif new_guess < target_number:
      guesses -= 1
      print("Too Low")
      print("Guess Again")
    else:
      print(f"You got it! The answer was {target_number}.")
      game_over = True

  else:
    print("You've run out of guesses, you lose.")
    game_over = True

    