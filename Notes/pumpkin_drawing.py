
# Pumpkin Drawing
# Author:
# Date: 31 October 2023


import time
import turtle

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(1000)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin

# Nose
carver.penup()
carver.setposition(50, 6)
carver.dot(50)
carver.forward(150)

turtle.done()
