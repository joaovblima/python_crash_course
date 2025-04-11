users = ['maria', 'ingrid', 'maria alice', 'admin', 'lidiane', 'ana leticia']
#users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else: 
    print("We need find some users.")