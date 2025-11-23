from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()
def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def clock_wise():
    tim.right(10)
    tim.forward(10)

def anticlockwise():
    tim.left(10)
    tim.forward(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w",fun=forward)
screen.onkey(key="s",fun=backward)
screen.onkey(key="d",fun=clock_wise)
screen.onkey(key="a",fun=anticlockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
