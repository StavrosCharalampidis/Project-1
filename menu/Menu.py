from calculator import Calculator

class Menu(Calculator):
    def __init__(self, option, x, y):
        super().__init__(x, y)
        self.option = option
        
    def menu(self, option, x, y):
        if option == "+":
            print(Calculator.add(x, y)) 
        else:
            pass

    

    
        
    
    