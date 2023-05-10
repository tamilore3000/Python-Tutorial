# A docstring is a string intentionally included by a programmer as part of the program documentation. By standard , a docstring begins with and is enclosed in """"
# You can use double quotation """x""" or single '''x''' marks 
'''This program is great'''
# To access a docstring __doc__ is used 
class My_class(object):
    """The class's docstring is written in this space 
    several lines could be used for documentation """

    def my_method(self):
        """The method's docstring is here. The method is the function defined for the class"""
print(__doc__)
print(My_class.__doc__)
print(My_class.my_method.__doc__)

# The magic method __base__ is used to access the parents of a class at run time.

class A(object):
    pass
class B(object):
    pass
class C(A,B):
    pass
print(C.__base__)

# The setattr is used to sets the named attribute on the given object with a specified value at run time.
class Country:
    pass

emp1 = Country()
setattr(emp1,'Area', "Kosofe LGA")
emp2 = Country()
setattr(emp2,"Location", "Gbagada")

print(emp1.Area)
print(emp2.Location)