from ratelimit import limits

from .throttle import RequestThrottle
from .models import Request, Flag, types, styles, formats
from .handlers import handleFlags, handleIcon, handleImageStatic
from .util import imageToByte

class Client(object):
    def __init__(self, host='https://api.pfp.lgbt/v3', user_agent='pfp_lgbt.py/0.1.0', key=None):
        self.host = host
        self.key = key
        self.headers = {
            'User-Agent': user_agent,
            'Accept': '*/*'
        }

        self.throttle = RequestThrottle()

    def flags(self):
        endpoint = f'{self.host}/flags'
        response = self.throttle.chew(Request(endpoint, self.headers, 'GET', None, None))
        return handleFlags(response, self.host)

    def icon(self, flag, byte=False):
        endpoint = f'{self.host}/icon/{flag.name}'
        if base64 is not False:
            response = self.throttle.chew(Request(endpoint, self.headers, 'GET', None, None))
            return handleIcon(response)
        return endpoint
    
    def imageStatic(self, image, itype, istyle, flag='pride', iformat='png', output_file=None):
        endpoint = f'{self.host}/image/static/{itype}/{istyle}/{flag}.{iformat}'
        if itype not in types: 
            raise ValueError(f'imageStatic: itype must be one of {types}')
        if istyle not in styles: 
            raise ValueError(f'imageStatic: istyle must be one of {styles}')
        if iformat not in formats:
            raise ValueError(f'imageStatic: iformat must be one of {formats}')
        files = {
            'file' : imageToByte(image)
        }
        response = response = self.throttle.chew(Request(endpoint, self.headers, 'POST', None, files))
        return handleImageStatic(response, output_file)
        

        
