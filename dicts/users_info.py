user_1 = {
    'nickname': 'benadryl',
    'first': 'joao',
    'last': 'lima',
}

user_2 = {
    'nickname': 'cafecomleite',
    'first': 'ana',
    'last': 'souza',
}

user_3 = {
    'nickname': 'zangado22',
    'first': 'lucas',
    'last': 'pereira',
}

users = [user_1, user_2, user_3]

for user in users:
    print(f"\nUsername: {user['nickname']}")
    full_name = f"{user['first']} {user['last']}"
    print(f"Full name: {full_name.title()}")
