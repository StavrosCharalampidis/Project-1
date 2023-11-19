#!bin/python3

from calculator import Calculator

x: int = 0
y: int = 1

calculator = Calculator(x, y)
print(calculator.div(x, y))
