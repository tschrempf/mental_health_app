from flask import Flask, request, jsonify, g
import sqlite3
from weather import weather_bp  # Import des Wetter-Blueprints

app = Flask(__name__)

# Absoluter Pfad zur SQLite-Datenbank (anpassen, falls nötig)
DATABASE = '/path/to/your/Recommendation_Database.db'

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

# Funktion: Optionen basierend auf Wetter abrufen
def get_options_based_on_weather(weather):
    conn = get_db_connection()
    query = """
        SELECT option_name, description
        FROM options
        WHERE weather = ?
    """
    cursor = conn.execute(query, (weather,))
    rows = cursor.fetchall()
    conn.close()
    
    options = [{'option_name': row['option_name'], 'description': row['description']} for row in rows]
    return options

# Funktion: Empfehlungen aus der Datenbank abrufen
def get_recommendations(weather, energy_level, interest):
    conn = get_db_connection()
    query = """
        SELECT activity, description, media1, media2, media3
        FROM recommendations
        WHERE weather = ? AND energy_level = ? AND interest = ?
    """
    cursor = conn.execute(query, (weather, energy_level, interest))
    rows = cursor.fetchall()
    conn.close()
    
    recommendations = [{
        'activity': row['activity'],
        'description': row['description'],
        'media': [media for media in [row['media1'], row['media2'], row['media3']] if media]
    } for row in rows]
    return recommendations

# Standardroute zur Überprüfung, ob die API läuft
@app.route('/')
def home():
    return "TEST."

# Route: Optionen abrufen
@app.route('/options', methods=['GET'])
def options_endpoint():
    from weather import fetch_weather  # Wetterfunktion importieren
    weather, status = fetch_weather()
    if status != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), status

    options = get_options_based_on_weather(weather)
    if not options:
        return jsonify({'message': 'No options available for the current weather.'}), 404
    
    return jsonify({'weather': weather, 'options': options})

# Route: Empfehlungen abrufen
@app.route('/recommendations', methods=['POST'])
def recommendations_endpoint():
    from weather import fetch_weather  # Wetterfunktion importieren
    data = request.json
    energy_level = data.get('energy_level')  # Erwartet: very-energetic, good, neutral, low, very-low
    interest = data.get('interest')  # Erwartet: outdoor, fitness, yoga, home, meditation

    if not energy_level or not interest:
        return jsonify({'error': 'Energy level and interest are required'}), 400

    weather, status = fetch_weather()
    if status != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), status

    recommendations = get_recommendations(weather, energy_level, interest)
    if not recommendations:
        return jsonify({'message': 'No recommendations found for the given inputs.'}), 404

    return jsonify({
        'city': 'Wien',
        'weather': weather,
        'energy_level': energy_level,
        'interest': interest,
        'recommendations': recommendations
    })

# Blueprint registrieren
app.register_blueprint(weather_bp)

# Start der Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=True, port=8000)
