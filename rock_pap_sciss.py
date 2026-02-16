# You think you can beat me in rock paper scissors? Lets find out. You can choose to play as many rounds as you like and you can also 
# quit at any time and your final score will be displayed. Lets play :)
import random

user_wins = 0
comp_wins = 0
rounds = 0


welcome = input('Welcome to rock paper scissors game\nYou can type "quit" to stop playing at any time and your final results will be displayed.\nType "Start" to play: ').lower()

win_pair = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
no_rounds = 0

choices = ['rock', 'paper', 'scissors']
if welcome == 'start':
    while True:
        try:
            numb_round = int(input('How many rounds will you like to play: '))
            break
        except ValueError:
            print('Please enter a valid number')

    while True:
        try:
            user_input = input('Choose between rock, paper and scissors: ').lower()
            if (user_input == 'quit'):
                print('Your score was', user_wins, 'while my score was', comp_wins, 'in', no_rounds, 'rounds.')
                break
            comp_rand = random.choice(choices)
            no_rounds += 1
            if (no_rounds == numb_round):
                print('Your score was', user_wins, 'while my score was', comp_wins, 'in', no_rounds, 'rounds.')
                break

            if comp_rand == user_input:
                print('It was a tie guess again')
            elif win_pair[user_input] == comp_rand:
                print('You win')
                user_wins += 1
            else:
                print('I win, I chose', comp_rand)
                comp_wins += 1
        except KeyError:
            print('Please choose between rock paper and scissors')
            no_rounds -= 1
            continue

        
