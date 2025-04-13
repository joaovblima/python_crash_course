cities = {
    'tokyo': {
        'country': 'japão',
        'population': 37400068,
        'fact': 'é a maior área metropolitana do mundo'
    },
    'paris': {
        'country': 'frança',
        'population': 2148000,
        'fact': 'abriga a famosa torre eiffel'
    },
    'rio de janeiro': {
        'country': 'brasil',
        'population': 6748000,
        'fact': 'conhecida pelo cristo redentor e o carnaval'
    }
}

for citie, information in cities.items():
    print(f"\n{citie.title()} its located in {information['country'].title()}, have {information['population']} inhabitants and has a very curious fact which is {information['fact']}")