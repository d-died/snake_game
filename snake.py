from turtle import Turtle

X_COORDS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.whole_snake = []
        self.create_snake()

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.whole_snake.append(snake_segment)

    def create_snake(self):
        for position in X_COORDS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.whole_snake[-1].position())

    def move(self):
        for snake_seg in range(len(self.whole_snake) - 1, 0, -1):
            new_x = self.whole_snake[snake_seg - 1].xcor()
            new_y = self.whole_snake[snake_seg - 1].ycor()
            self.whole_snake[snake_seg].goto(new_x, new_y)
        self.whole_snake[0].forward(20)

    def up(self):
        if self.whole_snake[0].heading() != DOWN:
            self.whole_snake[0].setheading(UP)

    def down(self):
        if self.whole_snake[0].heading() != UP:
            self.whole_snake[0].setheading(DOWN)

    def left(self):
        if self.whole_snake[0].heading() != RIGHT:
            self.whole_snake[0].setheading(LEFT)

    def right(self):
        if self.whole_snake[0].heading() != LEFT:
            self.whole_snake[0].setheading(RIGHT)
