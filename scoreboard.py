# create scoreboard at the top-center, increase and update score, show game-over at the center when game finished.
from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            # keep track of high score even after closing game.
            try:
                self.high_score = int(data.read())
            except ValueError:  # if data file is empty, start with 0
                self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()    # clear() stops overwriting on current score, turtle method : write(text, align, font)
        self.write(arg=f"Score: {self.score} | High Hcore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def restart_game(self):
        # section added to keep track of high score
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                # python write method to update high score if it's less than the current score.
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = 0  # live score start with 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
