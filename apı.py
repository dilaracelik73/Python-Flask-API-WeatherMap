import requests
import os
from datetime import datetime
#Ana işler apı.py klasöründe yapıldı.Bu yüzden app.py dosyasına aktarım yapılması gerekecek.
#Çünkü Flask uygulamamız orada çalışacak.
#Raporda bahsedilen genel fonksiyondur.
#Gereken bilgiler burada api_data ile app.py dosyasına return edilecek ve fonksiyonlarda oradan ulaşılabilir olacaktır.
def get_weather_data(location):
    user_api = os.environ['current_weather_data']
    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"
    response = requests.get(complete_api_link)
    api_data = response.json()
    return api_data

#Yukarıda alınan api_key ve url ile bağlantı sağladıktan sonra karşımıza json dosyası çıkar ve oradan gereken bilgiler çekilir.
#Bunun içinde ayrı ayrı fonksiyonlar oluşturulur.
def temperature_city_func(api_data):
    formatted_temperature = "{:.2f}".format(api_data['main']['temp'] - 273.15)
    return formatted_temperature
def weather_desc_func(api_data):
    return api_data['weather'][0]['description']
def humidity_func(api_data):
    return api_data['main']['humidity']
def wind_speed_func(api_data):
    return api_data['wind']['speed']
def date_time_func():
    return datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
