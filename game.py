"""A number-guessing game."""

import random

def guessing(low=1, high=100):
    """plays a number guessing game.
Asks the player to identify themselevs and make a series of guesses as to 
which integer between 1-100 (or bewteen optional parameters) was generated .
Tells player if the guess is high or low or correct and how mnay guesses it took."""

    name = input ("Howdy, what's your name? ")
    print( f"{name}, I'm thinking of a number between {low} and {high}.")
    print ("Try to guess my number.")
    best_scores = None


    while True:
        count = 0
        guess = 0
        num = random.randint(low, high)
    
        while guess != num:
            try:
                guess = int(input("Your guess? "))
                count += 1
            except:
                print("Error")
                continue

            print (f"{guess}?")

            if guess < num:
                print("Your guess is too low, try again. ")
            if  guess > num:
                print("Your guess is too high, try again. ")
    
        print(f"Well done {name}! You found my number in {count} tries!")
        if best_score== None or best_score > count:
            best_score = count
        print(f"Your best score is {best_score}.")
        ask= input("Do you want to play again? y/n")
        if ask == 'n':
            return best_score

guessing()

