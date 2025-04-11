current_users = ['maria', 'ingrid', 'maria alice', 'admin', 'lidiane', 'ana leticia']
new_users = ['maria', 'ingrid', 'joao', 'matheus', 'cicera']


for user in new_users:
    if user in current_users:
        print(f"{user.title()} its not available.")
    else:
        print(f"{user.title()} is available.")