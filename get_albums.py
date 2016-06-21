import settings
import requests
import time
import json

def album_getter():
    headers = {"Authorization": "Bearer {}".format(settings.SPOTIFY_ACCESS_TOKEN)}
    album_url = "https://api.spotify.com/v1/me/albums"
    offset = True
    albums = []
    data = {"next": "next"}
    while "next" in data and data["next"]:
        data = requests.get(album_url, {"limit": 50}, headers=headers)

        data = data.json()
        if "next" not in data:
            print("Done!")
            break
        if data["next"]:
            offset = True
            album_url = data["next"]
            print(data["offset"])
        albums += data["items"]
        time.sleep(1)
    return albums

if __name__ == "__main__":
    albums = album_getter()
    with open("albums.json", 'w+') as f:
        json.dump(albums, f)