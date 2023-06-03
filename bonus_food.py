from turtle import Turtle
import random

class BonusFood(Turtle):
    def __init__(self):
        super().__init__()

    def show_bonus_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def bonus_refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)