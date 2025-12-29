import turtle

WIDTH, HEIGHT = 500,500


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
print(racers)
