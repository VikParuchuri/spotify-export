Spotify Exporter
------------------

Export all your albums from Spotify, then import then into Google Play Music.

## Installation

* `pip install -r requirements.txt`

## Usage

* Register a Spotify application, and get a client key and secret.
* Create a `private.py` file, and set `SPOTIFY_API_KEY` and `SPOTIFY_API_SECRET`
* `python server.,py`
* Go to `localhost:5000/spotify`, then copy and paste the URL that is displayed into your browser bar.
* Finish following the Spotify login instructions.
* Check the server process logs to find the `access_token`.
* Set `SPOTIFY_ACCESS_TOKEN` in `private.py`
* Run `python get_albums.py` to export all of the albums in your Spotify collection.
* Set `GOOGLE_EMAIL` and `GOOGLE_PASSWORD` in `private.py` to your google account credentials.
* Run `python add_albums.py` to import your albums to Google Play Music.
