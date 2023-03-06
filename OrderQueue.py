#OrderQueue.py
from Pizza import *
from SpecialtyPizza import *
from CustomPizza import *
from PizzaOrder import *

class OrderQueue():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def addOrder(self, pizzaOrder):
        self.heapList.append(pizzaOrder)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def processNextOrder(self):
        if self.currentSize == 0:
            raise QueueEmptyException
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval.getOrderDescription()


    def percUp(self,i):
        while i // 2 > 0: 
            if self.heapList[i].getTime() < self.heapList[i // 2].getTime():
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2 #not done running yet, keep swapping and percolating upwards

    def percDown(self,i):
        #check if left child exists
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            #if parent is greater than children then swap and percolate
            if self.heapList[i].getTime() > self.heapList[mc].getTime():
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def minChild(self,i): 
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2].getTime() < self.heapList[i*2+1].getTime():
                return i * 2
            else: return i * 2 + 1

class QueueEmptyException(Exception):
    pass

