import random

for i in range(3):
    print(random.randint(1,20))

members = ["Carlsen", "Kasparov", "Karpov", "Fischer", "Capablanca", "Murphy"]
leader = random.choice(members)
print("The best is: ", leader)
