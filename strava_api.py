from stravaio import strava_oauth2
from stravaio import StravaIO

from config import CLIENT_ID, CLIENT_SECRET
from notion_api import NotionInterface

token = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Get Strava Data
client = StravaIO(access_token=token["access_token"])
activities = client.get_logged_in_athlete_activities()

# Upload information to Notion
notion = NotionInterface()
table = notion.create_activity_log_table()
for activity in activities:
    notion.add_row_to_table(table, activity)
