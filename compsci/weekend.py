# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program tells you the days and hors left until the weekend

time = int(input("Enter a number of hours: "))

days = (time)//24      # this division gives the total value of the operation, without the remainder
hours = (time)%24      # this one gives the remainder of the operation

print("days: ", days)
print("hours: ", hours)
