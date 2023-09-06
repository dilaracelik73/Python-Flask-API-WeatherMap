from flask import Flask, request, render_template
from apı import get_weather_data, temperature_city_func, weather_desc_func, humidity_func, wind_speed_func, date_time_func
#Yukarıda apı dosyasından fonksiyonlar import edilmiştir.

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        api_data = get_weather_data(location)

# apı dosyasındaki veriler orada return edilen api_data ile bağlantılı hale getirilmiştir.
        temperature = temperature_city_func(api_data)
        weather_description = weather_desc_func(api_data)
        humidity = humidity_func(api_data)
        wind_speed = wind_speed_func(api_data)

# işlemler hatasız bir şekilde işlerse o zaman weather.html sayfasına yönlendirilme yapılacak ve bilgiler çekilecek.
        return render_template('weather.html',
                               location=location.title(),
                               date_time=date_time_func(),
                               temperature=temperature,
                               weather_desc=weather_description.title(),
                               humidity=humidity,
                               wind_speed=wind_speed)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
