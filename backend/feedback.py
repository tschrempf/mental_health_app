from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import re
import os

app = Flask(__name__)

# CORS activates und is restricted to a certain domain
CORS(app, resources={r"/feedback": {"origins": "http://localhost:5173"}})

# Absoluter Pfad zur Datenbank
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #describes the directory of the current file
DB_PATH = os.path.join(BASE_DIR, 'feedback.db')  # Absolute Path to the database

# Function to initialize the database and create the table
def init_db():
    print(f"Verwendete Datenbank: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)  # Connect to the SQLite database
    cursor = conn.cursor()

    # Create the feedback table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_address TEXT NOT NULL,
            feedback_text TEXT NOT NULL,
            star_rating INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()  # Save changes
    conn.close()   # Close the connection

# Call the init_db function when the app starts
init_db()

@app.route('/')
def home():
    return "Der Flask-Server läuft erfolgreich!"

# Define a route to handle feedback submission
@app.route('/feedback', methods=['POST'])
def save_feedback():
    data = request.json  # Get JSON data from the POST request
    email_address = data.get('email_address')
    feedback_text = data.get('feedback_text')
    star_rating = data.get('star_rating')

     #Collect all validation errors
    errors = []

    # Collect missing fields
    missing_fields = []
    if not email_address:
        missing_fields.append("E-Mail-Adresse")
    if not feedback_text:
        missing_fields.append("Feedback-Text")
    if star_rating is None or star_rating == "" or star_rating == 0:
        missing_fields.append("Sternebewertung")

    # If any fields are missing, return an error
    if missing_fields:
        return jsonify({"error": f"Fehlende Felder: {', '.join(missing_fields)}"}), 400
    
    # Validate star_rating to ensure it's an integer between 1 and 5
    try:
        star_rating = int(star_rating)
        if not (1 <= star_rating <= 5):
            return jsonify({"error": "Sternebewertung muss zwischen 1 und 5 liegen"}), 400
    except ValueError:
        return jsonify({"error": "Sternebewertung muss eine Zahl zwischen 1 und 5 sein"}), 400

    # Validate email format (no spaces allowed)
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if not re.match(email_regex, email_address):
        return jsonify({"error": "Ungültige E-Mail-Adresse"}), 400

    # Save feedback to the database
    try:
        with sqlite3.connect(DB_PATH) as conn:  # Use absolute path to connect to the database
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO feedback (email_address, feedback_text, star_rating)
                VALUES (?,?,?)
            """, (email_address, feedback_text, star_rating))
    except sqlite3.Error as e:
        print(f"SQLite-Fehler: {e}")
        return jsonify({"error": f"Fehler beim Speichern des Feedbacks: {str(e)}"}), 500

    return jsonify({"message": "Vielen Dank! Feedback erfolgreich übermittelt"}), 201

# Ensure the app runs only when executed directly
if __name__ == '__main__':
    app.run(debug=True)
