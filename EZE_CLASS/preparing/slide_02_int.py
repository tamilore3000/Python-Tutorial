# Constructors are implemented using the __init__ method 

class Person:
    def __init__(self,name):
        self.name = name 

    def call(self):
        print("Your name is ", self.name)
              
Human = Person("Tami")
Human.call()

# A Book has four chapters, with number of pages as 20, 10, 17 
# and 21 respectively. Create a Python class known as Book, 
# with four fields as number of pages in each of the chapters

class Book:
    def __init__(self,pg_no_chapt1,pg_no_chapt2,pg_no_chapt3,pg_no_chapt4):
        self.pg_no_chapt1 = pg_no_chapt1
        self.pg_no_chapt2 = pg_no_chapt2
        self.pg_no_chapt3 = pg_no_chapt3
        self.pg_no_chapt4 = pg_no_chapt4

book_page = Book(20,10,17,21)
print(book_page.pg_no_chapt1)  # Output: 20
print(book_page.pg_no_chapt2)  # Output: 10
print(book_page.pg_no_chapt3)  # Output: 17
print(book_page.pg_no_chapt4)  # Output: 21
    
# Create a class called Mobile, consisting of a constructor and two
# methods. Method 1 displays a message, asking for which mobile network
# you use, while Method 2 lists them. The class should be instantiated as an
# object called mynet, and used to invoke the two methods earlier defined.
# Run the program in Python environment and capture the output.

class Mobile:
    def __init__(self,mtn,airtel,glo,_9mobile):
        self.mtn = mtn
        self.airtel = airtel
        self.glo = glo
        self._9mobile = _9mobile

    def display(self):
        print("Which mobile network do you use?")

    def lists(self):
        print(f"List of networks are \n 1. {self.mtn}, \n 2. {self.airtel} \n 3. {self.glo} \n 4. {self._9mobile}")

mynet = Mobile("MTN", "AIRTEL", "GLO", "9MOBILE")
mynet.display()
mynet.lists()

# Using the same class Mobile, create a python main method.
# Ensure that the main method is used to invoke the two methods earlier
# defined, after performing appropriate confirmations. Run the program in
# Python environment and capture the output.

def main():
    mynet = Mobile("MTN", "AIRTEL", "GLO", "9MOBILE")
    mynet.display()
    mynet.lists()

if __name__ == "__main__":
    main()
# if __name__ == "__main__": statement to ensure that certain code is only executed when the module is run as the main program