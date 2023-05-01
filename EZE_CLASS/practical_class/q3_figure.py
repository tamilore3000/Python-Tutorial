import math

def calculate_total_area():
    square_area = 10**2
    circle_radius = 10 / 2
    circle_area = math.pi * circle_radius**2
    total_area = square_area + circle_area
    return total_area

total_area = calculate_total_area()
print("Total area:", total_area)
