# Using method Overiding in python 

class Shape:
    width = 0
    height = 0

    def area(self):
        print("Parent class Area")

class Triangle(Shape):
    def __init__(self , w, h):
        self.width= w
        self.height = h
    def area(self):
        print("The area of the Triangle is: ", (self.height * self.width/2))
call = Shape()
call.area()
call = Triangle(23,23)
call.area()

    
class PrimaSchool():
    def name(self):
        print("Halifield Primary School")
    def location(self):
        print("Lekki") 
    def established(self):
        print("2018")
class SecSchool():
    def name(self):
        print("Halifield College")
    def location(self):
        print("Maryland") 
    def established(self):
        print("2008")

callingPrima = PrimaSchool()
callingSec = SecSchool()

for school in (callingPrima.callingSec):
    school.name()
    school.location
    school.established()

class PrimarySchool:
    def __init__(self, name, location, year):
        self.name = name
        self.location = location
        self.year = year

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_year(self):
        return self.year


class SecondarySchool:
    def __init__(self, name, location, year):
        self.name = name
        self.location = location
        self.year = year

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_year(self):
        return self.year


# Create a tuple of objects
schools = (PrimarySchool("ABC Primary School", "Lagos", 1980),
           SecondarySchool("XYZ Secondary School", "Abuja", 1995),
           PrimarySchool("DEF Primary School", "Port Harcourt", 1975),
           SecondarySchool("UVW Secondary School", "Kano", 2000))

# Iterate through the tuple of objects
for school in schools:
    # Call the methods without being concerned which class type each object is
    print(f"School Name: {school.get_name()}, Location: {school.get_location()}, Established: {school.get_year()}")


class PrimarySchool:
    def __init__(self, name, location, year):
        self.name = name
        self.location = location
        self.year = year

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Year Established: {self.year}")

class SecondarySchool:
    def __init__(self, name, location, year):
        self.name = name
        self.location = location
        self.year = year

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Year Established: {self.year}")

primary_school1 = PrimarySchool("St. Mary's Primary School", "Lagos", 1965)
primary_school2 = PrimarySchool("Redemption Primary School", "Abuja", 1978)
secondary_school1 = SecondarySchool("Federal Government College", "Kano", 1952)
secondary_school2 = SecondarySchool("Kings College", "Lagos", 1909)

schools = (primary_school1, primary_school2, secondary_school1, secondary_school2)

for school in schools:
    school.get_details()
