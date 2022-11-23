from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.initial_snake_size = 0
        self.snake_segments = []
        self.create_initial_snake()
        self.head = self.snake_segments[0]

    def create_initial_snake(self):
        for _ in range(3):
            self.create_snake()

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.snake_segments[0].forward(20)
        # self.snake_segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def increase_snake(self):
        self.create_snake()

    def create_snake(self):
        my_snake = Turtle(shape="square")
        my_snake.color("white")
        my_snake.penup()
        my_snake.setx(self.initial_snake_size)
        self.initial_snake_size -= 20
        self.snake_segments.append(my_snake)


