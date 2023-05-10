# Three major types of inheritances supported by 
# Python are:
# 1. Single Level Inheritance
# 2. Multi-Level Inheritance
# 3. Multiple Level Inheritance
# Single inheritance: In single inheritance, a subclass inherits from a single superclass. The subclass inherits all the methods and attributes of the superclass.

# Multi-level inheritance: In multi-level inheritance, a subclass inherits from a superclass, which itself inherits from another superclass. This creates a hierarchical inheritance structure.

# Multiple inheritance: In multiple inheritance, a subclass inherits from two or more superclasses. This allows the subclass to inherit and combine the methods and attributes of multiple superclasses

# sun_moon.py
class Sun:
    def __init__(self):
        pass
class Moon (Sun): # Inheritance statement
    def __init__(self):
        pass

# QUE 8: Create four classes called A, B, C and D such that B inherits from A, C
# inherits from B, while D inherits C and A in that order. The constructor methods
# should be populated with pass statements. Moreover, the design should contain
# comment statements showing the type of inheritance in operation, then executed.

class A: # inherit_abcd.py
    def __init__(self):
        pass
#Single Level Inheritance
class B(A):
    def __init__(self):
        pass
#Multi-Level Inheritance
class C (B):
    def __init__(self):
        pass    
#Multiple Inheritance
class D (C, A):
    def __init__(self):
        pass

# Create two Python Programs called b4overide.py
# and afteroveride.py to illustrate Overriding in Python.

#b4overide 
class King:
    def action():
        print("King in the north")

class Prince(King):
    pass

x = Prince
x.action()

#afteroveride 

class NedStark():
    def status():
        print("King in the North")

class JonSnow(NedStark):
    def status():
        print("The new King in the north")

y = JonSnow
y.status()