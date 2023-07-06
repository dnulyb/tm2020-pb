from authentication import *
from records import *
import data
from gsheet import *

#token = authenticate()
#print(token)

#map_ids = get_map_ids(data.maps, token)
# caching results so i dont have to spam the api
#map_ids = ['3ce5ba27-17cf-48e9-9f80-f94e2e322abe', 'b91e8abe-58a2-4901-85bd-8bda86416baa']
#map_ids = ['3ce5ba27-17cf-48e9-9f80-f94e2e322abe', '13810c4c-42fe-4e55-9ed7-e4c6c07f2cbc', 'b91e8abe-58a2-4901-85bd-8bda86416baa']
map_ids = ['3ce5ba27-17cf-48e9-9f80-f94e2e322abe', '13810c4c-42fe-4e55-9ed7-e4c6c07f2cbc', 'b91e8abe-58a2-4901-85bd-8bda86416baa']
print(map_ids)

records = get_map_records(data.players, map_ids, token)
print(records)

#write_google_sheet(records)