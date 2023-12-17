from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def choose_mode():
    mode_choice = screen.textinput("Select a mode.", "Type 'easy', 'medium', or 'hard': ").lower()
    if mode_choice == "hard":
        snake.game_mode = "fastest"
    elif mode_choice == "medium":
        snake.game_mode = "fast"
    for s in snake.snake_body:
        s.speed = snake.game_mode


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
choose_mode()

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

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.update()
        scoreboard.add_point()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
