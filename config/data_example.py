# Example of what your data.py file should look like

# You can get map uids from trackmania.io
maps = [
    "MAP1_UID",
    "MAP2_UID", 
    "MAP3_UID"
]

# Complete map data. 
# Get this from running get_map_data.py and storing the complete result
# Each list entry is a list of ["map_id", "map_uid", "map_name"]
map_data = [
    ["MAP1_ID", "MAP1_UID", "MAP1_NAME"], 
    ["MAP2_ID", "MAP2_UID", "MAP2_NAME"],
    ["MAP3_ID", "MAP3_UID", "MAP3_NAME"]
]

# Usually maps have a long and complicated prefix before the name.
# Here you can define a simple name for the map.
map_names_simple = {
    "MAP1_NAME": "MAP1_SIMPLENAME",
    "MAP2_NAME": "MAP2_SIMPLENAME"
}

# Where on the google sheet the map times should be.
# Example of sheet ranges: "C2:C12", "L1:L3", etc.
map_sheet_ranges = {
    "MAP1_SIMPLENAME": "MAP1_SHEET_RANGE",
    "MAP2_SIMPLENAME": "MAP2_SHEET_RANGE"

}

# player_data is a dict of "account_id": "username"
# You can get account ids from trackmania.io
player_data = {
    "ACCOUNT1_ID": "ACCOUNT1_NAME",
    "ACCOUNT2_ID": "ACCOUNT2_NAME",
    "ACCOUNT3_ID": "ACCOUNT3_NAME"
}