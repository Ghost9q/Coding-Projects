import requests
from PIL import Image
from io import BytesIO
base_url = 'http://api.weatherapi.com/v1'
# create an account at www.weatherapi.com website to obtain an api key then copy and paste your key below.
key = 'enter your key here'
def current_weather(city):
    response = requests.get(f'{base_url}/current.json?key={key}&q={city}')
    if response.status_code == 200:
        weather_data = response.json()

        print(f'city: {weather_data['location']['name']}')
        print(f'Country: {weather_data['location']['country']}')
        print(f'Latitude: {weather_data['location']['lat']}')
        print(f'Longitude: {weather_data['location']['lon']}')
        print(f'Weather: {weather_data['current']['condition']['text']}')
        print(f'Temperature(C): {weather_data['current']['temp_c']}')
        print(f'Temperature(F): {weather_data['current']['temp_f']}')
        
        return weather_data
    else:
        return 'failed to retrieve data. Please get new api key of check your internet connection.'
city = input('Enter the name of the city: ')
weather_data = current_weather(city)



