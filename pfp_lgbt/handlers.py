from .models import Flag
from .util import byteToImageFile

def handleFlags(response, host):
    json = response.json()
    flags = []
    for i in json:
        flag = Flag(i, json[i]['defaultAlpha'], json[i]['tooltip'], f'{host}/icon/{i}')
        flags.append(flag)
    return flags

def handleIcon(response):
    return response.content

def handleImageStatic(response, file_output):
    if file_output is not None:
        byteToImageFile(response.content, file_output)
    return response.content

    