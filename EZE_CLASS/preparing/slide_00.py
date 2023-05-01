# OOP focuses on using DRY(DO NOT REPEAT YOURSELF CONCEPT)
# A CLASS IS A BLUEPRINT FOR WHICH OBJECTS ARE CREATED. IT REPRESENTS A SET OF PROPERTIES OR METHODS THAT ARE COMMON TO ALL OBJECTS OF ONE TYPE
# An object is an instance of a class 
# Attributes: Attributes are data members of a class. They store data that describes the state of an object. 
# Methods: Methods are functions that are defined inside a class. They define the behavior of an object. 
# A constructor is a special method used for initializing the instance variables during object creation .


# Creates class Car
class Car:
    # create class attributes
    name = "c200"
    make = "mercedez"
    model = 2010
# create class methods
def start(self):
    print ("Engine started")
def stop(self):
    print ("Engine switched off")

mycar = Car()
mycar.name = "Toyota Yaris"
mycar.make = "Toyota"
mycar.model = "2007"
print(mycar.model,mycar.make,mycar.name)