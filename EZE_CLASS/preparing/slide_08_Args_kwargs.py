# # The term “splatting” in python relates to spreading, unpacking or explosion. In other words, you 
# # splat a sequence by unpacking all its content inside another one. In Python, the asterisk is used as 
# # a splat operator. Example:

# x = [20,1,2,3,4,5]
# y = [6,7,8,9,10,11]
# w = [100, 100,*x]

# print(w)
# z=[60,60,*y,70,70,70,*x]
# print(z)

# # The term *args stands for variable number of arguments, while ** stands for variable number of keyword arguments. 
# # The implication is that when any of *args and **kwargs appear in function definitions,
# #  the function calls could involve any number of arguments, though the later uses keyword arguments.

# # There are positional argument and keyword arguments 

# def testscores(surname, regnum, *scores):
#     print(f"Surname is: {surname}")
#     print(f"Reg Num: {regnum}")
#     for score in scores:
#         print(score)

# testscores("Olaogun", "19/2075", 80,80,80,85,89,92)
# testscores("Phelps", "19/2375", 90,89,85,84,89,92)
# testscores("Carlsen", "19/1075", 99,78,83,83,86,92)


# # IMPORTANT NOTE:
# # 1. When there are more than one type of arguments in a function call, the following order 
# # must be maintained:
# # a. positional arguments
# # b. varied arguments (*args) 
# # c. keyword varied arguments (**kwargs)
# # Example: functcall(vara, *args, **kwargs)
# # If one deviates from this rule, system will send an error message.
# # 2. Thus, one cannot place **kwargs before *args.
# # 3. You can use args and kwargs in for…loop statement. Example:

# # The name 'args' is just a convention in other words you can use '*boys' or whatever.

# def  sum(*args):
#     add = 0
#     for i in args:
#         add += i
#     print("The sum is: ",add )

# sum(1,2,3,4,5,6,7,8,9)


# def demokwargs(**kwargs):
#     for x, y in kwargs.items():
#         print(x,y)

# demokwargs(Name='Samuel', Height='6.8feet', Colour='Tinted Black', Sex='Male', Age=24)


# Write a method that will use **kwargs to keep tract of the books in the library. Precaution must 
# be taken to ensure that the keywords data supplied is not empty. To program should be tested using 
# the following three books: Physics by Dr. Jaa, Maths by Prof. Dan, English by Dr. Roy

def books(**kwargs):
    if kwargs != None:
        for key,value in kwargs.items():
            print(key,value)
    else:
        print("None value detected")
    
books(bk1 = "Physics by Dr Sheldon Cooper", bk2 = "Mathematics by Slyvester", bk3 ="Introduction to computing by Walter O brien")

