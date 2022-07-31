from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.x_cor = 0
        self.generate()
    def generate(self):
        for x in range(3):
            newsquare = Turtle(shape='square')
            newsquare.color('white')
            newsquare.penup()
            newsquare.goto(self.x_cor, 0)
            self.all_turtles.append(newsquare)
            self.x_cor -= 20
    def up(self):
        self.all_turtles[0].setheading(90)
    def down(self):
        self.all_turtles[0].setheading(270)

    def left(self):
        self.all_turtles[0].setheading(180)

    def right(self):
        self.all_turtles[0].setheading(0)


    def move(self):
        for x in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[x - 1].xcor()
            new_y = self.all_turtles[x - 1].ycor()
            self.all_turtles[x].goto(new_x, new_y)
        self.all_turtles[0].forward(20)

