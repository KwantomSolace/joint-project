from items import *
from map import rooms

inventory = [item_portrait, item_hair]#Trump starts out with a portrait of himself and his toupee in his inventory
votes = 70000000#Trump starts out with 70,000,000 votes, nearly half of all American registered voters

# Start game at the trump tower
global current_room
current_room = rooms["Tower"]
