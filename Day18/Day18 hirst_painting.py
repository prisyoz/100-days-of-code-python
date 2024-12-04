import colorgram
import turtle as turtle_module
import random

# List to store tuples
colour_list = []

# Extract colours 
colours = colorgram.extract('hirst_dots.jpg', 30)

def colour_extract(colour):
    rgb = colour.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b

    colour_tuple = (red, green, blue)
    return colour_tuple

for line in colours:
    extracted_colour = colour_extract(line)
    colour_list.append(extracted_colour)

turtle_module.colormode(255)
timmy = turtle_module.Turtle()

timmy.penup()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
timmy.speed("fastest")
timmy.hideturtle()
number_of_dots = 50

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(colour_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        # Set a new line
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()