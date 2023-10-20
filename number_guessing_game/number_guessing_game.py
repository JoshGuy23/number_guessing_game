import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100!")

player_guess = 0
target_number = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 0
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives - 5
    
while player_guess != target_number and lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    if player_guess == target_number:
        print(f"You got it! The answer was {target_number}.")
    else:
        if player_guess > target_number:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again.")
        lives -= 1
        
    if lives == 0:
        print("You've run out of guesses, you lose.")