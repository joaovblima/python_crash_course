favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['jen', 'phil']
for person, language in favorite_languages.items():
    print(f"{person.title()} favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()} thank you for taking the poll.")