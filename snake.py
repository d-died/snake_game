from turtle import Turtle

X_COORDS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.whole_snake = []
        self.create_snake()

    def create_snake(self):
        for each in X_COORDS:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(each)
            self.whole_snake.append(snake_segment)

    def move(self):
        for snake_seg in range(len(self.whole_snake) - 1, 0, -1):
            new_x = self.whole_snake[snake_seg - 1].xcor()
            new_y = self.whole_snake[snake_seg - 1].ycor()
            self.whole_snake[snake_seg].goto(new_x, new_y)
        self.whole_snake[0].forward(20)