# Import necessary modules
from flask import Flask, render_template, request
import requests
import geocoder

app = Flask(__name__)

# Define the API key
API_KEY = "eb4c54849afb42309d7211800243108"

# Define a function to get the weather data
def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    return response.json()

# Define a function to get the forecast data
def get_forecast(city, days):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}"
    response = requests.get(url)
    return response.json()

# Define a function to get the current location's weather
def get_curr_location_weather():
    g = geocoder.ip('me')
    query_val = None
    try:
        query_val= g.postal
    except:
        try:
            query_val = g.city
        except:
            lat, lng = g.latlng
            query_val = f"{lat},{lng}"

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={query_val}"
    response = requests.get(url)
    return response.json()

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    forecast_data = None
    current_location_weather = None
    popular_places_weather = []

    if request.method == 'POST':
        city = request.form['city']
        days = request.form.get('days', '')
        if days == 'current_location':
            current_location_weather = get_curr_location_weather()
        elif days == "":
            weather_data = get_weather(city)
        elif days == "1":
            weather_data = get_weather(city)
        else:
            forecast_data = get_forecast(city, days)

    popular_places = ['New York', 'London', 'Paris', 'Tokyo']
    for place in popular_places:
        popular_places_weather.append(get_weather(place))

    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data, popular_places_weather=popular_places_weather, current_location_weather=current_location_weather)

if __name__ == '__main__':
    app.run(debug=True)
