# Strava-2-Notion
Import Strava information to Notion.

![Notion Data](/media/notion.png)

# How to use

### Setup 
1. Create an App though the [Strava API](https://www.strava.com/settings/api)
2. Insert `Client ID` and `Client Secret` into [`strava_api.py`](strava_api.py).
3. Insert token from Notion cookies into [`notion_api.py`](notion_api.py).
4. Create a page called `Strava` in Notion (top level).

### How to run
1. `git clone https://github.com/IVIURRAY/strava2notion.git`
2. `cd strava2notion`
3. `virtualenv venv`
4. `source venv/bin/activate` (Mac) or `venv/Scripts/activate` (Window)
5. `pip install -r requirements.txt`
6. `python strava_api.py` (Requires 3.5+)
7. If you've set it up correctly a Strava App auth page will appear.
8. Click Authorize ![Strava Auth](/media/oauth.png)
9. The script will then look for a page called `Strava` in your top level Notion pages.
10. You will be able to see it adding data in real time (Press `Ctrl + r` if you see nothing happening)
11. ![Notion Data](/media/notion.png)
  
