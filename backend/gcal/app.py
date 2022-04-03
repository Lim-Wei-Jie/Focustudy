from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

import os.path
# import requests
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
# from requests.structures import CaseInsensitiveDict
# import json

all_events = []
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']

def main():
    creds=None
    if os.path.exists('token.json'):
        print('Token and credentials found, attempting to authenticate...')
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_console()
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    all_events.append(events)
    # print(all_events)

@app.route("/calendar", methods=["POST"])
def get_all_events():

    data = all_events
    final_events = {}

    for event in data[0]['items']:
        # print(event)
        id = event['id']
        name = event['summary']
        start = event['start']
        end = event['end']
        link = event['htmlLink']
        final_events[id] = {'name': name, 'start': start, 'end': end, 'link': link}

    if final_events:
        return jsonify (
            {
                "code": 200,
                "data": final_events
            }
        ), 200

    return jsonify (
        {
            "code": 404,
            "message": "No events in calendar." 
        }
    ), 404

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=5000, debug=True)
    main()