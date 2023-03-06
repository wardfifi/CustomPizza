#CustomPizza.py
from Pizza import *

class CustomPizza(Pizza):
    def __init__(self, size):
        super(CustomPizza,self).__init__(size)
        self.toppingsList = ""
        if self.getSize() == 'S':
            self.setPrice(8.00)
        if self.getSize() == 'M':
            self.setPrice(10.00)
        if self.getSize() == 'L':
            self.setPrice(12.00)
            

    def addTopping(self, topping):
        self.toppingsList += "\t+ " + topping + "\n"
        if self.getSize() == 'S':
            newestprice = self.getPrice() + 0.5
            self.setPrice(newestprice)
        elif self.size == 'M':
            newestprice = self.getPrice() + 0.75
            self.setPrice(newestprice)
        else:
            newestprice = self.getPrice() + 1
            self.setPrice(newestprice)


    def getPizzaDetails(self):
        return "CUSTOM PIZZA\nSize: {}\nToppings:\n{}Price: ${:0.2f}\n"\
            .format(self.size, self.toppingsList, self.price)

