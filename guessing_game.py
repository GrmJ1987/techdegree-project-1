"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import sys


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """  
    # write your code inside this function.
    high_score = 100
    while True:
        answer = random.randint(1, 10)
        attempts = 1   
        name = input("What is your name?  ")
        guess = ""
        print("""
        Welcome {}. Today we're going to play a game.
        I will think about a number between 1 and 10. 
        You will try to guess it. Of course some additional
        help and hints will be provided. Best of luck!
        """.format(name))
        while guess != answer:
            try:
                guess = int(input("Please enter your guess: "))
                if guess < 1 or guess > 10:
                    raise ValueError("Only guesses with range (1-10) are allowed")
                    continue
            except ValueError as err:
                print("Oh no, we ran into an issue. {}. Please try again.".format(err))
                continue
            else:
                if guess > answer:
                    print("It's lower")
                    attempts += 1
                    continue
                if guess < answer:
                    print("It's higher")
                    attempts += 1
                    continue
            print("Got it! The number we were looking for was {}. It took you {} attempts to finish the game".format(answer, attempts))
            if attempts < high_score:
                high_score = attempts
            play_again = input("Well that was fun. I hope you enjoyed it too! Want to play again?  Y/N? ")
            if play_again.lower() == 'y':            
                print("The current best score: {} - {} attempts".format(name, high_score))
                continue
            else:
                print("Thanks for hanging with us today {}. Hope to see you soon.".format(name))
                sys.exit()    
# Kick off the program by calling the start_game function.
start_game()