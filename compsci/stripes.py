# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program shows an image with stripes of different colors

import matplotlib.pyplot as plt
import numpy as np


num = int(input("Enter the size: "))
file = input("Enter output file: ")
img = np.ones((num,num,3))
img[::2,:,1] = 0
img[1::2,:,2] = 0
plt.imsave(file,img)
