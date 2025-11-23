from turtle import Turtle,Screen
screen = Screen()
starting_positions=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in starting_positions:
            self.add_square(position)

    def add_square(self,position):
        square = Turtle("square")
        square.penup()
        square.color("white")
        square.goto(position)
        self.segments.append(square)
    def extend_snake(self):
        self.add_square(self.segments[-1].position())

    def move(self):
            for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(x=new_x, y=new_y)
            self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)


