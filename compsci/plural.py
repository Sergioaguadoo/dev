# Sergio Aguado Negrín
# sergio.aguadonegrin68@myhunter.cuny.edu
# this program counts the fraction of plural words

def plural_fraction(words):
    word_list = words.split()
    total_words = len(word_list)
    plural_words = sum(1 for word in word_list if word.endswith("s"))

    if total_words == 0:
        print("Nothing entered")
    else:
        fraction_plural = plural_words / total_words
        print(f"Total words: {total_words}")
        print(f"Fraction of words plural: {fraction_plural:.2f}")

user_input = input("Enter nouns")
plural_fraction(user_input)