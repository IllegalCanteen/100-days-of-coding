import random
import turtle
from turtle import Turtle, Screen


tommy = Turtle()
screen = Screen()
turtle.colormode(255)
def pick_a_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return  random_color
tommy.speed("fastest")
tilt=0
while tilt <=360:
    color=pick_a_color()
    tommy.color(color)
    tommy.circle(100)
    tommy.left(1)
    tilt+=1
screen.exitonclick()
