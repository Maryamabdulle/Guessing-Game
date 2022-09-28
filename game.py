"""A number-guessing game."""

from mimetypes import guess_all_extensions
import random
number = random.randint (1, 100)
# print("Howdy, what's your name? ")
name= input ("Howdy, what's your name? ")
print( f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

number_of_guesses = 0

while True:
    guess = int (input ("Your guess: "))

    if guess < number:
        print("Your guess is too low, try again.")
        number_of_guesses +=1 
    if  guess > number:
        print( "Your guess is too high, try again.")
        number_of_guesses +=1 

    if guess == number:
     
        print(f"Well done {name}! You found my number in {number_of_guesses} tries!")
        break





# Put your code here
