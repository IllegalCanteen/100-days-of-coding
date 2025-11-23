from turtle import Screen
import time
from snake import Snake
from snake_game.food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(" My Snake Game",)
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
#recognise what movements each key does to a snake
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun= snake.right)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.new_score()
        snake.extend_snake()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on=False
    #Detect collision with Tail,
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
                game_is_on=False
                scoreboard.game_over()




screen.exitonclick()