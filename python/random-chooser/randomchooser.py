import requests
from flask import Flask, send_file
from json import loads
import io

app = Flask(__name__)


@app.route('/fact')
def fact():
    request = requests.get('https://catfact.ninja/fact')
    return request.text


unsplash_auth_headers = {
    'Authorization': 'Client-ID JOwuj48WYzLIx-4iItgnmgkMjffTrX7OhrD1b9gU69E'
}


@app.route('/picture')
def picture():
    request = requests.get('https://api.unsplash.com/photos/random', headers=unsplash_auth_headers)
    image_link = loads(request.text)['urls']['full']
    image_response = requests.get(image_link, stream=True)
    file_like_object = io.BytesIO()
    file_like_object.write(image_response.content)
    file_like_object.seek(0)  # move to the beginning of file
    return send_file(file_like_object, mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
