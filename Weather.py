import os
import requests
from flask import Flask, request, send_file
from dotenv import load_dotenv
load_dotenv() #loading the .env file to get the API key

app = Flask(__name__)
api_key = os.environ.get("api_key")

@app.route("/")
def index():
   return send_file("index.html")

@app.route("/api/weather", methods=["GET"])
def weather():
    user_input = request.args.get("city")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
    )
    if weather_data.json()['cod'] == '404':
        return {"error": "City not found"}
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        return {"city": user_input, "temp": temp, "weather": weather}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)