from flask import Flask
from urllib.parse import quote_plus
from flask import request
import requests
import settings

app = Flask(__name__)

@app.route('/spotify')
def spotify():
    query_params = "client_id={}&response_type=code&redirect_uri={}&scope=user-library-read".format(settings.SPOTIFY_API_KEY, quote_plus(settings.CALLBACK_URL))
    return "https://accounts.spotify.com/authorize/?{}".format(query_params)

@app.route("/callback")
def keys():
    code = request.args.get("code")

    resp = requests.post("https://accounts.spotify.com/api/token", {
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": quote_plus(settings.CALLBACK_URL),
        "client_id": settings.SPOTIFY_API_KEY,
        "client_secret": settings.SPOTIFY_API_SECRET
    })

    data = resp.json()
    print(data)
    return "Got the keys!"

if __name__ == "__main__":
    app.run()