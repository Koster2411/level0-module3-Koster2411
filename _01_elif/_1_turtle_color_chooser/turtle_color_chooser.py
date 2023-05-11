import random
import turtle
from tkinter import messagebox, simpledialog, Tk
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them
    turtle_ = turtle.Turtle()
    color = simpledialog.askstring(title=("color"), prompt=("choose a red green or yellow"))
    if color == "red":
        turtle_.pencolor("red")
    elif color == "yellow":
        turtle_.pencolor("yellow")
    elif color == "green":
        turtle_.pencolor("green")
    else:
        get_random_color()

    turtle_.penup()
    turtle_.goto(-200, 200)
    turtle_.pendown()
    turtle_.pensize(10)
    for i in range(4):
        turtle_.forward(500)
        turtle_.right(90)

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
