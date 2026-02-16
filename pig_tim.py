import random

def roll():
    max_dicno = 6
    min_dicno = 1
    roll = random.randint(min_dicno, max_dicno)
    return roll

while True:
    try:
        players = int(input('Enter the number of players: '))
        if 1 >= players or players > 4:
            print('Number of players cannot be less than 2 or more than 4')
            continue
        break
    except ValueError:
        print('Please enter a valid number.')
    