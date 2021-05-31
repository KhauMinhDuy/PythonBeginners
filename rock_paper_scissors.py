import random

computer = random.choice(['rock', 'paper', 'scissors'])

user = input('Do you want - Rock, Paper, Scissors: ')

if user == computer:
    print("TIE")
elif user == 'rock' and computer == 'scissors':
    print('WIN, the computer had ' + computer)
elif user == 'paper' and computer == 'rock':
    print("WIN, the computer had " + computer)
elif user == 'scissors' and computer == 'paper':
    print("WIN, the computer had " + computer)
else:
    print("Lose")
