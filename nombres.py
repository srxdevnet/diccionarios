import json
import random

def get_nombres():
    with open('nombres.json', 'r') as fn:
        names = json.load(fn)

    return random.choices(names, k=30)

    
