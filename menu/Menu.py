from calculator import Calculator

class Menu:
    
    def __init__(self, option: str, x: float | int, y: float | int) -> None:
        self.option = option
        self.x = x
        self.y = y
    
    def menu(self, option: str, x: float | int, y: float | int) -> float | int:
        if self.option == "+":
            Calculator.add(self.x, self.y) 
    
        
    
    