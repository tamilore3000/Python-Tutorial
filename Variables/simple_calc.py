first = float(input("Enter First Number: "))
second = float(input("Enter Second Number: "))

sum = first + second
print("The sum is ", round(sum))

#abs returns postive numbers 

try:
    x=int(input('Enter a number upto 100: '))
    if x > 100:
        raise ValueError(x)
except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")
