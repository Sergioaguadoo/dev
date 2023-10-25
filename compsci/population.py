# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program prints the. population average from the borough you want

import pandas as pd

pop = pd.read_csv("nycHistPop.csv", skiprows = 5)

borough = input("Enter a borough: ")

average = pop[borough].mean()
maximum = pop[borough].max()

print("Average population:", average)
print("Maximum population:", maximum)
