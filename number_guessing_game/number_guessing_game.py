import art      # Imports ASCII art for the logo
import random   # Imports random module to generate random number.

# Display ASCII logo and the intro.
def intro():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100!")

# If the player got the guess right, display a congratulatory message.
# Otherwise, display the appropriate feedback and subtract a life from the player.
def check_answer(guess, answer, lives):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
    else:
        if guess > answer:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again.")
        lives -= 1
    return lives

# Get the user to choose a difficulty and give them the appropriate number of guesses.
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = 0
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    return lives
    
def game():
    intro()
    # Set the initial guess to 0, and randomly generate the number to guess.
    player_guess = 0
    target_number = random.randint(1,100)
    # Get the user to choose a difficulty and give them the appropriate number of guesses.
    lives = set_difficulty()
    # The game goes on until the player correctly guesses the number or runs out of lives.
    while player_guess != target_number and lives > 0:
        # Display the number of guesses remaining.
        print(f"You have {lives} attempts remaining to guess the number.")
        # Get the user to guess the number.
        player_guess = int(input("Make a guess: "))
    
        # If the player got the guess right, display a congratulatory message.
        # Otherwise, display the appropriate feedback and subtract a life from the player.
        lives = check_answer(player_guess, target_number, lives)
     
        # If the player ran out of lives, give a game over message and display the number they were supposed to guess.
        if lives == 0:
            print(f"You've run out of guesses, you lose. The answer was {target_number}.")
            
game()