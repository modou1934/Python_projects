import turtle
import time
import random

WIDTH, HEIGHT = 500,500
COLORS = ["red","green","blue","orange","purple","brown","pink","gray","gold","cyan"]

def number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Invalid number of racers!")
                continue
        else:
            print("Please enter a number!")
            continue

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")
    screen.bgcolor("lightblue")



racers = number_of_racers()
init_turtle()
random.shuffle(COLORS)
random_color = COLORS[:racers]
racer = turtle.Turtle()
racer.speed(1)
racer.penup()
racer.shape("turtle")
racer.color(random_color[0])
racer.forward(90)
racer.left(90)
racer.forward(90)
racer.left(90)
racer.pendown()
racer.forward(90)
racer.left(90)
racer.forward(90)

time.sleep(5)

print(racers)
