import requests

def get_weather_data():
    # API-URL
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.12&longitude=16.22&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    # API-Abfrage durchführen
    response = requests.get(url)
    
    # Prüfen, ob die Antwort erfolgreich war
    if response.status_code == 200:
        data = response.json()
        
        # Extrahiere die relevanten Daten
        hourly_data = data['hourly']
        temperatures = hourly_data['temperature_2m']
        humidity = hourly_data['relative_humidity_2m']
        wind_speeds = hourly_data['wind_speed_10m']
        
        # Berechne die Durchschnittswerte
        avg_temperature = sum(temperatures) / len(temperatures)
        avg_humidity = sum(humidity) / len(humidity)
        avg_wind_speed = sum(wind_speeds) / len(wind_speeds)
        
        # Rückgabe der Daten als Dictionary
        return {
            "avg_temperature": avg_temperature,
            "avg_humidity": avg_humidity,
            "avg_wind_speed": avg_wind_speed
        }
    else:
        print(f"Fehler beim Abrufen der Daten: {response.status_code}")
        return None

