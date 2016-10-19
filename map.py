#this file holds the information for all the rooms
#info includes ascii art (labelled as image), name, description, exits, and items

from items import *

room_bar = {
    "image":'''		                                                                                                                           `....            
		                                                                                                                       .+hmmmmmmds:         
		                                                                                              `y`                     :mNNNNNNNds:.o`       
		   :+//////////////////////////////////////////////////////////////////////////////////////-  +my:                    +NNmmmmmds-`-ys       
		  y/```````````````````````````````````````````````````````````````````````````````````````s:.`ymy+`                .o.dmNmhmmdh/+hNy       
		  d          ..:/++.        `...       `.-://++oo+                             :ys.        :/`-hmdy+                .yhmNmhhdmNmhdNN+       
		  d      ./oyhhhyss:      -oyhhh+`  .syhhhyysssoo+    `.-.                    +hh+`        :/  .-/ds/                .shhhhhhhmmmNNy`       
		  d    :shhs+:.``        +hho--hho   -/:./+/`     ./syyhhho      /-     ``   `:/-          :/    .mhs-                .yhhysyhmNNNy`-++     
		  d   /hho.`           `shh:   /dh.      sdh     /hhs/:-odh    -hNh-   :yy-     `.-:/os-   :/    `mdyo-            ss+::yhhhyhmNNm.+yhN-    
		  d   -yhy+-`         `sdy-````:dd-      sdh    /hh+`   +dd`  `sNNy  .ohh+` `:oyyhhysso.   :/     hddys.          `mmsyommddhhmNNN++ood-    
		  d    `:syhyyo+:.`   /ddhyyyyyhmd-      sdh   `hdh/++oodmh   odmdh.:yds-  `shdo:-.``      :/     :mddys-          +y/ymddhhyyddhhdmdo/     
		  d       `.:+syhhyo..hdo//////sdd-      hds   +ddysssoymm+  /hhoddyhh+`   .yhdy+-`        :/      +mmdhs/`        .:ydhhyyyydhyyyymh+-:-   
		  d            `.-ydy+dd.      sdh      .dd/  `hds``   sdy` `hds`hmNh:      `.:ohhs:       :/       :ydmhso-       +/hhhhyydmdyyyyh:.osoy-  
		  d    `...``` ``./ddodd-     .hd+      odh.  -dd:    /dh:  -yh: :oo:           .+dh:      :/        `/dmdyo+-     +mNmmy-omNmhhyyy.yos:y+  
		  d    :hhhyssssyhhy+.hy/     `:/.      /o/   :sy`    .:/   ``.      `.`````````.:dd/      :/       .+shmmdds+/.    hhhdmdmNNmmdyys+h-yys+  
		  d    `.--//////:.`  .`                        `                    +hyyyyyyyyyyhhs.      :/      ./sdmmmmddyo//.  oyyyhhdddy:hyy+oh`.:/.  
		  d`                                                                 .-:::::::::--.        :/     ./sdmmmmmmddds//:`/yyyyyhs-  shys-h/      
		  /o-.....................................................................................:s.    .+ydmmhmmmmmmddhohsyyyyyh+`   +hyy`oy:     
		   `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-`    -ohdmmo`smmmmmds//hdhhyyyhy-   :hyh.-ho     
		                                                                                              `/ydmds-  `smddmy/-:syymmmdsmh`  `yyh-+y/     
		                                                                                             -sddy/.     `ododhhyyyyyydd++Nms`  /hhsyy`     
		                                                                                           `+hdh:          :shdhhyyyyyyh/mmhyy:.-hyhhso+:`  
		                                                                                           +hmd`             :ohhhyyyyyhdd/ -+sss+osyy+/+:  
		                                                                                          :sdyy                 .-:++++/-`            `     
		                                                                                          oy/ .                                             
		                                                                                         .-`                                                ''',

    "name": "Satan's Bar",

    "description":
    """You enter the dark and dingy bar, a thick layer of
smoke fogs the atmosphere and the musky stench of Tabaco
clings to your throat. The bar is in a circle shape at the
middle of the room, with bar stools placed around it. Seedy
looking individuals sit in the booths placed against the
walls of the rooms, they all look like they are up to no good.""",

    "exits": {"out":"Car", "left":"Booths"},

    "items": []
}

