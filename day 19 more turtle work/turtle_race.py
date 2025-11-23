import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="Make a bet", prompt="Which turtle do you think will win the race?").lower()
colors=["red","orange","yellow","green","blue","indigo","purple"]
turtles=["a","b","c","d","e","f","g"]
y_position=-150
for i in range(0,7):
    turtles[i]=Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230,y=y_position)
    y_position += 50
if user_bet in colors:
    is_race_on = True
else:
    print("Not a valid color")
while is_race_on:
  for i in range(0,7):
        if turtles[i].xcor() > 230:
            if user_bet==turtles[i].pencolor():
                print(f"You win the {turtles[i].pencolor()} turtle has won!")
                is_race_on = False

            else:
                print(f"You lose the {turtles[i].pencolor()} turtle has won! ")
                is_race_on = False

        else:
            rand_dist=random.randint(1,10)
            turtles[i].forward(rand_dist)


screen.exitonclick()
