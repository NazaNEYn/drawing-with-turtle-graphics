# Interactive Turtle Drawing App 🐢
This is a simple interactive drawing application built using Python's `turtle` and `random` modules. The program allows a user to control a turtle on the screen using keyboard inputs to draw and change colors.

<hr>

### You can check out the video demo in my [tweet](https://x.com/nazanin_ashrafi/status/1957866431917207995).

<hr>


# Features ✨
* **Move Forward/Backward**: The turtle can be moved forwards and backwards to create lines.

* **Turn Left/Right**: The turtle's heading can be changed to draw in any direction.

* **Color Control**: The user can change the turtle's pen color to a new random color or make it white to "erase."

* **Reset**: The entire drawing can be cleared, resetting the turtle to its original state.
* <hr>


# How to Run 🏃‍♂️
1. **Dependencies**: This app uses two standard Python libraries, turtle and random, which are included in most Python installations. No special installation is needed.

2. **Save the Code**: Save the two Python files (`main.py` and `random_color.py`) in the same folder. The `random_color.py` file contains the `generate_random_hex_code()` function.

3. **Run from Terminal**: Open a terminal or command prompt, navigate to the folder where you saved the files, and run the main file using the command: `python main.py`.

<hr>

# Key Bindings ⌨️
The application is controlled entirely by the keyboard. The following keys are mapped to specific actions:

| Key | Action |
|---|---|
| `W` | Move the turtle forward |
| `S` | Move the turtle backward |
| `A` | Rotate the turtle left |
| `D` | Rotate the turtle right |
| `Space` | Change the pen color to white (erase) |
| `Return` | Set the pen color to a new random color |
| `Escape` | Clear the screen and reset the turtle |

<hr>


# Code Structure ⚙️
The code is divided into two files for better organization:

* `main.py`: This is the main program file. It initializes the `turtle` screen and a turtle object, sets up the key bindings, and defines the functions that handle user input.

* `random_color.py`: This file contains a single helper function, `generate_random_hex_code()`, which is used to create a random color. This separation of concerns makes the code cleaner and easier to manage.

<hr>





