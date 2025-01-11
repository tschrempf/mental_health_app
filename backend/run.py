from flask import Flask, jsonify
from weather_api import get_weather_data  # Importiere die Funktion aus weather_api.py

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def weather():
    weather_data = get_weather_data()  # Abrufen der Wetterdaten
    if weather_data:
        return jsonify(weather_data)  # Die Wetterdaten als JSON zurückgeben
    else:
        return jsonify({"error": "Daten konnten nicht abgerufen werden"}), 500  # Fehlerbehandlung

if __name__ == "__main__":
    app.run(debug=True)
