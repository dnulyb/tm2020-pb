from authentication import *
from records import *
import config.data as data

token = authenticate()
map_data = get_map_data(data.maps, token)
print(map_data)