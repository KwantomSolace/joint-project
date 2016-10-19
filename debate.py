from items import *
#9 questions
#Debate announcer only asks 6
question_poverty = {'moderator':'How do you aim to combat poverty?',
                    'hillary':'I want us to invest in YOU, I want us to invest in your future. Donald only cares about the 1%.'	
                    }

question_president = {'moderator':'Why do you think you\'ll make a good president?',
                      'hillary':'Unlike my opponent I actually do have a great temperament *shoulder shimmies*, and I don\,t grab people by their genitalia.'
                      }

question_immigration = {'moderator':'How do you feel about immigration?',
                        'hillary':'Building a wall isn\'t going to stop immigrants, which is probably an idea that won\'t get through to my dense opponent. What we need is a better system at logging and vetting immigrants.'
                        }

question_changes = {'moderator':'What changes will you make during your time in office?',
                    'hillary':'I will raise taxes for the rich, I will make sure equality is achieved, and I will finally move our country into the future.'
                    }

question_inspiration = {'moderator':'What inspiration do you take from past presidents?',
                        'hillary':'Well first of all, I would start appearing on talk shows and do funny segments like carpool karaoke \'cause they\'re hip and I can totes relate to young people.'
                        }

question_climate = {'moderator':'What will you do about climate change?',
                    'hillary':'Climate change is real, people. And it is here. The thing about science is that whether you believe in it or not, it is still the truth and everyone of us has to do something.'
                    }

question_favourite = {'moderator':'What is your favourite thing about America?',
                      'hillary':'America is the land of endless possibilities, where you can go to the Moon, become a star, and even run for president regardless of your qualifications.'
                      }

question_personal = {'moderator':'What is so appealing about you personally?',
                     'hillary':'I am a very relatable person, I can dab, I can do the nay nay and I can even make YOU Pokemon GO TO THE POLLS!'
                     }

question_gun = {'moderator':'What will you do about the gun issue?',
                'hillary':'I will work with responsible gun owners so we can pass reforms on common sense because I dont want you to be shot by an idiot *cough* I mean someone who shouldnt have a gun'
                }

questions = [question_poverty, question_president, question_immigration, question_changes, question_inspiration, question_climate, question_favourite, question_personal, question_gun]

#13 responses
response_taxes = {
'full response':'LOWER TAXES!!!!!! *ahem*ForTheRich*ahem*',
'regular result':'The crowd applauds. You gained 500,000 votes.',
'fit result':'The crowd roars! You gained 1,000,000 votes.',
'fitting questions': [question_poverty, question_changes], 
'regular votes':500000,
'fit votes': 1000000
}

response_man = {
'full response':'I\'m a man',
'regular result':'The crowd applauds. You gained 100,000 votes.',
'fit result':'''The crowd starts chanting, \'Trump! Trump! Trump!\' keeping in mind that Hillary loves to
brag she\'s a woman. You gained 750,000 votes.''',
'fitting questions':[question_president, question_personal], 
'regular votes':100000,
'fit votes':750000
}

response_wall = {
'full response':'We need to build a wall. And a dome. And we need to place mines underground along the borders.',
'regular result':'You hear people of all sorts of backgrounds applaud, strangely. You gained 500,000 votes.',
'fit result':'You hear people of all sorts of backgrounds shout with great approval, strangely. You gained 500,000 votes.',
'fitting questions':[question_changes, question_immigration], 
'regular votes':500000,
'fit votes':750000
}

response_locker_room = {
'full response':'Come with me to a locker room and you\'ll find the answer.',
'regular result':'Apparently that made no sense. The crowd is rather silent, except for a crying baby somewhere. You lost 200,000 votes.',
'fit result':'''The brighter ones among your supporters cheer and explain what you mean to those poor souls who are smart enough to have
stayed impartial in the election yet aren\'t smart enough to get the innuendo and scoff at it. You gained 500,000 votes''',
'fitting questions':[question_personal], 
'regular votes':-200000,
'fit votes':500000
}

response_great = {
'full response':'Make America great again.',
'regular result':'''Your fans are no longer entertained by that phrase, and the people who don\'t
support you roll their eyes. You didn\'t lose or gain any votes.''',
'fit result':'The people thinking about voting for you love hearing that phrase again! You gained 250,000 votes.',
'fitting questions':[question_favourite, question_changes], 
'regular votes':0,
'fit votes': 250000
}

response_guns = {
'full response':'Are guns the problem, or is Islam the problem?',
'regular result':'''Though that was a rather random comment, everyone goes crazy at the mention of Islam.
You inwardly smile at the commotion, as you have gained 250,000 votes.''',
'fit result':'''OH, SNAP! The mention of Islam reawakens the fear people have about ISIS and makes them
believe you will get rid of all terrorists. You gained 800,000 votes.''',
'fitting questions':[question_gun], 
'regular votes':250000,
'fit votes':800000
}

