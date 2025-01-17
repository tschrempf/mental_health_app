from recommendation import get_recommendation
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from weather import weather_bp
from feedback import get_feedback_from_db, save_feedback
import config


app = Flask(__name__)
cors = CORS(app, origins="*")
app.register_blueprint(weather_bp)


# Route: Main Page
@app.route('/')
def home():
    return jsonify({
        'Welcome': 'This is the Mental Health App API index page.',
        'API': 'For a detailed api description check out the openapi route',
        'Routes': ['/weather', '/recommendations', '/feedback', '/openapi'],
    })

# Route: OpenAPI-Specification
@app.route('/openapi', methods=['GET'])
def openapi():
    return send_file('../resources/mental_health_app_api.yaml')

# Route: read all feedback 
@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedback = get_feedback_from_db()
    return jsonify(feedback)

# Route: save feedback
@app.route('/feedback', methods=['POST'])
def post_feedback():
    data = request.json  # Get JSON data from the POST request
    feedback = save_feedback(data)
    return feedback


# Route: get recommendations
@app.route('/recommendations', methods=['GET'])
def recommendations_endpoint():
    # get recommendations based on the request parameters (energy_level, interest) given by the frontend
    recommendations = get_recommendation(request)
    return recommendations
    

# Start der Flask-Anwendung
if __name__ == '__main__':
    app.run(debug=config.DEBUG, port=config.PORT, host=config.IP)
