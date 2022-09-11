names = ["matilda", "sheldon", "Carlsen", "Kasparov", "Penny", "Daenerys Targaryen"]
names.insert(0 ,"David")
names.sort()

# To capitalize lists in  python
name_caps = [name.capitalize() for name in names]

print("David" in names , " \nChecks if an index exists") # Checks if an index exists 
print(name_caps)

for name in name_caps: # To print out the elements one per line 
    print(name)

sentence = " " .join(names)
print(sentence)