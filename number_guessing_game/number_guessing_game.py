import art
import random

print(art.logo)

player_guess = 0
target_number = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 0
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives - 5
    
