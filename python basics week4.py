# Exercise 1
weather = {
    "city": "Lisbon",
    "country": "Portugal",
    "temperature": 17.94,
    "humidity": 77
}

# Display the weather in Lisbon such as:
city = weather["city"]
celcius_temperature = round(weather["temperature"])
farenheit_temperature = round(celcius_temperature * (9 / 5) + 32)
print(
    f'it is currently {celcius_temperature}C({farenheit_temperature}F) in {city}'
)
# It is 18ºC (64ºF) in Lisbon, Portugal, the humidity level is 77%.

# Exercise 2
forecast = {
    "city": "Lisbon",
    "country": "Portugal",
    "daily": [17.76, 13.08, 12.14, 11.25, 14.29]
}

# Display the forecast in Lisbon such as:
# The forecast for Lisbon, Portugal for the next 5 days is:
cities = forecast["city"]
country = forecast["country"]
print(f' The forecast for {cities}, {country} for the next 5 days is:')
index = 0
index_2 = 0
for component in forecast["daily"]:

    daily_temperature = round(forecast["daily"][index_2])
    index = index + 1
    index_2 = index_2 + 1
    # Day 1: 18ºC
    # Day 2: 13ºC
    # Day 3: 12ºC
    # Day 4: 11ºC
    # Day 5: 14ºC
    print(f'Day {index}: {daily_temperature} degree Celsius')
