import requests
from os import path

from .models import mimes
from .error import UnsupportedMIMEError, ConvertImageError

def byteToImageFile(byte, file):
    if isinstance(byte, (bytes, bytearray)):
        with open(file, 'wb') as f: 
            f.write(byte)

def imageToByte(image):
    if isinstance(image, (bytes, bytearray)):
        return image
    elif isUrl(image): 
        if isValidMIME(image):
            response = requests.get(image)
            return response.content
    elif path.exists(image):
        try: 
            with open(image, 'rb') as img: 
                return img.read()
        except:
            raise
    else: 
        raise ConvertImageError('Provided image must be byte array, url or path')

def isUrl(image):
    try:
        if image.startswith('https') or image.startswith('http'):
            return True 
        return False 
    except:
        return False
    
def isValidMIME(image):
    response = requests.head(image)
    if 'Content-Type' in response.headers:
        if response.headers['Content-Type'] in mimes:
            return True 
        raise UnsupportedMIMEError(f'Expected {mimes}, got {response.headers['Content-Type']}')
    raise UnsupportedMIMEError(f'Content-Type not in headers.')

