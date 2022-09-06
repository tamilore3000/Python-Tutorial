# BMI CALCULATOR IN PYTHON
import os
from datetime import datetime


# define our clear function
def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def weight_converter(w):
    global converted
    weight_unit = input("What is the weight unit Kgs or Lbs: ")
    if weight_unit.upper() == "KG":
        converted = w / 1  
        print("weight in kg is: ", converted)
    elif weight_unit.upper() == "LBS":
        converted = w / 2.2
        print("weight in kg is: ", converted)
    return converted


def height_converter(w):
    global converted
    height_unit = input("What is the weight unit meters or feet: ")
    if height_unit.upper() == "METERS":
        converted = w / 1  
        print("height in meters is: ", converted)
    elif height_unit.upper() == "FEET":
        converted = w / 3.281
        print("height in meters is: ", converted)
    return converted


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


date = datetime.now()
BMI = float(wconverted / (hconverted ** 2))
print("Your BMI is: ", BMI, "as of ", date) 
print("You are using a", os.name, "system")
