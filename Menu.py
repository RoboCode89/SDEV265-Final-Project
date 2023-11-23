class Menu():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
        
    def setPrice(self, price):
        self.price = price
    
    def getPrice(self):
        return self.price
    
        
class Appetizer(Menu):
    def __init__(self, name, price, addBread):
        super().__init__(name, price)
        self.addBread = addBread
        if(self.addBread == True):
            self.price += 1
        
    def setAddBread(self, addBread):
        self.addBread = addBread
    
    def getAddBread(self):
        return self.addBread
    

class Entree(Menu):
    def __init__(self, name, price, addSoup, addSalad):
        super().__init__(name, price)
        self.addSoup = addSoup
        self.addSalad = addSalad
        if(self.addSoup == True):
            self.price += 2
        if(self.addSalad == True):
            self.price += 2
    
    def setAddSoup(self, addSoup):
        self.addSoup = addSoup
    
    def getAddSoup(self):
        return self.addSoup
    
    def setAddSalad(self, addSalad):
        self.addSalad = addSalad
        
    def getAddSalad(self):
        return self.addSalad
    



class Dessert(Menu):
    def __init__(self, name, price, isAlaMode):
        super().__init__(name, price)
        self.isAlaMode = isAlaMode
        if(self.isAlaMode == True):
            self.price += 2
        
    def setIsAlaMode(self, isAlaMode):
        self.isAlaMode = isAlaMode
    
    def getIsAlaMode(self):
        return self.isAlaMode
        
   
    
    

class Drink(Menu):
    def __init__(self, name, price, addLemon, addSugar):
        super().__init__(name, price)
        self.addLemon = addLemon
        self.addSugar = addSugar
        
    def setAddLemon(self, addLemon):
        self.addLemon = addLemon
        
    def getAddLemon(self):
        return self.addLemon
        
    def setAddSugar(self, addSugar):
        self.addSugar = addSugar
        
    def getAddSugar(self):
        return self.AddSugar
        
    
    

class Alcohol(Menu):
    def __init__(self, name, price, addWhippedCream, addDoubleShot):
        super().__init__(name, price)
        self.addWhippedCream = addWhippedCream
        self.addDoubleShot = addDoubleShot
        if(self.addDoubleShot == True):
            self.price += 3
        
    def setAddWhippedCream(self, addWhippedCream):
        self.addWhippedCream = addWhippedCream
        
    def getAddWhippedCream(self):
        return self.addWhippedCream
    
    def setAddDoubleShot(self, addDoubleShot):
        self.addDoubleShot = addDoubleShot
    
    def getAddDoubleShot(self):
        self.addDoubleShot = addDoubleShot
        
    