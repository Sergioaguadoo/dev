# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program prints a picture in purple

import matplotlib.pyplot as plt
import numpy as np

picture = input("enter an input: ")
purple = input("enter an output: ")

img = plt.imread(picture)

img2 = img.copy()
img2[:,:,1] = 0

plt.imsave(purple, img2)
