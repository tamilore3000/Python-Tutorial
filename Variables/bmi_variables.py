# BMI CALCULATOR IN PYTHON
from datetime import datetime
import os , time 

#from time import clock_settime

# define our clear function
def clear():

    # for windows
    if os.name == 'nt':
        os.system('cls')
     
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

while True:
    try:
        age = input("How old are you? ")
        age = int(age)
        weight = input("What is your weight: ")
        weight = float(weight)
        height= input("What is your height: ")
        height = float(height)
        break
    except ValueError:
        #os.system(clock_settime)
        print("No valid integer! Please try again ...")
        ~clear()

date = datetime.now()
print("You are using a",os.name,"system")
BMI = float(weight / height ** 2)   
print("Your BMI is: ", BMI, "as of ", date) 
