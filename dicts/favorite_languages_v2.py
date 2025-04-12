favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'joao': 'rust',
}

list_person = ['joao', 'edward', 'lidiane', 'ingrid', 'leticia']

for name, language in favorite_languages.items():
    print(f"{name.title()} you love the language {language.title()}")
    if name in list_person:
        print(f"{name.title()} thank you for taking the poll.")