response_anthem = {
'full response':'Sing the national anthem, harmonising with yourself.',
'regular result':'The audience starts to sing along! You gained 750,000 votes.',
'fit result':'''The audience starts to sing along, though eventually the sound of sobbing takes over.
Probably because it was so beautiful. You gained 1,000,000 votes.''',
'fitting questions':[question_favourite, question_president], 
'regular votes':750000,
'fit votes':1000000
}

response_card = {
'full response':'Pull out Trump(TM) Card.',
'regular result':'Aren\'t you clever! You gained 500,000 votes.',
'fit result':'''Aren\'t you clever! Your supporters raise their own gold-plated Trump(TM) Cards, baffling
everyone else in the audience but stealing the attention of the camerapeople. You gained 500,000 votes.''',
'fitting questions':[question_personal], 
'regular votes':500000,
'fit votes':500000
}

response_noises = {
'full response':'Make fart noises with your foul-smelling mouth.',
'regular result':'\'Right,\' says the moderator. You didn\'t lose or gain votes.',
'fit result':'''That\'s right! You don\'t need to actually use words to explain how awesome you are.
You gained 250,000 votes by making fart noises, and your faith in humanity doesn\'t quiver.''',
'fitting questions':[question_personal], 
'regular votes':0,
'fit votes':250000
}

response_jfk = {
'full response':'Ask not what your president can do for you, ask what you can do for your president.',
'regular result':'Sounds like something JFK said. You gained 250,000 votes.',
'fit result':'People whoop and froth at the mouth at the JFK reference. You gained 600,000 votes.',
'fitting questions':[question_inspiration], 
'regular votes':250000,
'fit votes':600000
}

response_abuse = {
'full response':'Bill Clinton has actually abused women, and Hillary has bullied, attacked, shamed and intimidated his victims.',
'regular result':'''That was a little out-of-the-blue (no pun initially intended, as
Democrats are represented by blue) but the crowd goes with it. You gained 100,000 votes.''',
'fit result':'Burn, Hill! A million of her supporters switch sides and now will vote for you.',
'fitting questions':[question_inspiration], 
'regular votes':100000,
'fit votes':1000000
}

response_climate = {
'full response':'Blame China. Do you see how they wear gas masks over there?',
'regular result':'Uh, okay... People in the crowd either nod or try to hold in laughter. You didn\'t lose or gain any votes.',
'fit result':'People yell, \'YEAH!\' You gained 750,000 votes.',
'fitting questions':[question_climate], 
'regular votes':0,
'fit votes':750000
}

response_people = {
'full response':'Hillary just says what people want to hear.',
'regular result':'Hillary\'s supporters have second thoughts as your fans cheer. You gained 500,000 votes.',
'fit result':'And you say what people don\'t want to hear, which is why you have supporters and have gained 750,000 more.',
'fitting questions':[question_personal], 
'regular votes':500000,
'fit votes':750000
}

responses = [response_taxes, response_man, response_wall, response_locker_room, response_great, response_guns, response_anthem, response_card, response_noises, response_jfk, response_abuse, response_climate, response_people]

spatk_eagle = {
    'option':'Use bald eagle',
    'result':'''You open your suit jacket and release the bald eagle. It swoops around
the debate room majestically, eventually making its way back to you and
perching on your forearm dramatically. The crowd cheer in adoration.
You have gained a million more votes thanks to your prestigious showmanship''',
    'votes':1000000,
    'item':item_eagle
}

spatk_satan = {
    'option':'Call Satan',
    'result':'''You take out your phone and give Satan a call. A dark cloud covers the
celling of the debate room and a hole appears from the ground, a few
centimetres from where Hillary is standing. Her eyes glow a dark red
colour, she starts to laugh and convulse uncontrollably. Satan appears
to have possessed her and she is creeping out the audience and viewers
at home. Two million of her supporters end up voting for you.''',
    'votes':2000000,
    'item':item_satans_number
}

spatk_photo = {
    'option':'Present photo of Bill Clinton',
    'result':'''You take out the photograph of Bill Clinton with the attractive female.
Hillary looks at it gritting her teeth, creating a pained smile. She looks
angry and appears to now be a lot more distracted than before.  You gain
750,000 votes''',
    'votes':750000,
    'item':item_photo
}

spatk_money = {
    'option':'Use your million dollars',
    'result':'''You make it rain! Money floods the stage from the ceiling, you look over to
Hillary. She's not impressed but the crowd go wild. You gain 1,000,000 votes.''',
    'votes':1000000,
    'item':item_money
}

spatks = [spatk_eagle, spatk_satan, spatk_photo, spatk_money]
