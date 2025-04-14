responses = {}
polling_active = True

while polling_active:
    name = input("\nQual seu nome? ")
    response = input("Qual montanha você gostaria de escalar um dia? ")

    responses[name] = response

    repeat = input("\nGostaria de deixar outra pessoa responder? (sim/não) ")
    if repeat == 'não':
        polling_active = False

print("\n--Resultados da enquente--")
for name, response in responses.items():
    print(f"{name} gostaria de escalar {response}")