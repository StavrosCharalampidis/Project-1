#!bin/python3

from menu.Menu import Menu
from calculator import Calculator
x: int = 0
y: int = 1

calculator = Calculator(x, y)
calculator_Menu = Menu("+",x, y)
calculator_Menu.menu()

#print(Calculator("+", x, y))
#print(calculator.add(x, y))
