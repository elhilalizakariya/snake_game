from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_count = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_count.count()

    # Detect collision with wall.
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < - 280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        score_count.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score_count.reset()
            snake.reset()





screen.exitonclick()