# Create two Python programs to illustrate how to
# inspect the properties of an object

class Person:
    def __init__(self,name,surname) :
        self.name = name 
        self.surname = surname
    def fullname(self):
        return "%s%s" (self.name, self.surname)
    
jane = Person("Jane", "Smith ")
print(dir(jane))

# A Diamond Problem is an issue resulting from multiple inheritance of
# four classes in OOP as explained in the following scenario. If classes B
# and C inherit from A and class D inherits from B and C, and both B and
# C have a method methodxyz. The issue then is, “Which of the
# competing methodxyz will D inherit? This ambiguity is known as the
# diamond problem, and different languages resolve it in different ways.
# In Python it is resolved using MRO (Method Resolution Ordering)
# algorithms.

class A:
    def methodxyz(self):
        pass
class B (A):
    def methodxyz(self):
        pass
class C (A):
    def methodxyz(self):
        pass
class D(B, C):
    def methodxyz(self):
        pass
 
called = D()
called.methodxyz

# A multiple inheritance design has eight classes A, B, C, D, E, F, G
# and H where B,C,D inherited A; E inherited B, C; F inherited B,D; G
# inherited C, D while H inherited E,F and G. Draw the inheritance diagram.

class A: 
    pass
class B(A): 
    pass 
class C(A): 
    pass
class D(A): 
    pass
class E(B,C): 
    pass
class F(B,D): 
    pass
class G(C,D): 
    pass
class H(E,F,G): 
    pass
print(H.mro())
# H, E, F, B, G, C, D, A

# CLASS ASSIGNMENT
# 1. Explain what you understand by MRO (Method Resolution 
# Ordering) in OOP.
# 2. Explain C3 Algorithm for MRO.
# 3. Trace the execution of C3 algorithm using 4 classes (A, B, C 
# and D) in a chain of inheritance in QUE 11. List the 
# chronological order in which the method search/execution 
# will occur.

# MRO (Method Resolution Ordering) is a mechanism used by object-oriented programming languages to determine the order in which methods are executed in the presence of multiple inheritance. It specifies how the inheritance hierarchy is traversed to search for the method or attribute being called, and ensures that the method is called only once even if it is inherited by multiple parent classes.

# C3 algorithm for MRO is a linearization algorithm that calculates a consistent and predictable ordering of the inheritance hierarchy. It takes into account the order of inheritance and the order of appearance of classes in the inheritance hierarchy, and generates a linear order that satisfies the following three conditions:

# Every class comes before its parents
# Parents are listed in the order they appear in the inheritance hierarchy
# If a class inherits from multiple classes, their order is preserved in the linearization.
# Let's consider the following inheritance chain: A -> B -> C -> D. We will trace the execution of the C3 algorithm in the following steps:
# Step 1: The linearization of the first class A is [A].
# Step 2: The linearization of the second class B is [B, A] because B inherits from A.
# Step 3: The linearization of the third class C is [C, B, A] because C inherits from B and B inherits from A.
# Step 4: The linearization of the fourth class D is [D, C, B, A] because D inherits from C and C inherits from B and B inherits from A.
# So, the chronological order in which the method search/execution will occur is D -> C -> B -> A, meaning that Python will first search for the method in class D, and then traverse the inheritance chain from C to A until the method is found or an error is raised.