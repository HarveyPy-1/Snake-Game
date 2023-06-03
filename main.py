from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from bonus_food import BonusFood
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Harvey Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
bonus_food = BonusFood()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on and scoreboard.lives > 0:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # When bonus ball appears
    when_to_appear = random.randint(0, 100)
    if when_to_appear == 1:
        bonus_food.showturtle()
        bonus_food.show_bonus_food()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    elif snake.head.distance(bonus_food) < 15:
        snake.extend()
        bonus_food.hideturtle()
        scoreboard.increase_bonus_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
scoreboard.game_over()


screen.exitonclick()

