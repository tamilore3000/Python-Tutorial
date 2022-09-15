# In classes,  you capitalize the first name of every word, from Pascal naming Convention
# Methods represent something the object can do, like actions i.e door can close or open
# Attributes refer the something the object has i.e doors have attributes like height , width
class Point:
    def __init__(self, x, y):     # A constructor that stores objects
        self.x = x
        self.y = y

    def move(self):
        print("moved")

    def draw(self):
        print("drawn")

point = Point(x=10, y=12)
print(point.move())
print(f"The points are {point.x} on x-axis and {point.y} on y-axis")

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Hello I am ", self.name)

user = Person("Tammy")
user.talk()
