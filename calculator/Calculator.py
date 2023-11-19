#!bin/python3

class Calculator:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y
    
    def add(self, x: float | int, y: float | int) -> float | int:
        return self.x + self.y

    def minus(self, x: float | int, y: float | int) -> float | int:
        return self.x - self.y
    
    def div(self, x: float | int, y: float | int) -> float | int:
        if y != 0:
            return self.x - self.y
        else:
            print("Error")