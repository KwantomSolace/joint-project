#!/usr/bin/python3

from introendings import *
from map import rooms
from player import *
from items import *
from gameparser import *
from debate import *
import os

game_over = False

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).
    """
    items_list = []
    for key in items:
        items_list.append(key["name"])
    return ", ".join(items_list)


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. 
    """
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.".
    """
    if (len(items) != 0):
        print()
        print("You have " + list_of_items(items) + ".")
        print()


def print_room(room):
    print(room["image"])
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)
    

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to).
    """
    global current_room
    if not current_room == rooms['Car']:
        print("GO " + direction.upper() + " to go to " + leads_to + ".")
    else:
        print("GO TO " + direction.upper() + " to go to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    global current_room
    if not current_room == rooms['Car']:
        for key in room_items:
            print("TAKE " + key["id"].upper() + " to take " + key["name"] + ".")
        for key in inv_items:
            print("DROP " + key["id"].upper() + " to drop " + key["name"] + ".")
        for key in inv_items:
            print("LOOK AT " + key["id"].upper() + " to look at " + key["name"] + ".")
    print()
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room

    try:
        if move(current_room["exits"], direction) == rooms['Debate'] and not (item_satans_number in inventory or item_eagle in inventory or item_money in inventory or item_photo in inventory):
            print('You are not prepared for the debate, so you cannot yet enter.')
            print()
            return
        elif move(current_room["exits"], direction) == rooms['Debate'] and (item_satans_number in inventory or item_eagle in inventory or item_money in inventory or item_photo in inventory):    
            print('You are prepared for the debate, but you only have one chance to reach 75 million votes. Proceed?')
            player_input = None
            while player_input == None:
                player_input = input('> ')
                if len(normalise_input(player_input))>0 and (normalise_input(player_input)[0] == 'yes' or normalise_input(player_input)[0] == 'y' or normalise_input(player_input)[0] == 'yeah' or normalise_input(player_input)[0] == 'yep' or normalise_input(player_input)[0] == 'yup' or normalise_input(player_input)[0] == 'aye'):
                    current_room = move(current_room["exits"], direction)
                    print_room(current_room)
                    debate()
                    return
                if len(normalise_input(player_input))>0 and (normalise_input(player_input)[0] == 'no' or normalise_input(player_input)[0] == 'n' or normalise_input(player_input)[0] == 'nope'):
                    print()
                    return
                else:
                    print('I didn\'t quite get that. Are you willing to debate?')
                    player_input = None
            return     
        elif move(current_room["exits"], direction) == rooms['House'] and not item_key in inventory:
            print('The doors to the White House are covered in chains and are padlocked. As presumed, it is a big house that is white!')
            print()
            return
        elif move(current_room["exits"], direction) == rooms['House'] and item_key in inventory:    
            print('There\'s no going back once you enter the White House. Proceed?')
            player_input = None
            while player_input == None:
                player_input = input('> ')
                if len(normalise_input(player_input))>0 and (normalise_input(player_input)[0] == 'yes'  or normalise_input(player_input)[0] == 'y' or normalise_input(player_input)[0] == 'yeah' or normalise_input(player_input)[0] == 'yep' or normalise_input(player_input)[0] == 'yup' or normalise_input(player_input)[0] == 'aye'):
                    print()
                    current_room = move(current_room["exits"], direction)
                    return
                if len(normalise_input(player_input))>0 and (normalise_input(player_input)[0] == 'no' or normalise_input(player_input)[0] == 'n' or normalise_input(player_input)[0] == 'nope'):
                    print()
                    return
                else:
                    print('I didn\'t quite get that. Are you willing to enter the White House?')
                    player_input = None
            return
        elif move(current_room["exits"], direction) == rooms['Booths'] and not item_photo in inventory:
            current_room = move(current_room["exits"], direction)
            inventory.append(item_photo)
            return
        if is_valid_exit(current_room["exits"], direction):
            current_room = move(current_room["exits"], direction)
        else:
            print("You cannot go there.")
    except:
        print("You cannot go there.")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    found = False
    for key in current_room["items"]:
        if item_id == key["id"]:
            inventory.append(key)
            current_room["items"].remove(key)
            found = True
            break
    if not found:
        print("You cannot take that.")
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    dropped = False
    for key in inventory:
        if item_id == key["id"]:
            inventory.remove(key)
            current_room["items"].append(key)
            dropped = True
            break
    if not dropped:
        print("You cannot drop that.")

def execute_look(item_id):
    for item in inventory:
        if item_id == item['id']:
            print(item['description'])
    

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            
    elif command[0] == "look":
        if len(command) > 1:
            execute_look(command[1])
        else:
            print("Look at what?")
        
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]
    
        
        

def main():
    os.system("Anthem.wav")
    #game_title()
    #game_intro()
    print()
    global game_over
    global previous_room
    previous_room = ''
    
    while not game_over:
        if previous_room != current_room["name"]:#this if statement and the code within prevents the room ASCII art from reappearing if the player
            print_room(current_room)#is only picking up, dropping, or looking at an item in the room
            previous_room = current_room["name"]#ie. the ASCII art only appears if the player changes rooms
        if current_room == rooms['Bar'] and not item_satans_number in inventory and item_money in inventory:#this executes after you first enter the bar with money in your inventory, and after the room details are displayed
            print('Press enter to continue.')
            wait = input()
            print('''You go over to the bar and slap down $20 for the finest drink on the menu. Satan
recognises you and says it's on the house. The two of you chat until you finish drinking,
then he gives you his number, telling you to call him whenever you need his help.''')
            inventory.append(item_satans_number)
            print()
            
        if not current_room == rooms['Car']:#the inventory is not displayed if Trump is in his limousine
            print_inventory_items(inventory)

        command = menu(current_room["exits"], current_room["items"], inventory)
            
        execute_command(command)
        if current_room == rooms['House']:#The game ends once Trump goes to the white house with the key in his inventory, or if Hillary wins the debate
            print_room(current_room)
            game_over = True
    
    if current_room == rooms['House']:
        execute_trump_wins()
    elif votes>=77000000:
        execute_trump_wins_too_much()
    else:
        execute_hillary_wins()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

