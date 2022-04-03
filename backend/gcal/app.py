from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

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
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    all_events.append(events)
    print(all_events)

if __name__ == "__main__":
    main()

        # try:
        #     credentials = get_credentials()
        #     service = build('calendar', 'v3', credentials=credentials)
        #     print('Authentication successful!')
        #     print('Attempting to get calendar data...')
        #     get_calendar_data(service)
        #     print('Calendar data retrieved!')
        #     print('Attempting to write calendar data to file...')
        #     write_calendar_data_to_file()
        #     print('Calendar data written to file!')
        # except:
        #     print('Authentication failed!')