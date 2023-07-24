#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

  
from art import logo
import random



def decide_difficulty():
  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty_level == "easy":
    return 10
  elif difficulty_level == "hard":
    return 5
  else:
    print("Invalid input")
    decide_difficulty(difficulty_level)

def check_guess(new_guess, target_number, guesses):

    if new_guess > target_number:
      print("Too High")
      return guesses - 1
    elif new_guess < target_number:
      print("Too Low")
      return guesses - 1
    else:
      print(f"You got it! The answer was {target_number}.")


  
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  target_number = random.randint(1, 100)
  print(f"Pssst, the correct answer is {target_number}")
  
  
  
  guesses = decide_difficulty()
  
  new_guess = 0
  
  
  while new_guess != target_number:
      print(f"You have {guesses} attempts remaining to guess the number.")
      new_guess = int(input("Make a guess: "))

      guesses = check_guess(new_guess, target_number, guesses)

      if guesses == 0:
        print("You've run out of guesses, you lose.")
        return
      elif new_guess != target_number:
        print("Guess Again")
      
game()