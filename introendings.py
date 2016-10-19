#these functions print the title and intro of the game
import time
import sys

def game_title():
	print( '''
   ___ ___  ____ __  _   ___       ____ ___ ___   ___ ____  ____   __  ____ 
  |   |   |/    |  |/ ] /  _]     /    |   |   | /  _]    \|    | /  ]/    |
  | _   _ |  o  |  ' / /  [_     |  o  | _   _ |/  [_|  D  )|  | /  /|  o  |
  |  \_/  |     |    \|    _]    |     |  \_/  |    _]    / |  |/  / |     |
  |   |   |  _  |     \   [_     |  _  |   |   |   [_|    \ |  /   \_|  _  |
  |   |   |  |  |  .  |     |    |  |  |   |   |     |  .  \|  \     |  |  |
  |___|___|__|__|__|\_|_____|    |__|__|___|___|_____|__|\_|____\____|__|__|
    ____ ____    ___  ____ ______       ____  ____  ____ ____ ____          
   /    |    \  /  _]/    |      |     /    |/    |/    |    |    \         
  |   __|  D  )/  [_|  o  |      |    |  o  |   __|  o  ||  ||  _  |        
  |  |  |    /|    _]     |_|  |_|    |     |  |  |     ||  ||  |  |        
  |  |_ |    \|   [_|  _  | |  |      |  _  |  |_ |  _  ||  ||  |  |        
  |     |  .  \     |  |  | |  |      |  |  |     |  |  ||  ||  |  |        
  |___,_|__|\_|_____|__|__| |__|      |__|__|___,_|__|__|____|__|__|                 ''')

def game_intro():

  print(''' \n\n\n\n\t\t\t -- I N T R O -- \n\n\n\n\t\t\t ''')
  
  text='''
America has lost its way... Obama has run this country to the ground!
We need you, Mr. Trump. Save us. MAKE US GREAT AGAIN.

Your plans for the wall and the future of America is in jeopardy.
It is being threatened by the likes of Hillary Clinton. You need to beat
her in the final debate to gain the sway of the voters.
      
To defeat a foe like crooked Hillary Clinton at the debate, you
need all the help you can get.

You need to move around the map and collect items that will grant you special
attacks that will allow you to win more votes and maybe win the elction!

You have already won the hearts of 70 million registered voters, and your
aim is to win 5 million more. You can use two special attacks in the
debate, after you respond to questions asked questions by the debate moderator.
Go to the debate hall when you think you have collected the right special
attacks.

We wish you the best of luck!
      '''
  for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.015)

  print()
  print('Press enter to continue.')
  wait = input()

def execute_trump_wins():
    os.system("TrumpWin.wav")
    #program delay and print ascii art. OR write short description of life after Trump

def execute_trump_wins_too_much():
    os.system("TrumpWin.wav")
    os.system("HillaryLaugh.wav")
    #He gets assassinated on the doorstep by ISIS mercenaries hired by Hillary
    
def execute_hillary_wins():
    #play music (need music) and print ascii art
    print()#delete this print statementafter adding music and ascii
        
