import data
import settings
from authentication import *
from records import *
from gsheet import *
from datetime import datetime

# Get access token
token = authenticate()
#print(token)
#token = settings.token

# Run this once and store map_ids and map_data in data.py
#map_data = get_map_data(data.maps, token)
#print(map_data)
#quit()

# Get map records for each map and player 
player_ids = list(data.player_data.keys())
# records is an array of tuples: [(time, name, map_name), ...]
map_ids = [maps[0] for maps in data.map_data]
records = get_map_records(player_ids, map_ids, token)

# Get player and map names
player_names = list(data.player_data.values())
map_names = [maps[2] for maps in data.map_data]
map_names_simple = data.map_names_simple

# Write map record data to google sheets
map_sheet_ranges = data.map_sheet_ranges
match = False
for map_name in map_names:

    map_values = []

    for player in player_names:
        for record in records:
            if(player == record[1]) and map_name == record[2]:
                map_values = map_values + [record[0]]
                match = True

        # No match, so the cell is empty
        #   Google sheets cannot handle empty values when plotting,
        #   so we add a really bad value if there is no pb
        if(not(match)):
            map_values = map_values + ["99.999"]

        match = False

    # Print map values so we have a copy if something goes wrong with the gsheet update
    print(map_values)

    # Update gsheet with map values
    map_range = map_sheet_ranges.get(map_names_simple.get(map_name))
    google_sheet_write(map_range, map_values, settings.spreadsheet_name, settings.sheet_number, settings.credentials_filename)


# Store current time in settings.date_cell
now = datetime.now()
dmY_HMS = now.strftime("%d/%m/%Y %H:%M:%S")
google_sheet_write(settings.date_cell, [dmY_HMS], settings.spreadsheet_name, settings.sheet_number, settings.credentials_filename)
