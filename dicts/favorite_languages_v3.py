favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()} favorite language is:")
    else:
        print(f"\n{name.title()} favorite languages are:")
    for language in languages:
        print(f"{language.title()}")