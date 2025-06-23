import os
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar.events']
creds = None
service = None

def init_google_calendar():
    global creds, service
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)

def add_event_to_google_calendar(date, event_text):
    global service
    if service is None:
        init_google_calendar()
    event = {
        'summary': event_text,
        'start': {'date': date.toString("yyyy-MM-dd")},
        'end': {'date': date.toString("yyyy-MM-dd")},
    }
    service.events().insert(calendarId='primary', body=event).execute()

def get_events_from_google_calendar(date):
    global service
    if service is None:
        init_google_calendar()
    start_of_day = datetime.datetime(date.year(), date.month(), date.day(), 0, 0, 0).isoformat() + '+09:00'
    end_of_day = datetime.datetime(date.year(), date.month(), date.day(), 23, 59, 59).isoformat() + '+09:00'
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_of_day,
        timeMax=end_of_day,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    return [event.get('summary', '') for event in events]
