#!/usr/bin/python3

from introendings import *
from map import rooms
from player import *
from items import *
from gameparser import *
from debate import *
import os

global game_over
game_over = False
global debate_over
debate_over = False

def list_of_items(items):
    items_list = []
    for key in items:
        items_list.append(key["name"])
    return ", ".join(items_list)


def print_room_items(room):
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")


def print_inventory_items(items):
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
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    global current_room
    if not current_room == rooms['Car']:
        print("GO " + direction.upper() + " to go to " + leads_to + ".")
    else:
        print("GO TO " + direction.upper() + " to go to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
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
    return chosen_exit in exits


def execute_go(direction):
    global current_room
    global debate_over
    try:
        if not debate_over and move(current_room["exits"], direction) == rooms['Debate'] and not (item_satans_number in inventory or item_eagle in inventory or item_money in inventory or item_photo in inventory):
            print('You are not prepared for the debate, so you cannot yet enter.')
            print()
            return
        elif not debate_over and move(current_room["exits"], direction) == rooms['Debate'] and (item_satans_number in inventory or item_eagle in inventory or item_money in inventory or item_photo in inventory):    
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
    look_successful = False
    for item in inventory:
        if item_id == item['id']:
            print(item['description'])
            look_successful = True
    if not look_successful:
        print("That didn't work.")
        
    

def execute_command(command):
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
    print_menu(exits, room_items, inv_items)

    user_input = input("> ")

    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    return rooms[exits[direction]]
    
        
def debate():#this function deals with the mechanics for the debate
    '''
    This function deals with the mechanics for the debate:
    The moderator asks six questions.
    After the question is asked, Hillary responds.
    Trump responds.
    After the questions are asked, Trump can do one or two special attacks, depending on if he has the corres if he has the corresponding item in his inventory
    The player is judged for how many votes they accumulated.
    '''
    global votes
    global game_over
    global debate_over
    print('''In the debate, the moderator will ask a question, Hillary will respond, then you\'ll make your response.
Six questions will be asked.
You earn more votes for better-fitting answers, but you cannot make the same response twice.''')#Insctructions for the debate
    print()
    print('Press enter to continue.')
    wait = input()
    print('The moderator asks his first question.''')

    shuffle(responses)
    your_special_attacks = []
    for attack in spatks:
        if attack['item'] in inventory:
            your_special_attacks.append(attack)
    #Questions are asked
    print()
    for debate_round in range(1, 7):#Moderator asks six questions, as this for loop suggests
        moderator_question = questions[random.randint(0, len(questions)-1)]
        print('QUESTION: ' + moderator_question['moderator'])
        print('HILLARY RESPONDS: ' + moderator_question['hillary'])
        print()
        
        player_response = None
        response_made = False


        print('You have ' + votes_to_string() + ' votes.')
        while not response_made:
            print('You can say one of the following:')
            menu_number = 1
            for response in responses:#this loop goes through the available responses and prints them out to create a menu
                print(str(menu_number) + ') ' + response['full response'])
                menu_number += 1
            print('Which option would you like to choose? Please enter a number.')
            player_input = input('> ')
            try:#this try and except prevents crashes from happening if user inputs wacky responses
                if int(player_input)>0 and int(player_input)<=len(responses):#if the player's input is between 1 and the amount of responses there are, it is valid input
                  player_response = responses[int(player_input)-1]
                  response_made = True
                else:
                    print('That didn\'t make sense.')
                    print('THE QUESTION WAS: ' + moderator_question['moderator'])
                    print('HILLARY RESPONDED: ' + moderator_question['hillary'])
                    print()
            except:
                print('That didn\'t make sense.')
                print('THE QUESTION WAS: ' + moderator_question['moderator'])
                print('HILLARY RESPONDED: ' + moderator_question['hillary'])
                print()
        fitting_response = False#we need to check if the response fits the question
        for question in player_response['fitting questions']:
            if question == moderator_question:
              fitting_response = True
                  
        if fitting_response:
            print(player_response['fit result'])
            votes += player_response['fit votes']
        else:
            print(player_response['regular result'])
            votes += player_response['regular votes']

        responses.remove(player_response)
                  
        if moderator_question in questions:
            questions.remove(moderator_question)
        print()
    #Special attack opportunity follows
    print('The questions are over.')
    if len(your_special_attacks)>1:
          print('You can perform two special attacks!')
          print()
          for special_attack_round in range(1, 3):
              print('You have ' + votes_to_string() + ' votes.')
              response_made = False
              while not response_made:
                  menu_number = 1
                  for spatk in your_special_attacks:
                      print(str(menu_number) + ') ' + spatk['option'][0].upper() + spatk['option'][1:] +'.')
                      menu_number += 1
                  print('Which option would you like to choose?')
                  player_input = input('> ')
                  try:
                      if int(player_input)>0 and int(player_input)<menu_number:
                          if player_response == spatk_satan:
                              os.system("Hillarylaugh.wav")
                          print(your_special_attacks[int(player_input)-1]['result'])
                          print()
                          votes += your_special_attacks[int(player_input)-1]['votes']
                          your_special_attacks.remove(your_special_attacks[int(player_input)-1])
                          response_made = True
                      else:
                          print('That didn\'t make sense.')
                  except:
                      print('That didn\'t make sense.')
    else:
        print('You have ' + votes_to_string() + ' votes.')
        print('You ' + your_special_attacks[0]['option'] + '.')
        print()
        print(your_special_attacks[0]['result'])
        votes += your_special_attacks[int(player_input)-1]['votes']
        print()
        
    #votes = 78000000#meant for testing game. if this is uncommented, comment from shuffle to line above
    debate_over = True
    print('The debate is over.')
    print('You ended with ' + votes_to_string() + ' votes.')
    print()
    if votes >= 75000000:
        print('Congratulations! You won the debate and became president. You obtained the key to the White House.')
        inventory.append(item_key)
    else:
        print('You lost the debate, as you needed at least 75,000,000 votes. Hillary became president. Welp.')
        game_over = True
    room_debate["description"] = '''The debate hall is now void of life. You spot a few tattered American flags on the floor.'''
    room_debate["image"] = ""
    print()
    print('Press enter to continue.')
    wait = input()

def votes_to_string():#puts commas in the right places
    global votes
    votes_as_string = ''
    character_number = 1
    for ch in str(votes)[::-1]:
        votes_as_string += ch
        if character_number%3==0:
            votes_as_string += ','
        character_number += 1
    return votes_as_string[::-1]

def main():
    os.system("Anthem.wav")
    game_title()
    game_intro()
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

    '''inventory.append(item_money)#meant for testing game. if this block is uncommented, comment while loop above
    inventory.append(item_eagle)
    while not game_over:
        print_room(current_room)#is only picking up, dropping, or looking at an item in the room
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)
        if current_room == rooms['House']:#The game ends once Trump goes to the white house with the key in his inventory, or if Hillary wins the debate
            print_room(current_room)
            game_over = True'''
    
    if current_room == rooms['House'] and votes<76500000:
        execute_trump_wins()
    elif current_room == rooms['House'] and votes>=76500000:
        execute_trump_wins_too_much()
    else:
        execute_hillary_wins()


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

