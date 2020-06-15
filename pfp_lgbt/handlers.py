from .models import Flag

def handleFlags(response, host):
    json = response.json()
    flags = []
    for i in json:
        flag = Flag(i, json[i]['defaultAlpha'], json[i]['tooltip'], f'{host}/icon/{i}')
        flags.append(flag)
    return flags

def handleIcon(response):
    return response.content

    