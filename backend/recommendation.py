from flask import jsonify, Response, g
from weather import fetch_weather
from collections import OrderedDict
import json
import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # path to the current file
DATABASE = os.path.join(BASE_DIR, 'database','Recommendation_Database.db')

def get_db_connection():
    '''
    Get a connection to the SQLite database.
    Returns:
        sqlite3.Connection: A connection to the SQLite database.
    '''

    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # Return rows as dictionaries
    return g.db


def get_recommendations(weather, energy_level, interest):
    '''
    Get recommendations based on the weather, energy level, and interest.
    Args:
        weather (str): The weather condition.
        energy_level (str): The energy level.
        interest (str): The interest category.
    Returns:
        list: A list of recommendations.
    '''

    conn = get_db_connection()

    # dynamic table name based on the weather
    table_name = f"{weather.lower()}_recommendation"

    # Debugging: check table name
    print(f"Verwende Tabelle: {table_name}")

    # SQL-query to get recommendations
    query = f"""
        SELECT activity, description, media AS media1, media2 AS media2
        FROM {table_name}
        WHERE "energy level" = ? AND interest = ?
    """
    print(f"Query: {query} mit energy_level={energy_level}, interest={interest}")
    cursor = conn.execute(query, (energy_level, interest))
    rows = cursor.fetchall()

    conn.close()

    # create recommendations list
    recommendations = [
        {
            'activity': row['activity'],
            'description': row['description'],
            'media': [media for media in [row['media1'], row['media2']] if media]
        }
        for row in rows
    ]
    return recommendations

def get_recommendation(request):
    '''
    Get recommendations based on the request parameters.
    The recommendations are read from the database based on the energy level and interest provided in the request
    and the current weather conditions.
    Args:
        request (flask.Request): The request object.
    Returns:
        flask.Response: The response containing the recommendations.
    '''

    # Input from Frontend
    energy_level = request.args.get('energy_level')  # Expected: very-energetic, good, neutral, low, very-low
    interest = request.args.get('interest')  # Expected: Outdoor, Fitness, Yoga, Home, Meditation

    # Debugging: check input
    print(f"Empfangen: energy_level={energy_level}, interest={interest}")

    # Missing parameters - return error
    if not energy_level or not interest:
        return jsonify({'error': 'Query parameters "energy_level" and "interest" are required'}), 400

    # Normalize and format input
    energy_level = energy_level.lower().strip()
    interest = interest.capitalize().strip()

    # call weather API
    weather, status = fetch_weather()
    if status != 200:
        return jsonify({'error': 'Failed to fetch weather data'}), status

    # Debugging: check weather data
    print(f"Ermitteltes Wetter: {weather}")

    # get all recommendations to the given weather, energy level and interest
    try:
        recommendations = get_recommendations(weather, energy_level, interest)
    except Exception as e:
        # Catch and return unexpected error
        print(f"Fehler bei der Abfrage: {e}")
        return jsonify({'error': 'Internal server error'}), 500

    if not recommendations:
        return jsonify({'message': f'No recommendations found for the weather: {weather}, energy level: {energy_level}, interest: {interest}'}), 404

    # Debugging: check recommendations
    print(f"Gefundene Empfehlungen: {recommendations}")

    # create response data with a specific order
    response_data = OrderedDict([
        ('city', 'Wien'),
        ('weather', weather),
        ('energy_level', energy_level),
        ('interest', interest),
        ('recommendations', recommendations)
    ])

    # create JSON
    response_json = json.dumps(response_data, indent=4)

    # return response
    return Response(response_json, content_type='application/json')