import random
print('Welcome to the number guessing game. You will choose a number then a random number will be generated between zero and the number you chose')
print('Lets see how many guesses will it take you to get the number')

no_of_gues = 1

# def run_game():
#     max_no = input(int('Enter any number that will be the upper limit: '))
#     numb = random.randint(0, max_no)
    # while True:
    #     gues_no = input(int('Alright try to guess the generated number: '))
    #     if numb == gues_no:
    #         print('Correct')
    #         return 'correct'
    #     else: 
    #         print('incorrect try again')
    #         no_of_gues += 1
    #         return gues_no - numb, no_of_gues
            
# dete = run_game[0]
# fin_no_gues = run_game[1]

while True:

    play = input('type start to play: ').lower()
    if play == 'start':
        print('Enter difficulty level')
        diff = input('1. Easy\n2. Hard\n').lower()
        if diff == 'easy':
            try:
                max_no = int(input('Enter any number that will be the upper limit: '))
                numb = random.randint(0, max_no)
                no_of_gues = 1
                gues_no = int(input('Alright try to guess the generated number: '))
                while True:
                    try:
                        if numb == gues_no:
                            print('Correct answer after ', no_of_gues, 'gueses')
                            break
                        elif gues_no > numb: 
                                 print('Incorrect the correct number is smaller: ')
                                 no_of_gues += 1
                                 gues_no = int(input('Please try again: '))
                                 continue

                        if gues_no < numb:
                            print('Incorrect the correct number is larger.')
                            no_of_gues += 1
                            gues_no = int(input('Please try again: '))
                            continue
                    except ValueError:
                         print('Please enter a valid number. ')
                        
            except ValueError: 
                 print('Invalid upper limit. Please enter a valid number. ')
                 continue
            
        if diff == 'hard':
                max_no = int(input('Enter any number that will be the upper limit: '))
                numb = random.randint(0, max_no)
                no_of_gues = 1 
                gues_no = int(input('Alright try to guess the generated number: '))
                while True:
                    if gues_no == numb:
                        print('Correct answer after ', no_of_gues, 'gueses')
                        break
                    else: 
                        print('Incorrect guess')
                        no_of_gues += 1   
                        gues_no = int(input('Please try again: '))
                        continue

    else: quit()        
            




