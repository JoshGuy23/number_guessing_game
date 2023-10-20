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
    