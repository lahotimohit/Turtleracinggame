from turtle import Turtle, Screen
import random

is_raceon = False
colours = ["red", "orange", "yellow", "green", "blue","purple"]
yindex = [-75,-50,-25,0,25,50]
all_turtles = []

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color name: ")

for turtle_item in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_item])
    new_turtle.goto(x=-230, y=yindex[turtle_item])
    all_turtles.append(new_turtle)

if user_bet:
    is_raceon = True

while is_raceon:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_raceon = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You wins! The {winning_color} color turtle is the winner.")
            else:
                print(f"You lost the game. The {winning_color} color is the winner.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()