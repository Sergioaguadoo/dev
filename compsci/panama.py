# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program prints your string in piramid form

s = input("Enter a string: ")

ls = len(s)
for i in range(0,ls-1):
    print(s[:i])
for i in range(0,ls-1):
    print(s[i:])

print("Thank you for using my program!")
