# File Modes 
# To read a file you use "r", you cant modify or change
# To Write a file you use "w", you can change 
# To append to the end of a file you use "a", you cant change or read
# To read and write you "r+"

Bond_file = open("Bond.txt", "r")
# print(Bond_file.readable()) # Checks if it is readable
# print(Bond_file.read())     # Reads entire files
# print(Bond_file.readline())  # Reads per line

for name in Bond_file.readlines():
    print(name)
# print(Bond_file.readlines()[2])  # Reads entire lines and puts as an array
Bond_file.close()