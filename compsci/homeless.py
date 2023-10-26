# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter name of input file: ")
output = input("Enter name of output file: ")
children = pd.read_csv(file)

children['Fraction Children'] = children['Total Children in Shelter'] / children['Total Individuals in Shelter']
children.plot( x = 'Date of Census', y = 'Fraction Children')

fig = plt.gcf()
fig.savefig(output)
