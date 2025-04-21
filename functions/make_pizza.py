def make_pizza(*toppings):
    print("\nFazendo uma pizza com os seguintes ingredientes: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('calabresa', 'file com queijo do reino', 'bacon')