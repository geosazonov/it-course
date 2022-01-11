from flask import Flask
import random

app = Flask(__name__)

weather_list = ['rain', 'sunny']


@app.route('/ml/weather-prediction')
def weather_prediction():
    return random.choice(weather_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
