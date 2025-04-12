person = {
    'first_name': "joao",
    "last_name": "lima",
    "age": 28,
    "city": "uniao dos palmares",
}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])
message = f"{person['first_name']} {person['last_name']}, have {person['age']} years old and living in {person['city']}"
print(message.title())