room_booths = {
"name": "the booths at Satan's Bar",

    "description":
    """In a dark corner of Satan's Bar you see Bill Clinton
with his arm around a young attractive female. You know this
is some useful dirt that could be used against Hillary, so
you take a picture.""",

    "exits": {"right":"Bar"},

    "items": []
}

room_debate = {
    "image":'''                                                        mMMMMMMMMMN- /MMMh  +MMMh-   `mMMM/      .mMMMN-       mMMM:              
		                                       `mMMMdhhhhhh. +MMMh  /MMMMMs` `mMMM-     `dMMMMMN-      mMMM:              
		                                       `NMMM-        +MMMh  /MMMMMMm:`mMMM-    `dMMN/mMMm`     dMMM:              
		                                       `NMMMNNNNNNd  /MMMh  /MMMmdMMMymMMM-    hMMN: :MMMd`    dMMM/              
		                                       `mMMMdhhhhhy  /MMMh  +MMMh +NMMMMMM:   yMMMMdhdMMMMy    dMMM:              
		                                       `NMMM-        /MMMd  +MMMh  .hMMMMM:  sMMMNNNNNNMMMMy   dMMMyoossss.       
		                                       `NMMM.        /MMMh  +MMMh    /NMMM- +MMMd`     `hMMMs  dMMMMMMMMMM/       
		                                        .---          ...`  `-...     `-..  `...`       `-...  ...........`       
		                                                                                                                  
		                          `dNNNmmNmdh+.   `mNNNmmNNNNN- `hNNNmmmmmdy/       -mmmmh    ymmmmmmmmNNNh``mNNNmmNNNNN: 
		                          `mMMMmddmMMMMy` .MMMMddmmdmm-  dMMMdhhdNMMMs     .mMMMMMy`  sdddNMMMNdddy `MMMMddmmdmm- 
		                          `mMMM.   .hMMMs `NMMN-....-.   mMMM:...oMMMh    .mMMmsMMMs      sMMMs     `NMMN-....-.  
		                          `mMMM-    -MMMm`.MMMMMMMMMMm   mMMMMMMMMMMm.   `dMMN- sMMM+     oMMMs     `MMMMMMMMMMm` 
		                          `NMMM.    oMMMh .MMMNoooooo+  `mMMMo//:oNMMm. `hMMMmyyhMMMM/    +MMMo     `MMMNoooooo+  
		                          `mMMMo+osdMMMm. `NMMN+++++++-  mMMM+:::/NMMM- yMMMMMMMMMMMMN:   oMMMs     `NMMN+++++++- 
		                          `NMMMMMMMMMd+`  .MMMMMMMMMMMs `mMMMMMMMMMMd: sMMMy`````.:NMMN-  oMMMs     .MMMMMMMMMMMs 
		                           -::::::-.`      :::::::::::.  -::::::::.`   ::::`       -:::-  .:::-      :::::::::::. 
		                                                `--:-.        `-::-.`         `-       `-::-.`                    
		                                             `omMMMMMMNh-   +dMMMMMMNh:   /ohmMN`   `smMMMMMMNh:                  
		                                             hMMMh+/oMMMN. yMMMms+sNMMM/ -MMMMMN`  `mMMMy//omNMN.                 
		                                             `..---:+NMMM-.MMMN`   -NMMm `:-NMMN`  :MMMN/oyys+:                   
		                                             .smMMMMMMMm/ -MMMm    `NMMN`   NMMN`  -MMMMMmdNMMMd.                 
		                                             mMMNs+//:.   .MMMN.   :MMMm    NMMN`  -MMMN-   yMMMs                 
		                                            `MMMNyyyyyyhh` sMMMNyshNMMN/ .osMMMNso``dMMMmsoyNMMN:                 
		                                            `MMMMMMMMMMMN.  -ymMMMMNds.  -MMMMMMMN`  +hNMMMMNds-                  
		                                             ```````  ```       `.`       ``` ````      ``.`                      ''',

    "name": "the debate hall",

    "description":"""The bright lights cause you to squint as you walk to
your podium. Once your eyes adjust, you see just how vast and
wild the audience is. There are stars and stripes everywhere,
and someone seems to have brought a grill to make burgers.
People are riding around on their Walmart mobility
scooters, complete with monster truck tyres."""
    ,

    "exits": {"out":"Car"},

    "items": []
}

