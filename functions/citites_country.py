def city_country(city, country):
    message = f"{city}, {country}"
    return message.title()

sao_paulo = city_country("são paulo", "brasil")
print(sao_paulo)