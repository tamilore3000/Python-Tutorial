# BMI CALCULATOR IN PYTHON
import os
import bmi_converter
from datetime import date


# define our clear function
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


while True:
    try:
        age = input("How old are you? ")
        age = int(age)

        weight = input("What is your weight: ")
        weight = float(weight)
        wconverted = bmi_converter.weight_converter(weight)

        height = input("What is your height: ")
        height = float(height)
        hconverted = bmi_converter.height_converter(height)
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
