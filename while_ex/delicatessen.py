sandwich_orders = [
    "Cheeseburger",
    "Frango Grelhado",
    "BLT",
    "Atum",
    "Vegetariano",
    "Pastrami",
    "Carne Louca",
    "Misto Quente",
    "Pastrami",
    "Queijo Quente",
    "Cuban Sandwich", 
    "Pastrami"
]
finished_sandwich = []

print("A delicatessen ficou sem pastrami")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Fiz seu sanduiche de {current_sandwich}")
    finished_sandwich.append(current_sandwich)
print()
for sandwich in finished_sandwich:
    print(f"Foi feito sanduiche de {sandwich}")