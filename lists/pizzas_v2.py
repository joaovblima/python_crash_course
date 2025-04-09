pizzas = ["banana nevada", "calabresa especial", "filé com queijo do reino"]
friend_pizzas = pizzas[:]
pizzas.append('carne de sol')
print("Minhas pizzas favoritas sao: ")
for pizza in pizzas:
    print(pizza.title())
print("\nAs pizzas favoritas do meu amigo são: ")
for pizza in friend_pizzas:
    print(pizza.title())