from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # read from environment

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        print("FORM SUBMITTED")
        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=44a5802ccde6f71a45128a11e3608065&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"]
            }
        else:
            error = data.get("message", "Something went wrong")

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)