from flask import Flask, request, jsonify, g, Response
from flask_cors import CORS
import sqlite3
from weather import weather_bp, fetch_weather  # Import des Wetter-Blueprints und der Funktion
import os
from collections import OrderedDict
import json


app = Flask(__name__)
cors = CORS(app, origins="*")
app.register_blueprint(weather_bp)

# Absoluter Pfad zur Datenbank relativ zu diesem Skript
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Pfad zum aktuellen Skript
DATABASE = os.path.join(BASE_DIR, 'database','Recommendation_Database.db')

# Debugging: Datenbankpfad ausgeben
print(f"Verwendete Datenbank: {DATABASE}")

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

def check_columns(table_name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    print(f"Spalten in der Tabelle '{table_name}':")
    for column in columns:
        print(column[1])  # Gibt die Namen der Spalten aus
    conn.close()

def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # Ergebnisse als Dictionary
    return g.db

@app.teardown_appcontext
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Funktion: Empfehlungen aus der Datenbank abrufen
def get_recommendations(weather, energy_level, interest):
    conn = get_db_connection()

    # Dynamische Auswahl der Tabelle basierend auf dem Wetter
    table_name = f"{weather.lower()}_recommendation"

    # Debugging: Tabellenname ausgeben
    print(f"Verwende Tabelle: {table_name}")

    # SQL-Abfrage
    query = f"""
        SELECT activity, description, media AS media1, media2 AS media2
        FROM {table_name}
        WHERE "energy level" = ? AND interest = ?
    """
    print(f"Query: {query} mit energy_level={energy_level}, interest={interest}")
    cursor = conn.execute(query, (energy_level, interest))
    rows = cursor.fetchall()

    conn.close()

    # Empfehlungen erstellen
    recommendations = [
        {
            'activity': row['activity'],
            'description': row['description'],
            'media': [media for media in [row['media1'], row['media2']] if media]
        }
        for row in rows
    ]
    return recommendations


# Route: Hauptseite
@app.route('/')
def home():
    return "Das ist ein Test"

# Route: Empfehlungen abrufen
@app.route('/recommendations', methods=['GET'])
def recommendations_endpoint():
    # Eingaben für energy_level und interest vom Frontend abrufen
    energy_level = request.args.get('energy_level')  # Erwartet: very-energetic, good, neutral, low, very-low
    interest = request.args.get('interest')  # Erwartet: Outdoor, Fitness, Yoga, Home, Meditation

    # Debugging: Eingaben prüfen
    print(f"Empfangen: energy_level={energy_level}, interest={interest}")

    # Fehlende Parameter abfangen
    if not energy_level or not interest:
        return jsonify({'error': 'Query parameters "energy_level" and "interest" are required'}), 400

    # Normalisierung der Parameter
    energy_level = energy_level.lower().strip()
    interest = interest.capitalize().strip()

    # Wetter abrufen
    weather, status = fetch_weather()
    if status != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), status

    # Debugging: Wetterwert prüfen
    print(f"Ermitteltes Wetter: {weather}")

    # Recommendations für das aktuelle Wetter, energy_level und interest abrufen
    try:
        recommendations = get_recommendations(weather, energy_level, interest)
    except Exception as e:
        # Debugging: Fehler bei der Abfrage
        print(f"Fehler bei der Abfrage: {e}")
        return jsonify({'error': 'Internal server error'}), 500

    if not recommendations:
        return jsonify({'message': f'No recommendations found for the weather: {weather}, energy level: {energy_level}, interest: {interest}'}), 404

    # Debugging: Erfolgreiche Empfehlungen ausgeben
    print(f"Gefundene Empfehlungen: {recommendations}")

    # JSON mit garantierter Reihenfolge erstellen
    response_data = OrderedDict([
        ('city', 'Wien'),
        ('weather', weather),
        ('energy_level', energy_level),
        ('interest', interest),
        ('recommendations', recommendations)
    ])

    # JSON-String erstellen
    response_json = json.dumps(response_data, indent=4)

    # Rückgabe mit korrektem Content-Type
    return Response(response_json, content_type='application/json')

# Start der Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=True, port=8000)
