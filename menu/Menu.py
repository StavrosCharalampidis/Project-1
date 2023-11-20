from calculator import Calculator

class Menu(Calculator):
    def __init__(self, option, x, y):
        super().__init__(x, y)
        self.option = option
        
    def menu(self):
        if self.option == "+":
            print(super().add(self.x, self.y)) 
        else:
            pass

    

    
        
    
    