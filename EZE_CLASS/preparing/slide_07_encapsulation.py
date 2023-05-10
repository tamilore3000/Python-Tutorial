# Encapsulation in object oriented programming involves the process of restricting access to 
# methods and variables. One of the major reason for encapsulation is to prevent unauthorized or 
# accidental modification of data

# Key was to remember encapsulation is Z,S,D (zero, single, double underscore)


# ACCESS RULES:
# 1. Protected members cannot be accessed outside the class but can be accessed from within 
# the class and it’s subclasses. 
# 2. Private members are similar to protected members, the difference is that the class 
# members declared private should neither be accessed outside the class nor by any base 
# class. 

# QUESTION:
# Create a Python class called Marriage, and a private method called engagement. Demonstrate how 
# the method can be called through the parent class. Also use a comment statement to indicate where 
# the private method cannot be called.

class Marriage():
    def __init__(self):
        self.__engagement()

    def __engagement(self):
        print("We are engaged")



Bride = Marriage()
# Bride.__engagement() not accessible

# make a program to show public , private and protected methods 

