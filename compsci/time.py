# Sergio Aguado Negrín
# sergio.aguadonegrin68@hunter.cuny.edu
# This program tells you what time your 


startTime = int(input("Enter starting time: "))
duration = int(input("Enter how long: "))

print("Your event starts at", startTime, "o'clock")

endTime = (startTime+duration)%12

print("Your event ends at", endTime, "o'clock")
