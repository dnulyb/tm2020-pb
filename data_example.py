# Example of what your data.py file should look like

# You can get map uids from trackmania.io
maps = [
    "MAP1_UID",
    "MAP2_UID", 
    "MAP3_UID"
]

# Use get_map_data() to get map id information
map_ids = [
    "MAP1_ID",
    "MAP2_ID",
    "MAP3_ID"
]

# Complete map data. 
# Get this from using get_map_data() and storing the complete result
# Each list entry is a list of ["map_id", "map_uid", "map_name"]
map_data = [
    ["MAP1_ID", "MAP1_UID", "MAP1_NAME"], 
    ["MAP2_ID", "MAP2_UID", "MAP2_NAME"],
    ["MAP3_ID", "MAP3_UID", "MAP3_NAME"]
]

# player_data is a dict of "account_id": "username"
# You can get account ids from trackmania.io
player_data = {
    "ACCOUNT1_ID": "ACCOUNT1_NAME",
    "ACCOUNT2_ID": "ACCOUNT2_NAME",
    "ACCOUNT3_ID": "ACCOUNT3_NAME"
}