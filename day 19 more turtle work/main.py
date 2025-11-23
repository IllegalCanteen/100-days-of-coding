from turtle import Turtle,Screen

tim=Turtle()
screen = Screen()
def move_forwards():
    tim.setheading(0)
    tim.forward(10)
def move_backwards():
    tim.setheading(180)
    tim.forward(10)
def move_left():
    tim.setheading(90)
    tim.forward(10)
def move_right():
    tim.setheading(270)
    tim.forward(10)
def pen_up():
    tim.up()
def pen_down():
    tim.down()


screen.listen()
screen.onkey(key="d",fun=move_forwards)
screen.onkey(key="a",fun=move_backwards)
screen.onkey(key="s",fun=move_right)
screen.onkey(key="w",fun=move_left)
screen.onkey(key=" ",fun=pen_up)
screen.onkey(key=".",fun=pen_down)


screen.exitonclick()