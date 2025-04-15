countries_loved = {"France": "Paris", "Canada": "Ottawa", "America": "USA"}
print(countries_loved)
print("Countries i would like to visit are:")
index = 0
for country, capital in countries_loved.items():
  index = index + 1
  print(f"{index}.{country}(capital city: {capital})")
