import json

employee = '{"employee": {"Firstname": "Bob", "age": 30, "city": "Lagos"}}'

# parse employee:
details = json.loads(employee)

print(details)

person = {
    "name" : "Bond",
    "NO" : "007", 
    "branch" : "M15"
}

to_json = json.dumps(person)

print(to_json)

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

employee1 = {
    "firstname" : "James",
    "lastname" : "Bond",
    "marital status" :  "single",
    "suspended" : False , 
    "children" : False,
    "cars" : [
        {"model": "Audi"},
        {"model" : "BMW"}
        ],
    "agent" : True 
}

print(json.dumps(employee1, indent=4))

