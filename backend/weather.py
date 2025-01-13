import requests
from flask import Blueprint, jsonify

# Open-Meteo API-Details
OPEN_METEO_URL = 'https://api.open-meteo.com/v1/forecast'
LATITUDE = 48.2082  # Wien
LONGITUDE = 16.3738  # Wien

# Blueprint für Wetter
weather_bp = Blueprint('weather', __name__)

# Funktion: Wetterdaten abrufen
def fetch_weather():
    params = {
        'latitude': LATITUDE,
        'longitude': LONGITUDE,
        'current_weather': True
    }
    response = requests.get(OPEN_METEO_URL, params=params)
    if response.status_code != 200:
        return None, response.status_code
    
    weather_data = response.json()
    weather_code = weather_data['current_weather']['weathercode']
    
    # Wettercode auf Wetterbedingungen mappen
    weather_map = {
        0: 'sunny',
        1: 'cloudy',
        2: 'cloudy',
        3: 'cloudy',
        45: 'cloudy',
        48: 'cloudy',
        51: 'rain',
        53: 'rain',
        55: 'rain',
        61: 'rain',
        63: 'rain',
        65: 'rain',
        66: 'rain',
        67: 'rain',
        71: 'snow',
        73: 'snow',
        75: 'snow',
        77: 'snow',
        80: 'rain',
        81: 'rain',
        82: 'rain',
        85: 'snow',
        86: 'snow',
        95: 'rain',
        96: 'rain',
        99: 'rain'
    }
    
    # Wetterwert formatieren
    def format_weather(weather):
        if weather == 'windy':
            return 'windy'  # Ausnahme für 'windig'
        return weather.capitalize()  # Erster Buchstabe groß, Rest klein

    weather = format_weather(weather_map.get(weather_code, 'sonnig'))  # Standard: sonnig
    return weather, 200

# Route: Wetterdaten abrufen
@weather_bp.route('/weather', methods=['GET'])
def weather_endpoint():
    weather, status = fetch_weather()
    if status != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), status
    return jsonify({'city': 'Wien', 'weather': weather}), 200
