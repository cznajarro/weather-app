# Weather App

A Flask weather application that retrieves current conditions from the OpenWeatherMap API and stores recent city searches in SQLite.

## Overview

This project combines a Python Flask backend with a vanilla JavaScript frontend. Users search for a city through the browser, the backend requests weather data from OpenWeatherMap, and the application returns the result to the page without requiring a full page reload.

Searches are stored locally in SQLite so the application can display recent search history through the `/api/history` route.

## Features

- Search for current weather by city
- OpenWeatherMap API integration
- Flask backend with JSON responses
- Vanilla JavaScript frontend using `fetch`
- SQLite search-history database
- Recent-search history endpoint
- API-key configuration through environment variables
- Local development setup with no hosted database required

## Technologies

- Python
- Flask
- SQLite
- JavaScript
- HTML and CSS
- OpenWeatherMap API

## Project Structure

```text
weather-app/
├── assets/              # Frontend assets, if included
├── data/                # Local SQLite database location, if included
├── .env                 # Local API key, not committed
├── .gitignore
├── Weather.py           # Flask application
├── index.html           # Frontend interface
├── requirements.txt
└── README.md
```

The exact local database filename may be created automatically when the application runs. Database files and secret configuration should remain excluded through `.gitignore`.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/cznajarro/weather-app.git
cd weather-app
```

### 2. Create a virtual environment

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

If your system uses `python` instead of `python3`, use the matching command for both Python and pip.

### 4. Create the environment file

Create a file named `.env` in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Create an API key through [OpenWeatherMap](https://openweathermap.org/api). Do not commit the `.env` file or expose the key in frontend code.

### 5. Start the Flask server

```bash
python3 Weather.py
```

Open the local address shown by Flask in your browser. The frontend should be accessed through Flask rather than opened directly with a `file://` URL.

## API Route

### `GET /api/history`

Returns recent searches saved in the local SQLite database.

Example request:

```text
http://127.0.0.1:5001/api/history
```

The frontend calls this route to update the displayed search history.

## Data Flow

1. The user submits a city search in the browser.
2. JavaScript sends the request to the Flask backend.
3. Flask requests weather data from OpenWeatherMap.
4. The search is written to SQLite.
5. The backend returns weather data to the frontend.
6. The page updates the weather display and search history.

## Database

The application uses SQLite for local persistence. Each search can be recorded with information such as the searched city and the associated weather response or timestamp, depending on the current database schema.

SQLite was selected because this project is intended to run locally without requiring a hosted database service.

## What I Practiced

- Building a Flask route that accepts browser requests
- Calling an external API from a Python backend
- Returning JSON data to a JavaScript frontend
- Persisting application data with SQLite
- Keeping API credentials in environment variables
- Connecting frontend behavior to backend routes

## Limitations

- The application requires an OpenWeatherMap API key.
- The database is local to the machine running the application.
- Weather data depends on the availability and response format of the external API.
- This project is configured for local use and is not currently deployed as a hosted service.

## Future Improvements

- Add automated tests for API responses and database writes
- Add clearer user-facing error messages for invalid locations and API failures
- Add pagination or a configurable limit for search history
- Add weather forecasts alongside current conditions

## Author

Carlos Zuniga

- GitHub: [cznajarro](https://github.com/cznajarro)
- LinkedIn: [Carlos Zuniga](https://www.linkedin.com/in/cznajarro)
