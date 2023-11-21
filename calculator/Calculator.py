#!bin/python3
from typing import Union

T = Union[int, float]

class Calculator():
    def __init__(self, x: T, y: T) -> None:
        self.x = x
        self.y = y
    
    def add(self, x: T, y: T) -> T:
        if not isinstance(x, int | float) or not isinstance(y, int | float):
            raise TypeError
        
        return self.x + self.y

    def minus(self, x: T, y: T) -> T:
        if not isinstance(x, int | float) or not isinstance(y, int | float):
            raise TypeError
        
        return self.x - self.y
    
    def mul(self, x: T, y: T) -> T:
        if not isinstance(x, int | float) or not isinstance(y, int | float):
            raise TypeError
        
        return self.x * self.y
    
    def div(self, x: T, y: T) -> None:
        if not isinstance(x, int | float) or not isinstance(y, int | float):
            raise TypeError
        
        if y != 0:
            print(self.x / self.y)
       
        else:
            raise ZeroDivisionError
       