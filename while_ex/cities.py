prompt = '\nDigite as cidades que você visitou: '
prompt +="\nDigite sair quado terminar. "

while True:
    city = input(prompt)
    if city == 'sair':
        break
    else:
        print(f"Eu adoraria ir para {city.title()}.")