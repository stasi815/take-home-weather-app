from flask import Flask, request, url_for, redirect, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with link to Weather page."""
    return render_template('index.html')

@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('weather_form.html')

@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')
    params = {
        'q': users_city,
        'appid': '7ea8229cfbcab8fd2f86056528d8d983'
    }
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
    json_response = response.json()
    print(json_response)
    main = json_response['main']
    print(main)
    temp = main['temp']
    first_step = float(temp) - 273.15
    fahrenheit = float(first_step) * 1.8 + 32
    temperature = int(fahrenheit)

    weather_category = json_response['weather']
    print(weather_category)
    weather_object = weather_category[0]
    weather_description = weather_object['description']
    humidity_level = main['humidity']
    return render_template('weather_results.html', temperature=temperature, users_city=users_city, weather_description=weather_description, humidity_level=humidity_level)


if __name__ == '__main__':
    app.run(debug=True)