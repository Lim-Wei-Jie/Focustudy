from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import cred.py

client_ID='61da850bbe2a4846a02394330c92992b'
client_SECRET='59b2d5bfd8f143c48211b04a5767d5ac'   
redirect_url='http://127.0.0.1:5000/'

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/TaskList'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# export dbURL=mysql+mysqlconnector://root:root@localhost:3306/TaskList
# app.config['SQLALEHCMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

CORS(app)

print("you're in")

@app.route("/music")
def top_tracks():
    scope = 'user-top-read'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret= client_SECRET, redirect_uri=redirect_url, scope=scope))
    results = sp.current_user_top_tracks(limit=10, offset=0, time_range='short_term')
    
    if len(results):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "tracks": results["items"]
                }
            }
        )

    return jsonify(
        {
            "code": 404,
            "message": "There are no tracks."
        }
    ), 404

    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(" ", idx, track['artists'][0]['name'], " - ", track['name'])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)