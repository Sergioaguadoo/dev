# Sergio Aguado
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program shifts the letters by 13 values


word = input("write a phrase")
codedWord = ""

for ch in word:
    offset = ord(ch) - ord("a") + 13
    wrap = offset % 26
    newChar = chr(ord("a") + wrap)
    print(wrap, chr(ord("a") + wrap))
    codedWord = codedWord + newChar

print(codedWord)