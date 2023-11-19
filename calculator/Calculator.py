#!bin/python3

class Calculator:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def add(self, x: float, y: float) -> float:
        return self.x + self.y
    
    def add(self, x: int, y: int) -> int:
        return self.x + self.y
