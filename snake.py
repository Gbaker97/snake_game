from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.game_mode = "normal"
        self.create_snake()
        self.head = self.snake_body[0]
        self.end = self.snake_body[-1]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.speed(self.game_mode)
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.end.position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
