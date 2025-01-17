# Mental Health Application (BrightenUp)

This is a small software project designed to enhance mental well-being by providing users with activity recommendations based on the current weather. This web application is specifically tailored for Vienna, offering personalized suggestions to help users make the most of their day, regardless of the weather conditions.

This project is made as part of the _Agile Software Engineering_ module at the FH Wien der WKW.

# The team

- CARUOCCIOLO Claudia
- ROSENMAIER Lena
- SCHREMPF Tekla
- TOŠIC Bibiana

# Project Content

## Project structure

- _frontend_ folder: contains the frontend
  - _public_: contains the public images used in the application
  - _src_: contains the frontend code - the elements of the frontend are stored as components
- _backend_ folder: contains the backend
  - _database_: contains the database of the application
- _resources_ folder: contains resources used during planning and development, but not relevant to the application

## How to start the project

### Configuration

The default configuration points to http://127.0.0.1:8000/. In case this is not sufficient for you, you can change the host and/or port in the following places:

- for the backend:
  - **config.py** - change the host/port number and the debugging settings
- for the frontend:
  - **vite.config.ts** - change the target location of the '/api'

Please make sure, that the backend and frontend points to the same place.

### Backend

- make sure you have python/python3 on your computer
- `cd backend`
- `python3 -m venv .venv` - create virtual environment
- `source .venv/bin/activate` - activate it (differs on Windows)
- `pip3 install Flask` - install Flask (differs on Windows)
- `pip3 install flask-cors` - install Flask-CORS library (differs on Windows)
- `pip3 install requests` - install requests library (differs on windows)
- `python3 run.py` - run the backend project

### Frontend

- make sure you have Node.js on your computer
- `cd frontend`
- `npm install` - install dependencies
- `npm run dev` - run the frontend project

## Dependencies and used libraries

TBD

# How to use the app

Using the BrightenUp app is simple and intuitive:

- Start by entering your name (optional).
- Select your current energy level and your interest/activity type (mandatory).
- Based on your selections, the app will provide personalized activity recommendations.

- If you have any feedback, you can send it to us using the button located in the upper right corner of the app.

Please note that sessions are not stored, so you will need to re-enter your information each time you use the app.
