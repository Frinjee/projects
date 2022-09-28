import requests

API_KEY = '_KEY'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

zip_code = input('Enter a zip code: ')
request_url = f'{BASE_URL}?zip={zip_code}&appid={API_KEY}'
res = requests.get(request_url)

if res.status_code == 200:
	data = res.json()
	weather = data['weather'][0]['description']


	_low = round(data['main']['temp_min'] - 273.15, 0)
	_high = round(data['main']['temp_max'] - 273.15, 0)
	
	
	temp_cels = round(data['main']['temp'] - 273.15, 2)
	temp_feel = round(data['main']['feels_like'] - 273.15, 0)
	humidity = data['main']['humidity']
	
	wind_speed = data['wind']['speed']
	
	city_name = data['name']
	country = data['sys']['country']

	print(f'{city_name}, {country} \nCurrent Temperature: {temp_cels}°c - Feels like: {temp_feel}°c \nLow of: {_low}°c & High of: {_high}°c')
	print(f'Humidity - {humidity} \nWind speeds of {wind_speed}')
	#print(f'Current Temperature is: {temp_cels}° in {city_name}, with {weather}')
	#print(data)

else:
	print('An error occurred')




''' format
{'coord': {'lon': -76.6681, 'lat': 39.2092}, 
'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}],
'base': 'stations', 
'main': {'temp': 292.92, 'feels_like': 292.39, 'temp_min': 291.08, 'temp_max': 294.5, 'pressure': 1020, 'humidity': 55}, 
'visibility': 10000, 'wind': {'speed': 3.58, 'deg': 292, 'gust': 8.05}, 'clouds': {'all': 40}, 'dt': 1664388796, 
'sys': {'type': 1, 'id': 3531, 'country': 'US', 'sunrise': 1664362786, 'sunset': 1664405686}, 
'timezone': -14400, 'id': 0, 'name': 'Linthicum Heights', 'cod': 200}

'''
