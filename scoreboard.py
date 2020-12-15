from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.score = 0
        self.hideturtle()
        self.write(f"Your score is {self.score}", move=False, align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.write(f"Your score is {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def clean(self):
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Arial", 24, "normal"))
