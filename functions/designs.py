unprinted_designs = ['capa de celular', 'pingente de robô', 'dodecaedro']
completed_models = []

while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"Imprimindo modelo: {current_designs}")
    completed_models.append(current_designs)

print("\nOs seguintes modelos foram impressos: ")
for completed_model in completed_models:
    print(completed_model)