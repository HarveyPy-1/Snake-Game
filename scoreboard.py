from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.lives = 5
        self.color("white")
        self.penup()
        self.goto(-30, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.highscore}    Lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode= "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def increase_bonus_score(self):
        self.score += 5
        self.update_scoreboard()