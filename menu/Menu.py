#!bin/python3
from calculator import Calculator
from typing import Union

T = Union[int, float]
V = str

class Menu(Calculator):
    def __init__(self, option: V, x: T, y: T) -> None:
        super().__init__(x, y)
        self.option = option
    
    
    def menuItems(self) -> None:
        if self.option == "+":
            print(super().add(self.x, self.y))
            
        if self.option == "-":
            print(super().minus(self.x, self.y))
        
        if self.option == "*":
            print(super().mul(self.x, self.y))

        if self.option == "/":
            super().div(self.x, self.y)

    

    
        
    
    