rivers = {
    'amazon': 'brasil', 
    'nile': 'egypt',
    'danube': 'ukraine'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")