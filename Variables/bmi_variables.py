# BMI CALCULATOR IN PYTHON
import os
from datetime import date

# # define our clear function
# def clear():
#     # for windows
#     if os.name == 'nt':
#         os.system('cls')
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = os.system('clear')
def weight_converter(w):
    while True:
        try:
            global converted
            converted = 0
            weight_unit = input("What is the weight unit Kgs or Lbs: ")
            if weight_unit.upper() == "KG":
                converted = w / 1
                print("weight in kg is: ", converted, "kg")
                return converted  # Made sure a decimal value was being returned
            elif weight_unit.upper() == "LBS":
                converted = w / 2.2
                print("weight in kg is: ", converted, "kg")
                return converted  # Same here
            else:
                raise ValueError(weight_unit)

        except (ValueError, IOError, IndexError):
            print("ERROR - Please enter proper unit of measure")


def height_converter(h):
    while True:
        try:
            height_unit = input("what is the height unit meters or feet: ")
            if height_unit.upper() == "METERS":
                converted = h / 1
                print("height in meters is: ", converted, "m")
                return converted  # And here
            elif height_unit.upper() == "FEET":
                converted = h / 3.281
                print("height in meters is: ", converted, "m")
                return converted  # And finally here
            else:
                raise ValueError(height_unit)
        except(ValueError, IOError, IndexError):
            print("ERROR - Please enter proper unit of measure")

while True:
    try:
        age = input("How old are you? ")
        age = int(age)

        weight = input("What is your weight: ")
        weight = float(weight)
        wconverted = weight_converter(weight)

        height = input("What is your height: ")
        height = float(height)
        hconverted = height_converter(height)
        break
    except ValueError:
        # os.system(clock_settime)
        print("No valid integer! Please try again ...")
        clear()
try:
    BMI = float(wconverted / (hconverted ** 2))
    print("Your BMI is: ", BMI, "as of ", date.today())  # You had not defined the variable "date"
    print("You are using a", os.name, "system")
except ZeroDivisionError:
    print("Can not divide,\nZero Division Error .")
