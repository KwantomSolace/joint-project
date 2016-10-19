from items import *

room_bar = {
    "name": "Satan's Bar",

    "description":
    """You enter the dark and dingy bar, a thick layer of
smoke fogs the atmosphere and the musky stench of Tabaco
clings to your throat. The bar is in a circle shape at the
middle of the room, with bar stools placed around it. Seedy
looking individuals sit in the booths placed against the
walls of the rooms, they all look like they are up to no good.""",

    "exits": {"north":"Tower", "left":"Booths"},

    "items": []
}

room_booths = {
"name": "booths at Satan's Bar",

    "description":
    """In a dark corner of Satan's Bar you see Bill Clinton with
his arm around a young attractive female. You know this is
some useful dirt that could be used against Hillary, so you
take a picture.""",

    "exits": {"right":"Bar"},

    "items": []
}

room_debate = {
    "name": "the Debate Room",

    "description":
    """The bright lights cause you to squint as you walk to your podium.
Once your eyes adjust, you see just how vast and wild the audience is.
There are stars and stripes everywhere, and someone seems to have brought
a grill to make burgers. People are riding around on their Walmart mobility
scooters, complete with monster truck tyres.""",

    "exits": {"west":"Tower"},

    "items": []
}

room_tower = {
    "name": "the Trump Tower",

    "description":
    """You enter the majestic building that is trump
tower. Everything is pained with a sheen of gold, the
walls, the doors and the floors. Grandiose looking
furniture fills the lobby and a golden cage meant for
housing a bald eagle sits in the very middle of the room.""",

    "exits": {"north":"House","east":"Debate","south":"Bar","west":"Office"},

    "items": [item_eagle]
}

room_house = {
    "name": "the White House",

    "description":'',

    "exits": {"south":"Tower"},

    "items": []
}

room_vault = {
    "name": "the Trump Vault",

    "description":
    """You open the huge gold door walk inside.  The
room is full of money piles fashioned to look like
pieces of furniture. A money sofa sits in the far
corner and a wall-to-wall flat screen money TV is placed in
front of it.""",

    "exits": {"south":"Office"},

    "items": [item_money]
}

room_office = {
    "name": "the Trump Office",

    "description":
    """You walk into the trump office, it's a
humongous room full of mirrors. You frequently use
this room to practice your debates, making sure you
always look good from every angle. You look yourself
up and down in one of the mirrors, you're looking
hot as always.""",

    "exits": {"north":"Vault","east":"Tower"},

    "items": []
}

rooms = {
    "Bar": room_bar,
    "Booths": room_booths,
    "Debate": room_debate,
    "Tower": room_tower,
    "House": room_house,
    "Vault": room_vault,
    "Office": room_office,
}
