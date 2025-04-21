def create_sandwich(*items):
    print("\nCriando um sanduiche com os seguintes ingredientes: ")
    for item in items:
        print(f"- {item}")


create_sandwich("chocolate")
create_sandwich("queijo", "presunto", "cebola")
create_sandwich('calabresa', 'hamburguer', 'cebola caramelizada', 'picles')