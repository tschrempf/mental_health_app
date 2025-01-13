from flask import Flask, request, jsonify, g
import sqlite3
from weather import weather_bp, fetch_weather  # Import des Wetter-Blueprints und der Funktion

app = Flask(__name__)
app.register_blueprint(weather_bp)

# Absoluter Pfad zur SQLite-Datenbank
DATABASE = './Recommendation_Database.db'

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

# Funktion: Empfehlungen aus der Datenbank abrufen
def get_recommendations(weather, energy_level, interest):
    conn = get_db_connection()
    query = """
    SELECT activity, description, "media", "media,,,"
    FROM recommendations
    WHERE weather = ? AND "energy level" = ? AND interest = ?
"""
    print(f"Executing query: {query}")
    print(f"With parameters: weather={weather}, energy_level={energy_level}, interest={interest}")
    cursor = conn.execute(query, (weather, energy_level, interest))
    rows = cursor.fetchall()
    conn.close()

    recommendations = [
        {
            'activity': row['activity'],
            'description': row['description'],
            'media': [media for media in [row['media'], row['media,,,']] if media]
        }
        for row in rows
    ]
    return recommendations

# Route: Empfehlungen abrufen
@app.route('/recommendations', methods=['GET'])
def recommendations_endpoint():
    # Eingaben für energy_level und interest vom Frontend abrufen
    energy_level = request.args.get('energy_level')  # Erwartet: very-energetic, good, neutral, low, very-low
    interest = request.args.get('interest')  # Erwartet: Outdoor, Fitness, Yoga, Home, Meditation

    if not energy_level or not interest:
        return jsonify({'error': 'Query parameters "energy_level" and "interest" are required'}), 400

    # Wetter abrufen
    weather, status = fetch_weather()
    if status != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), status

    # Recommendations für das aktuelle Wetter, energy_level und interest abrufen
    recommendations = get_recommendations(weather, energy_level, interest)
    if not recommendations:
        return jsonify({'message': f'No recommendations found for the weather: {weather}, energy level: {energy_level}, interest: {interest}'}), 404

    # Ausgabe erstellen und an das Frontend zurückgeben
    return jsonify({
        'city': 'Wien',
        'weather': weather,
        'energy_level': energy_level,
        'interest': interest,
        'recommendations': recommendations
    })

# Start der Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=True, port=8000)
