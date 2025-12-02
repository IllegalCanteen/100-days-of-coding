from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        with open("data.txt") as file:
            contents= file.read()
            self.highscore=int(contents)
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT )
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.update_score()

    def new_score(self):
        self.score += 1
        self.update_score()