import random
import sys


def evaluateGuess(guess, number):
    if guess == number:
        print("Congratulations, you got it!")
        return True
    else:
        print("Try again!")

    return False


def setupStartAndStop():
    try:
        start = sys.argv[1]
    except:
        start = 1
        print(f"Updating starting number to a positive integer: {start}.")
    try:
        stop = sys.argv[2]
    except:
        stop = start + 10
        print(f"Updating stopping number to a positive integer: {stop}.")

    if int(start) < 0:
        start = 1
        print(f"Updating starting number to a positive integer: {start}.")
    if int(stop) < 0:
        stop = int(start) + 10
        print(f"Updating stopping number to a positive integer: {stop}.")
    return start, stop


def promptUser(start, stop):
    print()
    print("Welcome to the guessing game!")
    print(f"I'm thinking of a number between {start} and {stop}, try and guess it!")
    print()


def main():
    start, stop = setupStartAndStop()
    promptUser(start, stop)
    number = random.randint(int(start), int(stop))

    while True:
        guess = int(input("Please enter a guess! (-1 to quit): "))

        if evaluateGuess(guess, number):
            break

        if guess == -1:
            print(f"Sorry to see you go, try again next time! P.S. It was {number}")
            break


if __name__ == '__main__':
    main()
