#!bin/python3

class Calculator:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y
    
    def add(self, x: float | int, y: float | int) -> float | int:
        if not isinstance(x, int | float):
            raise TypeError
        
        return self.x + self.y

    def minus(self, x: float | int, y: float | int) -> float | int:
        if not isinstance(x, int | float):
            raise TypeError
        
        return self.x - self.y
    
    def div(self, x: float | int, y: float | int) -> float | int | None:
        if not isinstance(x, int | float) and not isinstance(y, int | float):
            raise TypeError
        
        elif y != 0:
            return self.x / self.y
        else:
            return "Error"