from rich import print
import requests

city = 'tokyo'
api_key = 'da7a1b3d460dbtbf7b304o1bb99604f1'
api_url = f'https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}'
response = requests.get(api_url)
weather = response.json()
print(weather)
city_temperature = weather['temperature']['current']
city_temperature = round(city_temperature)
country = weather['country']
humidity = weather['temperature']['humidity']
print(f'it is current {city_temperature} C in {city},{country} and the humidity is {humidity}'
)

