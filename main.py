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

# Initialize game objects
snake = Snake()
food = Food()
score = Score()

def restart_game():
    global game_is_on
    score.reset()
    snake.reset_snakes()
    food.refresh()
    game_is_on = True

# Définis les touches de navigation du serpent
screen.onkey(lambda: snake.move_up(), "Up")
screen.onkey(lambda: snake.move_down(), "Down")
screen.onkey(lambda: snake.move_left(), "Left")
screen.onkey(lambda: snake.move_right(), "Right")
screen.onkey(lambda: restart_game(), "space")
screen.listen()

# Game loop
game_is_on = True
while True:  # Changed to infinite loop, we'll control exit differently
    screen.update()
    time.sleep(0.1)

    if game_is_on:
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.refresh_score()
            snake.add_snake()

        # Detect collisions (wall or self)
        if (snake.head.ycor() > 285 or snake.head.ycor() < -285 or
                snake.head.xcor() > 285 or snake.head.xcor() < -285 or
                any(snake.head.distance(segment) < 10 for segment in snake.turtles[1:])):
            score.reset()
            score.is_lost()
            game_is_on = False

    # This handles the paused state after game over
    while not game_is_on:
        screen.update()
        time.sleep(0.1)

screen.exitonclick()