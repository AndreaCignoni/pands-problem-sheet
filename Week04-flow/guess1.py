# guess1.py
# this program prompts the user to guess a number until he gets the right on
# Author: Andrea Cignoni

numberToGuess = 30

guess = int (input("Please guess the number: "))
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)