room_tower = {
    "image":'''		              .yyyyyyyyyyyyyy`     ///////////:-`       /+++/      /+++/      -++++++`     :+++++/      ://////////:.`   
		              -MMMMMMMMMMMMMM`     NMMMMNNNNNMMMm+      NMMMd      NMMMm      +MMMMMMs    -NMMMMMm      mMMMMNNNNMMMMd-  
		              `////yMMMMs////      NMMMm...--mMMMM`     NMMMd      NMMMm      +MMMMMMM+  .mMMMMMMm      mMMMN----/MMMMh  
		                   +MMMM/          NMMMNhhhhdMMMMy      NMMMm      NMMMm      +MMMMsMMN-`hMMymMMMm      mMMMNyyyydMMMN+  
		                   +MMMM/          NMMMNhhdMMMMy-       NMMMm     `NMMMd      +MMMM-sMMmyMMm`mMMMm      mMMMMddddddho-   
		                   +MMMM/          NMMMd  `yMMMN+       yMMMMy/::/hMMMMo      +MMMM-`dMMMMN- mMMMm      mMMMm            
		                   /mmmm/          mNNNh   `oNNNmo      `+hmNMMMMMMNmh/       +mmmm- .mmmm/  hmmmh      dNNNd            
		                   ``````          ....`     .....         `..----..`         `````   ````   `````      .....            ''',

    "name": "the Trump Tower",

    "description":
    """You enter the majestic building that is Trump
Tower. Everything is painted with gold: the walls, the
doors, the floors, the ceiling... Grandiose, shimmering
furniture fills the lobby, and a golden cage meant for
housing a bald eagle sits in the very middle of the room.""",

    "exits": {"out":"Car","left":"Office"},

    "items": [item_eagle]
}

