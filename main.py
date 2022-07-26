from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

whole_snake = []
x_coords = [(0, 0), (-20, 0), (-40, 0)]

for each in x_coords:
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(each)
    whole_snake.append(snake_segment)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    for snake_seg in range(len(whole_snake)-1, 0, -1):
        new_x = whole_snake[snake_seg - 1].xcor()
        new_y = whole_snake[snake_seg - 1].ycor()
        whole_snake[snake_seg].goto(new_x, new_y)
    whole_snake[0].forward(20)
    whole_snake[0].left(90)
    # game_on = False




screen.exitonclick()