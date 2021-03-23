# Даны катеты прямоугольного треугольника.
# Найти его гипотенузу.
import math

cathet1 = float(input("Enter the first cathet: "))
cathet2 = float(input("Enter the second cathet: "))

hypotenuse = math.sqrt( (cathet1 ** 2) + (cathet2 ** 2) )

print("hypotenuse is: %.4f" % (hypotenuse))