# Modules & Librairies
import turtle
import time
from snake import Snake
from food import Food
from score import Score

# Screen setup
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Global Scope
turtles = []
t_position = [0, 0]
game_is_on = True

# Ajoute les 3 tortues initiales
snake = Snake()
food = Food()
score = Score()

# Définis les touches de navigation du serpent
screen.onkey(lambda: snake.move_up(), "Up")
screen.onkey(lambda: snake.move_down(), "Down")
screen.onkey(lambda: snake.move_left(), "Left")
screen.onkey(lambda: snake.move_right(), "Right")

screen.listen()

# Game loop
while game_is_on:
    # Attends que les tortues finissent leurs animations pour les afficher
    screen.update()
    time.sleep(0.1)
    # fais bouger toutes les tortues de la file
    snake.move()

    # Augmente le score si la tete est a proximité de la nourriture
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh_score()
        snake.add_snake()

    # Vérifie que le serpent est dans le cadre sinon la partie est perdu
    if snake.head.ycor() > 285 or snake.head.ycor() < -285 or snake.head.xcor() > 285 or snake.head.xcor() < -285:
        game_is_on = False
        if not game_is_on:
            score.is_lost()

    # Vérifie si la tete n'entre pas en collision avec un élément du corp
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 15:
            game_is_on = False
            if not game_is_on:
                score.is_lost()
        else:
            pass

screen.exitonclick()