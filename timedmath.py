# Random simple math problems will be generated for you. lets see how long it will take you to solve them. Watch out for version 2.0 :)

import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEM = 10

def generate_problem():
    leftval = random.randint(MIN_OPERAND, MAX_OPERAND)
    rightval = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(leftval) +" " + operator +" " +  str(rightval)
    answer = eval(expr)
    return expr, answer

wrong = 0
input('Press any key to start the challenge')
print('------------------------------------------------------')

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr, answer = generate_problem()
    while True:
        playans = input('Problem #' + str(i + 1) + ': ' + expr + ': ')
        if playans == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print('------------------------------------------------------')
print('Weldone. You finished the test in ', int(total_time), 'seconds')