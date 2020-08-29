from stravaio import strava_oauth2
from stravaio import StravaIO
from notion_api import NotionInterface

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"

token = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Get Strava Data
client = StravaIO(access_token=token["access_token"])
athlete = client.get_logged_in_athlete()
activities = client.get_logged_in_athlete_activities()

# Upload information to Notion
notion = NotionInterface()
table = notion.create_activity_log_table()
for activity in activities:
    notion.add_row_to_table(table, activity)
