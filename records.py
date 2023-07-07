import requests
import data

user_agent = "github.com/dnulyb/tm2020-pb"

map_info_url = "https://prod.trackmania.core.nadeo.online/maps/?mapUidList="

map_record_url = "https://prod.trackmania.core.nadeo.online/mapRecords/"

def get_map_ids(map_uids, token):

    uid_str = ','.join(map_uids)
    complete_url = map_info_url + uid_str

    headers = {
        'Authorization': "nadeo_v1 t=" + token,
        'User-Agent': user_agent
    }

    res = requests.get(complete_url, headers=headers)
    res = res.json()
    
    map_ids = [[elem["mapId"],
                    elem["mapUid"],
                    elem["name"]]
                for elem in res]

    return map_ids

    

def get_map_records(account_ids, map_ids, token):

    account_id_str = ','.join(account_ids)
    map_id_str = ','.join(map_ids)

    complete_url = map_record_url + \
                    "?accountIdList=" + account_id_str + \
                    "&mapIdList=" + map_id_str
    
    headers = {
        'Authorization': "nadeo_v1 t=" + token,
        'User-Agent': user_agent
    }

    res = requests.get(complete_url, headers=headers)
    res = res.json()
    #print(res)

    #Record format: time, accountId, mapId
    records = [[elem["recordScore"]["time"],
                    elem["accountId"],
                    elem["mapId"]] 
                for elem in res]
    #print(len(records))
    
    # Make sure records are in correct format
    #records = list(map(format_map_record, records))
    #records = ['60.015', '63.295', '60.141', '63.355']
    # Separate by map
    #records = separate_map_records(records)

    return records

def format_map_record(record):
    record = str(record)
    return record[:-3] + "." + record[-3:]

# Separates map records by map.
# Each array entry will have all users records on that map.
def separate_map_records(records):
    n = len(data.maps) # number of maps
    map_records = [records[index::n] for index, _ in enumerate(data.players)]
    return map_records



def get_record_tuple(record):

    time = format_map_record(record[0])
    name = data.player_data[record[1]]
    map = None

    #Get map name
    for m in data.map_data:
        if m[0] == record[2]:
            map = m[2]

    return (time, name, map)

