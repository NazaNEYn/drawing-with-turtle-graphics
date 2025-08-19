from turtle import Turtle, Screen
from random_color import generate_random_hex_code

# Initialize turtle and screen objects
tim = Turtle()
screen = Screen()

# Set up the screen properties
screen.colormode(255)
tim.pensize(2)


def rotate_right():
    """Rotates the turtle right by 10 degrees."""
    tim.right(10)


def rotate_left():
    """Rotates the turtle left by 10 degrees."""
    tim.left(10)


def forward():
    """Moves the turtle forward by 20 units."""
    # Corrected typo from 'fowrad' to 'forward' for clarity
    tim.forward(20)


def backward():
    """Moves the turtle backward by 20 units."""
    tim.forward(-20)


def delete():
    """Changes the pen color to white to 'erase' the drawing."""
    tim.pencolor("white")


def draw():
    """Generates a new random color and sets the turtle's pen color."""
    # This ensures a new color is generated on each key press
    random_color = generate_random_hex_code()
    tim.color(random_color)


def reset():
    """Clears the screen and resets the turtle's position and heading."""
    screen.reset()


# Set up the event listeners
# These lines listen for key presses and call the corresponding function.
screen.listen()
screen.onkeypress(fun=rotate_right, key="d")
screen.onkeypress(fun=rotate_left, key="a")
screen.onkeypress(fun=forward, key="w")
screen.onkeypress(fun=backward, key="s")
screen.onkey(fun=delete, key="space")
screen.onkey(fun=draw, key="Return")
screen.onkey(fun=reset, key="Escape")

# Keep the window open until the user clicks it.
screen.exitonclick()
