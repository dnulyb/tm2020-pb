from authentication import *
from records import *
import data
from gsheet import *
import settings

token = authenticate()
#token = settings.token

map_ids = ['3ce5ba27-17cf-48e9-9f80-f94e2e322abe', '13810c4c-42fe-4e55-9ed7-e4c6c07f2cbc', 'b91e8abe-58a2-4901-85bd-8bda86416baa']
#map_data = get_map_ids(data.maps, token)
#print(map_data)

player_ids = list(data.player_data.keys())
#print(players)


records = get_map_records(player_ids, map_ids, token)
records = list(map(get_record_tuple, records))
#print(records)

#record format: time, accountId, mapId
#records = [[60015, '76e48117-ef20-4446-85a3-9883cefc7db7', 'b91e8abe-58a2-4901-85bd-8bda86416baa'], [63295, '76e48117-ef20-4446-85a3-9883cefc7db7', '3ce5ba27-17cf-48e9-9f80-f94e2e322abe'], [60141, 'f5788168-5d7d-4552-a30a-42565e1f9019', 'b91e8abe-58a2-4901-85bd-8bda86416baa'], [63355, 'f5788168-5d7d-4552-a30a-42565e1f9019', '3ce5ba27-17cf-48e9-9f80-f94e2e322abe']]


#records = [('47.308', 'ikewolf', '$fa0TM$fffF $FF4Summer - $fff18'), ('60.015', 'stufts', 'Breaking E'), ('63.295', 'stufts', 'Frosty E'), ('60.141', 'whizzy', 'Breaking E'), ('63.355', 'whizzy', 'Frosty E')]


player_names = list(data.player_data.values())
map_names = [maps[2] for maps in data.map_data]
#print(player_names)
#print(map_names)


# Create value list that matches the google sheets layout
# Todo: find better way to do this than nesting for loops
all_values = ["", ""]
match = False
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

#print(all_values)

write_google_sheet(all_values)
