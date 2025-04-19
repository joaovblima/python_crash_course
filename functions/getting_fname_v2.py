def getting_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPor favor, diga seu nome: ")
    print("Pressione 'q' para sair aqualquer momento.")

    f_name = input("Nome: ")
    if f_name == 'q':
        break
    l_name = input("Sobrenome: ")
    if l_name == 'q':
        break


    formatted_name = getting_formatted_name(f_name, l_name)
    print(f"Olá {formatted_name}")