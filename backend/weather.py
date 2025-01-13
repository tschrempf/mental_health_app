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
        0: 'sonnig',
        1: 'bewölkt',
        2: 'bewölkt',
        3: 'bewölkt',
        45: 'bewölkt',
        48: 'bewölkt',
        51: 'regen',
        53: 'regen',
        55: 'regen',
        61: 'regen',
        63: 'regen',
        65: 'regen',
        66: 'regen',
        67: 'regen',
        71: 'schnee',
        73: 'schnee',
        75: 'schnee',
        77: 'schnee',
        80: 'regen',
        81: 'regen',
        82: 'regen',
        85: 'schnee',
        86: 'schnee',
        95: 'regen',
        96: 'regen',
        99: 'regen'
    }
    
    # Wetterwert formatieren
    def format_weather(weather):
        if weather == 'windig':
            return 'windig'  # Ausnahme für 'windig'
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
