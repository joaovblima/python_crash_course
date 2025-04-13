fav_numbers = {
    'joao': [9, 3],
    'lele': [8],
    'touro': [7, 14, 21],
    'ingrid': [6, 12]
}

for user, numbers in fav_numbers.items():
    if len(numbers) == 1:
        print(f"\n{user.title()} favorite number is: ")
    else:
        print(f"\n{user.title()} favorite numbers are: ")
    for number in numbers:
        print(f"{number}")