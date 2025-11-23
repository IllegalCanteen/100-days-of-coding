from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x=random.randrange(-280,280)
        random_y=random.randrange(-280,280)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        random_x=random.randrange(-280,280)
        random_y=random.randrange(-280,280)
        self.goto(random_x,random_y)