# Let the Roasting Begin
# Later on, this will be integrated into Dyme where if someone you know is near you, it will automatically send them a roast

import pull
import pyperclip

def Roast(person, age):
    if age < 20:

    elif age < 30:

    elif age < 40:

    elif age < 50:

    else:

n = 10
roastees = pull.users(n)

for person in roastees:
    pyperclip.copy(Roast(person, person['age']))
    #pull.send()
    #time.sleep as worst case


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


