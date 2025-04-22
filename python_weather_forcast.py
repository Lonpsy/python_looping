def display_weather(city):
  print(f'The temperature in {city} is 25°C ')


city = input('input your city ')
city = city.strip()
if city:
  display_weather(city)
else:
  print('you need to enter a valid city')
