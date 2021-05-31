import random

number = random.randint(1,6)

guess = int(input("Guess the dice roll: "))

if guess == number:
    print("Correct! They rolled a " + str(number))
else:
    print("Wrong! They rolled a " + str(number))
