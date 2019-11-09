# Let the Roasting Begin
# Later on, this will be integrated into Dyme where if someone you know is near you, it will automatically send them a roast

import pull
import pyperclip
import random
# from time import sleep

def Roast(person, age = None):
    #TODO
    roast = []
    if age == None:
        for categ in roasts.keys():
            if categ.lower() in person["bio"].lower():
                roast.append(random.choice(roasts[categ]))
    elif age < 20:
        pass
    elif age < 30:
        pass
    elif age < 40:
        pass
    elif age < 50:
        pass
    else:
        pass

    return '; '.join(roast)

n = 10
roastees = pull.users(n)

for person in roastees:
    try:
        pyperclip.copy(Roast(person, person['age']))
    except:
        pyperclip.copy(Roast(person))
    #pull.send()
    # sleep(10)


roasts = {
        'photography' : [],
        'beer' : [],
        'wine' : [],
        'travelling' : [],
        'smoking' : [],
        'reading' : [],
        'cat' : [],
        'mates' : [],
        'friends' : [],
        'adventure' : [],
        'fitness' : [],
        'camping' : [],
        'Netflix' : [],
        'beach' : [],
        'dog': [],
        'adventures': [],
        'snapchat': [],
        'coffee': [],
        'instagram': [],
        'IG': [],
        'boys': [],
        'jokes': [],
        'tattoos': [],
        'drinking': [],
        'party': []}
