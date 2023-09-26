"""
Example file to show how to use the tm2020-pb functionality.

This will retrieve personal best times for players and maps 
    from the official Nadeo leaderboards,
    and upload them to your Google Sheet.
    For optimal results make sure your Google Sheet layout
        matches the one from this program, or vice versa.

Before usage, the players and maps to use should be defined in a "data.py" file,
    see "data_example.py".

Ubisoft and Google Sheet information must be defined in a "settings.py" file,
    see "settings_example.py".

To use, run in terminal: 
    python3 example.py
"""

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

# Get map records for each map and player 
player_ids = list(data.player_data.keys())
# records is an array of tuples: [(time, name, map_name), ...]
records = get_map_records(player_ids, data.map_ids, token)
#print(records)

# Get player and map names
player_names = list(data.player_data.values())
map_names = [maps[2] for maps in data.map_data]

# Create value list that matches the google sheets layout

# Store current time
now = datetime.now()
dmY_HMS = now.strftime("%d/%m/%Y %H:%M:%S")

all_values = ["", dmY_HMS]
match = False
# Store data in the correct map and player order
# Todo: find better way to do this than nesting for loops
for player in player_names:
    for map_name in map_names:
        for record in records:
            if(player == record[1]) and map_name == record[2]:
                #print("we have a match: " + player + "," + map_name)
                all_values = all_values + [record[0]]
                match = True

        #No match, so the cell is empty
        if(not(match)):
            all_values = all_values + [""]

        match = False

# Print the values so we have a copy if something goes wrong with the upload
print(all_values)

# Write to google sheets
google_sheet_write_full_row(all_values, settings.spreadsheet_name, settings.sheet_number, settings.credentials_filename)
