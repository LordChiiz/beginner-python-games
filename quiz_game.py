#A very simple quiz game
score = 0
questions = 5

print('Welcome to the quiz')
playing = input('Are you ready to play? ').lower()
if playing != "yes":
    quit()

answer = input('Full meaning of CPU? ').lower()
if answer == 'central processing unit':
    score += 1
    print('correct')
else:
    print('incorrect')


answer = input('Full meaning of RAM? ').lower()
if answer == 'random access memory':
    score += 1
    print('correct')
else:
    print('incorrect')


answer = input('Full meaning of GPU? ').lower()
if answer == 'graphics processing unit':
    score += 1
    print('correct')
else:
    print('incorrect')


answer = input('Full meaning of PSU? ').lower()
if answer == 'power supply unit':
    score += 1
    print('correct')
else:
    print('incorrect')

answer = input('Full meaning of ALU? ').lower()
if answer == 'arithmetic logic unit':
    score += 1   
    print('correct')
else:
    print('incorrect')
  

print(str(score) + '/' + str(questions))