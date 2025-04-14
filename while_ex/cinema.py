prompt ="\nDiga sua idade: "
active = True

while active:
    idade = int(input(prompt))
    if idade <3:
        print("Seu ingreso é gratuito.")
        active = False
    elif idade > 3 and idade <12:
        print("Seu ingresso custa R$10.")
        active = False
    else:
        print("Seu ingresso é R$15.")
        active = False