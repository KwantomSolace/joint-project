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

  print(''' \n\n\n\n\t\t\t -- I N T R O -- \n\n\n\n ''')
  
  text='''
        America has lost its way.. Obama has run this country to the ground!
      We need you Mr Trump, save us, MAKE US GREAT AGAIN.

      Your plans for the Wall and the Future of America is in jeopardy
      It is being threatened by the likes of Hillary Clinton. You need to beat
      her in the debates to gain the sway of the voters.
      
      To defeat a foe like Crooked Hillary Clinton at the final Debate, you
      need all the help you can get, we wish you the best of luck! '''
  for char in text:
          sys.stdout.write(char)
          time.sleep(0.036)
