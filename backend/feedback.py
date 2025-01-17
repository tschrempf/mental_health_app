from flask import request, jsonify
import sqlite3
import re
import os

# Absolute path to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #describes the directory of the current file
DB_PATH = os.path.join(BASE_DIR, 'database','feedback.db') # path to the feedback database

# Function to initialize the database and create the table
def init_db():
    print(f"Verwendete Datenbank: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)  # Connect to the SQLite database
    cursor = conn.cursor()

    # Create the feedback table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email_address TEXT NOT NULL,d
            feedback_text TEXT NOT NULL,
            star_rating INTEGER NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()  # Save changes
    conn.close()   # Close the connection

# Call the init_db function when the app starts
init_db()

def save_feedback(data):
    '''
    Saves feedback data to the database.
    Retrieves the email address, feedback text, and star rating from the JSON
    data in the POST request. Validates the input data, including checking for
    missing fields, validating the star rating, and validating the email
    address format. If any validation errors are found, an appropriate error
    response is returned. If the data is valid, the feedback is saved to the
    database.
    Returns:
        Response: A JSON response indicating the success or failure of the
        feedback submission, along with an appropriate HTTP status code.'''
    
    # data = request.json  # Get JSON data from the POST request
    email_address = data.get('email_address')
    feedback_text = data.get('feedback_text')
    star_rating = data.get('star_rating')

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

def get_feedback_from_db():
    '''
    Retrieves feedback data from the database.
    Connects to the SQLite database specified by DB_PATH, fetches all records
    from the 'feedback' table, and orders them by the 'created_at' column in
    descending order. The feedback data is then converted into a list of
    dictionaries, where each dictionary represents a feedback entry.
    Returns:
        tuple: A tuple containing:
            - feedback_list (list): A list of dictionaries, each containing
              the following keys:
                - "id" (int): The unique identifier of the feedback entry.
                - "email_address" (str): The email address of the user who
                  provided the feedback.
                - "feedback_text" (str): The text of the feedback.
                - "star_rating" (int): The star rating given by the user.
                - "created_at" (str): The timestamp when the feedback was
                  created.
            - status_code (int): The HTTP status code (200 for success).'''
    
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM feedback
            ORDER BY created_at DESC
        """)
        feedback = cursor.fetchall()

    # Convert the feedback data to a list of dictionaries
    feedback_list = []
    for item in feedback:
        feedback_list.append({
            "id": item[0],
            "email_address": item[1],
            "feedback_text": item[2],
            "star_rating": item[3],
            "created_at": item[4]
        })

    return feedback_list, 200