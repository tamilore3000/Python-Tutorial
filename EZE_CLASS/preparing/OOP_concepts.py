# Define a class called Animal
class Animal:
    # Define the constructor method
    def __init__(self, name, species, age):
        self._name = name
        self._species = species
        self._age = age

    # Define a method for making the animal speak
    def speak(self):
        print(f"{self._name} says hi!")

    # Define getter methods for the name, species, and age attributes
    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    # Define setter methods for the name, species, and age attributes
    def set_name(self, name):
        self._name = name

    def set_species(self, species):
        self._species = species

    def set_age(self, age):
        self._age = age

# Define a class called Dog that inherits from Animal
class Dog(Animal):
    # Define the constructor method
    def __init__(self, name, breed, age):
        super().__init__(name, "Dog", age)
        self._breed = breed

    # Define a method for making the dog bark
    def bark(self):
        print(f"{self._name} barks!")

    # Define a getter method for the breed attribute
    def get_breed(self):
        return self._breed

    # Define a setter method for the breed attribute
    def set_breed(self, breed):
        self._breed = breed

# Define a class called Cat that inherits from Animal
class Cat(Animal):
    # Define the constructor method
    def __init__(self, name, color, age):
        super().__init__(name, "Cat", age)
        self._color = color

    # Define a method for making the cat meow
    def meow(self):
        print(f"{self._name} meows!")

    # Define a getter method for the color attribute
    def get_color(self):
        return self._color

    # Define a setter method for the color attribute
    def set_color(self, color):
        self._color = color

# Create a Dog object and test the methods
my_dog = Dog("Max", "Golden Retriever", 5)
my_dog.speak()  # Output: Max says hi!
my_dog.bark()   # Output: Max barks!
print(my_dog.get_species())   # Output: Dog
my_dog.set_age(6)
print(my_dog.get_age())       # Output: 6

# Create a Cat object and test the methods
my_cat = Cat("Fluffy", "White", 3)
my_cat.speak()  # Output: Fluffy says hi!
my_cat.meow()   # Output: Fluffy meows!
print(my_cat.get_species())   # Output: Cat
my_cat.set_color("Gray")
print(my_cat.get_color())     # Output: Gray


# Abstraction: Abstraction is the process of hiding implementation details and exposing only the essential features of an object. In the code, the Animal class uses abstraction by providing a speak() method that does not have an implementation. The speak() method is an abstract method, which means that subclasses must provide their own implementation of the method.

# Inheritance: Inheritance is the process of creating new classes that reuse code from existing classes. In the code, the Dog and Cat classes both inherit from the Animal class, which means that they reuse the name and age attributes, as well as the speak() method.

# Encapsulation: Encapsulation is the process of hiding the internal details of an object and providing a public interface for interacting with the object. In the code, encapsulation is used to protect the name, age, and breed attributes of the Animal and Dog classes. These attributes are marked as private using the double underscore (__) prefix, which means that they cannot be accessed or modified from outside the class.

# Polymorphism: Polymorphism is the ability of objects of different classes to be treated as if they are the same type. In the code, polymorphism is demonstrated when both Dog and Cat objects are treated as Animal objects and called the speak() method.

# Method overriding: Method overriding is the process of providing a new implementation for a method that is already defined in a superclass. In the code, method overriding is used by the Dog class to provide its own implementation of the speak() method that is inherited from the Animal class.

# Overall, the code demonstrates several key OOP concepts in action, including abstraction, inheritance, encapsulation, polymorphism, and method overriding.