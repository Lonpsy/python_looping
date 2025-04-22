"""Create a Repl
Ask for a city name
Display the current weather for this specific city such as
It is currently 23ºC in Paris, France”"""
from rich import print
import requests

city = input('Enter your current city ')
city = city.strip()
api_key = 'da7a1b3d460dbtbf7b304o1bb99604f1'
api_url = f'https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}'
weather = requests.get(api_url)
weather = weather.json()
print(weather)
temperature = round(weather['temperature']['current'])
country = weather['country']
print(f'It is currently {temperature}ºC in {city}, {country}')
