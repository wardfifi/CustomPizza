#Pizza.py

class Pizza():
    def __init__(self, size = ""):
        self.size = size
        self.price = 0.0
        
    def getPrice(self):
        return self.price

    def setPrice(self, price = 0.0):
        self.price = price
    
    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size