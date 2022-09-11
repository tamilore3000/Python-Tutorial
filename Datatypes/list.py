names = ["matilda", "sheldon", "Carlsen", "Kasparov", "Penny", "Daenerys", "Targaryen", "Aegon", "Mufasa"]
names.insert(0 ,"David")
print("David" in names , " -Checks if an index exists") # Checks if an index exists 
names.sort()

# To capitalize lists in  python
name_caps = [name.capitalize() for name in names]
print(name_caps)

# for name in name_caps: # To print out the elements one per line 
#     print(name)

sentence = " " .join(names)
print(print("To print the elements joined together"),sentence)
names.pop()
print(names)
names.remove("Targaryen")
print(names)
print(names[0:3])