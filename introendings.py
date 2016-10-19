#these functions print the title and intro of the game
import time
import sys
import os

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
      
To defeat a foe like Crooked Hillary Clinton at the debate, you
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
  print('''
    ```.-:::/++ooosssssssssssssssss+-`                                     
                                                         `..-:::/+osssssyyyyyyyyhhhhhhhyhhhhhyhhhyyyo/-`                                    
                                                 `..-:/++osyhhhhddddhhhhhhhhhyyso+++//:::-..`..-::+o/-`                                     
                                          ``.-/+osyyyyhhhhhhhhhhhyso+/::-.````                                                              
                                    `.-/+ossyyhhhhhhhysoo+:..````                                                                           
                    ym-         `.:+syyhhhhhhys+/:-```                                                                                      
                   +MMd`     `-+yyhhhhyo+:-.``                                            `.......--:::::/+++o++++++///:::-.`               
                  .Nd+Mo    .oyhhso/-.`                                     ``````.--:/+oossysssssssyyyyyyyyyyyyyyyysyyyyss+-`              
                 `dN- hM:   oy+:.`                                  `.-:::/oossoosyyhhdddhhhhhhhhhhhhyyyyyyssooooosyyyyyyys+-`              
                 oM+  .mm` -/.                           ``.-:/++++ossyyyyyhhhhhhhhhhhyyso+/:...--...``````       ```````...`               
                -Nh    :My `                        .-/+ossyyyhhhhhhhhysssso/:::::-..```                                                    
 `:::::::://////mN.     sM+//////:::::::-        `:oyhhhhyyysoo+///::.````                                                                  
 /dNMmhyyysssssss-      `osssssssyyydNMNy`     `-syss+:-...``                                                                               
  `:ydh+.                        `:ydh+-       .:.```                                                                                       
     ./ydh/.                  `:sddo-`                                                                                                      
        ./hdh/`             -sddo-`                                                                                                         
           .mM.             hM+`    ./oyyys+-`  `:syhhys/`   oyo.    /ys`  `:oyhhhy+-   /yyyyyys+-       /yy:    yyyyyyyyyy/ ./shhhys/.     
           :My              -Mh    +mNho++smd- -dMdo//odMd-  dMMd/`  oMm` -hNdo//+yd+   sMN++++yMN/     /NNMm-   ++++NMh+++-.dMd+//ohm+     
          `mm`     ./+-`     sM/  .MM+     `. `dMh`    `hMm  dMddMy- oMm` dMh` `:::/:-  sMm-.../NM+    :NM+sMm-     `NMo    `dNms+:-..      
          oM/  `.+hdhsdds:`  `mN` :MN.        `mMs      oMM` dMy`sNNosMm` NMs  :dddNMd  sMNdddmMNo    :NMh::dMm-    `NMo     `:+shdmmd+`    
         -Nh`.+hmy/.  `:odds:`/Ms .NMs.`  `-:` sMm:````:mMy  dMy  -hMNMm` sMm:```.-mMd  sMm-..-yMm-  :NMmddddmMm.   `NMo     :+.```.oMM-    
         dMyhmy/`         -oddymM- -hNmhhhdNd- `+mNdhhdNmo`  hMy   `+mMm` `+dNdhhdmmMd  sMd`   `sNm--mNs     `hNd`  `NMo    .ymNdhhdmms`    
        :Nms:`               -+dNy   .:///:-`    `-://:-`    -:-     .:-    `.://:..:-  .:-     `::--::       `::.   ::.      `-://:-`      
    `.` `-`   `..  `.......`    ..   ........`   ........`    ..........   ``.--..`   `..  `.......`    `.........` `..`     ..` ...........
    sMm:     `yMm. :MNNmmmmmy-      `mMNmmmmmd+  yMNmmmmmdo`  dMNmmmmmmh` :hmmmmNmd+  +MN` :NNNmmmmmy-  -MMNmmmmmm+ -NNh-   `dMo`hmmmNMNmmmh
    yMMN/   .dMMm. :MN-```.dMd      `mMo````+MM: hMd````/NM+  mMs```````  NMd-``.:s-  +MN` :MM:```-sMN: -MM:``````  -MMNNo` `mMs ````dMh````
    yMNmN+ -mMmMm. :MMsoooyNN/      `mMh///+hMm. hMmoooohMd.  mMmhhhhhy.  :hNNmhyo/`  +MN` :MM-    `mMy -MMdhhhhhs  -MM+hMm/`mMs     hMh    
    yMd-mMsmM+oMm. :MMyssyNMy`      `mMmhhhhy+`  hMmsssdMN/   mMh+++++/`   ``.:+odMm- +MN` :MM-    .mMs -MMo+++++/  -MM: /mMymMs     hMh    
    yMd .dMN/ +Mm. :MN-   .dMh`     `mMo         hMh    /NM+  mMh::::::- `smy+:-:oMM/ +MN` :MM+::/+dMd. -MM+::::::. -MM:  `sMMMs     hMh    
    ody  `y:  /dh` :dd.    .hds     `hd+         sds     /dd: yddddddddy` -oydmmmhs-  /dd` -ddddddhs/`  -ddddddddd+ -dd-    -hd+     sds)''')
   
  os.system("TrumpWin.wav")
  textwin= '''
    \n\n\n\n\t\t\t Y O U - W I N \n\n\n\n\t\t\t
    Congratulations MR TRUMP. The White House is yours.
    A new era begins for the United States. .


    Life after Trump appears normal. . . . albeit strangely very few minorities
    are spotted. The economy. . Isn't getting better, This wall. .I thought Mexico
    was paying for it. wait. no. GO BACK. WE NEED TO GO BACK. 

    '''

  for char in textwin:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.020)

    #program delay and print ascii art. OR write short description of life after Trump

def execute_trump_wins_too_much():
    os.system("TrumpWin.wav")

    print('''
    \n\n\n\n\t\t\t Y O U - W I N \n\n\n\n\t\t\t
    Congratulations MR TRUMP. The White House is yours.
    A new era begins for the United States. .''')

    time.sleep(2.0)
    textexc='''
    ******BOOOM******
    Y O U   H A V E  B E E N  K I L L E D

    It appears your overwhelming success had forced Crooked Hillary Clinton 
    to hire ISIS mercenaries for your execution.
    \n\n\n\n\t\t\t Game--Over \n\n\n\n\t\t\t'''

    for char in textexc:
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(0.020)
    
    os.system("HillaryLaugh.wav")
    
def execute_hillary_wins():

  print('''\n\n\n\n\t\t\t Game--Over \n\n\n\n\t\t\t''')
  print('''You let Crooked Hillary Clinton Win! Once again one of those scummy political types
    has the country in its grasp! You Failed America!''')
        
