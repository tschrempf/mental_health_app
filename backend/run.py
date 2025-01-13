from flask import Flask, request, jsonify, g
import sqlite3
from weather import weather_bp, fetch_weather  # Import des Wetter-Blueprints und der Funktion

app = Flask(__name__)
app.register_blueprint(weather_bp)

# Absoluter Pfad zur SQLite-Datenbank
DATABASE = './Recommendation_Database.db'

import os

# Debugging: Zeige den absoluten Pfad der Datenbank an
print(f"Verwendete Datenbank: {os.path.abspath(DATABASE)}")

def check_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Abfrage aller Tabellen in der Datenbank
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Vorhandene Tabellen in der Datenbank:")
    for table in tables:
        print(table[0])  # Namen der Tabellen ausgeben
    conn.close()


# Debugging: Tabelle prüfen
check_tables()

def check_columns():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Überprüfe die Spalten der Tabelle 'recommendations'
    cursor.execute("PRAGMA table_info(recommendations);")
    columns = cursor.fetchall()
    print("Spalten in der Tabelle 'recommendations':")
    for column in columns:
        print(column[1])  # Gibt die Namen der Spalten aus
    conn.close()

# Debugging: Spalten prüfen
check_columns()

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
        SELECT activity, description, media1, media2, media3
        FROM recommendations
        WHERE weather = ? AND energy_level = ? AND interest = ?
    """
    print(f"Executing query: {query}")  # Debugging-Ausgabe
    print(f"Parameters: weather={weather}, energy_level={energy_level}, interest={interest}")  # Debugging-Ausgabe
    
    # SQL-Abfrage ausführen
    cursor = conn.execute(query, (weather, energy_level, interest))
    rows = cursor.fetchall()

    print(f"Rows fetched: {rows}")  # Debugging-Ausgabe, zeigt die zurückgegebenen Zeilen
    
    conn.close()

    # Empfehlungen erstellen
    recommendations = [
        {
            'activity': row['activity'],  # Zugriff auf die Spalte 'activity'
            'description': row['description'],  # Zugriff auf die Spalte 'description'
            'media': [  # Liste der verfügbaren Medien
                media for media in [row['media1'], row['media2'], row['media3']] if media
            ]
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
