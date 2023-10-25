# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# borough fraction

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows = 5)
borough = input("Enter borough name: ")
outputfile = input("Enter output file name: ")
pop['Fraction'] = pop[borough]/pop['Total']

pop.plot(x='Year', y='Fraction')

fig = plt.gcf() 
fig.savefig(outputfile)
