countries = {
    'Nigeria': {
        'capital': 'Abuja',
        'number_of_state': 36,
        'languagees': 30
    },
    'france': {
        'capital': 'paris',
        'number_of_state': 15,
        'languagees': 1
    },
    'canada': {
        'capital': 'Ottawa',
        'number_of_state': 12,
        'languagees': 2
    }
}

print(countries)
print(countries['canada'])
print(countries['canada']['number_of_state'])
for country, country_details in countries.items():
  capital = countries[country]['capital']
  print(f"The capital of {country} is {capital}")
