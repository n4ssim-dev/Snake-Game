import turtle
from art import GAME_OVER_ART

class Score:
    def __init__(self):
        self.score = 0

        # Read high score from file (create if missing)
        try:
            with open('high_score.txt', mode="r") as file:
                self.high_score = int(file.read())
        except (FileNotFoundError, ValueError):
            # If file doesn't exist or contains invalid data, reset to 0
            self.high_score = 0
            with open('high_score.txt', mode="w") as file:
                file.write("0")

        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt',mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()  # Make sure to add this if not already present

    def refresh_score(self):
        """Add a score point and refresh the score displayed on top."""
        self.score += 1
        turtle.clear()
        self.write_score()

    def write_score(self):
        """Write the users score on top."""
        turtle.clear()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(0, 270)
        turtle.color("white")
        turtle.write(f"Score: {self.score} | High-score : {self.high_score}",align="center",font=("Arial", 18, "bold"))

    def is_lost(self):
        """Clears the screen and display the game over sceen."""
        screen = turtle.Screen()
        screen.clear()
        screen.bgcolor("black")
        screen.tracer(0)
        turtle.penup()
        turtle.goto(0, -100)
        turtle.color("red")
        turtle.write(GAME_OVER_ART,align="center", font=("Arial", 6, "bold"))
        turtle.goto(0, -155)
        turtle.hideturtle()
        turtle.write(f"High-score : {self.high_score}", align="center", font=("Arial", 22, "bold"))