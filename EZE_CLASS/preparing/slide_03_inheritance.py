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