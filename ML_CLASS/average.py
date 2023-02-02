
print("Array to find the average of 5 positive integers")
myarray = []


for number in range(4):
    x= int(input("Enter a number: "))
    myarray.append(x)
    total = sum(myarray)
    avg = sum(myarray)/len(myarray)
print("The average is: ", avg)


