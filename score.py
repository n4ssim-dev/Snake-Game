import turtle
from art import GAME_OVER_ART

class Score:
    def __init__(self):
        self.score = 0
        self.write_score()

    def refresh_score(self):
        self.score += 1
        turtle.clear()
        self.write_score()

    def write_score(self):
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(0, 270)
        turtle.color("white")
        turtle.write(f"Score: {self.score}",align="center",font=("Arial", 18, "bold"))

    def is_lost(self):
        screen = turtle.Screen()
        screen.clear()
        screen.bgcolor("black")
        screen.tracer(0)
        turtle.penup()
        turtle.goto(0, -100)
        turtle.color("red")
        turtle.write(GAME_OVER_ART,align="center", font=("Arial", 6, "bold"))
        turtle.goto(0, -140)
        turtle.write(f"Your score : {self.score}", align="center", font=("Arial", 22, "bold"))
