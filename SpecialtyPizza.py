#SpecialtyPizza
from Pizza import *

class SpecialtyPizza(Pizza):
    def __init__(self, size, name):
        super(SpecialtyPizza,self).__init__(size)
        self.name = name
        if self.getSize() == 'S':
            self.setPrice(12.00)
        if self.getSize() == 'M':
            self.setPrice(14.00)
        if self.getSize() == 'L':
            self.setPrice(16.00)

    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:0.2f}\n"\
            .format(self.size, self.name, self.price)
            