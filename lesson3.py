fruits = ["яблоко", "банан", "апельсин", "груша"]

print(fruits)
print(fruits[0])
print (fruits[-1])
print(len(fruits))

fruits.append("манго")
fruits.remove("банан")
fruits.insert(1, "киви")

print(fruits)
print(len(fruits))

for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

person = {
    "name": "yzalessky",
    "age": 41,
    "city": "Moscow",
    "is learning": True,
}

print(person["name"])
print(person["city"])

person["job"] = "analyst"
person["city"] = "Riga"
del person["is learning"]

print(person)

for j, v in person.items():
    print(f"{j}: {v}")