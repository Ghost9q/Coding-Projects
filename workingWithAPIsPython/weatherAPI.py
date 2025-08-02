import requests
from PIL import Image
from io import BytesIO
base_url = 'http://api.weatherapi.com/v1'
key = '2dbe97d9d79640f0ae095014251807'
def current_weather(city):
    response = requests.get(f'{base_url}/current.json?key={key}&q={city}')
    if response.status_code == 200:
        weather_data = response.json()
        # if you wanted to display the weather icon as well you can do this ut unfortunately you cannot display images in the terminal so if created a program with a gui someday you might use this.
        #image_url = f"https:{weather_data['current']['condition']['icon']}"
        #image_response = requests.get(image_url)
        #image = Image.open(BytesIO(image_response.content))
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
weather_data = current_weather('Frankfurt')
