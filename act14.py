

from abc import abstractmethod
from xml.etree.ElementTree import PI
from abc import ABC, abstractclassmethod
import math

class Figura(ABC):
    @abstractmethod
    def area()->int:
        pass

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi
        
    def area(radi):
        print (math.pi*radi*radi)
        
class Rectangle(Figura):
    def __init__(self, base,altura):
        self.base = base
        self.altura=altura
    
    def area(base,altura):
        print (base*altura)

class Triangle(Figura):
    def __init__(self, costat):
        self.costat = costat
    
    def area(base,altura):
        print ((base*altura)/2)
        
class Quadrat(Rectangle):
    def __init__(self,costat):
        self.costat = costat
        
        
c = Cercle(10)
print( " Radi: "+ c.radi + " Area: " +c.area)

r = Rectangle(5,10)
r.area(r.altura,r.base)

t = Triangle(3)
t.costat=3
t.area(t.costat)

q = Quadrat()
q.altura(8)
q.base(4)
q.area(q.base,q.altura)


