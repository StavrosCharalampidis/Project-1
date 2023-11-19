#!bin/python3

from calculator import Calculator

x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))

calculator = Calculator(x, y)
print(calculator.div(x, y))
