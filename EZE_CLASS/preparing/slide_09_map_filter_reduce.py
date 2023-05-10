
# In Python, mapping refers to the process of applying a function to each item in an iterable and returning a new iterable containing the results. This is commonly achieved using the map() function in Python.

# The map() function takes two arguments: a function and an iterable. The function is applied to each item in the iterable, and the results are returned as a new iterable. Here is an example:


# Define a function to square a number
def square(x):
    return x**2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the square function to each number in the list
squares = map(square, numbers)

# Print the resulting list of squares
print(list(squares))  # Output: [1, 4, 9, 16, 25]

# A function to generate the cube of all the integers from 3 to 10 using loop construct
# Rewrite using map function

def cube():
    integer = [3,4,5,6,7,8,9]
    cubes = []
    for ex in integer:
        answer = ex ** 3 
        print(f"The cube of {ex} is {answer}")

    for ex in integer:
        cubes.append (ex ** 3)
    print("Output is", cubes)

cube()  

print("Using Maps")
def cube(x):
    return x ** 3 
nums = [3,4,5,6,7,8,9]

answer= list(map(cube,nums))
print("output ", answer)