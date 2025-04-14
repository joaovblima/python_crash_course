responses = {}
active_responses = True

while active_responses:
    name = input("\nQual o seu nome? ")
    reponse = input("Qual lugar você gostaria de visitar? ")
    
    responses[name] = reponse
    
    option = input("\nDeseja que outra pessoa responta? (sim/não) ")
    if option == 'não':
        active_responses = False

for name, response in responses.items():
    print(f"{name.title()} gostaria de visitar {reponse.title()}")