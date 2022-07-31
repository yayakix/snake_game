from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import  Scoreboard

import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

food = Food()
scoreboard= Scoreboard()

snake = Snake()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_spot()
        scoreboard.add_one()


    # game_on = False


screen.exitonclick()