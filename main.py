#!bin/python3

from menu.Menu import Menu
from calculator import Calculator
x: int = 0
y: int = 1

calculator = Calculator(x, y)
option = "+"
M = Menu(option, x, y)

M.menu(option, x, y)

#print(Calculator("+", x, y))
#print(calculator.add(x, y))
