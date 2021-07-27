import colorgram
import turtle
import random

# Draw a Hirst painting

# extract colors from OIP picture to get the colors
colors = colorgram.extract('OIP.jpg', 255)
rgb_colors = []

# only extract RGB colors and safe them in rgb_colors
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# draw the paining
turtle.colormode(255)
artist = turtle.Turtle()
artist.penup()
artist.hideturtle()

for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        artist.dot(20, random.choice(rgb_colors))
        artist.goto(x,y)

screen = turtle.Screen()
screen.exitonclick()