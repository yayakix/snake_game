from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('orange')
        self.speed('fast')
        self.new_spot()
    def new_spot(self):
        random_spot = random.randint(-270, 270)
        self.goto(random_spot, random_spot)

