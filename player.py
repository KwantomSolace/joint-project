from items import *
from map import rooms

inventory = [item_portrait, item_hair]
votes = 70000000

# Start game at the trump tower
global current_room
current_room = rooms["Tower"]
