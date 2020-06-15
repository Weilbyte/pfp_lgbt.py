from .models import Flag

def handleFlags(response):
    json = response.json()
    flags = []
    for i in json:
        flags.append(Flag(i, json[i]['defaultAlpha'], json[i]['tooltip']))
    return flags
    