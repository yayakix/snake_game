from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.x_cor = 0
        self.generate()
        self.head = self.all_turtles[0]
    def generate(self):
        for x in range(3):
            newsquare = Turtle(shape='square')
            newsquare.color('white')
            newsquare.penup()
            newsquare.goto(self.x_cor, 0)
            self.all_turtles.append(newsquare)
            self.x_cor -= 20
    def add_segment(self,position):
        newsquare = Turtle(shape='square')
        newsquare.color('white')
        newsquare.penup()
        newsquare.goto(position)
        self.all_turtles.append(newsquare)

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    def move(self):
        for x in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[x - 1].xcor()
            new_y = self.all_turtles[x - 1].ycor()
            self.all_turtles[x].goto(new_x, new_y)
        self.all_turtles[0].forward(20)



