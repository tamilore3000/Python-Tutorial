monthConventions = {
    "Jan" : "January",
    "Feb" : "Feburary",
    "Mar" : "March",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sept" : "Sept",
    "Oct" : "October"
}

print(monthConventions.get("jan"))

customer = {
    "name" : "Tamilore Targaryen",
    "age" : 30,
    "is_verified" : True
}

print(customer.get("name", "Key word doesnt exist"))
customer["name"] = "Jack Sparrow"
print(customer.get("name", "Key word doesnt exist"))