


def TotalWithTax(food,tip):
    tax = 0.1 * food
    return(food + tax + tip)

lunch = float(input("Enter lunch total: "))
l_tip = float(input("Enter lunch tip: "))
l_total = TotalWithTax(lunch, l_tip)
print("Lunch total is: ", l_total)

dinner = float(input("Enter dinner total: "))
d_tip = float(input("Enter tip value: "))
d_total = TotalWithTax(dinner, d_tip)
print("dinner total is: ", d_total)