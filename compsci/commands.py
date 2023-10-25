# Sergio Aguado negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program reads the commands

import turtle
thomas = turtle.Turtle()
commands = input("Enter a command string: ")
myWin = turtle.Screen()
for ch in commands:
    if ch =="B":
        thomas.backward(50)
    elif ch == "l":
        thomas.left(45)
    elif ch == "S":
        thomas.stamp()
    elif ch == "r":
        thomas.right(45)
    elif ch == "p":
        thomas.color("purple")
    elif ch == "L":
        thomas.left(90)
    elif ch == "F":
        thomas.forward(50)
    elif ch == "R":
        thomas.right(90)
    elif ch == "^":
        thomas.penup()
    elif ch == "v":
        thomas.pendown()
    else:
        print("command not existent", ch)

print("see garaphic window for result")
myWin.exitonclick()