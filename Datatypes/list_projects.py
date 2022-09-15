def sum_list(array_list):
    for _ in array_list:
        total = sum(array_list)
    print(total)


# List to find the sum of five positive integers


print("Array to find the sum of 5 positive integers")
myarray = []
total = 0
i = 0

while True:
    try:
        n = int(input("How many integers are you entering: "))  # Number of Integers in the list
        if n > 0:  # To catch if the value is a Positive Integer
            while i < n:  # While loop to add the elements to the list
                try:
                    number = int(input("Enter Integer: "))
                    myarray.append(number)
                    i += 1
                except (ValueError, IndexError):
                    print("Wrong Element Inputted")
        else:
            raise ValueError(n)
        break
    except ValueError:
        print("Wrong Integer")

sum_list(myarray)

array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_list(array2)
