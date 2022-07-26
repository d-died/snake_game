from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # game_on = False




screen.exitonclick()