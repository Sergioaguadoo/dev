# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program tells the amount of snow.

import matplotlib.pyplot as plt

img = input("Enter file name: ")
ca = plt.imread(img)
t = 0.75
snowCount = 0

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
            snowCount = snowCount + 1
print("Snow count is: ", snowCount)
