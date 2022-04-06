from flask import Flask, jsonify
from flask_cors import CORS

import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_ID='61da850bbe2a4846a02394330c92992b'
client_SECRET='59b2d5bfd8f143c48211b04a5767d5ac'   
redirect_url='http://127.0.0.1:5005/'

app = Flask(__name__)

CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/chosen/<string:playlist_id>", methods=["POST", 'GET'])
def chosen_playlist(playlist_id):
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret= client_SECRET, redirect_uri=redirect_url, scope=scope))
    print("HEREEEEEE")
    print(str(playlist_id))
    results = sp.playlist(playlist_id, additional_types=('track', ))

    if len(results):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "tracks": results
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "There are no playlists."
        }
    ), 404



@app.route("/playlists", methods=["POST", 'GET'])
def all_playlists():
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret= client_SECRET, redirect_uri=redirect_url, scope=scope))
    results = sp.current_user_playlists(limit=50, offset=0)

    if len(results):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "tracks": results
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "There is no selected playlist."
        }
    ), 404



@app.route("/music", methods=["POST", "GET"])
def top_tracks():
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret= client_SECRET, redirect_uri=redirect_url, scope=scope))
    results = sp.current_user_top_tracks(limit=20, offset=0, time_range='short_term')
    # print(type(results))
    
    if len(results):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "tracks": results
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "There are no tracks."
        }
    ), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)