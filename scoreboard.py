from turtle import Turtle

ALIGN_BOARD = "center"
FONT_BOARD = ('Arial', 10, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGN_BOARD, font=FONT_BOARD)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN_BOARD, font=FONT_BOARD)

    def score_refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

