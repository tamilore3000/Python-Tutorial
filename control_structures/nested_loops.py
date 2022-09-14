# for x in range(5):
#     for y in range(3):
#         print(f'( {x}, {y})')

numbers = [5, 2, 5, 2, 2 ]

for x_count in numbers:
    shape = ""
    for item in range(x_count):
        shape += "x"
    print(shape) 