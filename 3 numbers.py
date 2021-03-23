number1 = float(input("First number: "))
number2 = float(input("Second number: "))
number3 = float(input("Third number: "))
number4 = float(input("Fourth number: "))

amount1 = number1+number2
#float(amount1)
amount2 = number3+number4
#float(amount2)

print("First number + second number = {0}" .format(amount1))
print("Third number + fourth number = {0}" .format(amount2))
print("Third number + fourth number = %.2f" % (amount1 / amount2))
