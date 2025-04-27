import turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        """Create three 'turtle' items stored in the 'turtles' list."""
        for locations in STARTING_POSITION:
            t = turtle.Turtle("square")
            t.color("white")
            t.penup()
            t.goto(locations)
            self.turtles.append(t)
        self.move()

    def add_snake(self):
        """Create a 'turtle' and append it to the existing snake."""
        t = turtle.Turtle("square")
        t.color("white")
        t.penup()
        last_turtle_cor = (self.turtles[-1].xcor(),self.turtles[-1].ycor())
        t.goto(last_turtle_cor)
        self.turtles.append(t)

    def move(self):
        """Moves the first item in the 'turtles' list by 'MOVE_DISTANCE'
        and assign the next item to the first one previous locations, the third
        to the second and so on and so forth. The process
        repeats for length of the 'turtles' list."""
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)

        self.turtles[0].forward(MOVE_DISTANCE)

    def move_right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def move_left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def move_up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def move_down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    # In snake.py
    def reset_snakes(self):
        for tortoise in self.turtles:
            tortoise.hideturtle()
            tortoise.clear()
        self.turtles = []
        self.create_snake()
        # Reset to initial direction (facing right)
        self.head.setheading(0)  # Add this line