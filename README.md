# Weather App

Welcome to the Weather App! This application allows you to check the current weather, get forecasts for multiple days, and view weather information for popular places. The app is built using Flask and leverages the WeatherAPI for weather data.

## Features

- Check current weather by city or your current location based on your ip.
- Get weather forecasts for 1, 3, 5, or 10 days.
- View weather information for popular cities (Currently - New York, London, Paris, Tokyo).

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shrilboss/weather-app.git
cd weather-app
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage your dependencies.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **On macOS/Linux:**

    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies

Create a `requirements.txt` file in your project directory with the following content:

```
Flask==2.1.0
requests==2.27.1
geocoder==1.38.1
```

Then, install the dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will be running at `http://127.0.0.1:5000/` by default.

### 2. Interact with the Application

- **Enter a city name** and select a forecast duration from the dropdown menu to get weather details.
- **Select "Current Location Weather"** to retrieve weather information for your current location.
- **View weather details** for popular cities like New York, London, Paris, and Tokyo.

## 3. Video demo

- Check out [Demo Video](https://drive.google.com/file/d/1mrZke2SGTHCj-jvhKz52NUDStXgapyZs/view?usp=sharing) to see the app in action!
  
## Credits

This application uses the [WeatherAPI](https://www.weatherapi.com/) for fetching weather data. Special thanks to WeatherAPI for providing free weather information.