room_house = {
    "image":'''		                                                                     `                                                                
		                                                                     :+/                                                              
		                                                                     :`.                                                              
		                                                                    `/.                                                               
		                                                               `.:+osyyo+/-`                                                          
		                                                     `-//oyyyhdddddddddddddddhyyys+/:.                                                
		                                                `-/+osyyhdddddddddddddddddddddddddhyyys+/:.                                           
		                                             .++oooyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyysoo++/                                        
		      /o++++++++ooo+++++++ooo+++++++ooo++++++ohdy++++++++++++/oooooooooooo+oo++/+++/+++++++ddy+//+++ooo+++++++ooo++++++/+ooo+++++++oo`
		      sdhssssssydddssssosydddysssoosdddhsosssohd+.............--------:::--::..............ydysossssdddysssssohddhssssssydddssssosydd.
		     .oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyys/..+yyyyyyyyyy+..:syyyyyyyy+..-syyyyyyyyys-.-oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:
		     .oyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy+  hdddhhdddddh` odddddddddd. /ddddddddddd/ .yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy:
		      sddddddddddddddddddddddddddddddddddddddddo  hhhddddddddh` +dddddddddh. /ddddddddddd/ .dddddddddddddhddddddddddddddddyhddddddddd.
		      sddyoooosddddhooooohddddooooohddddsoooosd+  shhsoooosddh` +ddoooooydh` /ddhooooohdd: .dhooooohddddoooooyddddyoooosyyhdhoooooddd.
		      shy/-  `/ddddy:   :hdddh:`  -sdddd/.  :+d+  ydd+-  -/ddh` +dh:`  :sdh` :yys-   :hdd: `dh:   :ydddd/`  :oddddo-  ./hdddy:   :ddd.
		      ooy+-  `:hdddy:   :hdddh:   -sdddd/.  -/h/  ydd+-  ./ddh  +dd:`  -sdh` -yys-   :hdd: `hh:   :ydddd/`  :oddddo.  .+ddddy:   :ddd.
		      ooh/:  `:hdddy:   :hdddh:   -sdddd/.  -/h+  ydd+-  ./ddy  /dd:`  -sdh` .yys-   -hdd-  hh:   :ydddd/`  :odddh+.  .+ddddy:   :ddh.
		      shs+:--:+ddddh/:::/hdddh/:::/ydddd+:::/od/  yddo/::/+ddy  /dd/:::/sdh  -sys:-::/hdd-  hh/:::/hdddd+:::/sdhhyo/::/+ddddy/:::/ddd.
		      sddddddddddddddddddddddddddddddddhhhhdddd/  sddddddddddy  /dddddddddh  -ddddddddddd-  hddddddddddddddddhhhhhddddddddddddddddddd.
		      sddhyyyyhddddhyyyyydddddyyyyyhdddhyyyyyhd/  sddhyyyyhdds  :ddyyyyyhdy  -dddyyyyyddd-  hdyyyyyhddddhyyyyyhdddhyyyyhddddhyyyyyddd.
		      sddo:``./ddddy:.`.:hdddh:.``-sdhdd/-``:+d/  sdd+-``-/dds  :dd:.``:ohy  .ddh:``.:hdd.  yh:.`.:ydddd/.``:oddddo-``-+dddds:.`.:ddd.
		      sddo:  `/ddddy:   :hdddh:   -sdddd/.  -+d:  odh+-  ./ddo  :dd:`  -sds  .ddh:   :hdh.  yh:   :ydddd/`  :oddddo.  .+dddds:   :ddd.
		      sddo:  `/ddddy:   :hdddh:   -sdddd/.  -+d:  odd+-  ./ddo  -dd:`  -sds  .hdh:   :hdh.  yh:   :ydddd/`  :oddddo.  .+ddddy:   :ddd.
		      sddo:.../ddddy:...:hdddh:...-sdddd/-..:+d:  odd+:..-/ddo  -dh:`  -sds  .hdh:...:hdh.  yh:...:ydddd/...:odddd+-..-/ddddy:...:ddd.
		      sddhhyhhhdddddhhhhhddddhhhhhhdddddhhhhhhh:  +ddhhhhhhddo  -dd:`  :sds  .hddyyhhhddh.  sdhhhhhhddddhhhhhhddddhhyyhhdddddhhhhhddd.
		      sddhddddddddddddddddddddddddddddddddddss++ssssssssssssssosssssssssssssssssssssssssssss/ssyddddddddddddddddddddddddddddddddddddh.
		      sdddddddhddddddddddhddddddddddddddddoo/sssssssssssssssosssssssssssssssssosssssossssssssso++hddddddddddddddddddddddddddddddddddd.
		      .-----------------------------------.-----------------------------------------------------.------------------------------------`''',

    "name": "the White House",

    "description":'',

    "exits": {"out":"Car"},

    "items": []
}

