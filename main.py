# interactive drawing app

import turtle

drawingBoard = turtle.Screen()
drawingBoard.bgcolor("light blue")
drawingBoard.title("Python Turtle")

turtleIns = turtle.Turtle()

def turtleForward():
    turtleIns.forward(100)

def turtleRightAngle():
    turtleIns.right(100)

def turtleLeftAngle():
    turtleIns.left(100)

def clearScreen():
    turtleIns.clear()

def returnHome():
    turtleIns.penup()
    turtleIns.home()
    turtleIns.pendown()

def penUp():
    turtleIns.penup()

def penDown():
    turtleIns.pendown()

drawingBoard.listen()
drawingBoard.onkey(fun=turtleForward, key="space")  # space for movement
drawingBoard.onkey(fun=turtleRightAngle, key="Down")
drawingBoard.onkey(fun=turtleLeftAngle, key="Up")
drawingBoard.onkey(fun=clearScreen, key="c")
drawingBoard.onkey(fun=returnHome, key="h")  # draws to home point -> added penup and pendown comments
drawingBoard.onkey(fun=penDown, key="w")
drawingBoard.onkey(fun=penUp, key="q")

turtle.mainloop()

