import requests

response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=51.9&longitude=4.5&current_weather=true')
print(response.status_code)
print(response.json())


data = response.json()
weather = data['current_weather']
print(f"Temperature: {weather['temperature']}°C")
print(f"Wind speed: {weather['windspeed']} km/h")
print(f"Is daytime: {bool(weather['is_day'])}")