room_vault = {
    "image":'''		                                                                       .+yhhhyo-              
		                                                                    `/dh+.   `:dy             
		                                                               `:+syms-        /M`            
		                                                             .ymyo/-`         `mmhs:          
		                                                           .:hN.             .dy``:hh`        
		                                                         `dNMMN.    -       -mo    :M-        
		                                                         :MMMMMm.   s      /m/   -omo         
		                                                          /hNMMMm:-.d:    om-./shy+.          
		                                                           `.:+ddoosmNs+odMMdyo:.             
		                                                             .oys+/:---:/+sdd.                
		                                                             od-:+syddmdho/:ys                
		                                                           `-smyo/+Ns:-oN/+shy-               
		                                                         .+hy/.``:o-    /y``-sdy:`            
		                                                       -ydo.    ..       .+.  .+hd/`          
		                                                     .ydo.        `.  .-   .`   `/hd/`        
		                                                   `oms.          +m+-mN-         `/dh:       
		                                                  -dd:          :smMNNMMmho`        `oms`     
		                                                 +Ns`          oMMmMm:hMdyd-          -dd-    
		                                                oN+            mMN:MN +My              `ym:   
		                                               oN/             sMMhMMoyMd.`             `yN.  
		                                              /M+               :shNMmmMMNh+`            `ms  
		                                             `md                   dM:.MNoNMy             +N- 
		                                             :M/               `.` hM/`NN`hMM.            .Ms 
		                                             /M:              `hNmydMo.NMoNMm`             Ny 
		                                             :M+               odNNMMMNMMMNy.          `  `Nsz
		                                             `md`                .-yMhoNM/.           :.  :M: 
		                                              :Ny`                 :y: +o`          `o:  .my  
		                                               :Nd-       .`                      `+h-  :my`  
		                                                .sNh/`    `/s/.                `/ymo.:odh:    
		                                                  .+dNdy++++odMmho+:-.....-:/sdMNNmdhs/.      
		                                                     `-:+sssso+::+oshhdddhysoo/-              
''',

    "name": "the Trump Vault",

    "description":
    """You open the huge gold door walk inside.  The
room is full of money piles fashioned to look like
pieces of furniture. A money sofa sits in the far
corner and a wall-to-wall flat screen money TV is placed in
front of it.""",

    "exits": {"up":"Office"},

    "items": [item_money]
}

room_office = {
    "image":'''		                                                                            ..` .-/:-  ....                                                 
		                                                                           :oso:y/h+/://:::-o....                                           
		                                                                         `./+oy/hoo/+yssso+sys/-:--`                                        
		                                                                        `:y/+yos+o:--``  `.--:ooyh::-+/-.                                   
		                                                                         -+o/oo/.              ./+o/so/y:                                   
		                                                                        `-:o+/-        `         .++yss++.                                  
		                                                                       `:-yo-`       ` .          `+/o/oo:.                                 
		                                                                       `::s:/        ` . .         .+oh++y:-                                
		                                                                        /ss:.        ``` `          o:o+ss:.                                
		                                                                        :os:-         . .           +:h::.`                                 
		                                                                       .:-s:+         . `           o+h+-`                                  
		                                                                       `:-yy::        .            -+s:/-                                   
		                                                                        `-:+o:/       `           :ohys-                                    
		                                                                        .:ss:y+/:`             `:+++//s:    (this is a mirror)              
		                                                                        .:y+oy+o++::-.`   `.:-/syy+hyd.+                                    
		                                                                         ..-:y/sso++osoo+oosso/osss/od-o:                                   
		                                                                             .-y+oy:-/++-/smh`hh:+s+ys:/o`                                  
		                                                                              ..:/-. .....:+s/:+oooo/y--:o                                  
		                                                                                              .:+so:::s:ym:                                 
		                                                                                                  -//yhyy+//.                               
		                                                                                                     `/o:--:+/`                             
		                                                                                                        :+:..:+:`                           
		                 `:+yyyy+:`      -////////.   :////////`  .//       `/oyyy+:`   ./////////`              .+/-.-:+/-                         
		               .yMNhoooshMMs`    yMmyyyyyy:  `NMhyyyyyy.  /MN`    :hMmyoooymN-  oMmoooooo+`                +/..`-:os:`.`                    
		              -mMs`      .dMd`   yMo         `NN-         /MN`   /NM+       -`  oMd                         ++.-::o/s+:/                    
		              dMh         .NM+   yMo         `NN-         /MN`  `NMs            oMd                          /hs:osmh+//.                   
		             `NMo          dMy   yMdssssso`  `NMysssss+   /MN`  :MN:            oMNmmmmmd.                   ./+shhmm/-/-                   
		             `NMo          mMs   yMy::::::`  `NM+:::::-   /MN`  :MM:            oMd``````                     :+/:-:hmdddo                  
		              hMd`        /MN-   yMo         `NN-         /MN`  `NMy            oMd                            `.-::mh``dd`                 
		              .mMd-     `+NN+    yMo         `NN-         /MN`   /NMy.     -+.  oMd                                 +hdhy:                  
		               `omMmhhhmNNs-     yMo         `NN-         /MN`    .sNMmhhhmNh.  oMNhhhhhhh-                                                 
		                  `-:::-`        `.`          ``           .`        .::::.`     ........`                                                  ''',

    "name": "the Trump Office",

    "description":
    """You walk into the trump office, it's a
humongous room full of mirrors. You frequently use
this room to practice your debates, making sure you
always look good from every angle. You look yourself
up and down in one of the mirrors, you're looking
hot as always.""",

    "exits": {"down":"Vault","right":"Tower"},

    "items": []
}

