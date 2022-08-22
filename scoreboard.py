from turtle import Turtle

with open("data.txt") as file:
    saved_hs = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = saved_hs
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def add_one(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode='w') as addfile:
                # addfile.write(self.highscore)
                addfile.write(str(self.highscore))
        self.clear()
        self.write(f'Score: {self.score} Highscore: {self.highscore}', align='center', font=('Arial', 24, 'normal'))

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

