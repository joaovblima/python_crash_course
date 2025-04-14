prompt = "\nDigite a cobertura que você quer em sua pizza:"
prompt += "\nDigite sair para encerrar o programa. "

while True:
    topping = input(prompt)
    if topping == 'sair':
        break
    else:
        print(f'{topping.title()} adicionado a sua pizza.')