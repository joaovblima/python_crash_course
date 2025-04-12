favorite_places = {
    'joao': ['rio de janeiro', 'chapada diamantina', 'gramado'],
    'ana': ['paris', 'veneza'],
    'lucas': ['tokyo']
}

for user, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{user.title()} favorite place is: ")
    else:
        print(f"\n{user.title()} favorite places are: ")
    for place in places:
        print(f"{place.title()}")
