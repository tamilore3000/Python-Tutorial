# The pass statement is used in an empty class to indicate the class is empty.

class Mammal:
    def __init__(self, name , specie, age, color, sex):
        self.name = name
        self.specie = specie
        self.age = age
        self.color = color
        self.sex = sex

    def walk(self):
        print("walking")

class Dog(Mammal):
   def bark(self):
       print("WOOF , WOOF!")

class Cat(Mammal):
    pass

dog1 = Dog(name="Bingo", specie= "German Shepard", age=12, color="Brown", sex="Male")
print(f"The name of my dog is {dog1.name}, he is a {dog1.sex} {dog1.specie}, {dog1.color} in color")
dog1.bark()
cat1 = Cat.walk(self="pass")


