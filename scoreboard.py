from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def add_one(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def reset_score(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 24, 'normal'))

