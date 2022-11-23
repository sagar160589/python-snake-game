from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Welcome to Snake Game")
is_game_on = True
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    snake.move()
    time.sleep(0.1)
    screen.update()
    #Detect collision with food. Distance method calculates distance between two turtle instances here snake and food
    if snake.head.distance(food) < 15:
        scoreboard.score_refresh()
        snake.increase_snake()
        food.refresh()

    #Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    #Detect collision with own tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()



screen.exitonclick()
