import praw
import config
import random
import time
import os
def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "created by farrygodjd to comment")
    return r
keywords = ['Aragorn' , 'aragorn' ]



def run_bot(r, comment_replied_to):
    for comment in r.subreddit('lotrmemes').comments(limit=25):
        for keyword in keywords:
            if keyword in comment.body and comment.id not in comment_replied_to and not comment.author == r.user.me:
                print( "Breakfast has been found")
                list = ['I would have gone with you to the end into the very fires of Mordor.',
                        'Not if we hold true to each other.', 'I thought I had wandered into a dream.',
                        'I will not let the White city fall nor our people fail', 'FOR FRODO!!',
                        'I will not let the White city fall nor our people fail.',
                        'You have my sword', 'You have my sword',
                        'My friends you bow to no one!',
                        'But I must admit that I hoped you would take to me for my own sake. A hunted man sometimes wearies of distrust and longs for friendship. But there, I believe my looks are against me.',
                        'For my part I forgive your doubt. Little do I resemble the figures of Elendil and Isildur as they stand carven in their majesty in the halls of Denethor. I am but a heir of Isildur, not Isildur himself. I have had a hard life and and a long; and the leagues that lie between here and Gondor are a small part in the count of my journeys. I have crossed many mountains and many rivers and trodden many plains ever into the far countries of Rhun and Harad where where the stars are strange!',
                        'Stand your ground, sons of Gondor of Rohan my brothers. I see in your eyes the same fear that would take the heart of me! A day may come when the courage of men fails when we forsake our friends and break all bonds of fellowship but it is not this day! An hour of wolves and shattered shields when the age of men comes crashing down but it is not this day, this day we fight!!! And for all that is dear to you in this world I bid you stand men of the west and fight! ',
                        'Ride out with me. Ride out and meet them.',
                        'Lonely men are we rangers of the wild. Hunters – but hunters ever of the servants of the enemy; for they are found in many places not in Mordor only. ”Strider” am I to one fat man who lives within a day´s march of foes that would freeze his heart or lay his little town in ruin if he were not guarded ceaselessly. Yet we would not have it otherwise. If simple folk are free from care and fear, simple they will be and we must be secret to keep them so. That has been the task of my kindred while the years have lengthened and the grass has grown.',
                        'War is upon you whether you risk it or not',
                        'Not if we hold true to each other. We will not abandon Merry and Pippin to torment and death. Not while we have strength left. Leave all that can be spared behind. We travel light. Let’s hunt some orc!',
                        'I am Isildur"s heir. Fight for me! And I will hold your oath fulfilled! What say you!?',
                        'You will suffer me',
                        'A hunted man sometimes wearies of distrust and longs for friendship. But there I believe my looks are against me.',
                        'Be at peace son of Gondor.',
                        'I would have guided Frodo to Mordor and gone with him to the end.',
                        'I do not want that power. I have never wanted it.',
                        '[Let us together rebuild this world that we may share in the days of peace.](https://www.youtube.com/watch?v=W6t9OF8_3n8)',
                        'The best revenge is letting go and living well.',
                        'Tis the lay of Luthien. The elf-maiden who gave her love to eren a mortal!',
                        'HES TRYING TO BRING DOWN THE MOUNTAIN! GANDALF WE MUST TURN BACK!',
                        'I swore to protect you.',
                        'THE BEACONS OF MINAS TIRITH! THE BEACONS ARE LIT! GONDOR CALLS FOR AID!',
                        'It is but a shadow and a thought that you love. I cannot give you what you seek',
                        ' Sauron will not have forgotten the sword of Elendil. The blade that was broken shall return to minas Tirith.',
                        'Murderers. Traitors. You would call upon them to fight? They believe in nothing. They answer to no one.',
                        'If Sauron had the ring we would know it!',
                        'No. There is still hope for Frodo. He needs time... And safe passage across the plains of Gorgoroth. We can give him that.',
                        'Draw out Sauron"s armies. Empty his lands. Then we gather our full strength and march on the Black Gate!',
                        'Hold your ground, hold your ground. Sons of Gondor, of Rohan my brothers. I see in your eyes the same fear that would take the heart of me. A day may come when the courage of men fails when we forsake our friends and break all bonds of fellowship but it is not this day. An hour of woes and shattered shields when the age of men comes crashing down but it is not this day. This day we fight! By all that you hold dear on this good earth I bid you stand, men of the west!',
                        'Let the lord of the Black Lands come forth, that justice be done upon him!',
                        ' We have time. Every day Frodo moves closer to Mordor.', ' Then I shall die as one of them!',
                        'My lady, there may come a time for valor without renown. Who then will your people look to in the last defense?',
                        'You have some skill with a blade.',
                        'You are a daughter of kings a shieldmaiden of Rohan. I do not think that will be your fate!',
                        'They do not come to destroy Rohan"s crops or villages. They come to destroy its people. Down to the last child.',
                        'Its the beards.',
                        'Open war is upon you whether you would risk it or not.',
                        'Farmers, ferriers, stable boys. These are no soldiers.',
                        ' It is an army bred for a single purpose, to destroy the world of men. They will be here by nightfall.',
                        'They were once men. Great kings of men. Then Sauron the Deceiver gave to them nine rings of power. Blinded by their greed, they took them without question, one by one falling into darkness. Now they are slaves to his will. They are the Nazgul, ringwraiths, neither living nor dead. At all times they feel the presence of the Ring, drawn to the power of the one. They will never stop hunting you.' , 
                       'You said you"d bind yourself to me, forsaking the immortal life of your people.' , ' Are you frightened?' , 'I have seen the White City, long ago' , 'Frodos fate is no longer in our hands.' , 'A little more caution from you; that is no trinket you carry' , 'Indeed. I can avoid being seen if I wish, but to disappear entirely, that is a rare gift.' , 'You cannot wield it. None of us can. The One Ring answers to Sauron alone. It has no other master.' , 'The same blood flows in my veins. The same weakness.' , 'I let Frodo go.' , ' By nightfall these hills will be swarming with orcs!... We must reach the woods of Lothlórien.' , 
                       'Boromir! Give the Ring to Frodo.' , 'They will look for his coming from the White Tower. But he will not return.' , 'Sam, do you know the Athelas plant?' , ' I will not lead the Ring within a hundred leagues of your city.' , '  You should be dead. That spear would have skewered a wild boar.' , 'He is passing into the Shadow World. He"ll soon become a wraith like them.' , 'Frodo, I have lived most of my life surrounded by my enemies. I will be grateful to die among my friends.' , 'Why have you come?' , 'Not for ourselves. But we can give Frodo his chance if we keep Sauron"s Eye fixed upon us. Keep him blind to all else that moves.' , 
                       'You shall not enter the realm of Gondor.' , 'I do not believe it! I will not!' , 'I summon you to fulfill your oath.' , ' It has been remade... Fight for us... and regain your honor.' , 'What does your heart tell you?' , 'They have a better chance defending themselves here than at Edoras...' , 'Then what do you fear, My Lady?' , 'He"s not alone. Sam went with him.' , 'Not a word.' , 'All Isengard is emptied.' , 'Ten thousand strong at least.' , 'It is an army bred for a single purpose, to destroy the world of men. They will be here by nightfall.' , 'They will look for his coming from the White Tower. But he will not return.' ,
                       ' Indeed. I can avoid being seen if I wish, but to disappear entirely, that is a rare gift.']
                random_item = random.choice(list)
                comment.reply(random_item)
                comment_replied_to.append(comment.id)

                with open("comment_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
            print("sleeping for 10 seconds")

def get_saved_comments():
    if not os.path.isfile("comment_replied_to.txt"):
        comment_replied_to = []
    else:
        with open("comment_replied_to.txt", "r") as f:
            comment_replied_to = f.read()
            comment_replied_to = comment_replied_to.split("\n")
    return comment_replied_to

r = bot_login()
comment_replied_to = get_saved_comments()
while True:
    run_bot(r, comment_replied_to)
 
