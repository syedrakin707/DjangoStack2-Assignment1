import random
import math

if __name__ == '__main__':
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100")
    chosen_number = math.ceil(100*(random.random()))
    attempts = 0
    guess = False
    while not guess:
        attempts += 1
        try:
            guessed_number = int(input("Enter your guess: "))
            if guessed_number > chosen_number:
                print("Too High!")
            elif guessed_number < chosen_number:
                print("Too Low!")
            elif guessed_number == chosen_number:
                print("Congratulations! You've guessed the number in {} attempts".format(attempts))
                guess = True
                continue
        except ValueError:
            print("Not a Number")






