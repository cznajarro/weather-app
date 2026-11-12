# Weather App

A small weather lookup app built with Python, Flask, and vanilla JavaScript. Enter a city to see its current temperature in Fahrenheit and a short description of the weather, powered by OpenWeatherMap.

The frontend requests data from a Flask endpoint and updates the page without a full reload. The API key stays on the backend and is loaded from an environment variable.

## Features

- Look up current weather by city name.
- Display temperature rounded to the nearest whole degree Fahrenheit.
- Show a weather condition such as Clear, Clouds, or Rain.
- Update results in the browser using JavaScript `fetch`.
- Configure the API key through a local `.env` file.

## Tech Stack

| Component | Technology |
| --- | --- |
| Backend and routes | Python, Flask |
| Weather API requests | Requests, OpenWeatherMap |
| Configuration | python-dotenv, environment variables |
| Frontend | HTML, vanilla JavaScript |

## Run Locally

You need Python 3, Git, an internet connection, and an [OpenWeatherMap API key](https://openweathermap.org/api).

### 1. Clone the repository

```bash
git clone https://github.com/cznajarro/weather-app.git
cd weather-app
```

Run the remaining commands from this project folder.

### 2. Create and activate a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Install dependencies

With the virtual environment activated:

```bash
python -m pip install -r requirements.txt
```

### 4. Add your API key

Create a file named `.env` alongside `Weather.py`, using the included `env.example` as a template:

```dotenv
OPENWEATHER_API_KEY=your_api_key_here
```

Replace the placeholder with your own key. The repository's `.gitignore` excludes `.env`; keep the real key out of committed files.

### 5. Start the app

```bash
python Weather.py
```

Open **[http://localhost:5001](http://localhost:5001)**, enter a city, and click **Weather?**

Access the page through Flask rather than opening `index.html` directly. Press **Ctrl+C** in the terminal to stop the server. To run it again later, activate the same virtual environment and run `python Weather.py`; dependencies do not need to be reinstalled each time.

## How It Works

1. Flask serves `index.html` at `/`.
2. Clicking the button sends a request to `/api/weather?city=<city>`.
3. The backend calls OpenWeatherMap's current-weather endpoint with imperial units and the server-side API key.
4. Flask returns the city, rounded temperature, and weather condition as JSON.
5. JavaScript displays the result on the page.

### Routes

| Route | Purpose |
| --- | --- |
| `GET /` | Serve the weather lookup page. |
| `GET /api/weather?city=Seattle` | Request current weather for a city. |

Illustrative successful response; values depend on current conditions:

```json
{
  "city": "Seattle",
  "temp": 55,
  "weather": "Clouds"
}
```

## Project Files

| File | Purpose |
| --- | --- |
| `Weather.py` | Flask application and OpenWeatherMap request logic. |
| `index.html` | Search form and JavaScript for fetching and displaying results. |
| `requirements.txt` | Python dependencies. |
| `env.example` | API-key configuration template. |
| `.gitignore` | Excludes local secrets, virtual environments, and Python cache files. |
| `LICENSE` | MIT license. |

## Current Limitations

- Searches are not saved; there is no database or search-history endpoint.
- Error handling is basic. The backend recognizes OpenWeatherMap's string `"404"` response code and returns a city-not-found message, but currently sends it with HTTP status 200.
- Blank input, invalid API keys, network failures, and unexpected API responses are not fully handled. External requests do not yet have a timeout.
- The app uses Flask's built-in development server and needs deployment configuration before public production use.

## Planned Improvements

- Validate city input and encode query parameters correctly.
- Add request timeouts and consistent error responses with appropriate HTTP status codes.
- Add loading feedback, Enter-key submission, and accessible form labels.
- Add automated tests for successful lookups and API failures.

## Skills Practiced

Flask routing, calling a third-party API, reading environment variables, returning JSON, and connecting a JavaScript frontend to a Python backend.

## License

This project is licensed under the [MIT License](LICENSE).
