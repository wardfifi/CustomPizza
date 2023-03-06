from Pizza import *
from SpecialtyPizza import *
from CustomPizza import *
from PizzaOrder import *
from OrderQueue import *
import pytest

def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    sp2 = SpecialtyPizza("M", "The Godfather")
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: The Godfather\n\
Price: $14.00\n"
    sp3 = SpecialtyPizza("L", "The Godfather")
    assert sp3.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: The Godfather\n\
Price: $16.00\n"

def test_CustomPizza():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"
    cp3 = CustomPizza("S")
    cp3.addTopping("rick and morty")
    cp3.addTopping("phone on half")
    assert cp3.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ rick and morty\n\
\t+ phone on half\n\
Price: $9.00\n"

def test_PizzaOrder():
    sp1 = SpecialtyPizza("S", "Carne-more")
    sp2 = SpecialtyPizza("M", "The Godfather")
    sp3 = SpecialtyPizza("L", "The Godfather")
    cp1 = CustomPizza("S")
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    cp3 = CustomPizza("S")
    cp3.addTopping("rick and morty")
    cp3.addTopping("phone on half")
    order = PizzaOrder(690008) 
    order.addPizza(cp1)
    order.addPizza(sp1)
    order.addPizza(sp2)
    order.addPizza(sp3)
    order.addPizza(cp3)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 690008\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: The Godfather\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: The Godfather\n\
Price: $16.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ rick and morty\n\
\t+ phone on half\n\
Price: $9.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $65.00\n\
******\n"

    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) 
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test_OrderQueue():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order1 = PizzaOrder(123000) 
    order1.addPizza(cp1)
    order1.addPizza(sp1)

    order2 = PizzaOrder(41234) 
    sp3 = SpecialtyPizza("L", "The Godfather")
    cp1 = CustomPizza("S")
    order2.addPizza(cp1)
    order2.addPizza(sp3)
    oq = OrderQueue()
    oq.addOrder(order1)
    oq.addOrder(order2)
    assert oq.processNextOrder() == \
"******\n\
Order Time: 41234\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: The Godfather\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $24.00\n\
******\n"
    cp1 = CustomPizza("M")
    cp1.addTopping("extra cheese")
    cp1.addTopping("meow")
    sp1 = SpecialtyPizza("S", "The Godfather")
    order1 = PizzaOrder(53000) 
    order1.addPizza(cp1)
    order1.addPizza(sp1)

    order2 = PizzaOrder(111234) 
    sp3 = SpecialtyPizza("L", "The Godfather")
    cp1 = CustomPizza("L")
    order2.addPizza(cp1)
    order2.addPizza(sp3)
    oq = OrderQueue()
    oq.addOrder(order1)
    oq.addOrder(order2)
    assert oq.processNextOrder() == \
"******\n\
Order Time: 53000\n\
CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ meow\n\
Price: $11.50\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: The Godfather\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $23.50\n\
******\n"

with pytest.raises(QueueEmptyException):
    heap = OrderQueue()
    heap.processNextOrder() 
