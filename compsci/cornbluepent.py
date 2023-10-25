# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program draws a cornflower blue pentagon


import turtle

thomas = turtle.Turtle()

thomas.shape("turtle")
thomas.color("#6495ED")

for i in range(5):
    thomas.forward(100)
    thomas.left(72)
    thomas.stamp()
