from flask import Flask, request, jsonify, g
import sqlite3
import requests
 
app = Flask(__name__)
 
# Pfad zur SQLite-Datenbank
DATABASE = '../Database/Recommendation_Database.db'
 
# Open-Meteo API-Details
OPEN_METEO_URL = 'https://open-meteo.com/en/docs#latitude=48.2085&longitude=16.3721'
LATITUDE = 48.2082  # Wien
LONGITUDE = 16.3738  # Wien
 
# Verbindung zur SQLite-Datenbank herstellen
def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # Ergebnisse als Dictionary
    return g.db
 
# Verbindung schließen
@app.teardown_appcontext
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()
 
# API-Route: Empfehlungen basierend auf Wetter, Energielevel und Interessen
@app.route('/personalized_recommendations', methods=['POST'])
def personalized_recommendations():
    # Eingaben des Benutzers
    data = request.json
    energy_level = data.get('energy_level')  # Erwartet: very-energetic, good, neutral, low, very-low
    interest = data.get('interest')  # Erwartet: outdoor, fitness, yoga, home, meditation
 
    # Validierung der Eingaben
    if not energy_level or not interest:
        return jsonify({'error': 'Energy level and interest are required'}), 400
 
    # Wetterdaten von Open-Meteo abrufen (nur für Wien)
    params = {
        'latitude': LATITUDE,
        'longitude': LONGITUDE,
        'current_weather': True
    }
    weather_response = requests.get(OPEN_METEO_URL, params=params)
    if weather_response.status_code != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), weather_response.status_code
 
    weather_data = weather_response.json()
    # Wettercode extrahieren
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
    weather = weather_map.get(weather_code, 'sonnig')  # Standard: sonnig
 
    # Datenbankabfrage basierend auf Wetter, Energielevel und Interesse
    conn = get_db_connection()
    query = """
        SELECT activity, description, media1, media2, media3
        FROM recommendations
        WHERE weather = ? AND energy_level = ? AND interest = ?
    """
    cursor = conn.execute(query, (weather, energy_level, interest))
    rows = cursor.fetchall()
    conn.close()
 
    # Vorschläge aus den Ergebnissen extrahieren
    recommendations = [{
        'activity': row['activity'],
        'description': row['description'],
        'media': [row['media1'], row['media2'], row['media3']]
    } for row in rows]
 
    # Filtere leere Medienlinks aus der Liste
    for rec in recommendations:
        rec['media'] = [media for media in rec['media'] if media]
 
    if not recommendations:
        return jsonify({'message': f'No recommendations found for the given inputs in Wien.'}), 404
 
    return jsonify({
        'city': 'Wien',
        'weather': weather,
        'energy_level': energy_level,
        'interest': interest,
        'recommendations': recommendations
    })
 
# Start der Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=True)
    