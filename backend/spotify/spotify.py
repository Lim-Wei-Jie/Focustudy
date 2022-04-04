from flask import Flask, jsonify
from flask_cors import CORS

import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import cred.py

client_ID='61da850bbe2a4846a02394330c92992b'
client_SECRET='59b2d5bfd8f143c48211b04a5767d5ac'   
redirect_url='http://127.0.0.1:5004/'

app = Flask(__name__)

CORS(app)

@app.route("/music", methods=["POST", "GET"])
def top_tracks():
    scope = 'user-top-read'
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