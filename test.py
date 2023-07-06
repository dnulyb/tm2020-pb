from authentication import *
from records import *
import data
from gsheet import *
from settings import token

#token = authenticate()
#print(token)

map_ids = ['3ce5ba27-17cf-48e9-9f80-f94e2e322abe', '13810c4c-42fe-4e55-9ed7-e4c6c07f2cbc', 'b91e8abe-58a2-4901-85bd-8bda86416baa']
#records = get_map_records(data.players, map_ids, token)
#print(records)

#record format: time, accountId, mapId
records = [[60015, '76e48117-ef20-4446-85a3-9883cefc7db7', 'b91e8abe-58a2-4901-85bd-8bda86416baa'], [63295, '76e48117-ef20-4446-85a3-9883cefc7db7', '3ce5ba27-17cf-48e9-9f80-f94e2e322abe'], [60141, 'f5788168-5d7d-4552-a30a-42565e1f9019', 'b91e8abe-58a2-4901-85bd-8bda86416baa'], [63355, 'f5788168-5d7d-4552-a30a-42565e1f9019', '3ce5ba27-17cf-48e9-9f80-f94e2e322abe']]