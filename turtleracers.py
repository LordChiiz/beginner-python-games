# Watch turtles race towards the finish line. 

import turtle
import time
import random

WIDTH, HEIGHT, = 500, 500
COLORS = ['red', 'green', 'orange', 'yellow', 'blue', 'black', 'purple', 'pink', 'cyan', 'brown' ]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit:
            racers = int(racers)
            if racers < 2 or racers > 10:
                print("Please enter a number between 2 and 10")
            else:
                return racers
        else:
            print('Please enter a valid number and try again')
            continue

def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]



def init_race():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')

def create_turtle(colors):
    turtles = []
    space_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup() 
        racer.setpos(-WIDTH//2 + (i + 1)*space_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer) 

    return turtles



racers = get_number_of_racers()
init_race()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"{winner} racer won the race")
time.sleep(5)

