pet_1 = {
    'name': 'bolt',
    'type': 'cachorro',
    'owner': 'joao'
}

pet_2 = {
    'name': 'mimi',
    'type': 'gato',
    'owner': 'ana'
}

pet_3 = {
    'name': 'zazu',
    'type': 'papagaio',
    'owner': 'lucas'
}

pet_4 = {
    'name': 'nina',
    'type': 'hamster',
    'owner': 'maria'
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nPet name: {pet['name'].title()}")
    print(f"Type: {pet['type'].title()}")
    print(f"Owner: {pet['owner'].title()}")
