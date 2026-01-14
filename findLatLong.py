import requests
import json

city_name = 'Buenos Aires'
state_code = 'BA'
country_code= 'AR'
API_KEY = '30ee784a80d81480dab1749d33980112'  # Esta API key no es real
url =f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}'
response = requests.get(url)
print(response.text) 


if response.status_code == 200:
    response_data = json.loads(response.text)
    print(response_data)

