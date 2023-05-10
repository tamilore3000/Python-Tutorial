# Now carefully study the follow two concatenation programs and explain difference in output. Both 
# programs (contact1.py and concat2.py) use **kwargs and a For-Loop to effect concatenation 
# using contents of a dictionary data structure.
# concat1.py

def concat1(**kwargs):
    output = ""
 # Here is a Concatenation For - Loop
    for arg in kwargs.values():
        output += arg
    return output
    

# concat2.py
def concat2(**kwargs):
    output = ""
 # Here is a Concatenation For - Loop
    for arg in kwargs:
        output += arg
    return output
 
print(concat1(a="First.", b="Second.", c="Third.", d="Fourth."))
print(concat2(a="First.", b="Second.", c="Third.", d="Fourth."))

# QUESTION:
# Which of the following function definitions (progA.py and progB.py) is correct, and which is 
# wrong? Mention reason for your view.
# # progA.py
# def babfunction(a, b, *args, **kwargs):
#  pass
# # progB.py
# def babfunction (a, b, **kwargs, *args):
#  pass
# ANSWER:
# The first one progA.py is correct, while the second one progB.py is wrong. The reason is that *args 
# must come before **kwargs in any function where both are present.

# unpack1.py
xyz = [30, 77, 92, 84]
print(*xyz)
# print(xyz)

# As shown, the unpack operator * unpacks the list xyz. The moment this is done, the print function 
# prints the content of the list, rather than the original list.

# Given the following function, create a list called myList and demonstrate how to make a function 
# call involving unpacking operation.
# Demonstrating Unpacking
def adder(*mylist):
    for list in mylist:
        print(list)

adder(10,9,8,7)
