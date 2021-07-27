from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

race_on = False
user_bet = screen.textinput(title="Color", prompt="Which turtle (color) will win? Possible answers: red/orange/yellow/green/blue/purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# create multiple turtles (based on the colors list), and align them on the left side
y = -100
for turtles in range(0, 6):
    # turtle_names = 'turtle' + str(turtles)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

# let the turtles race
# for every loop the turtles are moved forward a random distance
while race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        # the first turtle that reaches the end stops the race
        if turtle.xcor() > 230:
            race_on = False
            if turtle.pencolor() == user_bet:
                print(f"Well done. You were right. {turtle.pencolor()} won.")
            else:
                print(f"You were wrong. {turtle.pencolor()} won, not {user_bet}.")


screen.exitonclick()
