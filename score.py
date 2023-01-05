from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 48, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


