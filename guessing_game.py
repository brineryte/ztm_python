import random
import sys

try:
    start = sys.argv[1] or 1
except:
    start = 1
    print(f"Updating starting number to a positive integer: {start}.")
try:
    stop = sys.argv[2] or 10
except:
    stop = start + 10
    print(f"Updating stopping number to a positive integer: {stop}.")

if int(start) < 0:
    start = 1
    print(f"Updating starting number to a positive integer: {start}.")
if int(stop) < 0:
    stop = int(start) + 10
    print(f"Updating stopping number to a positive integer: {stop}.")

number = random.randint(int(start), int(stop))

print()
print("Welcome to the guessing game!")
print(f"I'm thinking of a number between {start} and {stop}, try and guess it!")
print()

guess = None
while guess != number and guess != -1:
    guess = int(input("Please enter a guess! (-1 to quit): "))

print(
    "Congratulations, you got it!" if guess == number else f"Sorry to see you go, try again next time! P.S. It was {number}")
