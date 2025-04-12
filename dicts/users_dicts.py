users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for user, user_info in users.items():
    print(f"\nUsername: {user}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location'].title()}"
    print(f"Full name: {full_name.title()}")
    print(f"Location: {location.title()}")