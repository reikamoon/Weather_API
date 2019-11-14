from flask import Flask, render_template, request
import requests
import pprint

app = Flask(__name__)

pp = pprint.PrettyPrinter(indent=4)
weather_url = "http://api.openweathermap.org/data/2.5/weather?q=Fairfield&appid=2608f679d4594364525f6c6cc2246c79"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/weather_results', methods=['GET', 'POST'])
def weather_results_page():
    city = request.args.get('city')
    params = {
        'q': city,
        'appid': '2608f679d4594364525f6c6cc2246c79'
    }

    r = requests.get(weather_url, params=params)
    if not r.status_code == 200:
        print("Error!")
    results = r.json()
    city = results['name']
    return render_template('weather_results.html', city=city, temp=temp)


if __name__ == '__main__':
    app.run()
