from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    if snake.whole_snake[0].distance(food) < 15:
        food.new_food()
        scoreboard.eat_food()
        snake.extend()

    if snake.whole_snake[0].xcor() > 280 or snake.whole_snake[0].ycor() > 280 or snake.whole_snake[0].xcor() < -280 or snake.whole_snake[0].ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.whole_snake[1:]:
        if snake.whole_snake[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()