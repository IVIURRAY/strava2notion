# strava2notion
Import Strava information to Notion

### How to use
1. Create an App though the [Strava API](https://www.strava.com/settings/api)
2. Insert `Client ID` and `Client Secret` into [`strava_api.py`](strava_api.py).
3. Insert access token from Notion cookies into [`notion_api.py`](notion_api.py).
4. Create a page called `Strava` in Notion (top level).
5. Run `strava_api.py` and it will try to find the `Strava` page in your Notion account and upload data into a table. 
