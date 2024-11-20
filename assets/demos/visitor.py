# Visitor/FlowerVisitors.py
# Demonstration of "visitor" pattern.
# From: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Visitor.html
"""
from __future__ import generators
import random

# The Flower hierarchy cannot be changed:
class Flower(object):
    def accept(self, visitor):
        visitor.visit(self)
    def pollinate(self, pollinator):
        print(self, "pollinated by", pollinator)
    def eat(self, eater):
        print(self, "eaten by", eater)
    def __str__(self):
        return self.__class__.__name__

class Gladiolus(Flower): pass
class Runuculus(Flower): pass
class Chrysanthemum(Flower): pass

class Visitor:
    def __str__(self):
        return self.__class__.__name__

class Bug(Visitor): pass
class Pollinator(Bug): pass
class Predator(Bug): pass

# Add the ability to do "Bee" activities:
class Bee(Pollinator):
    def visit(self, flower):
        flower.pollinate(self)

# Add the ability to do "Fly" activities:
class Fly(Pollinator):
    def visit(self, flower):
        flower.pollinate(self)

# Add the ability to do "Worm" activities:
class Worm(Predator):
    def visit(self, flower):
        flower.eat(self)

def flowerGen(n):
    flwrs = Flower.__subclasses__()
    for i in range(n):
        yield random.choice(flwrs)()

# It's almost as if I had a method to Perform
# various "Bug" operations on all Flowers:
bee = Bee()
fly = Fly()
worm = Worm()
for flower in flowerGen(10):
    flower.accept(bee)
    flower.accept(fly)
    flower.accept(worm)
"""

""" The Courses hierarchy cannot be changed to add new 
functionality dynamically. Abstract Crop class for 
Concrete Courses_At_GFG classes: methods defined in this class 
will be inherited by all Concrete Courses_At_GFG classes."""
# https://www.geeksforgeeks.org/visitor-method-python-design-patterns/
class Courses_At_GFG: 

	def accept(self, visitor): 
		visitor.visit(self) 

	def teaching(self, visitor): 
		print(self, "Taught by ", visitor) 

	def auditing(self, visitor): 
		print(self, "Audited by ", visitor) 

	def studying(self, visitor): 
		print(self, "studied by ", visitor) 


	def __str__(self): 
		return self.__class__.__name__ 


"""Concrete Courses_At_GFG class: Classes being visited."""
class SDE(Courses_At_GFG): pass

class STL(Courses_At_GFG): pass

class DSA(Courses_At_GFG): pass


""" Abstract Visitor class for Concrete Visitor classes: 
method defined in this class will be inherited by all 
Concrete Visitor classes."""
class Visitor: 

	def __str__(self): 
		return self.__class__.__name__ 


""" Concrete Visitors: Classes visiting Concrete Course objects. 
These classes have a visit() method which is called by the 
accept() method of the Concrete Course_At_GFG classes."""
class Instructor(Visitor): 
	def visit(self, crop): 
		crop.teaching(self) 


class Student(Visitor): 
	def visit(self, crop): 
		crop.studying(self) 

class Auditor(Visitor):
    def visit(self, crop):
        crop.auditing(self)

"""creating objects for concrete classes"""
sde = SDE() 
stl = STL() 
dsa = DSA() 

"""Creating Visitors"""
instructor = Instructor() 
student = Student() 
auditor = Auditor()

"""Visitors visiting courses"""
sde.accept(instructor) 
sde.accept(student) 
sde.accept(auditor)

stl.accept(instructor) 
stl.accept(student) 

dsa.accept(instructor) 
dsa.accept(student) 
