# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

mytuple = (1,2,3,4,5,6)

my_iterator = iter(mytuple)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self 
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x 
    
myclass = myNumbers()
myiter = iter(myclass)