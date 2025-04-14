unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verificando usuario: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nOs seguintes usuarios foram verificados: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())   