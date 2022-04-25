# program to calculate income tax
print ("Please enter you Gross Income to the nearest penny")
g_income = float(input())
if (g_income > 10000):
    print ("Please enter the number of dependents you have")
    dep = int(input())
    income = float (g_income - 10000 - (dep * 3000))
    print ("Your taxable income is = $", income)
    tax = float (20/100 * income)
    print ("Your income tax= $", tax)
else:
    print ("No income tax for you")

