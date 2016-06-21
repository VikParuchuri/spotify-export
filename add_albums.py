from gmusicapi import Mobileclient
import settings
import json
import time
import logging
log = logging.getLogger(__name__)

with open("albums.json", 'r') as f:
    albums = json.load(f)

api = Mobileclient()
api.login('vik.paruchuri@gmail.com', settings.GOOGLE_PASSWORD, Mobileclient.FROM_MAC_ADDRESS)

def import_album(album):
    name = album["name"]
    artist = album["artists"][0]["name"]
    print(name)
    data = api.search("{} {}".format(name, artist))
    album = data["album_hits"][0]["album"]
    album_id = album["albumId"]

    tracks = api.get_album_info(album_id, include_tracks=True)
    for track in tracks["tracks"]:
        api.add_store_track(track["storeId"])
        time.sleep(.1)

def import_all_albums(albums):
    for i, album in enumerate(albums):
        print(i)
        try:
            import_album(album["album"])
        except (IndexError, KeyError):
            log.exception("Error")
        time.sleep(2)

import_all_albums(albums)