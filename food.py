from turtle import Turtle
import random

COLORS = [
    "LightPink",
    "LightCoral",
    "LightSalmon",
    "LightGoldenRodYellow",
    "LightYellow",
    "LightGreen",
    "LightCyan",
    "LightSkyBlue",
    "LightBlue",
    "LightSteelBlue"
]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        random_color = random.choice(COLORS)
        self.color(random_color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Relocate the food item when touched by the head."""
        random_location = (random.randint(-280, 280), random.randint(-280, 250))
        self.goto(random_location)