from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "eb4c54849afb42309d7211800243108"  # Replace with your OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    return response.json()

def get_forecast(city, days):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}"
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    forecast_data = None
    popular_places_weather = []

    if request.method == 'POST':
        city = request.form['city']
        days = int(request.form.get('days', 1))
        
        if days == 1:
            weather_data = get_weather(city)
        else:
            forecast_data = get_forecast(city, days)

    # Example popular places
    popular_places = ['New York', 'London', 'Paris', 'Tokyo']
    for place in popular_places:
        popular_places_weather.append(get_weather(place))

    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data, popular_places_weather=popular_places_weather)

if __name__ == '__main__':
    app.run(debug=True)
