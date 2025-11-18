from turtle import Turtle,Screen

tom=Turtle()
screen=Screen()
tom.teleport(-250,0)
for i in range(25):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()
screen.exitonclick()