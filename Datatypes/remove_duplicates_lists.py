# To remove the duplicates in a list
numbers = [1, 3, 4, 5, 2, 5, 6, 3, 4, 6, 7, 2]
non_duplicates = []
numbers.sort()
for number in numbers:
    if number not in non_duplicates:
        non_duplicates.append(number)

print(non_duplicates)
