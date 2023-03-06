#PizzaOrder.py
from SpecialtyPizza import *
from CustomPizza import *
from Pizza import *

class PizzaOrder():
    def __init__(self, time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        totalprice = 0
        eachpizza = ""
        firstLine = "******" + "\n" + "Order Time: " + str(self.time) + "\n"
        endstring = "\n" + "----" + "\n"
        for pizza in self.pizzas:
            eachpizza += pizza.getPizzaDetails() + endstring
            totalprice += pizza.getPrice()
            
        return firstLine + eachpizza + "TOTAL ORDER PRICE: ${:0.2f}\n".format(totalprice) + "******" + "\n"

