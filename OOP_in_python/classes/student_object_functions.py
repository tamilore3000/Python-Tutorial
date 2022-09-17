from honors_checker import Student


student1 = Student("Oscar", "Accounting", 3.1)
student1.on_honor_roll
print(f"Is {student1.name} is on Honor Roll: {student1.on_honor_roll()}")
student2 = Student("Magnus", "Chess", 4.0)
print(f"Is {student2.name} is on Honor Roll: {student2.on_honor_roll()}")