room_car = {
    "image":'''		                                            `:/:::::::/dddmmmhy+///++++++/////////////:::+ydd+-----::-::::-``                               
		                                        `-+/:`        sMMMMMMo/                         .+mMM:          `-+dmhs/.    `                      
		                                    `./++-`          -NMMNMMm:-                         -+MNM-           . `yMNMNy:` -                      
		                         ````````.:ohNd:            `dMMNMMMo                            sNMM.           `  `MNMMMMh--``                    
		        `...--://+ossyyhhdddddmmmNMmdMMdssyyyyyyyyyyhMMNNMMMdyyyyyyyyyyyyyyyyyyyyyyyyyyyyNNMMhhhyyyyyyyyyhyyhMmMMMMMNmdhhhyso+/:-..`        
		    -+syyddNMMNNNNMNNNNNNNMMMMNNNNNNNMMMMMMMNNNNmmmmNMMmMMMMMMNNNNNNNNNNNNMNNNNNNNNNNNNNNNmNNNNNNNNNNNMNmmmmNMmNNNNNNMMNNNNNMNNMMNmo:.      
		   /+:-.-:+NNNMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMNmmmNMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMMNmmmNNNMMMMMMMMMNyhNMMMMMMMm::.     
		 -odhhhhddmMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMNNMMMMMMMMMMMMNdmMMMMMMMMMmhs.    
		`mMMMMMMMMMMMMMMmy+/oyNMMMMMMNNNNmNNNNNNNNNNNNNNNNNNNNNmNNmNNNNNNNNNNNNNNNNNmNNNNNNNNNNNNmNNNNNNNNNNNNNNNNMMmyo/+ymMMMMMMMMMMMMNMMMMMMMNh`  
		`mNNNNNNNNMMMMMd-.....-mMMMMMNmmmmmmmmmmmmmmmmdddddddddhhhhhhhhhhhhhhhhhhhddddddddddddmmmdmmmmmmmmmmmmmmNMMm-.....-dMMMMmmmmmmmmNmNNNNMMM.  
		 -+oshdmmNMMMMMy`..`..`yMMMNNMMMMMMMMMNNNmmdddhhyyysssoo++++////::::::::////+++ooossyyyhhhddmmmNNNMMMMMNMMMy`..``.`yMMMMMMMMMMMMMMMMMMNmh   
		      `````+MMMMs-...-sMMMMo/+++++++++++++++++++++///////////:::::::::://////////++++++ooooooosssssssss+yMMMs-...-sNMMmsssoo+++//::-..``    
		            :dMMMNNmNNMMMm/                                                                              +mMMNNmNNMMNs`                     
		              -ohmNNNmho-                       `                                                          -oyhddyo/`                       ''',

    "name": "Trump's limousine",

    "description": """Your chauffeur picked you up.""",

    "exits": {"house":"House","hall":"Debate","bar":"Bar","tower":"Tower"},

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
    "Car": room_car,
}
