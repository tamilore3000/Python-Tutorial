# Polymorphism comes from the greek works poly and morphism meaning many forms 
# Examples of inbuilt polymorphism is :

# 1
print(len("Great University"))

# 2
print(len([11,22,33,44,55]))

# 3 
print(len((11,22,33,44,55,66)))

# One of the main differences between sets and lists in Python is that sets are unordered collections of unique elements, 
# while lists are ordered collections of elements that may contain duplicates.

# E.g Create two functions addition and multiplication where the calculator has the ability to take two operands or three at the discretion of the user.

def addition(x,y,z=0):
    return x+y+z

def multiplication(x,y,z=1):
    return x*y*z

print(addition(2,3))
print(addition(2,3,4))

print(multiplication(2,3,4))
print(multiplication(2,3))