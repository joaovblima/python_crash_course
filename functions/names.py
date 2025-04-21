def greet_users(users):
    for user in users:
        print(f"Hi {user.title()}")


users_test = ['joao', 'touro', 'lidiane']

greet_users(users_test)