# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program draws shades of blue

import turtle

turtle.colormode(255)
thomas = turtle.Turtle()
thomas.shape("turtle")
thomas.backward(100)

for i in range(0,255,10):
    thomas.forward(10)
    thomas.pensize(i)
    thomas.color(0,0,i)
