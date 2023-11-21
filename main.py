#!bin/python3
from menu.Menu import Menu
from calculator import Calculator

def menuFloat() -> None:
    option: str = input("Enter Option (+ - / *) and q to exit: ")
    while(option == 'q'):
        exit(0)
        
    while(option not in "+-/*"):
        option: str = input("Enter Option (+ - / *) and q to exit: ")
        break
    
   
    x: float = float(input("Enter Number 1: "))
    y: float = float(input("Enter Number 1: "))
    
    calculator: Calculator = Calculator(x, y)
    calculator_Menu: Menu = Menu(option, calculator.x, calculator.y) 
    calculator_Menu.menuItems()
   
def menuInt() -> None:
    option: str = input("Enter Option (+ - / *) and q to exit: ")
    while(option == 'q'):
        exit(0)
        
    while(option not in "+-/*"):
        option: str = input("Enter Option (+ - / *) and q to exit: ")
        break
    
   
    x: int = int(input("Enter Number 1: "))
    y: int = int(input("Enter Number 1: "))
    
    calculator: Calculator = Calculator(x, y)
    calculator_Menu: Menu = Menu(option, calculator.x, calculator.y) 
    calculator_Menu.menuItems()
        
if __name__ == '__main__':   
    IntOrFloat: str = input("Enter The Nuber type int for intigers and float for float nublers only: ")
    while(IntOrFloat != "int" or IntOrFloat != "float"):
        IntOrFloat: str = input("Enter The Nuber type int for intigers and float for float nublers only: ")
        break
    while(IntOrFloat == "int"): 
        menuInt()
        
    while(True): 
        menuFloat()

