# project PIG is a multiplayer game where 2 or more ppl play in turn 
# and roll the dice the can keep rolling the dice however times they like however if the get a one all the scores accumulated 
# will be automatically converted to a zero

import random 

print('Welcome to the PIG game roll the dice how many times you like \nbut if you get a one score in that round will be zero')
while True:
    try:
        begin = input('Input start to play and quit to exit the game at any time: ').lower()
    except ValueError:
        print('Please type either start or quit')
        continue
    if begin == 'quit':
        break
    

    while True:
        try:
            max_score = int(input('Choose the maximum score. First to reach it wins: '))
        except ValueError:
            print('Please enter a valid number')
            continue
        
        comp_score = 0
        user_score = 0

        while comp_score <= max_score and user_score <= max_score:

            usero_score = 0
            compro_score = 0
            comp_score += compro_score
            user_score += usero_score


            try:
                user_inp = input('Its your turn press r to roll: ').lower()
                if user_inp == 'r':
                    user_roll = random.randint(1,6)
                    print('You got a', user_roll)
                elif user_inp == 'q':
                    quit
                    if user_roll == 1:
                        print('You got a one on your first try damn! Its my turn now')
                        user_roll = 0
                    else:            
                        while True:
                            usero_score += user_roll
                            try:
                                us_inp = input('Press r to roll again and q to stop and add your score: ').lower()
                                if us_inp == 'r':
                                    user_roll =  random.randint(1,6)

                                    if user_roll == 1:
                                        usro_score = 0
                                        print('it was a One your total score is', user_score)
                                        break

                                    else:
                                        print('You got a', user_roll)
                                        continue
                                while True:
                                    if us_inp ==  'q':
                                        print('Your total score right now is', user_score)
                                        print('I will roll now.')
                                        comp_roll = random.randint(1,6)
                                        print('I got a', user_roll)
                                        if comp_roll == 1:
                                            print('I got a one. Its your turn to roll now.')
                                            comp_roll = 0
                                            break
                                        comp_choice = random.randint(0,2)
                                        if comp_choice == 0 or 2:
                                            print('I choose to roll again')
                                            comp_roll += random.randint(1,6)
                                        compro_score += comp_roll

                                

                                continue     

                                    
                            except ValueError:
                                print('Please enter either r or q')
            except ValueError:
                print('Please enter either r or q')

