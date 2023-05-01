# Create a parameterized constructor for farm fruits. The
# parameter is called fruitname. The Fruit class has two other methods.
# The first one queries a person for the type of fruit he/she loves, and
# another responds with “I Love xyz” where xyz is the actual fruit name
# supplied as an argument to method invocation. The class should be
# instantiated accordingly.The program output should be captured.

class FarmFruits():
    def __init__(self,fruitname) :
        self.fruitname = fruitname
    
    def favFruit(self):
        print("What is your favorite fruit")

    def response(self,fruitname):
        print("I love " +  fruitname)

fruit = FarmFruits("Banana")
fruit.favFruit()
fruit.response(fruitname="Banana")

# Create a Non-Parameterized constructor for farm fruits. As in
# parameterized case, the Fruit class has two other methods. The first one
# queries a person for the type of fruit he/she loves, and another responds
# with “I Love xyz” where xyz is the actual fruit name, defined within the
# constructor as an instance variable. The class should be instantiated
# accordingly.The program output should be captured.

class FarmFruits():
    def __init__(self) :
        self.fruit = "Pineapples"
    
    def favFruit(self):
        print("What is your favorite fruit")

    def response(self):
        print("I love " +  self.fruit)

fruit = FarmFruits()
fruit.favFruit()
fruit.response()
