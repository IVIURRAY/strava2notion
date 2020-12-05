from notion.block import CollectionViewBlock
from notion.client import NotionClient

from config import TOKEN_V2
from table_schema import SCHEMA


class NotionInterface:
    def __init__(self):
        self.token_v2 = TOKEN_V2
        self.client = NotionClient(token_v2=self.token_v2)
        self.strava_page_title = "Strava"
        self.strava_table_title = "Activity Logbook"

    def get_strava_page(self):
        strava_page = None
        for page in self.client.get_top_level_pages():
            if self.strava_page_title == page.title:
                strava_page = page

        if strava_page is None:
            raise LookupError(
                f"Unable to find Strava page, is there a page with a "
                f"title of '{self.strava_page_title}' in your workspace?"
            )

        return strava_page

    def create_activity_log_table(self):
        strava_page = self.get_strava_page()

        # Check if we've a table already
        for block in strava_page.children:
            if hasattr(block, 'title') and block.title == self.strava_table_title:
                return block

        # Create a table
        strava_table = strava_page.children.add_new(CollectionViewBlock)
        strava_table.collection = self.client.get_collection(
            self.client.create_record("collection", parent=strava_table, schema=SCHEMA)
        )
        strava_table.title = self.strava_table_title
        strava_table.views.add_new(view_type="table")

        return strava_table

    def add_row_to_table(self, table, data):
        # HACK - needs to happen to work!
        table.collection.parent.views

        rows = table.collection.get_rows()
        if not any([r.name == data.name and r.date.start.date() == data.start_date_local.date() for r in rows]):
            row = table.collection.add_row()

            row.set_property("title", data.name)
            row.set_property("date", data.start_date_local)
            row.set_property("type", data.type)
            row.set_property("distance (m)", data.distance)
            row.set_property("time (s)", data.moving_time)
            row.set_property("cals", data.kilojoules)
            print(f'Added {data.name} on {data.start_date_local} to Notion!')
        else:
            print(f'Skipping {data.name} for {data.start_date_local}')
